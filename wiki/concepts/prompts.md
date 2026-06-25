---
tags: [langchain, concept, prompts]
created: 2026-06-25
updated: 2026-06-25
---

# Prompts — Prompt Templates

**Prompt Templates** là cách LangChain quản lý prompt dưới dạng template có tham số. Thay vì hard-code prompt, bạn định nghĩa template với các biến được điền vào tại runtime.

## ChatPromptTemplate

```python
from langchain_core.prompts import ChatPromptTemplate

# Cách 1: Từ template string
prompt = ChatPromptTemplate.from_template(
    "Translate to {language}: {text}"
)

# Cách 2: List messages (khuyến nghị)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a {role} assistant."),
    ("human", "Help me with {task}"),
])

# Invoke: điền biến
messages = prompt.invoke({
    "role": "translation",
    "task": "Translate 'hello' to Vietnamese"
})
```

## Các Loại Message Template

| Class | Shorthand | Vai Trò |
|-------|-----------|---------|
| `SystemMessagePromptTemplate` | `"system"` | System prompt — định hướng model |
| `HumanMessagePromptTemplate` | `"human"` | User input |
| `AIMessagePromptTemplate` | `"ai"` | AI response (cho few-shot) |
| `MessagesPlaceholder` | `"placeholder"` | Chèn danh sách messages động |

## MessagesPlaceholder — Dynamic History

```python
from langchain_core.prompts import MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
])

# chat_history là list[BaseMessage] được chèn vào giữa
```

## PromptTemplate (Text)

Dùng cho completion models (legacy) hoặc khi cần text thuần:

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {topic}."
)
```

## Few-Shot Prompt Templates

```python
from langchain_core.prompts import FewShotChatMessagePromptTemplate

examples = [
    {"input": "hello", "output": "xin chào"},
    {"input": "goodbye", "output": "tạm biệt"},
]

example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}"),
])

few_shot = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
)

final_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a translator."),
    few_shot,
    ("human", "{input}"),
])
```

## Prompt Composition

Kết hợp nhiều prompt templates:

```python
system_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert in {domain}.")
])

instruction_prompt = ChatPromptTemplate.from_messages([
    ("human", "Answer: {question}")
])

# Kết hợp
full_prompt = system_prompt + instruction_prompt
# Hoặc dùng MessagesPlaceholder
```

## Pipeline Prompt

```python
# Prompt -> Model -> Parser
chain = prompt | model | StrOutputParser()
```

## Hub Prompts (LangSmith Hub)

LangSmith Hub cho phép lưu và chia sẻ prompt:

```python
from langchain import hub

# Pull prompt từ hub
prompt = hub.pull("rlc/chat-prompt")

# Push prompt lên hub
hub.push("my-org/my-prompt", prompt)
```

## Best Practices

1. **Phân tách System vs Human** — System prompt chứa instructions, Human chứa input
2. **Dùng MessagesPlaceholder** cho chat history — Không nhồi history vào system prompt
3. **Version prompts** với LangSmith Hub — Dễ rollback và A/B test
4. **Validate biến** — Dùng `prompt.input_schema.schema()` để xem biến cần điền
5. **Few-shot nên có cấu trúc** — Dùng `FewShotChatMessagePromptTemplate` thay vì nhồi text

## Trang Liên Quan

- [Chat Models](chat-models.md) — Models nhận prompt và sinh output
- [Output Parsers](output-parsers.md) — Parse output từ model
- [Runnables](runnables.md) — Runnable interface
