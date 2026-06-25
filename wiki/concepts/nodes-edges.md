---
tags: [langgraph, concept, nodes-edges]
created: 2026-06-25
updated: 2026-06-25
---

# Nodes & Edges — Định Nghĩa Luồng Xử Lý

**Nodes** là các bước xử lý trong graph. **Edges** là các kết nối định nghĩa luồng dữ liệu đi từ node nào sang node nào.

## Nodes

Mỗi node là một function nhận state và trả về state updates.

```python
def my_node(state: MyState) -> dict:
    # state: current state (read-only)
    # return: partial state update (được merge vào state hiện tại)
    return {"key": "value"}
```

### Node Patterns

#### 1. LLM Call Node
```python
def agent_node(state: AgentState) -> dict:
    response = model.invoke(state["messages"])
    return {"messages": [response]}
```

#### 2. Tool Node
```python
from langgraph.prebuilt import ToolNode

tool_node = ToolNode(tools)
# Tự động gọi tool từ AIMessage.tool_calls
```

#### 3. Conditional / Router Node
```python
def router_node(state: AgentState) -> dict:
    question = state["messages"][-1].content
    if "weather" in question:
        return {"next": "weather_agent"}
    else:
        return {"next": "general_agent"}
```

#### 4. Data Processing Node
```python
def format_context_node(state: RAGState) -> dict:
    docs = state["documents"]
    context = "\n\n".join(d.page_content for d in docs)
    return {"context": context}
```

#### 5. Async Node
```python
async def async_node(state: State) -> dict:
    result = await some_async_function(state["key"])
    return {"result": result}
```

## Edges

### Fixed Edges
Luôn đi từ node A sang node B:

```python
graph.add_edge("node_a", "node_b")
# Sau khi node_a chạy xong → chạy node_b

# Special edges
graph.add_edge("tools", "agent")    # Tool → Agent loop
graph.set_entry_point("agent")      # Điểm bắt đầu
```

### Conditional Edges
Routing dựa trên state:

```python
from typing import Literal

def router(state: MyState) -> Literal["tools", "answer", "__end__"]:
    last_msg = state["messages"][-1]
    
    if last_msg.tool_calls:
        return "tools"
    elif needs_human_approval(state):
        return "approval"
    else:
        return "__end__"

graph.add_conditional_edges(
    "agent",             # Source node
    router,              # Router function
    {                    # Mapping: return value → target node
        "tools": "tools",
        "approval": "human_approval",
        "__end__": "__end__",
    }
)
```

### Routing với Function Router

```python
# Router function trả về target node name
def route_by_content(state) -> str:
    if "weather" in state["question"].lower():
        return "weather_node"
    return "default_node"

# Có thể bỏ qua mapping nếu tên function trả về trùng tên node
graph.add_conditional_edges(
    "router",
    route_by_content,
    # Mặc định: function return "__end__" → kết thúc
)
```

## Prebuilt Components

LangGraph cung cấp sẵn:

### create_react_agent

```python
from langgraph.prebuilt import create_react_agent

# Tạo agent ReAct hoàn chỉnh
agent = create_react_agent(model, tools, checkpointer=memory)
```

### ToolNode

```python
from langgraph.prebuilt import ToolNode

# Node tự động dispatch tool calls
tool_node = ToolNode(tools)

# Custom
from langgraph.prebuilt import tools_condition
# Router: nếu tool_calls → tools, else → end
```

## Common Graph Patterns

### 1. ReAct Loop
```
agent ──┬──► tools ──► agent
         │
         └──► __end__
```

### 2. Supervisor (Multi-Agent)
```
supervisor ──┬──► agent_a ──► supervisor
             ├──► agent_b ──► supervisor
             ├──► agent_c ──► supervisor
             └──► __end__
```

### 3. Map-Reduce
```
input ──► parallel_a ──┐
input ──► parallel_b ──┼──► aggregator ──► output
input ──► parallel_c ──┘
```

### 4. Human-in-the-Loop
```
agent ──► approval? ──┬──► tools
                       │
                       └── (interrupt) → wait human
```

## Trang Liên Quan

- [StateGraph](state-graph.md) — Định nghĩa graph
- [LangGraph Overview](langgraph-overview.md) — Tổng quan
- [Human-in-the-loop](human-in-the-loop.md) — Interrupt patterns
- [Multi-Agent](multi-agent.md) — Supervisor pattern
