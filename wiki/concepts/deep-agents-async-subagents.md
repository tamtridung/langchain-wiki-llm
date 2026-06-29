---
tags: [langchain, deep-agents, concept]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/deep-agents-subagents, concepts/multi-agent, concepts/deployment]
---

# Deep Agents — Async Subagents (Preview)

> Preview feature từ `deepagents>=0.5.0`. APIs có thể thay đổi.

Async subagents cho phép supervisor launch background tasks — supervisor tiếp tục tương tác với user trong khi subagents chạy concurrent. Giao tiếp qua **Agent Protocol**.

## Sync vs Async

| Dimension | Sync Subagents | Async Subagents |
|-----------|---------------|-----------------|
| Execution | Supervisor blocks | Returns job ID; supervisor continues |
| Concurrency | Parallel but blocking | Parallel, non-blocking |
| Mid-task updates | Not possible | `update_async_task` |
| Cancellation | Not possible | `cancel_async_task` |
| Statefulness | Stateless | Stateful (own thread) |

## Configuration

```python
from deepagents import AsyncSubAgent, create_deep_agent

async_subagents = [
    AsyncSubAgent(
        name="researcher",
        description="Research agent for information gathering",
        graph_id="researcher",
    ),
    AsyncSubAgent(
        name="coder",
        description="Coding agent for code generation",
        graph_id="coder",
        url="https://coder-deployment.langsmith.dev",  # Optional: HTTP transport
    ),
]

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    subagents=async_subagents,
)
```

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | `str` | Yes | Unique identifier |
| `description` | `str` | Yes | What subagent does |
| `graph_id` | `str` | Yes | Graph ID trên Agent Protocol server |
| `url` | `str` | No | Omit → ASGI (co-deployed). Set → HTTP (remote) |
| `headers` | `dict` | No | Custom headers cho remote server |

## Tools

| Tool | Purpose | Returns |
|------|---------|---------|
| `start_async_task` | Start background task | Task ID (immediate) |
| `check_async_task` | Check status + result | Status + result |
| `update_async_task` | Send new instructions | Confirmation |
| `cancel_async_task` | Stop running task | Confirmation |
| `list_async_tasks` | List all tracked tasks | Task summary |

## Lifecycle

1. **Launch** — tạo thread mới, start run, return thread ID
2. **Check** — fetch run status, lấy final output nếu completed
3. **Update** — interrupt + restart với instructions mới (cùng task ID)
4. **Cancel** — `runs.cancel()`, mark as `"cancelled"`
5. **List** — iterate tracked tasks, fetch live status cho non-terminal

## State Management

Task metadata lưu trong state channel riêng (`async_tasks`), **không** trong message history. Điều này quan trọng vì message history bị compact khi context window đầy. Dedicated channel đảm bảo supervisor luôn recall được tasks.

## Transport Options

| Transport | Khi Nào Dùng |
|-----------|-------------|
| **ASGI** (in-process, no URL) | Co-deployed, zero network latency. Default |
| **HTTP** (with URL) | Independent scaling, different teams |

## Deployment Topology

- **Single deployment** — tất cả agents co-deployed (ASGI). Recommended starting point
- **Split deployment** — supervisor + subagents trên servers khác nhau (HTTP)
- **Hybrid** — một số ASGI, một số HTTP

## Trang Liên Quan

- [Deep Agents Subagents](deep-agents-subagents.md) — Synchronous subagents
- [Deep Agents Production](deep-agents-production.md) — Production considerations
- [Deployment](deployment.md) — LangSmith Deployments
