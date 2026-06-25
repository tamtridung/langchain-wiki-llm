---
tags: [langsmith, source, advanced]
created: 2026-06-25
updated: 2026-06-25
sources: [raw/langchain_docs/langsmith/caching.md, raw/langchain_docs/langsmith/custom-endpoint.md, raw/langchain_docs/langsmith/custom-routes.md, raw/langchain_docs/langsmith/custom-store.md, raw/langchain_docs/langsmith/semantic-search.md, raw/langchain_docs/langsmith/context-hub.md, raw/langchain_docs/langsmith/run-evals-api-only.md]
related: [concepts/deployment, concepts/checkpointing, concepts/evaluation]
---

# Nguồn: LangSmith Advanced Features

## Tóm Tắt

7 files về advanced features: caching, custom endpoints, custom store, semantic search, context hub, REST API evals.

## Điểm Then Chốt

### Server-Side Caching (Beta)
- `swr()` (stale-while-revalidate) API
- States: Miss → Fresh → Stale → Expired
- `max_age` capped at 1 ngày
- Yêu cầu Agent Server v0.7.79+

### Custom Endpoints & Routes
- Custom model servers via LangServe
- Custom routes: Starlette (Python) / Hono (TS) via `http.app` trong `langgraph.json`
- Cho phép full web app alongside agent

### Custom Store (Alpha)
- Replace built-in Postgres store với `BaseStore`
- Async context manager pattern
- ⚠️ Replaces built-in store entirely — không fallback

### Semantic Search
- Vector search trên cross-thread store
- Config trong `langgraph.json` với `store.index`
- Dùng pgvector
- ⚠️ Chỉ 1 embedding model per deployment

### Context Hub
- Version-controlled agent instructions/tools
- "Context" = versioned bundle (skill hoặc full agent)
- Environment promotion support

### REST API Evals
- Chạy evaluations không cần SDK — raw HTTP requests
- Manual lifecycle: fetch examples → create experiment → POST runs → close experiment

## Code Mẫu

```python
# SWR caching
from langgraph_sdk.cache import swr
result = await swr(
    "config:global",
    load_config,
    fresh_for=timedelta(minutes=5)
)

# Semantic search
results = await store.asearch(
    namespace=("memory", "facts"),
    query="search query",
    limit=3
)
```

## Trang Liên Quan
- [Deployment](../concepts/deployment.md)
- [Checkpointing](../concepts/checkpointing.md)
- [Evaluation](../concepts/evaluation.md)
