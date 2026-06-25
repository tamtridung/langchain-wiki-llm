---
tags: [langserve, concept, deployment]
created: 2026-06-25
updated: 2026-06-25
---

# LangServe & Deployment — Triển Khai Ứng Dụng LangChain

**LangServe** là framework để triển khai LangChain chains/agents thành REST APIs. Tự động sinh API endpoints từ Runnable.

## LangServe — Deploy as API

### Quick Start

```python
# serve.py
from fastapi import FastAPI
from langserve import add_routes
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

app = FastAPI(
    title="My LangChain API",
    version="1.0",
)

# Chain
prompt = ChatPromptTemplate.from_template("Tell me a {topic} joke")
chain = prompt | ChatOpenAI() | StrOutputParser()

# Tự động sinh REST API
add_routes(app, chain, path="/joke")

# Chạy: python -m uvicorn serve:app --reload

# Endpoints tự động:
# POST /joke/invoke
# POST /joke/stream
# POST /joke/batch
# POST /joke/stream_log
# GET  /joke/input_schema
# GET  /joke/output_schema
# GET  /joke/config_schema
```

### Client

```python
from langserve import RemoteRunnable

# Gọi API như local Runnable
remote = RemoteRunnable("http://localhost:8000/joke")
result = remote.invoke({"topic": "programming"})

# Stream cũng hoạt động
for chunk in remote.stream({"topic": "programming"}):
    print(chunk, end="")
```

### LangGraph với LangServe

```python
from langserve import add_routes
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(model, tools, checkpointer=memory)

add_routes(
    app,
    agent,
    path="/agent",
    # LangGraph config
    per_reply_config={
        "configurable": {"thread_id": "123"}
    }
)
```

## LangGraph Platform

LangGraph cung cấp nền tảng deployment riêng mạnh mẽ hơn LangServe:

### LangGraph.json

```json
{
  "python_version": "3.12",
  "dependencies": ["."],
  "graphs": {
    "agent": "./agent.py:graph"
  },
  "env": ".env",
  "store": {
    "index": {
      "embedding": "openai:text-embedding-3-small"
    }
  }
}
```

### LangGraph Cloud

```bash
# Deploy lên LangGraph Cloud
langgraph deploy

# Hoặc tự host
langgraph build --tag my-agent:latest
docker run -e OPENAI_API_KEY=$KEY my-agent:latest
```

Deployment tạo sẵn:
- REST API endpoints
- WebSocket streaming
- Background runs (cron jobs)
- Human-in-the-loop support
- Monitoring với LangSmith

## Agent Server Architecture

LangGraph Agent Server quản lý vòng đời agent qua 3 concepts:

```
Assistants (config prompt/tools) 
  → Threads (state per conversation) 
    → Runs (execute workload)
```

### Runtime Modes
| Mode | Mô Tả | Khi Nào Dùng |
|------|-------|-------------|
| **Single host** | Một process cho API + queue | Development |
| **Split API/queue** | Tách biệt API servers và queue workers | Production scalable |
| **Distributed** | Nhiều replicas, high concurrency | Enterprise, >500 req/s |

⚠️ **Important**: 
- Queue workers = execution engine; API servers chỉ handle requests
- Server tự động inject checkpointer và memory store — **không config trong graph code**
- Graphs nên dùng **compiled graphs** (load 1 lần), không phải factory functions

### Cron Jobs

```python
from langgraph_sdk import get_client

client = get_client()

# Schedule daily summary at 8 PM UTC
await client.crons.create(
    thread_id=thread["thread_id"],
    assistant_id="agent",
    schedule="0 20 * * *",  # cron expression (UTC)
    input={"messages": [{"role": "user", "content": "daily summary"}]},
)
```

### Background Runs

```python
# Non-blocking execution
await client.runs.create(
    thread["thread_id"],
    "agent",
    input=input_data
)
```

## Self-hosted Deployment

Yêu cầu **Enterprise license** và **Kubernetes** (Helm charts provided).

### Architecture Components
```
Frontend UI → Backend API → Platform Backend → Queue → ACE Backend
Databases: ClickHouse (traces), PostgreSQL (ops), Redis (queuing), Blob (artifacts)
```

### Scaling Guide
| Load | Traces/s | Platform Backend | Queue | ClickHouse |
|------|----------|-----------------|-------|-----------|
| Low | 50 | 3 replicas | 4 | Single node |
| Medium | 200 | 8 replicas | 10 | 2 nodes |
| High | 1000 | 20 replicas | 24 | 3 replicas |

### TTL & Data Retention
- `longlived`: 400 ngày mặc định (configurable)
- `shortlived`: 14 ngày mặc định
- ClickHouse cleanup: chạy weekends (expensive operation)

### Requirements
- KEDA (Kubernetes Event-driven Autoscaling) recommended
- Có thể externalize: AWS RDS (Postgres), ElastiCache (Redis)

## Server-Side Caching (Beta)

```python
from langgraph_sdk.cache import swr
from datetime import timedelta

# Stale-while-revalidate pattern
result = await swr(
    "config:global",
    load_config,
    fresh_for=timedelta(minutes=5),  # fresh period
)
# States: Miss → Fresh → Stale → Expired
# max_age capped at 1 day
```

## Custom Routes

Thêm web routes bên cạnh agent:

```json
// langgraph.json
{
  "http": {
    "app": "./custom_app.py:app",  // Starlette (Python) or Hono (TS)
    "path": "/webhook"
  }
}
```

## Deployment Options

| Option | Use Case | Complexity |
|--------|----------|------------|
| **LangServe + FastAPI** | Simple chain API | Thấp |
| **LangGraph Cloud** | Full agent deployment via UI/CLI | Thấp |
| **LangGraph + Docker** | Containerized custom deployment | Trung bình |
| **Self-hosted (K8s)** | Enterprise control, data residency | Cao |
| **Standalone server** | Docker + Postgres/Redis, no control plane | Trung bình |
| **AWS/GCP/Azure** | Cloud infrastructure | Cao |

## Production Checklist

- [ ] **Rate limiting** — Tránh abuse (slowloris, DDoS)
- [ ] **Authentication** — API keys, JWT, OAuth, custom auth
- [ ] **Caching** — SWR caching pattern
- [ ] **Monitoring** — LangSmith tracing, alerts, dashboards
- [ ] **Error handling** — Graceful degradation, fallbacks
- [ ] **Logging** — Request/response logging
- [ ] **Streaming** — Server-Sent Events (SSE) cho UX
- [ ] **Timeout** — Configurable timeout mỗi request
- [ ] **Cost control** — Max tokens, budget alerts
- [ ] **Data retention** — Configure TTL policies

## Trang Liên Quan

- [LangSmith Overview](langsmith-overview.md) — Monitoring deployed apps
- [Tracing](tracing.md) — Trace production requests
- [LangGraph Overview](langgraph-overview.md) — LangGraph deployment
