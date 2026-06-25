---
tags: [langsmith, concept, tracing, observability]
created: 2026-06-25
updated: 2026-06-25
---

# Tracing — Observability & Ghi Lại Mọi Bước Xử Lý

**Tracing** ghi lại mọi bước xử lý trong ứng dụng LLM — từ input, LLM calls, retrieval, tool calls, đến output cuối cùng. LangSmith tracing là **zero-instrumentation** cho LangChain/LangGraph apps.

## How Tracing Works

```
User: "What's weather in Hanoi?"
         │
         ▼
    ┌─────────┐     Trace
    │  Chain   │ ───────────────────┐
    │          │                    │
    ├─────────┤                    │
    │ Prompt  │ ─── Run ────────── │
    ├─────────┤                    │
    │ LLM     │ ─── Run ────────── │  LangSmith
    │ (GPT-4) │   (tokens, cost)   │  Platform
    ├─────────┤                    │
    │ Tool    │ ─── Run ────────── │
    │(Weather)│   (input, output)  │
    ├─────────┤                    │
    │ Parser  │ ─── Run ────────── │
    └─────────┘                    │
         │                         │
         ▼                         ▼
    "It's sunny..."           Dashboard
```

## Setup Tracing

### Cách 1: Environment Variables

```bash
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=ls__...
export LANGCHAIN_PROJECT=my-project
```

### Cách 2: Python SDK

```python
from langsmith import Client

client = Client(
    api_url="https://api.smith.langchain.com",
    api_key="ls__..."
)
```

### Cách 3: LangGraph với Tracing

```python
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

# Tự động trace khi LANGCHAIN_TRACING_V2=true
agent = create_react_agent(model, tools, checkpointer=MemorySaver())
```

## Tracing Components

### Project-level

```python
# Mỗi project chứa tất cả traces của một app
os.environ["LANGCHAIN_PROJECT"] = "my-rag-app-v2"

# Hoặc dynamic
from langchain_core.callbacks import configure_metadata
chain.invoke(input, config={"metadata": {"version": "v2"}})
```

### Custom Run Metadata

```python
chain.invoke(
    {"question": "Hello"},
    config={
        "run_name": "my-custom-chain",
        "tags": ["production", "user-facing"],
        "metadata": {
            "user_id": "123",
            "session": "abc",
        }
    }
)
```

### Add Metadata to Runs

```python
from langchain_core.callbacks import BaseCallbackHandler

class MetadataHandler(BaseCallbackHandler):
    def on_chain_start(self, serialized, inputs, **kwargs):
        # Add custom metadata
        kwargs.get("metadata", {}).update({
            "environment": "staging",
            "timestamp": time.time()
        })
```

## Nested Traces

```python
# Runs tự động nest theo cấu trúc chain
# chain a → chain b → LLM
# Sẽ tạo trace: a (b (LLM))

# Nếu cần trace riêng:
from langsmith import traceable

@traceable(name="custom_function")
def my_function(x):
    return process(x)
```

## Distributed Tracing

Propagate traces giữa các microservices:

```python
from langsmith.run_helpers import get_current_run_tree

# Client: propagate trace headers
headers = {}
if run_tree := get_current_run_tree():
    headers.update(run_tree.to_headers())
    # Headers: langsmith-trace, baggage

# Service nhận: dùng TracingMiddleware
from langsmith.tracing import TracingMiddleware
from fastapi import FastAPI

app = FastAPI()
app.add_middleware(TracingMiddleware)
# Hoặc manual:
from langsmith.run_helpers import tracing_context
with tracing_context(parent=request_headers):
    result = process(request)
```

⚠️ **Security**: Chỉ accept distributed-tracing headers từ trusted services. Không expose `TracingMiddleware` ở public endpoints.

## Conditional Tracing

Kiểm soát tracing theo request/tenant với 3 levels (ưu tiên giảm dần):

```python
from langsmith import tracing_context as ls_tracing_context

# Level 1 (highest): Per-request control
with ls_tracing_context(enabled=False):
    result = process_pii(data)  # Không được trace

# Level 2: Global toggle
import langsmith
langsmith.configure(enabled=False)

# Level 3: Environment variable
# export LANGSMITH_TRACING=false
```

Use cases:
- **Per-tenant tracing** — Chỉ trace cho Enterprise customers
- **PII gating** — Không trace requests chứa PII
- **Sampling** — Chỉ trace 10% requests

## Trace Data Model & Limits

```
Project
  └── Trace (một operation, max 25,000 runs)
        └── Run (LLM call, retrieval, tool call, ...)
              └── Feedback (scores, comments)
Threads: Liên kết traces qua metadata keys (session_id, thread_id, conversation_id)
```

- **Max 25,000 runs per trace** — vượt quá sẽ bị reject
- **Data retention**: 400 ngày (SaaS), configurable (self-hosted)
- **Threads**: Cho phép multi-turn conversations tracking

## Threading & Conversations

```python
# Trace multi-turn conversations
from langsmith import traceable

@traceable(metadata={"thread_id": "user-123", "session_id": "sess-abc"})
def chat_turn(message: str) -> str:
    return model.invoke(message)

# Tất cả traces với cùng thread_id được group lại
```

## Dynamic Project Routing

```python
# Static: env var
export LANGCHAIN_PROJECT=my-project

# Dynamic per-call
@traceable(project_name="experiment-v2")
def my_function(x):
    return process(x)
```

## Nested Traces & Async (Python < 3.11)

Python < 3.11 không propagate contextvars tự động qua asyncio:

```python
# Fix: manually pass config
chain.invoke(input, config={"callbacks": [handler]})

# Hoặc parent RunTree
from langsmith.run_trees import RunTree
parent = RunTree(name="parent", run_type="chain")
child = parent.create_child(name="child", run_type="llm")
```

## Viewing Traces

LangSmith UI cung cấp:

1. **Trace view** — Tree view của tất cả runs
2. **Timeline** — Thời gian thực hiện từng bước
3. **Token usage** — Số tokens, cost estimate
4. **Input/Output** — Chi tiết từng bước
5. **Feedback** — User ratings và annotations
6. **Comparison** — So sánh nhiều traces cạnh nhau

## Tracing với Non-LangChain Apps

```python
from langsmith import traceable
from openai import OpenAI

client = OpenAI()

@traceable(name="my_openai_call", run_type="llm")
def call_openai(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

result = call_openai("Explain AI")
```

## Cost Tracking

```python
# Tự động tracking cost cho supported providers
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# View cost trong LangSmith dashboard
# Cần set model pricing nếu dùng model custom
```

## Best Practices

1. **Luôn bật tracing trong development** — Debug nhanh hơn 10x
2. **Dùng tags** — `tags=["staging", "v2.1"]` để filter traces
3. **Metadata cho business context** — user_id, session_id, feature_flag
4. **Tên run có nghĩa** — `run_name="qa_chain_v3"` dễ tìm hơn `RunnableSequence`
5. **Tracing trong production** — Không ảnh hưởng latency, chỉ thêm ~5ms

## Trang Liên Quan

- [LangSmith Overview](langsmith-overview.md) — Tổng quan
- [Evaluation](evaluation.md) — Đánh giá với traces
- [Datasets](datasets.md) — Tạo datasets từ traces
- [Callbacks](callbacks.md) — Callback mechanism
