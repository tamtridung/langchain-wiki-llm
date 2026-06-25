---
tags: [langgraph, concept, human-in-the-loop]
created: 2026-06-25
updated: 2026-06-25
---

# Human-in-the-Loop — Con Người Trong Luồng Agent

**Human-in-the-loop (HIL)** cho phép agent tạm dừng và chờ con người xác nhận trước khi thực hiện hành động quan trọng.

## Tại Sao Cần HIL?

- **Safety critical** — Xác nhận trước khi xoá dữ liệu, gửi email, thanh toán
- **Quality control** — Người duyệt kết quả trước khi gửi cho khách hàng
- **Edge cases** — Agent không chắc chắn, hỏi người để quyết định
- **Compliance** — Yêu cầu pháp lý về human approval

## Cơ Chế Interrupt

LangGraph dùng cơ chế **interrupt** — dừng graph tại điểm xác định, chờ input từ bên ngoài.

```python
# Compile với interrupt points
app = graph.compile(
    checkpointer=MemorySaver(),
    interrupt_before=["tools"],      # Dừng trước khi gọi tool
    interrupt_after=["agent_node"],  # Dừng sau khi agent suy nghĩ
)
```

## Basic HIL Pattern

```python
from langgraph.graph import StateGraph, MessagesState
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode

graph = StateGraph(MessagesState)
graph.add_node("agent", call_agent)
graph.add_node("tools", ToolNode(tools))
graph.add_edge("tools", "agent")
graph.set_entry_point("agent")

# Dừng trước khi agent trả lời (sau khi gọi tool xong)
app = graph.compile(
    checkpointer=MemorySaver(),
    interrupt_after=["agent"],
)

# User gửi message
config = {"configurable": {"thread_id": "session-1"}}
for chunk in app.stream(
    {"messages": [("human", "I need to send email to john@example.com")]},
    config=config
):
    # Agent sẽ gọi tool, rồi dừng
    pass

# Kiểm tra trạng thái
state = app.get_state(config)
last_msg = state.values["messages"][-1]
print(last_msg.content)  # "I'm about to send: ..."

# Hỏi user: "Bạn có muốn gửi không?"
# Nếu user đồng ý → resume
app.invoke(None, config=config)
# Agent tiếp tục và trả lời
```

## Approval Pattern

```python
from langgraph.graph import StateGraph, START
from typing import TypedDict, Literal

class ApprovalState(TypedDict):
    messages: list
    approved: bool

# Node duyệt
def human_approval(state) -> Literal["approved", "rejected"]:
    if state.get("approved"):
        return "approved"
    return "rejected"  # Pause và chờ

graph = StateGraph(ApprovalState)
graph.add_node("agent", agent_node)
graph.add_node("tools", ToolNode(tools))
graph.add_node("check_approval", human_approval)

# Agent → check_approval (có thể interrupt) → tools
graph.add_edge("agent", "check_approval")
graph.add_conditional_edges("check_approval", lambda s: "tools" if s.get("approved") else "__end__")
graph.add_edge("tools", "agent")
graph.set_entry_point("agent")

app = graph.compile(
    checkpointer=MemorySaver(),
    interrupt_before=["check_approval"],  # Dừng chờ duyệt
)

# Chạy
app.invoke({"messages": [("human", "Delete user 123")]}, config)

# User duyệt
app.update_state(config, {"approved": True})

# Resume
app.invoke(None, config)
```

## Edit State During Interrupt

```python
# Trong lúc tạm dừng, user có thể sửa state
state = app.get_state(config)

# Sửa message cuối
last_msg = state.values["messages"][-1]
last_msg.content = "[MODIFIED] " + last_msg.content

# Update state
app.update_state(config, {"messages": [last_msg]})

# Resume với state đã sửa
app.invoke(None, config)
```

## Dynamic Interrupt (Trong Node)

```python
from langgraph.types import interrupt, Command

def sensitive_action(state):
    # Tạm dừng và chờ xác nhận
    confirmation = interrupt(
        "Are you sure you want to delete this user?" 
    )
    
    if confirmation.get("approved"):
        # Thực hiện action
        result = delete_user(state["user_id"])
        return {"result": result}
    else:
        return {"result": "Action cancelled"}
```

## HIL cho Multi-Agent

```python
# Supervisor có thể pause và hỏi human
def supervisor_node(state):
    if needs_approval(state):
        decision = interrupt({
            "type": "supervisor_decision",
            "next_candidates": ["agent_a", "agent_b"],
            "context": state["messages"][-1].content
        })
        return {"next_agent": decision["selected"]}
    return {"next_agent": auto_route(state)}
```

## Time Travel — Fork & Resume

Time travel cho phép **fork** execution từ bất kỳ checkpoint nào trong quá khứ:

```python
from langgraph_sdk import get_client

client = get_client()

# 1. Tạo thread và chạy
thread = await client.threads.create()
result = await client.runs.wait(
    thread["thread_id"], 
    "agent", 
    input={"messages": [{"role": "user", "content": "Tell a joke"}]}
)

# 2. Lấy checkpoint history
history = await client.threads.get_history(thread["thread_id"])
checkpoint_id = history[0]["checkpoint_id"]  # Quay lại checkpoint

# 3. Fork: update state tại checkpoint đó
await client.threads.update_state(
    thread["thread_id"],
    {"messages": [{"role": "user", "content": "Better joke about AI"}]},
    checkpoint_id=checkpoint_id
)

# 4. Resume từ checkpoint — tạo branch mới
result = await client.runs.wait(
    thread["thread_id"],
    "agent",
    input=None,
    checkpoint_id=checkpoint_id
)
```

### Fork Semantics
- Time travel luôn tạo một **fork** (branch mới) trong history
- Không overwrite execution gốc
- Có thể quay lại checkpoint bất kỳ và chạy với input/state khác

## HIL với LangGraph SDK

```python
# SDK patterns cho HIL
# 1. Create thread
thread = await client.threads.create()

# 2. Run graph — sẽ hit interrupt
result = await client.runs.wait(
    thread["thread_id"], "agent", 
    input={"messages": [{"role": "user", "content": "Delete user 123"}]}
)

# 3. Kiểm tra interrupt
print(result["__interrupt__"])  # Payload từ interrupt({...})

# 4. Resume với Command
result = await client.runs.wait(
    thread["thread_id"], "agent",
    command=Command(resume={"approved": True})
)
```

## Best Practices

1. **Interrupt ở đúng chỗ** — Trước tool calls nguy hiểm (delete, send, pay)
2. **Cung cấp context** — Cho user thấy agent đang định làm gì
3. **Cho phép edit** — User không chỉ approve/reject mà còn sửa được
4. **Timeout** — Nếu user không trả lời trong X phút, tự động reject
5. **Audit log** — Luôn log ai approved cái gì, khi nào
6. **Stream progress** — Cho user thấy trạng thái: "Đang chờ duyệt..."

## Trang Liên Quan

- [Checkpointing](checkpointing.md) — Persistence cho HIL
- [Agent Architectures](agent-architectures.md) — Agent patterns
- [Multi-Agent](multi-agent.md) — Multi-agent HIL
