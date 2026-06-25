---
tags: [langgraph, concept, multi-agent]
created: 2026-06-25
updated: 2026-06-25
---

# Multi-Agent Systems — Hệ Thống Nhiều Agent

**Multi-Agent Systems** là kiến trúc trong đó nhiều agent chuyên biệt phối hợp với nhau để giải quyết tác vụ phức tạp. Mỗi agent có tools và expertise riêng.

## Supervisor Pattern (Phổ Biến Nhất)

Một **supervisor agent** điều phối các **worker agents** chuyên biệt.

```
                    User Input
                        │
                        ▼
                  ┌──────────┐
                  │Supervisor │  (quyết định agent nào phù hợp)
                  └─────┬────┘
                        │
          ┌────────┬────┼────┬────────┐
          ▼        ▼         ▼        ▼
     ┌────────┐┌────────┐┌────────┐┌────────┐
     │Weather ││  Math  ││ Search ││Coding  │
     │ Agent  ││ Agent  ││ Agent  ││ Agent  │
     └───┬────┘└───┬────┘└───┬────┘└───┬────┘
         │         │         │         │
         └─────────┴────┬────┴─────────┘
                        │
                        ▼
                  ┌──────────┐
                  │Supervisor │  (tổng hợp kết quả)
                  └──────────┘
                        │
                        ▼
                  Trả lời user
```

## Implementation với LangGraph

```python
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from typing import TypedDict, Literal

# === 1. Định nghĩa tools cho từng agent ===

@tool
def get_weather(location: str) -> str:
    """Get weather for a location."""
    return f"Sunny, 32°C in {location}"

@tool
def calculate(expression: str) -> str:
    """Evaluate a math expression."""
    return str(eval(expression))

# === 2. Tạo worker agents ===

model = ChatOpenAI(model="gpt-4o")

weather_agent = create_react_agent(
    model, [get_weather],
    state_modifier="You are a weather specialist."
)

math_agent = create_react_agent(
    model, [calculate],
    state_modifier="You are a math specialist."
)

# === 3. Supervisor node ===

def supervisor_router(state) -> Literal["weather_agent", "math_agent", "__end__"]:
    messages = state["messages"]
    last = messages[-1].content.lower()
    
    if "weather" in last:
        return "weather_agent"
    elif any(w in last for w in ["calculate", "math", "+", "-", "*", "/"]):
        return "math_agent"
    return "__end__"

# === 4. Build graph ===

def call_weather(state):
    return {"messages": weather_agent.invoke(state)["messages"]}

def call_math(state):
    return {"messages": math_agent.invoke(state)["messages"]}

graph = StateGraph(MessagesState)
graph.add_node("supervisor", supervisor_router)
graph.add_node("weather_agent", call_weather)
graph.add_node("math_agent", call_math)
graph.set_entry_point("supervisor")
graph.add_conditional_edges("supervisor", supervisor_router)
graph.add_edge("weather_agent", "__end__")
graph.add_edge("math_agent", "__end__")

app = graph.compile(checkpointer=MemorySaver())
```

## Agent Communication Patterns

### 1. Supervisor (Hub-and-Spoke)

```
Supervisor điều phối, workers trả kết quả về supervisor
```

### 2. Network (Peer-to-Peer)

```
Agents có thể nói chuyện trực tiếp với nhau
```

### 3. Hierarchical

```
Supervisor cấp 1 → Supervisor cấp 2 → Workers
```

### 4. Swarm

```
Không có supervisor — agents tự negotiate
```

### 5. A2A (Agent-to-Agent Protocol)

Google's A2A protocol cho phép agents giao tiếp trực tiếp với nhau qua REST API:

```python
# LangGraph Agent Server hỗ trợ A2A endpoint
# Agents từ different systems có thể gọi nhau
# Mỗi agent expose khả năng của mình qua A2A card

# A2A endpoint trên Agent Server
GET /a2a/card  # Khả năng của agent
POST /a2a      # Gọi agent khác
```

**MCP vs A2A:**
| Tiêu Chí | MCP | A2A |
|----------|-----|-----|
| Mục đích | Tools cho LLMs | Agent-to-Agent |
| Protocol | JSON-RPC | REST API |
| Transport | Streamable HTTP | HTTP |
| Auth | OAuth 2.1/API Key | JWT/OAuth |

## Supervisor với LLM Routing

```python
# Supervisor dùng LLM để quyết định
def supervisor_agent(state):
    response = supervisor_model.invoke([
        SystemMessage(content="""You are a supervisor. 
Given the conversation, decide which agent to call next.
Options: weather_agent, math_agent, FINISH"""),
        *state["messages"],
        HumanMessage(content="Which agent next? Respond with exact name.")
    ])
    return {"next": response.content.strip()}
```

## Shared State giữa các Agents

```python
from typing import TypedDict, Annotated

class MultiAgentState(TypedDict):
    messages: Annotated[list, add_messages]
    agent_scratchpad: str      # Ghi chú chung
    documents: list[Document]  # Shared knowledge base
    pending_actions: list      # Hành động chờ duyệt
```

## Hierarchical Agent Teams

Khi số lượng agents lớn, dùng **hierarchical supervision** — mỗi team có supervisor riêng:

```
Top-level Supervisor
    ├── Research Team Supervisor
    │   ├── Search Agent
    │   └── Web Scraper Agent
    └── Document Team Supervisor
        ├── Outline Agent
        ├── Writer Agent
        └── Editor Agent
```

Mỗi team là một **subgraph** riêng, supervisor cấp cao routing giữa các teams:

```python
# Tạo team agent
def create_agent(llm, tools, system_prompt):
    return create_react_agent(llm, tools, prompt=system_prompt)

# Research team nodes
def research_supervisor(state):
    # Route to search_agent or web_scraper
    ...

# Document team nodes
def doc_supervisor(state):
    # Route to outline_agent, writer, or editor
    ...

# Top-level graph
workflow = StateGraph(MessagesState)
workflow.add_node("research_team", research_team_graph)  # subgraph
workflow.add_node("doc_team", doc_team_graph)            # subgraph
workflow.add_node("top_supervisor", top_supervisor_node)
```

## Multi-Agent Network (Peer-to-Peer)

Không có supervisor — agents collaborate ngang hàng qua shared message state:

```
Researcher ←→ Chart Generator
```

Dùng `Command(goto=...)` pattern:

```python
from langgraph.types import Command

def research_node(state) -> Command[Literal["chart_generator", END]]:
    result = research_agent.invoke(state)
    # Nếu agent có "FINAL ANSWER" → kết thúc
    goto = END if "FINAL ANSWER" in result["messages"][-1].content else "chart_generator"
    return Command(
        update={"messages": result["messages"]},
        goto=goto,
    )

def chart_node(state) -> Command[Literal["researcher", END]]:
    result = chart_agent.invoke(state)
    goto = END if "FINAL ANSWER" in result["messages"][-1].content else "researcher"
    return Command(
        update={"messages": result["messages"]},
        goto=goto,
    )

workflow = StateGraph(MessagesState)
workflow.add_node("researcher", research_node)
workflow.add_node("chart_generator", chart_node)
workflow.add_edge(START, "researcher")
```

Đặc điểm:
- Agents tự quyết định khi nào work done (FINAL ANSWER)
- Shared message history — agents thấy toàn bộ conversation
- Dùng `Command` để routing + update state cùng lúc
- Phù hợp: research + visualization, code + review

## Use Cases Thực Tế

| Use Case | Pattern | Agents |
|----------|---------|--------|
| Customer support | Supervisor | Order, Refund, Tech support |
| Code generation | Supervisor/Network | Planning, Coding, Review, Testing |
| Research + Report | Hierarchical | Research Team → Document Team |
| Data analysis | Network | Data fetcher, Chart generator, Analyst |
| Content creation | Hierarchical | Research, Write, Design, Review |

## Best Practices

1. **Bắt đầu với supervisor pattern** — Đơn giản, dễ debug
2. **Mỗi agent một chuyên môn** — Tools + system prompt riêng
3. **Supervisor không cần mạnh** — Model nhỏ hơn có thể làm supervisor
4. **Shared state cẩn thận** — Tránh conflict khi nhiều agent cùng ghi
5. **Timeouts** — Mỗi agent có max steps để tránh infinite loop
6. **Human oversight** — Supervisor có thể hỏi human khi không chắc

## Trang Liên Quan

- [LangGraph Overview](langgraph-overview.md) — LangGraph cơ bản
- [Nodes & Edges](nodes-edges.md) — Graph patterns
- [Agent Architectures](agent-architectures.md) — Agent patterns
- [Human-in-the-loop](human-in-the-loop.md) — HIL cho multi-agent
