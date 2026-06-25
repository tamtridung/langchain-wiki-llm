---
tags: [langchain, concept, core]
created: 2026-06-25
updated: 2026-06-25
---

# LangChain Core — Framework Nền Tảng

**LangChain Core** là thư viện nền tảng của toàn bộ hệ sinh thái LangChain. Nó cung cấp các abstractions cốt lõi và interface thống nhất cho mọi component.

## Triết Lý Thiết Kế

LangChain core được xây dựng dựa trên 3 nguyên lý:

1. **Composability** — Mọi component implement cùng một interface (`Runnable`), có thể kết hợp bằng `|`
2. **Provider Agnostic** — Abstractions hoạt động với mọi model provider (OpenAI, Anthropic, Google, v.v.)
3. **Observability First** — Callbacks và tracing được tích hợp sẵn trong mọi component

## Các Module Cốt Lõi

### `langchain_core.runnables`
Interface thống nhất cho mọi component:
- `Runnable` — Base class với `invoke`, `stream`, `batch`, `ainvoke`, `astream`, `abatch`
- `RunnableSequence` — Chuỗi các runnable (`chain1 | chain2 | chain3`)
- `RunnableParallel` — Chạy song song nhiều runnable
- `RunnablePassthrough` — Pass-through, thường dùng để inject context
- `RunnableLambda` — Bọc function Python thành Runnable
- `RunnableBranch` — Routing theo điều kiện

### `langchain_core.prompts`
Quản lý prompt templates:
- `ChatPromptTemplate` — Template cho chat messages
- `PromptTemplate` — Template cho text prompts
- `MessagesPlaceholder` — Placeholder cho danh sách messages (lịch sử)
- `HumanMessagePromptTemplate`, `AIMessagePromptTemplate`, `SystemMessagePromptTemplate`

### `langchain_core.language_models`
Interface cho LLMs:
- `BaseChatModel` — Base class cho chat models (GPT-4, Claude, Gemini...)
- `BaseLLM` — Base class cho completion models (legacy)

### `langchain_core.output_parsers`
Parse output từ LLMs:
- `StrOutputParser` — Lấy string từ output
- `PydanticOutputParser` — Parse thành Pydantic model
- `JsonOutputParser` — Parse JSON
- `CommaSeparatedListOutputParser` — Parse danh sách
- `DatetimeOutputParser` — Parse datetime

### `langchain_core.messages`
Cấu trúc dữ liệu messages:
- `BaseMessage`, `HumanMessage`, `AIMessage`, `SystemMessage`, `ToolMessage`
- Message có `content`, `additional_kwargs`, `response_metadata`

### `langchain_core.documents`
Cấu trúc dữ liệu document:
- `Document` — page_content + metadata
- Được dùng trong Retrieval, Document Loaders

### `langchain_core.embeddings`
Interface cho embeddings:
- `Embeddings` — `embed_documents()`, `embed_query()`

### `langchain_core.tools`
Interface cho tools:
- `BaseTool`, `Tool`, `StructuredTool`
- `tool` decorator — biến function thành tool

### `langchain_core.retrievers`
Interface cho retrieval:
- `BaseRetriever` — `invoke()`, `get_relevant_documents()`
- Tích hợp với vector stores, ensembles, và custom logic

### `langchain_core.callbacks`
Hệ thống event/hooks:
- `CallbackHandler` — Base handler
- `BaseCallbackHandler` — Async variant
- Được gọi tự động bởi mọi Runnable

### `langchain_core.tracers`
Tracing integration:
- `RootListenersTracer`, `LangChainTracer`
- Tích hợp sâu với LangSmith

## Cài Đặt

```bash
pip install langchain-core          # Chỉ core
pip install langchain               # Core + community integrations phổ biến
pip install langchain-community     # Tất cả integrations
pip install langchain-openai        # OpenAI integration
pip install langchain-anthropic     # Anthropic integration
pip install langchain-google-genai  # Google integration
```

## Import Pattern

```python
# Ưu tiên import từ langchain_core
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

# Provider-specific
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
```

## Trang Liên Quan

- [LCEL](lcel.md) — LangChain Expression Language
- [Runnables](runnables.md) — Runnable interface chi tiết
- [Prompts](prompts.md) — Prompt templates
- [Chat Models](chat-models.md) — Chat models
- [Output Parsers](output-parsers.md) — Output parsers
- [Tools](tools.md) — Tools & tool calling
- [Callbacks](callbacks.md) — Callbacks & event system
