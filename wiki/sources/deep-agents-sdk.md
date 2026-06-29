---
tags: [langchain, deep-agents, source]
created: 2026-06-29
updated: 2026-06-29
sources: [raw/deep_agents_docs/ (30 files)]
related: [concepts/managed-deep-agents, concepts/sandboxes, concepts/mcp, concepts/human-in-the-loop]
---

# Deep Agents SDK — Tổng Hợp Tài Liệu Nguồn

Trang này tổng hợp **30 file tài liệu gốc** từ `raw/deep_agents_docs/` về **Deep Agents SDK** — framework xây dựng AI agent production-grade của LangChain.

## Cấu Trúc Tài Liệu Gốc

Tài liệu gốc được chia làm 3 nhóm:

### Nhóm 1: Deep Agents SDK (Core Library)
Từ `docs.langchain.com/oss/python/deepagents/` — thư viện Python `deepagents`:

| File | Mô Tả |
|------|-------|
| `overview.md` | Tổng quan Deep Agents — harness, built-in tools, capabilities |
| `quickstart.md` | Hướng dẫn tạo deep agent đầu tiên với `create_deep_agent` |
| `customization.md` | Toàn bộ tham số `create_deep_agent`, model, tools, middleware |
| `models.md` | Supported models, model eval scores, provider profiles, runtime model selection |
| `tools.md` | Custom tools, MCP tools, built-in harness tools, multimodal tool outputs |
| `memory.md` | Long-term memory, agent-scoped & user-scoped, StoreBackend, background consolidation |
| `backends.md` | Filesystem backends — StateBackend, FilesystemBackend, StoreBackend, ContextHubBackend, CompositeBackend |
| `permissions.md` | Declarative permission rules — allow/deny/interrupt on filesystem paths |
| `sandboxes.md` | Isolated code execution — LangSmith, Daytona, E2B, Modal, Runloop, Vercel sandboxes |
| `profiles.md` | HarnessProfile & ProviderProfile — per-provider/per-model tuning bundles |
| `subagents.md` | Synchronous subagents — dictionary spec, CompiledSubAgent, general-purpose subagent |
| `async-subagents.md` | Async subagents — Agent Protocol, background tasks, start/check/update/cancel lifecycle |
| `skills.md` | Skills system — progressive disclosure, SKILL.md frontmatter, skill discovery |
| `context-engineering.md` | Input context, runtime context, context compression, summarization, offloading |
| `multimodal.md` | Multimodal I/O — images, audio, video, PDF in tools and messages |
| `streaming.md` | Streaming (subgraph-based) — subagent progress, LLM tokens, tool calls |
| `event-streaming.md` | Event streaming (v3 API) — `stream.subagents`, interleave, concurrent consumption |
| `human-in-the-loop.md` | HITL — interrupt_on, InterruptOnConfig, conditional interrupts, decision types |
| `interpreters.md` | Code interpreters (QuickJS) — programmatic tool calling (PTC), dynamic subagents, eval tool |
| `rubric.md` (từ grading rubrics) | LLM-as-a-judge — RubricMiddleware, self-evaluation & iteration |
| `comparison.md` | So sánh với Claude Agent SDK |
| `acp.md` | Agent Client Protocol — expose deep agents sang IDE (Zed, JetBrains, VS Code) |
| `going-to-production.md` | Production checklist — LangSmith Deployments, multi-tenancy, auth, async, durability |

### Nhóm 2: Deep Agents Code (CLI Tool — `dcode`)
Từ `docs.langchain.com/oss/python/deepagents/code/` — CLI coding agent:

| File | Mô Tả |
|------|-------|
| `overview.md` | dcode overview, quickstart, built-in tools table, CLI reference, commands |
| `configuration.md` | config.toml, provider credentials, /auth, env vars, key resolution, web search |
| `providers.md` | Provider reference table, sign-in with ChatGPT, open weights, model routers |
| `subagents.md` | AGENTS.md subagents, cost-efficient subagents, model override |
| `memory-and-skills.md` | Automatic memory, AGENTS.md files, skills creation, community skills, skill discovery |
| `mcp-tools.md` | MCP config (.mcp.json), auto-discovery, Claude Code compat, field reference |
| `remote-sandboxes.md` | Sandbox providers, flags, pluggable providers, setup scripts |
| `data-locations.md` | Directory structure, precedence rules, .deepagents vs .agents |

### Nhóm 3: Managed Deep Agents (LangSmith Hosted)
Từ `docs.langchain.com/langsmith/` — managed runtime:

| File | Mô Tả |
|------|-------|
| `managed-deep-agents-overview.md` | Overview, workflow, sandbox backends, limits, private beta scope |

## Chủ Đề Chính

### Kiến Trúc Deep Agents

```
┌──────────────────────────────────────────┐
│            create_deep_agent()            │
│  Model | System Prompt | Tools           │
│  Memory | Skills | Subagents             │
│  Middleware | Backend | Permissions      │
├──────────────────────────────────────────┤
│         Default Middleware Stack         │
│  PlanningMiddleware                      │
│  LocalContextMiddleware (CLI only)       │
│  MemoryMiddleware                        │
│  SkillsMiddleware                        │
│  FilesystemMiddleware (ls/read/write/)   │
│  SubAgentMiddleware (task tool)          │
│  HumanInTheLoopMiddleware                │
│  SummarizationMiddleware                 │
│  PatchToolCallsMiddleware                │
├──────────────────────────────────────────┤
│         Backend (Filesystem Layer)       │
│  StateBackend | FilesystemBackend        │
│  StoreBackend | CompositeBackend         │
│  LangSmithSandbox | DaytonaSandbox ...   │
├──────────────────────────────────────────┤
│         LangGraph Foundation             │
│  StateGraph | Checkpointing | Streaming  │
└──────────────────────────────────────────┘
```

### 4 Loại Context

Deep Agents có 4 loại context:
1. **Input context** — system prompt, memory, skills (tĩnh, khởi tạo)
2. **Runtime context** — `context_schema`, pass qua `invoke(..., context=...)`, propagate xuống subagents
3. **Context compression** — offloading tool results > threshold, summarization messages cũ
4. **Context isolation** — subagents quarantine heavy work, chỉ trả kết quả về supervisor

### Backend System

| Backend | Mô Tả | Dùng Khi |
|---------|-------|----------|
| `StateBackend` | File trong LangGraph state, per-thread | Scratch pad mặc định |
| `FilesystemBackend` | File thật trên disk, có `virtual_mode` | Development local |
| `StoreBackend` | File trong LangGraph store, cross-thread | Long-term memory |
| `ContextHubBackend` | File trong LangSmith Context Hub | Agent instructions |
| `LocalShellBackend` | File thật + shell execution | CLI tools (có rủi ro) |
| `CompositeBackend` | Route paths đến backend khác nhau | Production: StateBackend + FilesystemBackend |
| Sandbox backends | Isolated env + execute tool | Code execution an toàn |

### Built-in Tools (Harness Tools)

| Tool | Mô Tả | HITL |
|------|-------|------|
| `ls` | List files | — |
| `read_file` | Read file (multimodal support) | — |
| `write_file` | Create/overwrite | Required |
| `edit_file` | String replacement edits | Required |
| `glob` | Find files by pattern | — |
| `grep` | Search text in files | — |
| `execute` | Shell commands (sandbox only) | Required |
| `web_search` | Tavily web search | Required |
| `fetch_url` | Fetch URL → markdown | Required |
| `task` | Delegate to subagents | Required |
| `ask_user` | Ask user questions | — |
| `compact_conversation` | Summarize & offload | Mixed |
| `write_todos` | Task planning | — |
| `get_current_thread_id` | Get thread ID | — |

### So Sánh: Deep Agents vs Claude Agent SDK

| Tiêu Chí | Deep Agents | Claude Agent SDK |
|----------|-------------|------------------|
| Mô hình | Any (100+ providers) | Claude-only |
| Backend execution | Pluggable (local, VFS, sandbox, custom) | Sandbox local filesystem |
| Deployment | Managed (LangSmith) + Self-hosted (Docker) | Self-hosted (tự build server) |
| Multi-tenancy | Built-in (scoped threads, per-user sandbox, RBAC) | Tự build |
| License | MIT | MIT (Claude Code proprietary) |
| Per-model tuning | Harness profiles (declarative) | Configure in code |

## Trang Liên Quan

- [Managed Deep Agents](../concepts/managed-deep-agents.md) — Concept page chính
- [Sandboxes](../concepts/sandboxes.md) — Isolated environments
- [MCP](../concepts/mcp.md) — Model Context Protocol
- [Human-in-the-loop](../concepts/human-in-the-loop.md) — Interrupt patterns
