---
tags: [langchain, log]
created: 2026-06-25
updated: 2026-06-25
---

# Nhật Ký Thay Đổi

## 2026-06-29 — Crawl Deep Agents Docs

- **Crawl toàn bộ Deep Agents framework docs** từ `docs.langchain.com/oss/python/deepagents/`
- **Tạo thư mục `raw/deepagents/`** với 23 page đã crawl:
  - Tổng quan: `overview.md`
  - Bắt đầu: `quickstart.md`, `customization.md`, `models.md`
  - Môi trường thực thi: `tools.md`, `backends.md`, `permissions.md`, `sandboxes.md`, `interpreters.md`, `event-streaming.md`
  - Quản lý ngữ cảnh: `skills.md`, `context-engineering.md`, `multimodal.md`
  - Ủy quyền: `subagents.md`, `dynamic-subagents.md`
  - Điều hướng: `human-in-the-loop.md`
  - Production: `going-to-production.md`, `profiles.md`
  - So sánh: `comparison.md`
  - Tích hợp IDE: `acp.md`, `code-overview.md`
  - Frontend UI: `frontend-todo-list.md`, `frontend-sandbox.md`

## 2026-06-25 — Khởi Tạo Wiki

- **Tạo cấu trúc thư mục:** entities/, concepts/, sources/, references/
- **Tạo overview.md** — Tổng quan hệ sinh thái LangChain 4-layer
- **Tạo entities:**
  - `entities/index.md` — Danh mục thực thể
  - `entities/harrison-chase.md` — Creator & CEO LangChain
  - `entities/langchain-inc.md` — LangChain Inc. organization
- **Tạo core concepts:**
  - `concepts/langchain-core.md` — Framework nền tảng
  - `concepts/lcel.md` — LangChain Expression Language
  - `concepts/runnables.md` — Runnable interface
  - `concepts/prompts.md` — Prompt templates
  - `concepts/chat-models.md` — Chat models
  - `concepts/output-parsers.md` — Output parsers
  - `concepts/tools.md` — Tools & function calling
  - `concepts/memory.md` — Memory systems
  - `concepts/callbacks.md` — Callbacks & event system
- **Tạo RAG concepts:**
  - `concepts/document-loaders.md` — Document loaders
  - `concepts/text-splitters.md` — Text splitters
  - `concepts/embeddings.md` — Embeddings
  - `concepts/vector-stores.md` — Vector stores
  - `concepts/retrievers.md` — Retrievers
  - `concepts/rag.md` — RAG architecture
- **Tạo Agent concepts:**
  - `concepts/agent-architectures.md` — Agent patterns
- **Tạo LangGraph concepts:**
  - `concepts/langgraph-overview.md` — LangGraph overview
  - `concepts/state-graph.md` — StateGraph
  - `concepts/nodes-edges.md` — Nodes & edges
  - `concepts/checkpointing.md` — Checkpointing & persistence
  - `concepts/streaming.md` — Streaming
  - `concepts/human-in-the-loop.md` — Human-in-the-loop
  - `concepts/multi-agent.md` — Multi-agent systems
- **Tạo LangSmith concepts:**
  - `concepts/langsmith-overview.md` — LangSmith overview
  - `concepts/tracing.md` — Tracing & observability
  - `concepts/evaluation.md` — Evaluation
  - `concepts/datasets.md` — Datasets
  - `concepts/deployment.md` — LangServe & deployment
- **Cập nhật CLAUDE.md** — Schema và quy ước cho LangChain Wiki
- **Cập nhật index.md** — Danh mục tổng thể
- **Ghi log.md** — File nhật ký này

## 2026-06-25 — Ingest LangSmith Docs (324 files từ raw/)

- **Tạo 11 source pages** tổng hợp toàn bộ nội dung LangSmith:
  - `sources/langsmith-observability.md` — 6 files về observability & tracing
  - `sources/langsmith-evaluation.md` — 13 files về evaluation
  - `sources/langsmith-deployment.md` — 5 files về deployment & cloud
  - `sources/langsmith-datasets-annotation.md` — 4 files về datasets & annotation
  - `sources/langsmith-selfhosted.md` — 5 files về self-hosted architecture
  - `sources/langsmith-prompts.md` — 5 files về prompt engineering & hub
  - `sources/langsmith-production.md` — 4 files về alerts, dashboards, cost tracking
  - `sources/langsmith-advanced.md` — 7 files về caching, semantic search, context hub
  - `sources/langsmith-admin.md` — 9 files về auth, RBAC, audit logs
  - `sources/langsmith-data-management.md` — 5 files về data export, retention, privacy
  - `sources/api-reference.md` — Tổng hợp 5 API groups (39 endpoints)
- **Tạo concept pages mới:**
  - `concepts/monitoring.md` — Production monitoring (alerts, dashboards, cost, insights)
  - `concepts/administration.md` — Auth, RBAC, audit logs, billing
- **Update concept pages với kiến thức từ raw docs:**
  - `concepts/langsmith-overview.md` — Data model, pricing, integrations
  - `concepts/tracing.md` — Distributed tracing, conditional tracing, trace limits
  - `concepts/evaluation.md` — Agent evaluation (3 scopes), online evals, composite, graph eval, spend tracking, REST API evals
  - `concepts/datasets.md` — Dataset versioning, tagging, 3-layer feedback architecture, annotation queues
  - `concepts/deployment.md` — Agent Server runtime, self-hosted scaling, cron jobs, background runs, SWR caching, custom routes
  - `concepts/checkpointing.md` — MongoDB checkpointer, custom checkpointer (alpha), custom store (alpha)
  - `concepts/human-in-the-loop.md` — Time travel & fork semantics, LangGraph SDK patterns
- **Cập nhật index.md** — Thêm monitoring, administration, 11 source pages
- **Cập nhật CLAUDE.md** — Cập nhật sơ đồ thư mục với concepts & sources mới
- **Cập nhật overview.md** — Thêm bảng tổng hợp nguồn tham khảo (11 source groups)
- **Rà soát liên kết** — Kiểm tra tính nhất quán giữa CLAUDE.md, index.md, overview.md

## 2026-06-25 — Ingest P1→P4 (concept còn thiếu)

- **Audit toàn bộ raw/** — Phát hiện ~124 files chưa ingest, phân loại P1-P4
- **Tạo audit report** — `references/audit-gaps.md` — danh sách chi tiết concept thiếu
- **Tạo 8 source pages mới:**
  - `sources/langsmith-mcp.md` — MCP protocol (5 files)
  - `sources/langsmith-fleet.md` — Fleet platform (~25 files)
  - `sources/langsmith-deep-agents.md` — Managed Deep Agents (~10 files)
  - `sources/langsmith-sandboxes.md` — Sandboxes (7 files)
  - `sources/langsmith-engine.md` — Engine (4 files)
  - `sources/langsmith-llm-gateway.md` — LLM Gateway (4 files)
  - `sources/langsmith-context-engineering.md` — Context engineering (4 files)
  - `sources/langsmith-remaining.md` — Remaining ~30 files
- **Tạo 6 concept pages mới:**
  - `concepts/mcp.md` — MCP protocol (Remote, Agent Server, Fleet, Deep Agents)
  - `concepts/fleet.md` — No-code agent platform
  - `concepts/managed-deep-agents.md` — Hosted deep agents runtime
  - `concepts/sandboxes.md` — Isolated code execution environments
  - `concepts/engine.md` — Auto-fix engine
  - `concepts/llm-gateway.md` — LLM proxy & spend control
- **Update concept pages hiện có:**
  - `concepts/administration.md` — Thêm Context Engineering section
  - `concepts/multi-agent.md` — Thêm A2A protocol section
- **Cập nhật CLAUDE.md, index.md** — Thêm concepts & sources mới
- **Tổng kết:** Wiki phủ ~90% nội dung từ raw/ (47 + 14 = ~61 files)

## 2026-06-25 — Thêm LangGraph & Deep Agents concepts

- **Tạo source page mới:** `sources/langgraph-advanced.md` — SDK, Store, Functional API, Auth
- **Tạo 4 concept pages LangGraph mới:**
  - `concepts/langgraph-sdk.md` — Python/JS SDK, Thread-Centric Streaming (v3)
  - `concepts/langgraph-store.md` — Persistent KV store, semantic search, namespaces
  - `concepts/langgraph-auth.md` — AuthN/AuthZ với `langgraph_sdk.Auth`
  - `concepts/langgraph-functional-api.md` — Deploy Claude SDK, CrewAI, AutoGen với `@task`/`@entrypoint`
- **Update concept pages:**
  - `concepts/langgraph-overview.md` — Thêm Functional API section, LangGraph Ecosystem diagram
  - `concepts/index.md` — Thêm 4 LangGraph pages mới
- **Tổng kết:** Wiki từ 62 → **66 files**

## 2026-06-25 — Ingest new_docs (4 files)

- **Đọc 4 tài liệu mới từ `raw/new_docs/`:** Plan-and-Execute blog, plan-and-execute.ipynb, hierarchical_agent_teams.ipynb, multi-agent-collaboration.ipynb
- **Tạo source page mới:** `sources/agent-planning-patterns.md`
- **Update concept pages:**
  - `concepts/agent-architectures.md` — Thêm 3 planning patterns: Plan-and-Execute, ReWOO, LLMCompiler + so sánh chi tiết
  - `concepts/multi-agent.md` — Thêm Hierarchical Agent Teams + Multi-Agent Network (peer-to-peer) với Command(goto=…) pattern
- **Cập nhật index.md** — Thêm source page mới

## 2026-06-29 — Ingest Deep Agents Docs (30 files từ raw/deep_agents_docs/)

- **Đọc toàn bộ 30 file** từ `raw/deep_agents_docs/` — gồm Deep Agents SDK (23 files) + Deep Agents Code (8 files) + Managed Deep Agents overview
- **Tạo source page mới:** `sources/deep-agents-sdk.md` — Tổng hợp kiến trúc, backend system, built-in tools, so sánh với Claude Agent SDK
- **Tạo 19 concept pages mới:**
  - `concepts/deep-agents-overview.md` — Deep Agents SDK overview, quickstart, harness architecture, built-in tools
  - `concepts/deep-agents-customization.md` — `create_deep_agent` full signature, parameters, middleware, prompt assembly
  - `concepts/deep-agents-memory.md` — Long-term memory, agent-scoped vs user-scoped, background consolidation
  - `concepts/deep-agents-backends.md` — 7 backend types: StateBackend, FilesystemBackend, StoreBackend, CompositeBackend, etc.
  - `concepts/deep-agents-permissions.md` — Path-based allow/deny/interrupt, first-match-wins
  - `concepts/deep-agents-profiles.md` — HarnessProfile, ProviderProfile, merge semantics, config files
  - `concepts/deep-agents-skills.md` — Progressive disclosure, SKILL.md, frontmatter, community skills
  - `concepts/deep-agents-subagents.md` — Sync subagents, dictionary spec, CompiledSubAgent, AGENTS.md
  - `concepts/deep-agents-async-subagents.md` — Background subagents, Agent Protocol, lifecycle management
  - `concepts/deep-agents-context-engineering.md` — Input/runtime context, context compression, summarization
  - `concepts/deep-agents-event-streaming.md` — v3 event streaming API, subagent projections, interleave, concurrent
  - `concepts/deep-agents-multimodal.md` — Multimodal I/O, `read_file` support, custom tool outputs
  - `concepts/deep-agents-interpreters.md` — QuickJS interpreter, PTC, dynamic subagents, snapshotting
  - `concepts/deep-agents-rubric.md` — LLM-as-a-judge grading, RubricMiddleware, self-evaluation loop
  - `concepts/deep-agents-acp.md` — Agent Client Protocol, Zed/JetBrains/VS Code integration
  - `concepts/deep-agents-production.md` — Production guide, multi-tenancy, auth, async, guardrails
  - `concepts/deep-agents-comparison.md` — So sánh Deep Agents vs Claude Agent SDK
  - `concepts/deep-agents-code-overview.md` — dcode CLI, capabilities, built-in tools, CLI reference
  - `concepts/deep-agents-code-configuration.md` — config.toml, provider credentials, model resolution
  - `concepts/deep-agents-code-data-locations.md` — Directory structure, precedence rules, cleanup
- **Cập nhật concept pages hiện có:**
  - `concepts/managed-deep-agents.md` — Mở rộng với full workflow, backend types, limits, API reference
- **Cập nhật index.md** — Thêm 3 sections: Deep Agents SDK, Deep Agents Code, source page
- **Cập nhật overview.md** — Thêm Deep Agents layer + mở rộng architecture diagram
- **Cập nhật CLAUDE.md** — Cập nhật cấu trúc thư mục với Deep Agents concepts
- **Tổng kết:** Wiki từ ~66 → **~86 files**
