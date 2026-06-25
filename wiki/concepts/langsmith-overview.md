---
tags: [langsmith, concept, observability]
created: 2026-06-25
updated: 2026-06-25
---

# LangSmith Overview — Observability, Evaluation & Testing

**LangSmith** là nền tảng cho **observability**, **evaluation**, và **testing** của LangChain ecosystem. Nó cung cấp:

1. **Tracing** — Ghi lại mọi bước xử lý (LLM calls, retrieval, tool calls)
2. **Evaluation** — Đánh giá chất lượng output so với datasets
3. **Datasets** — Quản lý bộ dữ liệu test
4. **Monitoring** — Dashboard real-time cho production
5. **Hub/Prompts** — Version control cho prompts
6. **Annotation** — Human feedback và labelling

## Architecture

```
┌────────────────────────────────────────────┐
│            LangSmith Platform              │
│                                            │
│  ┌─────────┐  ┌──────────┐  ┌──────────┐  │
│  │ Tracing │  │Evaluation│  │ Datasets │  │
│  └─────────┘  └──────────┘  └──────────┘  │
│  ┌─────────┐  ┌──────────┐  ┌──────────┐  │
│  │Monitoring│  │  Hub/    │  │Annotation│  │
│  │         │  │  Prompts │  │  Queues  │  │
│  └─────────┘  └──────────┘  └──────────┘  │
└────────────────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────────┐
│            SDK Integration             │
│  LangChain │ LangGraph │ Any LLM App  │
└────────────────────────────────────────┘
```

## Quick Start

```python
import os
from langchain_openai import ChatOpenAI
from langsmith import Client

# 1. Setup environment
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "ls__..."
os.environ["LANGCHAIN_PROJECT"] = "my-project"

# 2. Tracing tự động
model = ChatOpenAI(model="gpt-4")
response = model.invoke("Hello!")
# → Tự động trace vào LangSmith project

# 3. Client SDK
client = Client()
```

## Core Concepts

### Projects
Container cho tất cả traces từ một ứng dụng:

```python
os.environ["LANGCHAIN_PROJECT"] = "my-rag-app"
```

### Traces & Runs
- **Trace** — Một lần gọi ứng dụng (một câu hỏi)
- **Run** — Một bước trong trace (LLM call, retrieval, tool call)

### Datasets
Bộ dữ liệu input-output để test:

```python
client.create_dataset("my-test-set")
client.create_example(
    dataset_name="my-test-set",
    inputs={"question": "What is LangChain?"},
    outputs={"answer": "A framework for LLM apps."}
)
```

### Experiments
So sánh nhiều phiên bản chain/agent:

```python
experiment = client.evaluate(
    chain,
    data="my-test-set",
    evaluators=[correctness_evaluator],
)
```

## Key Features

| Feature | Use Case |
|---------|----------|
| Tracing | Debug, understand flow |
| Distributed Tracing | Propagate traces across services |
| Conditional Tracing | Per-request/per-tenant control |
| Evaluation | Compare prompts/models/chains/graphs |
| Datasets | Versioned test data with tagging |
| Annotation Queues | Human feedback with rubric & assignments |
| Pairwise Annotation | Side-by-side A/B comparison |
| Hub/Prompts | Prompt versioning with env promotion |
| Monitoring | Production alerts, dashboards, cost tracking |
| Insights | AI-powered trace analysis |
| Playground | Interactive prompt editor |
| A/B Testing | Compare configurations |
| Context Hub | Versioned agent instructions & tools |
| Semantic Search | Cross-thread vector search |
| Cron Jobs | Scheduled agent runs |
| Background Runs | Non-blocking long-running tasks |
| Server-Side Caching | SWR caching pattern |

## Data Model

```
Project (ứng dụng)
  └── Trace (một operation)
        └── Run (một bước: LLM call, retrieval, tool call)
              └── Feedback (scores, comments)
Threads: liên kết traces qua multi-turn (session_id/thread_id/conversation_id)
```

- Max **25,000 runs per trace**
- Data retention: **400 ngày** (SaaS), configurable (self-hosted)
- Base retention: 14 ngày, Extended: up to 400 ngày

## Instrumentation Methods

1. **Integrations** — Auto-instrumentation (LangChain, OpenAI, Anthropic, CrewAI, Vercel AI SDK, Pydantic AI...)
2. **`@traceable` decorator** — Simple function decorator
3. **`trace` context manager** — `with trace("name", run_type="chain"):`
4. **`RunTree`** — Low-level API
5. **`TracingMiddleware`** — ASGI/FastAPI/Starlette cho distributed tracing

## Pricing

| Plan | Traces (month) | Key Features |
|------|---------------|-------------|
| **Developer** | 5K (free) | 1 project, basic tracing |
| **Plus** | 10K | Unlimited projects, annotations, evaluations |
| **Enterprise** | Custom | SSO, self-hosted, audit logs, custom auth |

## Integrations

LangSmith hỗ trợ tracing cho hầu hết các LLM providers và frameworks:
- **Model providers**: OpenAI, Anthropic, Google, AWS Bedrock, Azure, Ollama, v.v.
- **Frameworks**: LangChain, LangGraph, CrewAI, AutoGen, Claude Agent SDK, Vercel AI SDK, Pydantic AI
- **Observability**: OpenTelemetry export

## Trang Liên Quan

- [Tracing](tracing.md) — Observability & tracing
- [Evaluation](evaluation.md) — Evaluation framework
- [Datasets](datasets.md) — Datasets management
- [Deployment](deployment.md) — LangServe & deployment
