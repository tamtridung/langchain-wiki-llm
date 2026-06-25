---
tags: [langgraph, concept, checkpointing]
created: 2026-06-25
updated: 2026-06-25
---

# Checkpointing — Persistence & Trạng Thái

**Checkpointing** cho phép LangGraph lưu trạng thái của graph sau mỗi node, cho phép:
1. **Resume** — Tiếp tục graph sau khi bị gián đoạn
2. **History** — Xem lại các bước trước đó
3. **Human-in-the-loop** — Dừng chờ xác nhận, sau đó tiếp tục
4. **Time travel** — Quay lại checkpoint cũ và chạy lại

## Checkpointer Types

```python
from langgraph.checkpoint.memory import MemorySaver   # In-memory (dev)
from langgraph.checkpoint.sqlite import SqliteSaver   # SQLite (local)
from langgraph.checkpoint.postgres import PostgresSaver  # PostgreSQL (prod)
from langgraph.checkpoint.aiosqlite import AsyncSqliteSaver  # Async SQLite
```

### MongoDB Checkpointer

Yêu cầu **replica set** — standalone `mongod` không được support:

```python
from langgraph.checkpoint.mongodb import MongoDBSaver

saver = MongoDBSaver.from_conn_string("mongodb://user:pass@host:27017/db?replicaSet=rs0")
```

### Custom Checkpointer (Alpha)

```python
import contextlib
from langgraph.checkpoint import BaseCheckpointSaver

@contextlib.asynccontextmanager
async def generate_checkpointer():
    async with AsyncSqliteSaver.from_conn_string("./checkpoints.db") as saver:
        await saver.setup()
        yield saver

# Server quản lý lifecycle
# Có conformance test suite: langgraph-checkpoint-conformance
```

### Custom Store (Alpha)

Replace built-in Postgres store:

```python
from langgraph.store import BaseStore

class MyCustomStore(BaseStore):
    async def get(self, namespace, key):
        ...
    async def search(self, namespace, query, limit):
        ...
    async def put(self, namespace, key, value):
        ...
    async def delete(self, namespace, key):
        ...

# ⚠️ Khi config custom store, nó REPLACES built-in store entirely
# Không fallback - phải tự implement TTL sweeping, semantic search
```

### Checkpointer Requirements (Production Deployment)

Khi deploy LangGraph Agent Server:
- **PostgreSQL** luôn required cho threads/runs/assistants/crons/store
- Chỉ có checkpoint data mới switch được (Postgres vs MongoDB)
- Không config checkpointer trong graph code — server tự inject

## Sử Dụng Cơ Bản

```python
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()

app = graph.compile(checkpointer=memory)

# Thread ID — xác định session
config = {"configurable": {"thread_id": "user-session-1"}}

# Lần 1
result = app.invoke(
    {"messages": [("human", "Hi, I'm John")]},
    config=config
)

# Lần 2 — app nhớ context từ lần 1
result = app.invoke(
    {"messages": [("human", "What's my name?")]},
    config=config
)
# → "Your name is John"
```

## Time Travel — Quay Lại Quá Khứ

```python
# Xem tất cả checkpoints
states = []
async for state in app.astate_history(config):
    states.append(state)
# states[0] = hiện tại, states[-1] = đầu tiên

# Quay lại checkpoint cụ thể
checkpoint = states[2]  # Checkpoint thứ 3
config["configurable"]["checkpoint_id"] = checkpoint["configurable"]["checkpoint_id"]

# Chạy từ checkpoint đó với input mới
app.invoke(
    {"messages": [("human", "Actually, forget that. Let's start over.")]},
    config=config
)
```

## Checkpointing với Human-in-the-Loop

```python
graph = StateGraph(AgentState)
# ... define nodes ...

# Compile với interrupt_before
app = graph.compile(
    checkpointer=MemorySaver(),
    interrupt_before=["tools"]  # Dừng trước mỗi tool call
)

# Chạy — sẽ dừng trước khi gọi tool
result = app.invoke(
    {"messages": [("human", "Send email to john@example.com")]},
    config=config
)

# Kiểm tra tool call đang chờ
pending_tool_calls = result["messages"][-1].tool_calls

# User xác nhận → tiếp tục
app.invoke(
    None,  # Không input mới, chỉ resume
    config=config
)
```

## Get & Update State

```python
# Lấy state hiện tại
state = app.get_state(config)
print(state.values["messages"][-1])

# Update state (thêm/sửa message)
app.update_state(
    config,
    {"messages": [AIMessage(content="Modified response")]},
)

# Lấy state history
for state in app.get_state_history(config):
    print(state.next, state.values["messages"][-1].content[:50])
```

## Production Checkpointing

### PostgreSQL (Production)

```python
from langgraph.checkpoint.postgres import PostgresSaver

conn_string = "postgresql://user:pass@host:5432/langgraph"
saver = PostgresSaver.from_conn_string(conn_string)

# Lần đầu: setup tables
saver.setup()

app = graph.compile(checkpointer=saver)
```

### Redis

```python
from langgraph.checkpoint.redis import RedisSaver

saver = RedisSaver.from_conn_string("redis://localhost:6379")
app = graph.compile(checkpointer=saver)
```

## Best Practices

1. **Dev: `MemorySaver`** — Nhanh, không cần setup
2. **Prod: `PostgresSaver`** — Persistent, scalable
3. **Luôn dùng `thread_id`** — Xác định session duy nhất
4. **Giới hạn history** — Xoá checkpoint cũ nếu cần (storage)
5. **Time travel** — Cực kỳ hữu ích cho debugging

## Trang Liên Quan

- [LangGraph Overview](langgraph-overview.md) — Tổng quan
- [Human-in-the-loop](human-in-the-loop.md) — HIL với checkpointing
- [Streaming](streaming.md) — Stream với checkpointing
