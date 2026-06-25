---
tags: [langgraph, concept, orchestration]
created: 2026-06-25
updated: 2026-06-25
---

# LangGraph Overview — Agent Orchestration Framework

**LangGraph** là framework cho phép xây dựng **stateful agent workflows** dưới dạng đồ thị (graph). Khác với LCEL (linear chain), LangGraph hỗ trợ loops, branching, checkpointing, và human-in-the-loop.

## Tại Sao LangGraph?

LCEL phù hợp cho pipeline tuyến tính:

```python
# LCEL: Linear flow
chain = prompt | model | parser
```

Nhưng khi cần:
- **Loops** — Agent gọi tool → nhận kết quả → suy luận → gọi tool tiếp
- **Conditional branching** — Nếu X thì làm A, nếu Y thì làm B
- **State management** — Lưu trạng thái giữa các bước
- **Human-in-the-loop** — Dừng chờ người duyệt
- **Streaming/Progress** — Stream từng bước agent

→ **Cần LangGraph**

## Core Concepts

```
State ──► Node ──► State' ──► Edge ──► Node ──► State''
 │                                      │
 └─────────────── Loop ◄───────────────┘
```

### State
Trạng thái của graph, thường là `TypedDict`:

```python
from typing import TypedDict, Annotated
from langgraph.graph import add_messages

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]  # reducer function
    next_agent: str
    documents: list
```

### Nodes
Các bước xử lý (function hoặc runnable):

```python
def agent_node(state: AgentState) -> dict:
    response = model.invoke(state["messages"])
    return {"messages": [response]}
```

### Edges
Kết nối giữa các nodes — có điều kiện hoặc cố định:

```python
graph.add_edge("agent", "tools")           # Fixed edge
graph.add_conditional_edges("agent", decide_next, {
    "continue": "tools",
    "end": "__end__"
})
```

### Reducers
Cách state được cập nhật khi merge kết quả từ nodes:

```python
from langgraph.graph import add_messages
from typing import Annotated

class State(TypedDict):
    messages: Annotated[list, add_messages]  # Append messages
    count: Annotated[int, operator.add]      # Add numbers
```

## Minimal LangGraph Agent

```python
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, MessagesState, add_messages
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

@tool
def get_weather(location: str) -> str:
    """Get weather."""
    return f"Sunny in {location}"

tools = [get_weather]
model = ChatOpenAI(model="gpt-4o").bind_tools(tools)

# 1. Define state
class AgentState(MessagesState):
    pass

# 2. Define nodes
def call_model(state):
    return {"messages": [model.invoke(state["messages"])]}

# 3. Define routing
def should_continue(state) -> Literal["tools", "__end__"]:
    last = state["messages"][-1]
    return "tools" if last.tool_calls else "__end__"

# 4. Build graph
graph = StateGraph(AgentState)
graph.add_node("agent", call_model)
graph.add_node("tools", ToolNode(tools))
graph.set_entry_point("agent")
graph.add_conditional_edges("agent", should_continue)
graph.add_edge("tools", "agent")

# 5. Compile with checkpointing
app = graph.compile(checkpointer=MemorySaver())

# 6. Run
result = app.invoke(
    {"messages": [("human", "What's weather in Hanoi?")]},
    config={"configurable": {"thread_id": "1"}}
)
```

## LangGraph Functional API

Cho phép deploy agents từ bất kỳ framework nào (Claude Agent SDK, CrewAI, AutoGen) lên Agent Server:

```python
from langgraph.func import entrypoint, task

@task
def my_task(input: dict) -> str:
    return process(input)  # delegate to any framework

@entrypoint()
def agent(input: dict, previous: dict | None = None):
    result = my_task(input).result()
    return entrypoint.final(value=result, save=previous)
```

Xem: [Functional API](langgraph-functional-api.md)

## Khi Nào Dùng LangGraph?

| Tình Huống | Giải Pháp |
|------------|-----------|
| Linear chain | LCEL |
| Agent cần gọi tool | LangGraph ReAct |
| Multi-turn conversation | LangGraph + Checkpointer |
| Human approval | LangGraph + interrupt_before |
| Multi-agent | LangGraph + Supervistor pattern |
| Complex workflow | LangGraph + StateGraph |
| Deploy non-LangGraph framework | LangGraph + Functional API |

## Trang Liên Quan

- [StateGraph](state-graph.md) — Định nghĩa graph
- [Nodes & Edges](nodes-edges.md) — Chi tiết nodes & edges
- [Checkpointing](checkpointing.md) — Persistence
- [Streaming](streaming.md) — Streaming
- [Human-in-the-loop](human-in-the-loop.md) — HIL
- [Multi-Agent](multi-agent.md) — Multi-agent
- [Agent Architectures](agent-architectures.md) — Agent patterns
- [LangGraph SDK](langgraph-sdk.md) — Python/JS SDK
- [LangGraph Store](langgraph-store.md) — KV Storage
- [LangGraph Auth](langgraph-auth.md) — Auth & authorization
- [LangGraph Functional API](langgraph-functional-api.md) — Deploy any framework
