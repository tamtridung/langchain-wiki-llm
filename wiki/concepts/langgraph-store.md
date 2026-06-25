---
tags: [langgraph, concept, store, memory]
created: 2026-06-25
updated: 2026-06-25
related: [concepts/checkpointing, concepts/memory, concepts/langgraph-sdk]
---

# LangGraph Store — Persistent Key-Value Storage

**Store** là namespaced key-value store trong LangGraph Agent Server, cho phép agents lưu trữ và truy xuất dữ liệu persistent giữa các threads và sessions.

## Kiến Trúc

```
Store Namespace Hierarchy:
(namespace: tuple[str, ...]) → key → value

Ví dụ:
("memory", "facts") → "user_123" → {"name": "John", "preferences": {...}}
("agent", "config")  → "my-agent"  → {"model": "gpt-4", "temperature": 0}
```

## SDK Usage

```python
from langgraph_sdk import get_client
client = get_client()

# Store/update an item
await client.store.put(
    namespace=("memory", "facts"),
    key="user_123",
    value={"name": "John", "last_seen": "2026-06-25"}
)

# Retrieve
item = await client.store.get(
    namespace=("memory", "facts"),
    key="user_123"
)

# Search within namespace
results = await client.store.search(
    namespace=("memory",),
    query="John",
    limit=10
)

# List namespaces
namespaces = await client.store.list_namespaces(
    prefix=("memory",),
    max_depth=2
)

# Delete
await client.store.delete(
    namespace=("memory", "facts"),
    key="user_123"
)
```

## Semantic Search

Khi configured với embedding model, store hỗ trợ semantic search:

```json
// langgraph.json
{
  "store": {
    "index": {
      "embedding": "openai:text-embedding-3-small"
    }
  }
}
```

```python
# Semantic search across namespace
results = await store.asearch(
    namespace=("memory", "facts"),
    query="What does John like?",
    limit=5
)
# results[0].score — similarity score
```

⚠️ **Chỉ 1 embedding model per deployment** — thay đổi model cần re-embed tất cả.

## Use Cases

| Use Case | Namespace | Key | Value |
|----------|-----------|-----|-------|
| User profiles | `("users",)` | user_id | Profile data |
| Session state | `("sessions",)` | session_id | Conversation context |
| Agent config | `("config", "agents")` | agent_id | Instructions, tools |
| Knowledge base | `("knowledge",)` | doc_id | Document chunks |
| Feature flags | `("flags",)` | feature_name | Boolean/config |

## API Endpoints

Agent Server cung cấp 5 REST endpoints cho store operations:
- `PUT /store/items` — Store/update an item
- `GET /store/items` — Retrieve a single item
- `POST /store/items/search` — Search items
- `GET /store/namespaces` — List namespaces
- `DELETE /store/items` — Delete an item

## Custom Store

Có thể replace built-in Postgres store với `BaseStore` implementation (alpha):

```python
from langgraph.store import BaseStore

class MyCustomStore(BaseStore):
    async def get(self, namespace, key): ...
    async def search(self, namespace, query, limit): ...
    async def put(self, namespace, key, value): ...
    async def delete(self, namespace, key): ...
```

## Best Practices

1. **Namespace hierarchy** — Dùng tuple phân cấp (`("domain", "subdomain")`)
2. **JSON-serializable values** — Store chỉ chấp nhận JSON-compatible data
3. **Semantic search cho text** — Dùng `asearch` cho natural language queries
4. **Cache thường xuyên truy cập** — Store calls có network latency
5. **Không lưu secrets** — Dùng workspace secrets thay vì store

## Trang Liên Quan
- [Checkpointing](checkpointing.md) — Thread-level persistence
- [Memory](memory.md) — Conversation memory
- [LangGraph SDK](langgraph-sdk.md) — SDK reference
- [Deployment](deployment.md) — Store configuration
