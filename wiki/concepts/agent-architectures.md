---
tags: [langchain, concept, agent]
created: 2026-06-25
updated: 2026-06-25
---

# Agent Architectures — Kiến Trúc Agent

**Agent** là hệ thống mà LLM tự quyết định hành động tiếp theo: gọi tool, tìm kiếm thông tin, hay trả lời trực tiếp. Khác với chain cố định, agent có vòng lặp **quan sát → hành động → suy luận**.

## Agent Loop Cơ Bản

```
User Input
    │
    ▼
┌─────────────────────┐
│    LLM + Tools      │  (suy nghĩ: tôi cần tool gì?)
└────────┬────────────┘
         │
    ┌────▼────┐
    │ Tool?   │
    └────┬────┘
         │               ┌──────────────┐
    Có ──┼──────────────►│ Execute Tool │
         │               └──────┬───────┘
         │                      │
         │                      ▼
         │              (quan sát kết quả)
         │                      │
         └──────────────────────┘
         │
    Không (trả lời trực tiếp)
         │
         ▼
    Final Response
```

## Các Loại Agent

### 1. Function Calling Agent (Khuyến nghị)

Dùng native tool calling của model (GPT-4, Claude 3+, Gemini).

```python
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

@tool
def get_weather(location: str) -> str:
    """Get weather."""
    return f"Sunny in {location}"

tools = [get_weather]
model = ChatOpenAI(model="gpt-4o")

# LangGraph ReAct Agent
agent_executor = create_react_agent(model, tools)

response = agent_executor.invoke({
    "messages": [("human", "What's weather in Hanoi?")]
})
```

### 2. ReAct Agent (Thought-Action-Observation)

Zero-shot ReAct: model tự sinh ra `Thought`, `Action`, `Observation` trong prompt.

```python
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("""Answer the following question:

You have access to these tools: {tools}

Use this format:
Question: {input}
Thought: ...
Action: {tool_name}
Action Input: {tool_input}
Observation: ...
... (repeat if needed)
Thought: I now know the answer
Final Answer: ...""")

agent = create_react_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

### 3. OpenAI Tools Agent (Legacy)

Agent dùng OpenAI function calling — vẫn hoạt động nhưng LangGraph preferred hơn.

```python
from langchain.agents import create_openai_tools_agent

agent = create_openai_tools_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)
```

## Agent với Memory

```python
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()

agent_executor = create_react_agent(
    model, tools,
    checkpointer=memory  # Lưu trạng thái giữa các turn
)

# Session-based conversation
config = {"configurable": {"thread_id": "user-123"}}
response = agent_executor.invoke(
    {"messages": [("human", "Hi, I'm John")]},
    config=config
)
response = agent_executor.invoke(
    {"messages": [("human", "What's my name?")]},
    config=config  # Nhớ tên từ turn trước
)
```

## Agent với Human-in-the-Loop

```python
from langgraph.graph import StateGraph, MessagesState
from langgraph.checkpoint.memory import MemorySaver

def call_model(state):
    response = model.invoke(state["messages"])
    return {"messages": [response]}

def should_continue(state):
    messages = state["messages"]
    last = messages[-1]
    if last.tool_calls:
        return "tools"
    return "approve"  # Chờ người duyệt trước khi trả lời

# Graph với interrupt trước khi trả lời
graph = StateGraph(MessagesState)
graph.add_node("agent", call_model)
graph.add_node("tools", ToolNode(tools))
graph.add_conditional_edges("agent", should_continue, {
    "tools": "tools", "approve": "__end__"
})
graph.add_edge("tools", "agent")
graph.set_entry_point("agent")

app = graph.compile(checkpointer=MemorySaver(), interrupt_before=["__end__"])
```

## Multi-Agent Systems

```python
# Agent 1: Router
def router_agent(state):
    question = state["messages"][-1].content
    if "weather" in question.lower():
        return "weather_agent"
    elif "math" in question.lower():
        return "math_agent"
    else:
        return "general_agent"

# Supervisor pattern
graph = StateGraph(MessagesState)
graph.add_node("router", router_agent)
graph.add_node("weather_agent", weather_agent_node)
graph.add_node("math_agent", math_agent_node)
graph.add_node("general_agent", general_agent_node)
graph.set_entry_point("router")
```

## Planning Agent Patterns (Plan-and-Execute)

Planning agents khắc phục nhược điểm của ReAct bằng cách **tách biệt planning khỏi execution**. Thay vì "nghĩ 1 bước làm 1 bước", agent lập kế hoạch nhiều bước trước rồi thực thi.

```
User → Planner → [step1, step2, step3] → Executor → Re-Planner → Response
```

### State cho Planning Agent

```python
class PlanExecute(TypedDict):
    input: str
    plan: List[str]
    past_steps: Annotated[List[Tuple], operator.add]
    response: str
```

### Graph với Plan → Execute → Replan Loop

```python
workflow = StateGraph(PlanExecute)
workflow.add_node("planner", plan_step)   # Lập kế hoạch
workflow.add_node("agent", execute_step)   # Thực thi từng bước
workflow.add_node("replan", replan_step)   # Đánh giá và điều chỉnh

workflow.add_edge(START, "planner")
workflow.add_edge("planner", "agent")
workflow.add_edge("agent", "replan")
workflow.add_conditional_edges("replan", should_end, ["agent", END])
```

### 3 Planning Agent Variants

| Pattern | Cách Hoạt Động | Ưu Điểm | Nhược Điểm |
|---------|---------------|---------|------------|
| **Plan-and-Execute** | Planner → serial step list → execute từng bước → replan | Đơn giản, dễ hiểu | Chậm (tuần tự) |
| **ReWOO** | Planner sinh plan với variables (#E1, #E2) → worker thực thi → solver tổng hợp | Tiết kiệm LLM calls, variable substitution | Vẫn tuần tự |
| **LLMCompiler** | Planner stream DAG tasks → task fetching unit schedule song song → joiner quyết định | **Nhanh nhất** (3.6x), parallel execution | Phức tạp hơn |

#### ReWOO
```python
# Planner output example:
# Plan: I need to know the teams playing
# E1: Search[Who is competing in the superbowl?]
# Plan: I need to know the quarterbacks
# E2: LLM[Quarterback for the first team of #E1]
```
- Worker thay thế `#E1` bằng kết quả thực tế
- Solver tổng hợp tất cả outputs → final answer

#### LLMCompiler
- Planner sinh DAG: mỗi task có tool, args, dependencies
- Task Fetching Unit chạy tasks song song khi dependencies satisfied
- Joiner (LLM) quyết định: final answer hoặc replan
- Paper claims **3.6x speedup** so với ReAct

## So Sánh Agent Patterns

| Pattern | Phức Tạp | Use Case |
|---------|----------|----------|
| Single tool-calling agent | Thấp | Câu hỏi đơn giản, 1-5 tools |
| ReAct agent | Trung bình | Cần reasoning chain rõ ràng |
| Plan-and-Execute | Trung bình | Multi-step tasks, tiết kiệm cost |
| ReWOO | Trung bình-Cao | Tasks có variable dependencies |
| Agent with memory | Trung bình | Conversation nhiều turns |
| Human-in-the-loop | Cao | Cần approval trước hành động |
| LLMCompiler | Cao | Cần tốc độ tối đa, parallel execution |
| Multi-agent supervisor | Cao | Nhiều chuyên gia, routing phức tạp |
| Swarm (peer-to-peer) | Cao | Agent collaboration ngang hàng |

## Best Practices

1. **Bắt đầu với `create_react_agent`** (LangGraph prebuilt) — đơn giản, mạnh mẽ
2. **Giới hạn tools** — 5-10 tools, nhiều hơn thì dùng grouping
3. **Luôn add memory/checkpointer** — Ít nhất là `MemorySaver` cho development
4. **Stream output** — UX tốt hơn, user thấy agent đang suy nghĩ
5. **Human-in-the-loop cho actions nguy hiểm** — Xoá DB, gửi email, thanh toán
6. **Test với diverse questions** — Agent dễ bị overfit vào pattern cố định

## Trang Liên Quan

- [Tools](tools.md) — Tools & function calling
- [Memory](memory.md) — Agent memory
- [LangGraph Overview](langgraph-overview.md) — Agent orchestration
- [Human-in-the-loop](human-in-the-loop.md) — HIL patterns
- [Multi-Agent](multi-agent.md) — Multi-agent systems
