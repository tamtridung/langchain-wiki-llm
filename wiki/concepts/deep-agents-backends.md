---
tags: [langchain, deep-agents, concept]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/deep-agents-memory, concepts/deep-agents-permissions, concepts/sandboxes, concepts/deep-agents-overview]
---

# Deep Agents — Filesystem Backends

Deep Agents expose một filesystem surface qua các tools (`ls`, `read_file`, `write_file`, `edit_file`, `glob`, `grep`). Các tool này operate thông qua **pluggable backend** — bạn có thể swap backend mà không cần đổi code agent.

## Backend Types

| Backend | Description | Use Case |
|---------|-------------|----------|
| `StateBackend` | File trong LangGraph state, per-thread | **Mặc định.** Scratch pad, intermediate results |
| `FilesystemBackend` | File thật trên disk | Local development, CI/CD |
| `StoreBackend` | File trong LangGraph Store, cross-thread | Long-term memory, shared state |
| `ContextHubBackend` | File trong LangSmith Context Hub | Agent instructions |
| `LocalShellBackend` | File thật + shell execution | CLI tools (⚠️ rủi ro bảo mật) |
| `CompositeBackend` | Route paths → backend khác nhau | Production patterns |
| Sandbox backends | Isolated env + `execute` tool | Code execution an toàn |

### StateBackend (Default)

```python
from deepagents import create_deep_agent
from deepagents.backends import StateBackend

agent = create_deep_agent(model="openai:gpt-5.5")  # StateBackend mặc định
```

- Lưu file trong LangGraph state của thread hiện tại
- Persist qua nhiều agent turns trong cùng thread (nhờ checkpointer)
- **Không** shared giữa các threads
- Shared giữa supervisor agent và subagents

### FilesystemBackend

```python
from deepagents.backends import FilesystemBackend

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    backend=FilesystemBackend(root_dir=".", virtual_mode=True),
)
```

- Đọc/ghi file thật dưới `root_dir`
- `virtual_mode=True` — sandbox paths, block `..`, `~`, absolute paths ngoài root
- ⚠️ Có rủi ro bảo mật: agent có thể đọc file chứa secrets

### StoreBackend (Cross-Thread)

```python
from deepagents.backends import StoreBackend

backend=StoreBackend(
    namespace=lambda rt: (rt.server_info.user.identity,),
)
```

- File trong LangGraph Store — persist qua nhiều threads
- Dùng namespace để phân lập dữ liệu (per-user, per-agent)

### CompositeBackend (Router)

Production pattern: route internal data (`/large_tool_results/`, `/conversation_history/`) vào StateBackend, project files vào FilesystemBackend:

```python
from deepagents.backends import CompositeBackend, StateBackend, FilesystemBackend

agent = create_deep_agent(
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/workspace/": FilesystemBackend(root_dir="/path/to/project", virtual_mode=True),
        },
    )
)
```

### ContextHubBackend

```python
from deepagents.backends import ContextHubBackend

backend = ContextHubBackend("my-agent")
```

- Lưu file trong LangSmith Context Hub repo
- Không cần provision LangGraph Store riêng
- Tốt cho agent instructions và configuration files

### LocalShellBackend (⚠️ Rủi Ro Cao)

```python
from deepagents.backends.local_shell import LocalShellBackend

backend = LocalShellBackend(root_dir=".", env={"PATH": "/usr/bin:/bin"})
```

- Filesystem + shell execution trực tiếp trên host
- **Không có isolation.** Chỉ dùng trong development có kiểm soát
- **Tuyệt đối không** dùng trong production, web servers, multi-tenant

## Policy Hooks

Ngoài `permissions=`, bạn có thể add custom validation logic qua backend policy hooks:

- Rate limiting
- Audit logging
- Content inspection

## Read_file Multimodal Support

`read_file` hỗ trợ multimodal files trên tất cả backends:
- Images: `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`
- Trả về multimodal content blocks (model-dependent)

## Trang Liên Quan

- [Deep Agents Permissions](deep-agents-permissions.md) — Path-based access control
- [Deep Agents Memory](deep-agents-memory.md) — Long-term memory với StoreBackend
- [Sandboxes](../concepts/sandboxes.md) — Sandbox backends
- [Deep Agents Customization](deep-agents-customization.md) — Backend parameter
