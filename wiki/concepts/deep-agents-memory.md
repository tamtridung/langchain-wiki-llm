---
tags: [langchain, deep-agents, concept]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/memory, concepts/deep-agents-backends, concepts/deep-agents-skills]
---

# Deep Agents — Memory Systems

Deep Agents có **long-term memory** — memory tồn tại qua nhiều conversation threads, khác với short-term memory (message history trong checkpoint).

## Kiến Trúc Memory

```
Short-term Memory                      Long-term Memory
(Thread-scoped)                        (Cross-thread)
┌──────────────────┐                  ┌──────────────────┐
│  Message History  │                  │  /memories/       │
│  Scratch Files    │    Checkpointer  │  AGENTS.md        │
│  Tool Results     │ ───────────────► │  Skills           │
│  Checkpoints      │                  │  Learned Prefs    │
└──────────────────┘                  └──────────────────┘
        ▲                                      │
        │           StoreBackend               │
        └──────────────────────────────────────┘
```

## Cách Memory Hoạt Động

1. **Point memory files** — pass file paths qua `memory=` parameter
2. **Agent reads memory** — load vào system prompt lúc startup, hoặc đọc on-demand
3. **Agent updates memory** — dùng `edit_file` tool để update memory files (nếu writable)

Hai pattern chính:

### Agent-Scoped Memory

Memory chia sẻ giữa tất cả users:

```python
from deepagents.backends import CompositeBackend, StateBackend, StoreBackend

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    memory=["/memories/AGENTS.md"],
    skills=["/skills/"],
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/memories/": StoreBackend(
                namespace=lambda rt: (rt.server_info.assistant_id,),
            ),
        },
    ),
)
```

### User-Scoped Memory

Mỗi user có memory riêng:

```python
backend=CompositeBackend(
    default=StateBackend(),
    routes={
        "/memories/": StoreBackend(
            namespace=lambda rt: (rt.server_info.user.identity,),
        ),
    },
)
```

## Seed Memory với InMemoryStore

```python
from deepagents.backends.utils import create_file_data
from langgraph.store.memory import InMemoryStore

store = InMemoryStore()
store.put(
    ("my-agent",),
    "/memories/AGENTS.md",
    create_file_data("""## Preferences
- Keep responses concise
- Use code examples where possible
"""),
)

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    memory=["/memories/AGENTS.md"],
    backend=..., store=store,
)
```

## Background Consolidation

Deep Agents có thể tự động consolidate memory giữa các conversation — học patterns từ tương tác và update memory files trong background.

## Read-Only vs Writable Memory

| Loại | Ví dụ | Write permissions |
|------|-------|-------------------|
| AGENTS.md | Project conventions | Agent writes |
| Skills | SKILL.md files | Developer writes |
| Organization policies | Policy files | Read-only cho agent |
| Learned memories | Auto-saved patterns | Agent writes |

Dùng `permissions=` để enforce read-only:

```python
permissions=[
    FilesystemPermission(operations=["write"], paths=["/policies/**"], mode="deny"),
]
```

## Trang Liên Quan

- [Memory (Core)](memory.md) — Short-term memory trong LangChain
- [Deep Agents Backends](deep-agents-backends.md) — Backend routing cho memory
- [Deep Agents Skills](deep-agents-skills.md) — Skills (on-demand knowledge)
- [Deep Agents Context Engineering](deep-agents-context-engineering.md) — Context compression
