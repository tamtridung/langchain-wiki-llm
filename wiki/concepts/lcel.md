---
tags: [langchain, concept, lcel]
created: 2026-06-25
updated: 2026-06-25
---

# LCEL — LangChain Expression Language

**LCEL (LangChain Expression Language)** là cú pháp khai báo (declarative) để kết hợp các Runnable component bằng toán tử `|` (pipe), giống pipeline trong Unix.

## Cú Pháp Cơ Bản

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template(
    "Translate to {language}: {text}"
)
model = ChatOpenAI(model="gpt-4")
parser = StrOutputParser()

# LCEL pipeline - đây là một RunnableSequence
chain = prompt | model | parser

# Sử dụng
result = chain.invoke({"language": "Vietnamese", "text": "Hello, world!"})
# -> "Xin chào thế giới!"
```

## Các Toán Tử LCEL

| Toán Tử | Ý Nghĩa | Ví Dụ |
|----------|---------|-------|
| `|` | Pipe — output của component trước vào component sau | `prompt \| model` |
| `\|` (với dict) | Chạy song song | `{"ctx": ctx \| model, "input": original}` |
| `.pipe()` | Tương đương `\|` | `prompt.pipe(model)` |

## Tại Sao LCEL Mạnh?

LCEL không chỉ là syntactic sugar. Nó cung cấp **tự động**:

- **Streaming** — Component cuối support stream → toàn bộ chain stream được
- **Async** — `ainvoke`, `astream` hoạt động ngay
- **Batch** — `batch` với nhiều input cùng lúc
- **Retry & Fallback** — Tích hợp sẵn error handling
- **Tracing** — LangSmith tracing tự động
- **Parallelism** — `RunnableParallel` chạy đồng thời
- **Configuration** — Chain có thể config tại runtime

## Các Pattern LCEL Quan Trọng

### 1. RunnableParallel — Chạy Song Song

```python
from langchain_core.runnables import RunnableParallel

chain = (
    RunnableParallel(
        context=retriever,
        question=RunnablePassthrough()
    )
    | prompt
    | model
    | parser
)
```

### 2. RunnableBranch — Routing Theo Điều Kiện

```python
from langchain_core.runnables import RunnableBranch

branch = RunnableBranch(
    (lambda x: len(x["query"]) > 100, long_chain),
    (lambda x: "urgent" in x["query"], urgent_chain),
    default_chain
)
```

### 3. RunnablePassthrough — Inject Context

```python
from langchain_core.runnables import RunnablePassthrough

# assign: thêm key vào dict, giữ nguyên các key khác
chain = (
    RunnablePassthrough.assign(
        context=lambda x: retriever.invoke(x["question"])
    )
    | prompt
    | model
    | parser
)
```

### 4. RunnableLambda — Custom Logic

```python
from langchain_core.runnables import RunnableLambda

def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

chain = retriever | RunnableLambda(format_docs) | prompt | model | parser
```

### 5. Config tại Runtime

```python
# Cấu hình model khác nhau mà không cần tạo chain mới
chain.with_config(configurable={"model_name": "gpt-4"})
```

## Giới Hạn của LCEL

- Chỉ hoạt động với **Runnable** components
- Linear/acyclic flows — Không phù hợp loop hay điều kiện phức tạp
- Với logic graph phức tạp → dùng **LangGraph**

## Khi Nào Dùng LCEL vs LangGraph?

| Tiêu Chí | LCEL | LangGraph |
|----------|------|-----------|
| Linear chain | ✅ Tối ưu | ❌ Overkill |
| Parallel branches | ✅ Dễ dàng | ✅ Cũng tốt |
| Conditional routing | ✅ RunnableBranch | ✅ Nodes/Edges |
| Loops | ❌ Không support | ✅ Core feature |
| Stateful multi-turn | ❌ Phải tự quản lý | ✅ Built-in |
| Human-in-the-loop | ❌ Phải tự implement | ✅ Native |

## Trang Liên Quan

- [Runnables](runnables.md) — Chi tiết về Runnable interface
- [LangChain Core](langchain-core.md) — Framework nền tảng
- [LangGraph Overview](langgraph-overview.md) — Khi LCEL không đủ
