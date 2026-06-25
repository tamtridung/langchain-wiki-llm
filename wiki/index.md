---
tags: [langchain, index]
created: 2026-06-25
updated: 2026-06-25
---

# LangChain Wiki — Danh Mục

Wiki kiến thức toàn diện về LangChain ecosystem — từ core framework đến production deployment.

## Tổng Quan

| Trang | Mô Tả |
|-------|-------|
| [Overview](overview.md) | Tổng quan hệ sinh thái LangChain 4-layer |
| [CLAUDE.md](../CLAUDE.md) | File hướng dẫn cho AI assistant |

## Thực Thự (Entities)

| Trang | Mô Tả |
|-------|-------|
| [Harrison Chase](../entities/harrison-chase.md) | Creator & CEO của LangChain |
| [LangChain Inc.](../entities/langchain-inc.md) | Công ty phát triển LangChain ecosystem |

## Khái Niệm Cốt Lõi (Core Concepts)

### LangChain Core Framework

| Trang | Mô Tả |
|-------|-------|
| [LangChain Core](concepts/langchain-core.md) | Framework nền tảng — modules, imports, cài đặt |
| [LCEL](concepts/lcel.md) | LangChain Expression Language — pipe syntax |
| [Runnables](concepts/runnables.md) | Runnable interface — invoke, stream, batch |
| [Prompts](concepts/prompts.md) | Prompt templates — ChatPromptTemplate, MessagesPlaceholder |
| [Chat Models](concepts/chat-models.md) | Chat models — GPT-4, Claude, Gemini, tool calling |
| [Output Parsers](concepts/output-parsers.md) | Output parsers — Pydantic, JSON, StrOutputParser |
| [Memory](concepts/memory.md) | Memory systems — buffer, summary, vector store memory |
| [Tools](concepts/tools.md) | Tools & function calling — @tool, StructuredTool, toolkits |
| [Callbacks](concepts/callbacks.md) | Callbacks & event system — logging, monitoring, tracing |

### RAG (Retrieval-Augmented Generation)

| Trang | Mô Tả |
|-------|-------|
| [Document Loaders](concepts/document-loaders.md) | Load dữ liệu từ 100+ nguồn |
| [Text Splitters](concepts/text-splitters.md) | Chia nhỏ văn bản — RecursiveCharacter, Token, Markdown |
| [Embeddings](concepts/embeddings.md) | Chuyển text thành vector |
| [Vector Stores](concepts/vector-stores.md) | Lưu trữ & tìm kiếm vector — Chroma, FAISS, Pinecone |
| [Retrievers](concepts/retrievers.md) | Truy xuất thông tin — MultiQuery, Ensemble, Contextual |
| [RAG](concepts/rag.md) | Kiến trúc RAG — indexing, retrieval, generation pipeline |

### Agent Patterns

| Trang | Mô Tả |
|-------|-------|
| [Agent Architectures](concepts/agent-architectures.md) | Kiến trúc Agent — ReAct, plan-and-execute, ReWOO, LLMCompiler |
| [create_agent](concepts/create-agent.md) | Agent harness đơn giản — middleware, tools, system prompt |

### LangGraph (Agent Orchestration)

| Trang | Mô Tả |
|-------|-------|
| [LangGraph Overview](concepts/langgraph-overview.md) | Tổng quan LangGraph — StateGraph, nodes, edges |
| [StateGraph](concepts/state-graph.md) | Định nghĩa graph — state schema, compile |
| [Nodes & Edges](concepts/nodes-edges.md) | Nodes, edges, conditional routing |
| [Checkpointing](concepts/checkpointing.md) | Persistence — MemorySaver, PostgresSaver, time travel |
| [Streaming](concepts/streaming.md) | Streaming — token streaming, event streaming |
| [Human-in-the-loop](concepts/human-in-the-loop.md) | Interrupt patterns — approval, pause, resume |
| [Multi-Agent](concepts/multi-agent.md) | Multi-agent systems — supervisor pattern, agent communication |
| [LangGraph SDK](concepts/langgraph-sdk.md) | Python/JS SDK — assistants, threads, streaming |
| [LangGraph Store](concepts/langgraph-store.md) | Persistent KV store — namespaced storage, semantic search |
| [LangGraph Auth](concepts/langgraph-auth.md) | Auth & authorization — @auth.authenticate, @auth.on |
| [LangGraph Functional API](concepts/langgraph-functional-api.md) | Deploy any framework — Claude SDK, CrewAI, AutoGen |

### LangSmith (Observability & Evaluation)

| Trang | Mô Tả |
|-------|-------|
| [LangSmith Overview](concepts/langsmith-overview.md) | Tổng quan LangSmith — data model, pricing, integrations |
| [Tracing](concepts/tracing.md) | Tracing & observability — distributed, conditional, threads |
| [Evaluation](concepts/evaluation.md) | Evaluation — agent eval, online evals, composite, graph eval |
| [Datasets](concepts/datasets.md) | Datasets — versioning, tagging, feedback architecture |
| [Monitoring](concepts/monitoring.md) | Monitoring — alerts, dashboards, cost tracking, insights |
| [Administration](concepts/administration.md) | Administration — auth, RBAC, audit logs, billing, context engineering |

### LangSmith Advanced Features

| Trang | Mô Tả |
|-------|-------|
| [MCP](concepts/mcp.md) | Model Context Protocol — Remote MCP, Agent Server MCP, Fleet MCP |
| [Fleet](concepts/fleet.md) | No-code agent platform — channels, skills, schedules |
| [Managed Deep Agents](concepts/managed-deep-agents.md) | Hosted runtime cho deep agents |
| [Sandboxes](concepts/sandboxes.md) | Isolated environments for code execution |
| [Engine](concepts/engine.md) | AI agent phát hiện & sửa lỗi tự động |
| [LLM Gateway](concepts/llm-gateway.md) | Unified proxy, redaction, spend policies |

### Deployment

| Trang | Mô Tả |
|-------|-------|
| [Deployment](concepts/deployment.md) | LangServe, LangGraph Cloud, Agent Server, self-hosted, cron |

## Nguồn Tham Khảo (Sources)

| Trang | Mô Tả |
|-------|-------|
| [LangSmith Observability](sources/langsmith-observability.md) | Observability & tracing source docs (6 files) |
| [LangSmith Evaluation](sources/langsmith-evaluation.md) | Evaluation source docs (13 files) |
| [LangSmith Deployment](sources/langsmith-deployment.md) | Deployment & cloud source docs (5 files) |
| [LangSmith Datasets & Annotation](sources/langsmith-datasets-annotation.md) | Datasets, annotation, feedback source docs (4 files) |
| [LangSmith Self-hosted](sources/langsmith-selfhosted.md) | Self-hosted architecture & scaling (5 files) |
| [LangSmith Prompts](sources/langsmith-prompts.md) | Prompt engineering & hub (5 files) |
| [LangSmith Production](sources/langsmith-production.md) | Alerts, dashboards, cost tracking, insights (4 files) |
| [LangSmith Advanced](sources/langsmith-advanced.md) | Caching, semantic search, context hub (7 files) |
| [LangSmith Administration](sources/langsmith-admin.md) | Auth, RBAC, audit logs, billing (9 files) |
| [LangSmith Data Management](sources/langsmith-data-management.md) | Data export, retention, privacy (5 files) |
| [API Reference](sources/api-reference.md) | Agent connections, auth, deployments, integrations, listeners |
| [LangSmith MCP](sources/langsmith-mcp.md) | MCP files (5 files) |
| [LangSmith Fleet](sources/langsmith-fleet.md) | Fleet files (~25 files) |
| [LangSmith Deep Agents](sources/langsmith-deep-agents.md) | Managed Deep Agents files (~10 files) |
| [LangSmith Sandboxes](sources/langsmith-sandboxes.md) | Sandboxes files (7 files) |
| [LangSmith Engine](sources/langsmith-engine.md) | Engine files (4 files) |
| [LangSmith LLM Gateway](sources/langsmith-llm-gateway.md) | LLM Gateway files (4 files) |
| [LangSmith Context Engineering](sources/langsmith-context-engineering.md) | Context engineering files (4 files) |
| [LangSmith Remaining](sources/langsmith-remaining.md) | Remaining ~30 files |
| [Agent Planning Patterns](sources/agent-planning-patterns.md) | Plan-and-execute, ReWOO, LLMCompiler, hierarchical teams (4 files) |

## Lộ Trình Học Đề Xuất

```
1. Bắt đầu:     LangChain Core → Prompts → Chat Models → LCEL
2. RAG:         Document Loaders → Text Splitters → Embeddings → Vector Stores → Retrievers
3. Tools:       Tools → Agent Architectures
4. LangGraph:   Overview → StateGraph → Nodes/Edges → Checkpointing → HIL
5. Nâng cao:    Multi-Agent → Streaming → Evaluation → Deployment
6. Chuyên sâu:  LangSmith Tracing → Datasets → Experiments
```
