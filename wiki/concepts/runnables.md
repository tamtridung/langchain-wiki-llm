---
tags: [langchain, concept, runnables]
created: 2026-06-25
updated: 2026-06-25
---

# Runnables — Interface Thống Nhất Cho Mọi Component

**Runnable** là interface cốt lõi của LangChain. Mọi component — prompt templates, models, output parsers, retrievers, tools — đều implement `Runnable`.

Điều này có nghĩa: **bất kỳ component nào** cũng có thể `invoke`, `stream`, `batch`, được kết hợp bằng `|`, và tự động tracing.

## Các Method Chính

| Method | Mô Tả | Sync | Async |
|--------|-------|------|-------|
| `invoke(input)` | Chạy một lần với input | ✅ | `ainvoke` |
| `stream(input)` | Stream output từng chunk | ✅ | `astream` |
| `batch(inputs)` | Chạy với list inputs | ✅ | `abatch` |
| `stream_log(input)` | Stream + logs chi tiết | ❌ | `astream_log` |
| `stream_events(input)` | Stream events (v2 API) | ❌ | `astream_events` |

## Các Loại Runnable

### Runnable Sequence
Tạo bởi `\|`. Pipeline tuần tự, output của component trước là input của component sau.

```python
chain = prompt | model | parser
# chain là RunnableSequence
```

### RunnableParallel
Chạy nhiều runnable song song, output là dict.

```python
parallel = RunnableParallel(
    answer = qa_chain,
    summary = summarize_chain
)
```

### RunnablePassthrough
Pass input qua không đổi. Thường dùng với `.assign()` để inject thêm dữ liệu.

```python
chain = (
    RunnablePassthrough.assign(
        context = retriever
    )
    | prompt
    | model
)
```

### RunnableLambda
Bọc function Python bất kỳ thành Runnable.

```python
def process(x: dict) -> str:
    return f"Result: {x['value']}"

runnable = RunnableLambda(process)
```

### RunnableBranch
Routing theo điều kiện. Giống if-else nhưng ở cấp độ graph.

```python
branch = RunnableBranch(
    (condition_fn, true_chain),
    (another_cond, another_chain),
    default_chain
)
```

### RunnableWithMessageHistory
Tự động quản lý lịch sử chat messages.

```python
from langchain_core.runnables.history import RunnableWithMessageHistory

chain = RunnableWithMessageHistory(
    prompt | model | parser,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)
```

### RunnableBinding
Gắn thêm tham số vào runnable (thường cho tool calling).

```python
model_with_tools = model.bind_tools(tools)
# hoặc
model_with_config = model.bind(temperature=0)
```

## Input/Output Types

Mỗi Runnable có kiểu input và output:

```python
class Runnable[Input, Output]:
    def invoke(self, input: Input) -> Output: ...
```

- **PromptTemplate**: Input `dict`, Output `PromptValue`
- **ChatModel**: Input `PromptValue`/messages, Output `AIMessage`
- **StrOutputParser**: Input `AIMessage`, Output `str`
- **Retriever**: Input `str`, Output `list[Document]`

## Error Handling: Fallbacks & Retry

```python
# Fallback - nếu model A lỗi, dùng model B
chain = model_a.with_fallbacks([model_b]) | parser

# Retry với delay
from langchain_core.runnables import RunnableRetry
safe_chain = RunnableRetry(chain, max_retries=3)
```

## Configuration

Runnables support runtime configuration:

```python
chain = prompt | model | parser

# Config model tại runtime
chain.with_config(
    configurable={"model": "gpt-4"},
    tags=["production"],
    metadata={"user_id": "123"}
)
```

## Tracing với Callbacks

Mọi Runnable đều tự động gọi callbacks:

```python
chain.invoke(
    {"topic": "AI"},
    config={"callbacks": [my_handler]}
)
# Hoặc tích hợp LangSmith
# export LANGCHAIN_TRACING_V2=true
```

## Best Practices

1. **Import từ `langchain_core`** — Tránh import từ `langchain` (có thể gây circular dependency)
2. **Dùng type hints** — `Runnable[Dict, str]` giúp IDE hiểu kiểu
3. **Test với `.invoke()` trước** — Rồi mới thêm `.stream()` để tối ưu
4. **Fallback cho production** — Luôn dùng `.with_fallbacks()` cho model calls

## Trang Liên Quan

- [LCEL](lcel.md) — Kết hợp Runnable bằng `|`
- [LangChain Core](langchain-core.md) — Framework nền tảng
