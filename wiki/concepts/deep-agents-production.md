---
tags: [langchain, deep-agents, concept]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/deep-agents-memory, concepts/deep-agents-backends, concepts/sandboxes, concepts/deployment]
---

# Deep Agents — Going to Production

Hướng dẫn đưa deep agent từ local prototype lên production deployment.

## LangSmith Deployments (Recommended)

### Managed Deep Agents

API-first hosted runtime (private beta). Cách đơn giản nhất:

```bash
# Scaffold
deepagents init research-assistant

# Deploy
deepagents deploy

# Run
python -c "
from managed_deepagents import Client
client = Client()
for chunk in client.runs.stream(thread_id, agent_id, input=input):
    print(chunk)
"
```

Xem [Managed Deep Agents](managed-deep-agents.md) cho details.

### LangSmith Deployment (Full Control)

```json
// langgraph.json
{
  "dependencies": ["."],
  "graphs": { "agent": "./agent.py:agent" },
  "env": ".env"
}
```

## Production Primitives

| Primitive | Scope | Purpose |
|-----------|-------|---------|
| **Thread** | Single conversation | Message history + scratch files |
| **User** | Person interacting | Identity + authorization |
| **Assistant** | Configured agent instance | Memory + files per agent |

### Invocation

```python
from dataclasses import dataclass
from deepagents import create_deep_agent
from langchain_core.utils.uuid import uuid7

@dataclass
class Context:
    user_id: str

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    context_schema=Context,
)

# Start conversation
config = {"configurable": {"thread_id": str(uuid7())}}
agent.invoke(
    {"messages": [{"role": "user", "content": "Plan a trip"}]},
    config=config,
    context=Context(user_id="user-123"),
)
```

## Multi-Tenancy

3 concerns cần xử lý:

### 1. User Identity & Access Control
Dùng custom authentication + authorization handlers trên LangSmith Deployments.

### 2. Team Access Control (RBAC)
| Role | Access |
|------|--------|
| Admin | Full permissions |
| Editor | Create/modify resources |
| Viewer | Read-only |

### 3. End-User Credentials
- **OAuth via Agent Auth** — managed OAuth 2.0 flow
- **Credential injection for sandboxes** — sandbox auth proxy
- **Workspace secrets** — shared API keys

## Async

LLM apps I/O-bound. Dùng `ainvoke` và async patterns:

```python
result = await agent.ainvoke(
    {"messages": [...]},
    config=config,
    context=Context(user_id="user-123"),
)
```

## Memory & Execution Environment

| Component | Production Pattern |
|-----------|-------------------|
| **Memory** | StoreBackend với user/agent namespaces |
| **Filesystem** | CompositeBackend: StateBackend (internal) + FilesystemBackend (project) |
| **Code execution** | Sandbox backends (LangSmith, Daytona, etc.) |
| **Checkpointer** | PostgresSaver hoặc MongoDB checkpointer |

## Guardrails

- **Permissions** — FilesystemPermission rules
- **HITL** — `interrupt_on` cho sensitive operations
- **Rate limiting** — backend policy hooks
- **Error handling** — retry + fallback middleware
- **Data privacy** — scoped memory, sandboxed execution

## Frontend

```python
from langgraph_sdk import get_client

client = get_client(url="<DEPLOYMENT_URL>", api_key="<LANGSMITH_API_KEY>")
thread = await client.threads.create()

async for chunk in client.runs.stream(
    thread["thread_id"],
    "agent",
    input={"messages": [{"role": "user", "content": "Hello!"}]},
    context={"user_id": "user-123"},
    stream_mode="updates",
):
    print(chunk.data)
```

## Trang Liên Quan

- [Managed Deep Agents](managed-deep-agents.md) — Hosted runtime
- [Deployment](deployment.md) — LangServe & LangGraph Cloud
- [Sandboxes](sandboxes.md) — Isolated code execution
- [Deep Agents Memory](deep-agents-memory.md) — Long-term memory
