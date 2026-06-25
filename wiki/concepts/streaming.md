---
tags: [langgraph, langchain, concept, streaming]
created: 2026-06-25
updated: 2026-06-25
---

# Streaming — Stream Kết Quả Theo Thời Gian Thực

**Streaming** cho phép nhận kết quả từ LLM khi chúng đang được sinh ra, thay vì chờ toàn bộ response. LangChain và LangGraph hỗ trợ nhiều cấp độ streaming.

## Các Cấp Độ Streaming

| Level | Mô Tả | Method |
|-------|-------|--------|
| **Token** | Từng token của LLM | `astream` / `astream_events` |
| **Node** | Kết quả từ mỗi node trong graph | `astream` (LangGraph) |
| **Event** | Cấu trúc events chi tiết | `astream_events` (v2) |

## 1. LCEL Streaming

```python
# Từng chunk
for chunk in chain.stream({"topic": "AI"}):
    print(chunk, end="")

# Async
async for chunk in chain.astream({"topic": "AI"}):
    print(chunk, end="")
```

## 2. LangGraph Streaming

```python
# Stream kết quả từ mỗi node
for event in app.stream(
    {"messages": [("human", "What's weather?")]},
    config=config,
    stream_mode="values"  # values, updates, debug, custom
):
    messages = event.get("messages", [])
    if messages:
        messages[-1].pretty_print()

# Stream modes:
# - "values": Toàn bộ state sau mỗi node
# - "updates": Chỉ partial updates từ node
# - "debug": Debug info
# - "custom": Custom event

# Async
async for event in app.astream(
    input_data,
    config=config,
    stream_mode="updates"
):
    for node_name, update in event.items():
        print(f"Node: {node_name}")
        print(f"Update: {update}")
```

## 3. Stream Events API (v2)

```python
async for event in chain.astream_events(
    {"topic": "AI"},
    version="v2"
):
    kind = event["event"]
    tags = event.get("tags", [])
    
    if kind == "on_chat_model_stream":
        # Từng token từ LLM
        chunk = event["data"]["chunk"]
        print(chunk.content, end="")
    
    elif kind == "on_chain_start":
        print(f"Starting: {event['name']}")
    
    elif kind == "on_chain_end":
        print(f"Completed: {event['name']}")
    
    elif kind == "on_tool_start":
        print(f"Tool: {event['name']}")
        print(f"Input: {event['data']['input']}")
    
    elif kind == "on_tool_end":
        print(f"Tool output: {event['data']['output']}")
    
    elif kind == "on_retriever_end":
        print(f"Retrieved {len(event['data']['output'])} docs")
```

## 4. Streaming với Multiple Outputs

```python
# Với RunnableParallel
chain = RunnableParallel(
    answer=qa_chain,
    summary=summary_chain,
)

# Stream từng output riêng
async for event in chain.astream_events(input, version="v2"):
    if event["event"] == "on_parser_end":
        # Parser hoàn thành cho một nhánh
        print(f"{event['name']}: {event['data']['output']}")
```

## 5. LangGraph Token Streaming

```python
from langchain_core.callbacks import BaseCallbackHandler

class TokenCollector(BaseCallbackHandler):
    def __init__(self):
        self.tokens = []
    
    def on_llm_new_token(self, token, **kwargs):
        self.tokens.append(token)
        print(token, end="")

# Gắn callback vào node
def agent_node(state):
    collector = TokenCollector()
    response = model.invoke(
        state["messages"],
        config={"callbacks": [collector]}
    )
    return {"messages": [response]}

# Hoặc dùng astream_events với LangGraph
async for event in app.astream_events(input, version="v2"):
    if event["event"] == "on_chat_model_stream":
        print(event["data"]["chunk"].content, end="")
```

## 6. Streaming trong Web App (FastAPI)

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

@app.post("/chat")
async def chat(request: dict):
    async def generate():
        async for event in agent.astream_events(
            {"messages": [("human", request["message"])]},
            version="v2"
        ):
            if event["event"] == "on_chat_model_stream":
                token = event["data"]["chunk"].content
                yield f"data: {token}\n\n"
            elif event["event"] == "on_tool_start":
                yield f"data: [Tool: {event['name']}]\n\n"
    
    return StreamingResponse(generate(), media_type="text/event-stream")
```

## Stream Mode Comparison

| Mode | LangGraph | LCEL | Use Case |
|------|-----------|------|----------|
| `values` | ✅ | ✅ | UI updates, show progress |
| `updates` | ✅ | ❌ | Fine-grained diffs |
| `events` (v2) | ✅ | ✅ | Streaming tokens, tool calls |
| `debug` | ✅ | ❌ | Development/debugging |
| `custom` | ✅ | ❌ | Custom event types |

## Best Practices

1. **Dùng `astream_events` (v2)** — Tương thích cả LCEL và LangGraph
2. **Stream cho UX** — User thấy agent đang làm gì (typing indicator)
3. **Tool calls trước, content sau** — Show "Đang tra cứu..." rồi mới stream answer
4. **Backpressure** — Đừng stream quá nhanh, dùng queue nếu cần
5. **Cache chunks** — Để có thể reconnect nếu mất kết nối

## Trang Liên Quan

- [LangGraph Overview](langgraph-overview.md) — LangGraph streaming
- [Callbacks](callbacks.md) — Callback handlers
- [Runnables](runnables.md) — Runnable streaming
