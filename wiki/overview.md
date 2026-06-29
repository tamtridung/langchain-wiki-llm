---
tags: [langchain, overview, ecosystem]
created: 2026-06-25
updated: 2026-06-25
---

# Tổng Quan Hệ Sinh Thái LangChain

**LangChain** là một framework mã nguồn mở được thiết kế để xây dựng ứng dụng dựa trên **Large Language Models (LLMs)**. Nó cung cấp các thành phần trừu tượng hoá (abstractions) và công cụ để kết nối LLMs với các nguồn dữ liệu bên ngoài, APIs, và thực thi các luồng tác vụ phức tạp.

## Kiến Trúc 4-Layer

Hệ sinh thái LangChain gồm **4 sản phẩm cốt lõi**:

```
┌─────────────────────────────────────────────┐
│              LangGraph                       │
│  (Agent Orchestration - Stateful Workflows)  │
├─────────────────────────────────────────────┤
│              LangChain                       │
│  (Core Framework - LCEL, Runnables, Chains)  │
├──────────────────────┬──────────────────────┤
│     LangSmith        │     LangServe        │
│  (Obs./Eval./Test)   │  (Deployment)        │
└──────────────────────┴──────────────────────┘
```

### 1. LangChain Core
Framework nền tảng với hệ thống **abstractions** có thể kết hợp (composable):

- **Runnable interface** — Giao diện thống nhất cho mọi component (`invoke`, `stream`, `batch`)
- **LCEL (LangChain Expression Language)** — Cú pháp `|` để kết hợp các component
- **Prompt Templates** — Quản lý và template hoá prompt
- **Chat Models / LLMs** — Wrapper thống nhất cho hàng trăm model provider
- **Output Parsers** — Parse output từ LLMs thành cấu trúc dữ liệu
- **Memory** — Lưu trữ lịch sử hội thoại
- **Retrievers** — Truy xuất thông tin từ vector stores và nguồn khác
- **Document Loaders** — Load dữ liệu từ 100+ định dạng/nguồn
- **Text Splitters** — Chia nhỏ văn bản cho RAG
- **Embeddings** — Chuyển văn bản thành vector
- **Vector Stores** — Lưu trữ và tìm kiếm vector
- **Tools** — Cho phép LLM gọi function bên ngoài
- **Callbacks** — Hệ thống event/hook để logging, monitoring

### 2. LangGraph
Framework xây dựng **agent stateful, đa bước** dưới dạng đồ thị (graph):

- **StateGraph** — Định nghĩa luồng xử lý dạng đồ thị có trạng thái
- **Nodes & Edges** — Các bước xử lý và luồng điều khiển
- **Checkpointing** — Persist trạng thái giữa các bước
- **Streaming** — Stream kết quả theo thời gian thực
- **Human-in-the-Loop** — Tạm dừng luồng chờ người xác nhận
- **Multi-Agent** — Phối hợp nhiều agent

### 3. LangSmith
Nền tảng observability, evaluation, và testing toàn diện:

- **Tracing** — Ghi lại mọi bước xử lý (LLM calls, retrieval, tool calls)
- **Evaluation** — Đánh giá chất lượng output với datasets
- **Datasets** — Quản lý bộ dữ liệu test
- **Annotation Queues** — Labelling và phản hồi của con người
- **Monitoring** — Dashboard real-time cho production
- **Experiments** — So sánh nhiều phiên bản chain/agent
- **Hub & Prompts** — Quản lý prompt versioning

### 4. LangServe
Framework triển khai LangChain apps thành REST APIs:

- Tự động sinh REST API từ Runnable
- Streaming, batching support
- Monitoring tích hợp LangSmith

## Tại Sao LangChain Lại Quan Trọng?

Trước LangChain, xây dựng ứng dụng LLM đòi hỏi code "thủ công" cho từng bước:
- Gọi API LLM → parse output → lưu memory → gọi lại → ...

LangChain giải quyết:
1. **Tính module** — Mỗi thành phần có thể thay thế độc lập
2. **Tính kết hợp** — Dùng `|` để ghép component như pipeline Unix
3. **Đa provider** — Chỉ cần đổi tên model, không cần đổi code
4. **Production-ready** — Observability, testing, deployment ngay từ đầu

## Lộ Trình Học

```
1. LangChain Core ─────────────────────── Runnables, LCEL, Prompts, Models
2. RAG ───────────────────────────────── Retrievers, Vector Stores, Document Loaders
3. Tools & Chains ────────────────────── Tools, Function Calling, Chains
4. LangGraph ─────────────────────────── StateGraph, Nodes, Edges, Streaming
5. Agent Patterns ────────────────────── Multi-Agent, Human-in-the-Loop
6. LangSmith ─────────────────────────── Observability, Evaluation, Datasets
7. Production ────────────────────────── LangServe, Monitoring, CI/CD
```

### 5. Deep Agents (Production-Grade Agent Harness)

**Deep Agents** là thư viện Python mã nguồn mở xây dựng trên LangGraph, cung cấp harness đầy đủ cho AI agent production:

- **`create_deep_agent`** — Hàm trung tâm tạo agent với model, tools, memory, skills, subagents
- **Pluggable backends** — StateBackend, FilesystemBackend, StoreBackend, CompositeBackend, sandbox backends
- **Memory** — Long-term memory qua StoreBackend (agent-scoped, user-scoped)
- **Skills** — Progressive disclosure, on-demand knowledge loading
- **Subagents** — Sync + async subagents với Agent Protocol
- **Middleware stack** — Planning, Filesystem, Skills, HITL, Summarization, etc.
- **Event streaming** — v3 API với subagent projections
- **Permissions** — Path-based filesystem access control
- **Profiles** — HarnessProfile + ProviderProfile cho per-model tuning
- **Interpreters** — QuickJS code interpreter + programmatic tool calling
- **Rubric** — LLM-as-a-judge grading với self-evaluation loop
- **ACP** — Agent Client Protocol cho IDE integration

**Deep Agents Code** (`dcode`) là CLI coding agent built trên SDK — terminal-based coding assistant với sandbox support, MCP tools, web search, và tracing.

## Kiến Trúc Mở Rộng

```
┌──────────────────────────────────────────────────┐
│                  LangChain Core                   │
│  Runnable | LCEL | Prompts | Models | Parsers    │
│  Memory | Tools | Callbacks | Retrievers          │
├──────────────────────────────────────────────────┤
│                   LangGraph                       │
│  StateGraph | Nodes/Edges | Checkpointing         │
│  Streaming | HIL | Multi-Agent                    │
├──────────────────────────────────────────────────┤
│                Deep Agents SDK                    │
│  create_deep_agent | Backends | Memory | Skills   │
│  Subagents | Interpreters | Profiles | ACP        │
├───────────────────────────┬──────────────────────┤
│       LangSmith           │    Deep Agents Code   │
│  Tracing | Evaluation     │   dcode CLI | Sandbox │
│  Datasets | Monitoring    │   MCP | Web Search    │
│  Managed Deep Agents      │   Auto Memory | Skills│
└───────────────────────────┴──────────────────────┘
```

## Nguồn Tham Khảo (Ingested từ raw/)

Wiki đã ingest toàn bộ nội dung từ `raw/langchain_docs/` và `raw/deep_agents_docs/`:

| Chủ Đề | Source Pages | Số File Gốc |
|--------|-------------|-------------|
| **Deep Agents SDK** | [source](../sources/deep-agents-sdk.md) | **30 files** (overview, customization, backends, memory, skills, subagents, streaming, ACP, v.v.) |
| Observability & Tracing | [source](../sources/langsmith-observability.md) | 6 files |
| Evaluation | [source](../sources/langsmith-evaluation.md) | 13 files |
| Deployment & Cloud | [source](../sources/langsmith-deployment.md) | 5 files |
| Datasets & Annotation | [source](../sources/langsmith-datasets-annotation.md) | 4 files |
| Self-hosted | [source](../sources/langsmith-selfhosted.md) | 5 files |
| Prompts & Hub | [source](../sources/langsmith-prompts.md) | 5 files |
| Production Monitoring | [source](../sources/langsmith-production.md) | 4 files |
| Advanced Features | [source](../sources/langsmith-advanced.md) | 7 files |
| Administration & Auth | [source](../sources/langsmith-admin.md) | 9 files |
| Data Management | [source](../sources/langsmith-data-management.md) | 5 files |
| API Reference | [source](../sources/api-reference.md) | ~39 endpoints |

## Trang Liên Quan

- [Entities Index](../entities/index.md) — Các thực thể chính trong ecosystem
- [LangChain Core](../concepts/langchain-core.md) — Framework nền tảng
- [LangGraph Overview](../concepts/langgraph-overview.md) — Agent orchestration
- [LangSmith Overview](../concepts/langsmith-overview.md) — Observability & evaluation
- [LCEL](../concepts/lcel.md) — LangChain Expression Language
- [Deep Agents Overview](../concepts/deep-agents-overview.md) — Deep Agents SDK
- [Agent Architectures](../concepts/agent-architectures.md) — Các mẫu Agent
- [Monitoring](../concepts/monitoring.md) — Production monitoring & alerts
- [Administration](../concepts/administration.md) — Auth, RBAC & billing
