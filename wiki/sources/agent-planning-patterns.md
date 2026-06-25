---
tags: [langchain, source, agent, planning, multi-agent]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/new_docs/Plan-and-Execute Agents.md, raw/new_docs/plan-and-execute.ipynb, raw/new_docs/hierarchical_agent_teams.ipynb, raw/new_docs/multi-agent-collaboration.ipynb]
related: [concepts/agent-architectures, concepts/multi-agent]
---

# Nguồn: Agent Planning Patterns & Multi-Agent

## Tóm Tắt

4 tài liệu mới về planning agents và multi-agent patterns trong LangGraph:

1. **Plan-and-Execute Agents.md** — Blog post về 3 planning agent architectures
2. **plan-and-execute.ipynb** — Implementation Plan-and-Execute agent
3. **hierarchical_agent_teams.ipynb** — Hierarchical agent teams
4. **multi-agent-collaboration.ipynb** — Multi-agent network (peer-to-peer)

## Điểm Then Chốt

### 1. Plan-and-Execute Agent

```
User Input → Planner (LLM) → Plan [step1, step2, step3]
                                  ↓
                            Executor (agent with tools)
                                  ↓
                            Re-Planner → continue? → Agent
                                  ↓
                              Response → User
```

**So sánh 3 Planning Architectures:**

| Pattern | Planning | Execution | Ưu điểm |
|---------|----------|-----------|---------|
| **Plan-and-Execute** | Serial plan list | Sequential task exec | Đơn giản, dễ implement |
| **ReWOO** | Plan with variables (#E1, #E2) | Task with var substitution | Không cần LLM mỗi bước |
| **LLMCompiler** | DAG of tasks | Parallel task scheduling | Nhanh nhất (3.6x claimed) |

### 2. Plan-and-Execute State

```python
class PlanExecute(TypedDict):
    input: str
    plan: List[str]
    past_steps: Annotated[List[Tuple], operator.add]
    response: str
```

### 3. Hierarchical Agent Teams

```
Top-level Supervisor
    ├── Research Team Supervisor
    │   ├── Search Agent
    │   └── Web Scraper Agent
    └── Document Writing Team Supervisor
        ├── Outline Agent
        ├── Writer Agent
        └── Editor Agent
```

### 4. Multi-Agent Network (Peer-to-Peer)

```
Researcher ←→ Chart Generator
     (Collaborate via shared message state)
```

Dùng `Command(goto=...)` pattern để routing messages giữa các agents.

## Code Mẫu

### Plan-and-Execute Graph
```python
workflow = StateGraph(PlanExecute)
workflow.add_node("planner", plan_step)
workflow.add_node("agent", execute_step)
workflow.add_node("replan", replan_step)
workflow.add_edge(START, "planner")
workflow.add_edge("planner", "agent")
workflow.add_edge("agent", "replan")
workflow.add_conditional_edges("replan", should_end, ["agent", END])
```

### Multi-Agent Network Node
```python
def research_node(state) -> Command[Literal["chart_generator", END]]:
    result = research_agent.invoke(state)
    goto = END if "FINAL ANSWER" in result["messages"][-1].content else "chart_generator"
    return Command(update={"messages": result["messages"]}, goto=goto)
```

## Trang Liên Quan
- [Agent Architectures](../concepts/agent-architectures.md)
- [Multi-Agent](../concepts/multi-agent.md)
