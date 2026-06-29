---
tags: [langchain, deep-agents, concept]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/deep-agents-overview, concepts/deep-agents-profiles, concepts/deep-agents-backends]
---

# Deep Agents — Customization (`create_deep_agent`)

`create_deep_agent()` là hàm trung tâm để tạo deep agent. Nó nhận model, tools, memory, skills, subagents, middleware, backend, permissions, và nhiều tham số khác.

## Full Function Signature

```python
create_deep_agent(
    model: str | BaseChatModel | None = None,
    tools: Sequence[BaseTool | Callable | dict[str, Any]] | None = None,
    *,
    system_prompt: str | SystemMessage | None = None,
    middleware: Sequence[AgentMiddleware] = (),
    subagents: Sequence[SubAgent | CompiledSubAgent | AsyncSubAgent] | None = None,
    skills: list[str] | None = None,
    memory: list[str] | None = None,
    permissions: list[FilesystemPermission] | None = None,
    backend: BackendProtocol | BackendFactory | None = None,
    interrupt_on: dict[str, bool | InterruptOnConfig] | None = None,
    response_format: ResponseFormat[ResponseT] | type[ResponseT] | dict | None = None,
    state_schema: type[DeepAgentState] | None = None,
    context_schema: type[ContextT] | None = None,
    checkpointer: Checkpointer | None = None,
    store: BaseStore | None = None,
    debug: bool = False,
    name: str | None = None,
    cache: BaseCache | None = None
)
```

## Tham Số Chính

| Parameter | Purpose |
|-----------|---------|
| `model` | Model string (`provider:model`) hoặc `BaseChatModel` instance |
| `system_prompt` | Custom instructions, prepended vào base prompt |
| `tools` | Domain tools agent có thể gọi (function, @tool, tool dicts) |
| `memory` | Paths đến AGENTS.md files, loaded vào system prompt |
| `skills` | Paths đến skills directories (progressive disclosure) |
| `backend` | Pluggable filesystem backend (StateBackend mặc định) |
| `permissions` | Path-level allow/deny/interrupt rules |
| `subagents` | Custom subagents cho delegated tasks |
| `middleware` | Extra middleware (appended sau default stack) |
| `interrupt_on` | Tool-level HITL config — approve/edit/reject/respond |
| `response_format` | Structured output schema |
| `state_schema` | Custom graph state schema |
| `context_schema` | Per-run context (user IDs, API keys, feature flags) |
| `checkpointer` | Required cho HITL và state persistence |
| `store` | LangGraph BaseStore cho cross-thread state |

## Ví Dụ Hoàn Chỉnh

```python
from deepagents import create_deep_agent, FilesystemPermission
from deepagents.backends import CompositeBackend, StateBackend, StoreBackend

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    system_prompt="You are a helpful research assistant.",
    tools=[search, fetch_url, run_query],
    memory=["./AGENTS.md", "/memories/preferences.md"],
    skills=["./skills/"],
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/memories/": StoreBackend(
                namespace=lambda rt: (rt.server_info.user.identity,),
            ),
        },
    ),
    permissions=[
        FilesystemPermission(operations=["write"], paths=["/**"], mode="deny"),
    ],
    interrupt_on={
        "write_file": True,
        "execute": {"allowed_decisions": ["approve", "reject"]},
    },
    context_schema=Context,
)
```

## Prompt Assembly

Thứ tự hệ thống prompt cuối cùng:

1. **Custom `system_prompt`** (nếu có)
2. **Base agent prompt** (built-in)
3. **To-do list prompt** — hướng dẫn planning
4. **Memory prompt** — AGENTS.md content (nếu `memory` provided)
5. **Skills prompt** — danh sách skills với frontmatter (nếu `skills` provided)
6. **Filesystem prompt** — docs cho ls/read/write tools
7. **Subagent prompt** — task tool usage
8. **User middleware prompts** — nếu custom middleware
9. **HITL prompt** — nếu `interrupt_on` set

## Middleware

Middleware intercept và modify model requests/responses. Default stack có sẵn 9 middleware. Bạn có thể thêm custom middleware qua `middleware=` parameter.

```python
from langchain.agents.middleware import wrap_model_call

@wrap_model_call
def logging_middleware(request, handler):
    print(f"Model call with {len(request.messages)} messages")
    response = handler(request)
    print(f"Response: {response.content[:100]}...")
    return response

agent = create_deep_agent(
    model="openai:gpt-5.5",
    middleware=[logging_middleware],
)
```

## Trang Liên Quan

- [Deep Agents Overview](deep-agents-overview.md) — Tổng quan Deep Agents SDK
- [Deep Agents Profiles](deep-agents-profiles.md) — HarnessProfile & ProviderProfile
- [Deep Agents Backends](deep-agents-backends.md) — Filesystem backends
- [Deep Agents Context Engineering](deep-agents-context-engineering.md) — Context management
