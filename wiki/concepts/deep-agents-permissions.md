---
tags: [langchain, deep-agents, concept]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/deep-agents-backends, concepts/deep-agents-customization, concepts/human-in-the-loop]
---

# Deep Agents — Permissions (Filesystem Access Control)

Permissions cho phép bạn control filesystem access bằng declarative rules. Pass `FilesystemPermission` list qua `permissions=` parameter.

> Yêu cầu `deepagents>=0.5.2`. `mode="interrupt"` yêu cầu `deepagents>=0.6.8`.

## Rule Structure

Mỗi `FilesystemPermission` có 3 fields:

| Field | Type | Description |
|-------|------|-------------|
| `operations` | `list["read" \| "write"]` | `"read"`: ls, read_file, glob, grep. `"write"`: write_file, edit_file |
| `paths` | `list[str]` | Glob patterns (`/**`, `{a,b}`) |
| `mode` | `"allow" \| "deny" \| "interrupt"` | Allow, deny, hoặc pause cho human approval |

**First-match-wins:** rule đầu tiên match quyết định outcome. Nếu không có rule nào match → **allowed** (permissive default).

## Ví Dụ

### Read-Only Agent

```python
from deepagents import FilesystemPermission, create_deep_agent

agent = create_deep_agent(
    model=model,
    backend=backend,
    permissions=[
        FilesystemPermission(operations=["write"], paths=["/**"], mode="deny"),
    ],
)
```

### Isolate Workspace

```python
permissions=[
    FilesystemPermission(operations=["read", "write"], paths=["/workspace/**"], mode="allow"),
    FilesystemPermission(operations=["read", "write"], paths=["/**"], mode="deny"),
]
```

### Protect Specific Files

```python
permissions=[
    FilesystemPermission(operations=["read", "write"], paths=["/workspace/.env"], mode="deny"),
    FilesystemPermission(operations=["read", "write"], paths=["/workspace/**"], mode="allow"),
    FilesystemPermission(operations=["read", "write"], paths=["/**"], mode="deny"),
]
```

### Pause for Human Approval (Interrupt)

```python
from langgraph.checkpoint.memory import InMemorySaver

agent = create_deep_agent(
    model=model,
    permissions=[
        FilesystemPermission(operations=["write"], paths=["/secrets/**"], mode="interrupt"),
    ],
    checkpointer=InMemorySaver(),  # Required!
)
```

## Scope Limitations

- Permissions chỉ áp dụng cho built-in filesystem tools (`ls`, `read_file`, `glob`, `grep`, `write_file`, `edit_file`)
- **Không** áp dụng cho custom tools, MCP tools, hoặc sandbox backends
- Dùng `permissions` cho path-based rules
- Dùng backend policy hooks cho custom validation (rate limiting, audit, content inspection)

## Trang Liên Quan

- [Deep Agents Backends](deep-agents-backends.md) — Filesystem backends
- [Deep Agents Customization](deep-agents-customization.md) — Permissions parameter
- [Human-in-the-loop](human-in-the-loop.md) — Interrupt patterns
