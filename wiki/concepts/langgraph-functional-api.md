---
tags: [langgraph, concept, functional-api, deployment]
created: 2026-06-25
updated: 2026-06-25
sources: [langgraph-advanced]
related: [concepts/deployment, concepts/langgraph-overview]
---

# LangGraph Functional API — Deploy Any Framework

**LangGraph Functional API** cho phép deploy agents từ **bất kỳ framework nào** (Claude Agent SDK, CrewAI, AutoGen, Strands) lên LangSmith Agent Server, bằng cách wrap chúng với `@task` và `@entrypoint` decorators.

## Khi Nào Dùng?

| Framework | Cách Deploy |
|-----------|------------|
| LangGraph | Native — compile graph trực tiếp |
| **Claude Agent SDK** | Dùng Functional API |
| **CrewAI** | Dùng Functional API |
| **AutoGen** | Dùng Functional API |
| **Strands** | Dùng Functional API |
| **Google ADK** | Dùng `deployments-wrap-sdk` |

## Cách Hoạt Động

```
Agent Server
    │
    ▼
@entrypoint ─── @task ─── Framework Agent
    │                        (Claude SDK, CrewAI, ...)
    │
    ▼
entrypoint.final(value=..., save=...)
    │
    ▼
Persist checkpoint → Stream output → LangSmith trace
```

### Flow Chi Tiết

1. Agent Server nhận run request
2. Gọi `@entrypoint` function với input + `previous` state
3. Entrypoint gọi `@task` function, delegate tới framework agent
4. Task trả kết quả về entrypoint
5. Entrypoint gọi `entrypoint.final(value=..., save=...)`
   - `value` — Response cho turn này
   - `save` — Checkpointed state cho turn sau (`previous`)
6. Agent Server persist checkpoint, stream output, trace

## Quick Start

```python
from langgraph.func import entrypoint, task

@task
def my_agent_task(input_data: dict) -> str:
    """Delegate to any framework here."""
    # Ví dụ: Claude Agent SDK, CrewAI, AutoGen...
    return f"Processed: {input_data}"

@entrypoint()
def agent(input: dict, previous: dict | None = None):
    """Entrypoint nhận input + previous state."""
    result = my_agent_task(input).result()
    return entrypoint.final(
        value={"response": result},
        save={"state": "checkpoint_data"}
    )
```

### Deploy

```json
// langgraph.json
{
  "python_version": "3.12",
  "dependencies": ["."],
  "graphs": {
    "agent": "./agent.py:agent"
  }
}
```

## Ví Dụ: Claude Agent SDK

```python
from langgraph.func import entrypoint, task
from claude_agent_sdk import Agent

@task
def claude_task(prompt: str) -> str:
    agent = Agent(name="assistant")
    return agent.run(prompt)

@entrypoint()
def agent_fn(input: dict, previous: dict | None = None):
    result = claude_task(input["messages"][-1]["content"]).result()
    return entrypoint.final(
        value={"messages": [{"role": "assistant", "content": result}]},
        save={"history": input.get("messages", [])}
    )
```

## Prerequisites

- Python 3.10+
- LangSmith API key
- `langgraph-cli` (for local dev)

## Best Practices

1. **`save` chỉ state cần thiết** — Không lưu toàn bộ context, chỉ checkpoint data
2. **Async support** — `@task` và `@entrypoint` đều support async
3. **Error handling trong task** — Bắt exception và trả về error message
4. **Test local trước** — Dùng `langgraph dev` để test trước khi deploy

## Trang Liên Quan
- [LangGraph Overview](langgraph-overview.md)
- [Deployment](deployment.md)
- [LangGraph SDK](langgraph-sdk.md)
