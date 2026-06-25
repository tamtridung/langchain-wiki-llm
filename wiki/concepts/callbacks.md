---
tags: [langchain, concept, callbacks]
created: 2026-06-25
updated: 2026-06-25
---

# Callbacks — Hệ Thống Event/Hooks

**Callbacks** cho phép hook vào các sự kiện trong vòng đời của Runnable — khi bắt đầu, kết thúc, lỗi, stream chunk, v.v. Đây là cơ chế nền tảng cho logging, monitoring, tracing (LangSmith), và custom side-effects.

## Các Event Chính

| Event | Khi Nào Xảy Ra |
|-------|----------------|
| `on_chain_start` | Runnable bắt đầu xử lý |
| `on_chain_end` | Runnable hoàn thành |
| `on_chain_error` | Runnable gặp lỗi |
| `on_llm_start` | LLM call bắt đầu |
| `on_llm_end` | LLM call kết thúc |
| `on_llm_new_token` | Stream chunk mới từ LLM |
| `on_retriever_start` | Retriever bắt đầu tìm kiếm |
| `on_retriever_end` | Retriever trả kết quả |
| `on_tool_start` | Tool bắt đầu chạy |
| `on_tool_end` | Tool hoàn thành |
| `on_tool_error` | Tool gặp lỗi |
| `on_chat_model_start` | Chat model call bắt đầu |

## Tạo Callback Handler

```python
from langchain_core.callbacks import BaseCallbackHandler

class MyCallbackHandler(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs):
        print(f"LLM started with prompts: {prompts}")

    def on_llm_end(self, response, **kwargs):
        print(f"LLM finished. Token usage: {response.llm_output}")

    def on_tool_start(self, serialized, input_str, **kwargs):
        print(f"Tool started: {serialized.get('name')}")

    def on_chain_start(self, serialized, inputs, **kwargs):
        print(f"Chain started")
```

## Sử Dụng Callbacks

### Cách 1: Config trong invoke

```python
handler = MyCallbackHandler()
chain.invoke({"topic": "AI"}, config={"callbacks": [handler]})
```

### Cách 2: Global callbacks

```python
from langchain_core.callbacks import CallbackManager
from langchain_core.tracers import LangChainTracer

manager = CallbackManager([handler])
chain = prompt | model | parser
chain.invoke({"topic": "AI"}, config={"callbacks": manager})
```

### Cách 3: Tag-based filtering

```python
chain.invoke(
    {"topic": "AI"},
    config={
        "callbacks": [handler],
        "tags": ["production", "user-facing"]
    }
)
```

## Async Callbacks

```python
from langchain_core.callbacks import AsyncCallbackHandler

class MyAsyncHandler(AsyncCallbackHandler):
    async def on_llm_start(self, serialized, prompts, **kwargs):
        await log_to_database(prompts)

    async def on_llm_end(self, response, **kwargs):
        await save_trace(response)
```

## Callbacks với LangSmith

LangSmith tracing hoạt động qua callback mechanism:

```python
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "ls__..."
os.environ["LANGCHAIN_PROJECT"] = "my-project"

# Mọi chain call đều tự động trace
chain.invoke({"question": "Hello!"})
```

## Stream Events API (v2)

```python
async for event in chain.astream_events(
    {"topic": "AI"},
    version="v2"
):
    kind = event["event"]
    if kind == "on_chat_model_stream":
        print(event["data"]["chunk"].content, end="")
    elif kind == "on_retriever_end":
        print(f"Retrieved {len(event['data']['output'])} docs")
```

## Use Cases

1. **Logging** — Ghi lại mọi LLM call, tool call
2. **Monitoring** — Đo latency, token usage
3. **Custom Tracing** — Tích hợp với hệ thống monitoring riêng
4. **UI Updates** — Stream từng bước xử lý lên frontend
5. **Rate Limiting** — Đếm số request và giới hạn
6. **Caching** — Cache LLM responses

## Best Practices

1. **Dùng `astream_events`** thay vì callbacks thủ công — dễ dùng hơn
2. **Async handlers** cho I/O operations (DB, API calls)
3. **Không throw exceptions** trong callbacks — có thể làm hỏng chain
4. **Filter bằng tags** — Chỉ gắn handler cho specific chains
5. **LangSmith tracing** cho production — không tự viết handler tracing

## Trang Liên Quan

- [LangChain Core](langchain-core.md) — Framework nền tảng
- [LangSmith Overview](langsmith-overview.md) — Tracing & observability
- [Runnables](runnables.md) — Config với callbacks
