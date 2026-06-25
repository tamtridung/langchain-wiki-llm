---
tags: [langsmith, source, observability, tracing]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/observability.md, raw/langchain_docs/langsmith/observability-concepts.md, raw/langchain_docs/langsmith/distributed-tracing.md, raw/langchain_docs/langsmith/conditional-tracing.md, raw/langchain_docs/langsmith/log-traces-to-project.md, raw/langchain_docs/langsmith/nest-traces.md]
related: [concepts/tracing, concepts/langsmith-overview]
---

# Nguồn: LangSmith Observability & Tracing

## Tóm Tắt Các File

6 files từ `raw/langchain_docs/langsmith/` về observability và tracing trong LangSmith.

## Điểm Then Chốt

### Data Model
- **Project → Trace → Run → Thread** là hệ thống phân cấp dữ liệu
- Trace = tập hợp các runs cho một operation duy nhất (tương tự OpenTelemetry)
- Threads liên kết traces qua nhiều turn hội thoại dùng metadata keys (`session_id`, `thread_id`, `conversation_id`)
- Max **25,000 runs per trace** — vượt quá sẽ bị reject
- Data retention SaaS: **400 ngày**, sau đó xoá vĩnh viễn

### Instrumentation Methods (4 cách)
1. **Integrations** — Auto-instrumentation cho LangChain, OpenAI, Anthropic, CrewAI...
2. **`@traceable` decorator** — Decorator đơn giản cho function
3. **`trace` context manager** — `with trace("name", run_type="chain") as rt:`
4. **`RunTree`** — Low-level API cho custom tracing

### Distributed Tracing
- Propagate traces giữa các services qua headers: `langsmith-trace` và `baggage`
- Dùng `TracingMiddleware` (ASGI/FastAPI/Starlette) — thêm từ `langsmith==0.1.133`
- ⚠️ **Security**: Chỉ accept distributed-tracing headers từ trusted services

### Conditional Tracing
- 3 levels (ưu tiên từ cao xuống thấp):
  1. `tracing_context(enabled=...)` — highest
  2. `ls.configure(enabled=...)` 
  3. Environment variables
- Dùng để: per-tenant tracing, PII-gating, selective sampling

### Project Routing
- Static: `LANGSMITH_PROJECT` env var
- Dynamic: `project_name` param trên `@traceable`/`langsmith_extra`

### Nesting & Troubleshooting
- Python < 3.11: async contextvars không propagate tự động
- Fix: manually pass `config` (LangChain) hoặc `parent` RunTree (LangSmith)

## Code Mẫu

```python
# Conditional tracing - skip sensitive data
with ls.tracing_context(enabled=False):
    result = process_pii(data)

# Dynamic project routing
@traceable(project_name="production-v2")
def my_function(x):
    return process(x)

# Distributed tracing - propagate headers
from langsmith.run_helpers import get_current_run_tree
if run_tree := get_current_run_tree():
    headers.update(run_tree.to_headers())
```

## Trích Dẫn
> "Runs are like spans in OpenTelemetry. They represent a unit of work — an LLM call, a retrieval step, or a formatting operation."

## Trang Liên Quan
- [Tracing](../concepts/tracing.md)
- [LangSmith Overview](../concepts/langsmith-overview.md)
- [Callbacks](../concepts/callbacks.md)
