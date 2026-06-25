---
tags: [langchain, concept, memory]
created: 2026-06-25
updated: 2026-06-25
---

# Memory — Lưu Trữ Lịch Sử Hội Thoại

**Memory** trong LangChain cho phép lưu trữ và truy xuất lịch sử hội thoại, giúp LLM nhớ ngữ cảnh của các lượt chat trước đó.

## Các Loại Memory

### 1. ConversationBufferMemory

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.save_context({"input": "Hi"}, {"output": "Hello!"})
memory.load_memory_variables({})
# -> {"history": "Human: Hi\nAI: Hello!"}
```

Lưu toàn bộ lịch sử — đơn giản nhất nhưng tốn token.

### 2. ConversationBufferWindowMemory

```python
from langchain.memory import ConversationBufferWindowMemory

# Chỉ giữ k lượt chat gần nhất
memory = ConversationBufferWindowMemory(k=3)
```

### 3. ConversationSummaryMemory

```python
from langchain.memory import ConversationSummaryMemory

# LLM tự động tóm tắt lịch sử
memory = ConversationSummaryMemory(llm=model)
```

### 4. ConversationSummaryBufferMemory

```python
from langchain.memory import ConversationSummaryBufferMemory

# Dùng summary khi vượt quá max_token_limit
memory = ConversationSummaryBufferMemory(
    llm=model,
    max_token_limit=2000
)
```

### 5. VectorStoreRetrieverMemory

```python
from langchain.memory import VectorStoreRetrieverMemory

# Dùng vector search để tìm các đoạn hội thoại liên quan nhất
memory = VectorStoreRetrieverMemory(
    retriever=vector_store.as_retriever(),
    memory_key="chat_history"
)
```

## Memory với LCEL

Cách hiện đại (recommended):

```python
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

chain = prompt | model | parser

chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history",
)

chain_with_history.invoke(
    {"question": "What's my name?"},
    config={"configurable": {"session_id": "user123"}}
)
```

## ChatMessageHistory — Backend Storage

LangChain hỗ trợ nhiều backend cho message history:

```python
from langchain_community.chat_message_histories import (
    ChatMessageHistory,           # In-memory
    PostgresChatMessageHistory,   # PostgreSQL
    RedisChatMessageHistory,      # Redis
    SQLChatMessageHistory,        # SQL databases
    MongoDBChatMessageHistory,    # MongoDB
    FileChatMessageHistory,       # File-based
)
```

## Memory trong Agent

```python
from langchain.agents import AgentExecutor, create_react_agent
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True,
)
```

## Best Practices

1. **Dùng `RunnableWithMessageHistory`** thay vì memory classes cũ — tương thích tốt hơn với LCEL
2. **Chọn memory strategy dựa trên use case:**
   - Short conversation → Buffer
   - Long conversation → SummaryBuffer
   - Knowledge-intensive → VectorStoreRetriever
3. **Lưu history vào database** cho production (Postgres/Redis)
4. **Window + Summary** — Kết hợp để có best of both worlds

## Trang Liên Quan

- [Runnables](runnables.md) — RunnableWithMessageHistory
- [Agent Architectures](agent-architectures.md) — Agent with memory
- [Chat Models](chat-models.md) — Models nhận history messages
