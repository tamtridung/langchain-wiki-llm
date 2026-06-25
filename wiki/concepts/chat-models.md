---
tags: [langchain, concept, chat-models]
created: 2026-06-25
updated: 2026-06-25
---

# Chat Models — Giao Diện Thống Nhất Cho LLMs

**Chat Models** là abstraction của LangChain cho các mô hình ngôn ngữ dạng chat (GPT-4, Claude, Gemini, v.v.). Mọi chat model đều implement `BaseChatModel` và tuân theo Runnable interface.

## Cài Đặt Provider

```python
# OpenAI
pip install langchain-openai
from langchain_openai import ChatOpenAI

# Anthropic
pip install langchain-anthropic
from langchain_anthropic import ChatAnthropic

# Google
pip install langchain-google-genai
from langchain_google_genai import ChatGoogleGenerativeAI

# Ollama (local)
pip install langchain-ollama
from langchain_ollama import ChatOllama

# AWS Bedrock
pip install langchain-aws
from langchain_aws import ChatBedrock

# Azure OpenAI
pip install langchain-openai
from langchain_openai import AzureChatOpenAI
```

## Cách Dùng Cơ Bản

```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

model = ChatOpenAI(model="gpt-4", temperature=0)

# invoke với messages
response = model.invoke([
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is LangChain?")
])
# response là AIMessage

# invoke với string (tự động convert)
response = model.invoke("Hello!")
```

## Message Types

```python
from langchain_core.messages import (
    HumanMessage,     # User input
    AIMessage,        # Model response
    SystemMessage,    # System instructions
    ToolMessage,      # Tool call result
    ChatMessage,      # Custom role
)

# AIMessage có thể chứa:
# - content: str
# - tool_calls: list[ToolCall] — khi model gọi tool
# - response_metadata: dict — thông tin phụ (token usage, v.v.)
```

## Init Chat Model (Multi-Provider)

```python
from langchain.chat_models import init_chat_model

# Tự động detect provider dựa trên tên model
model = init_chat_model("gpt-4o", temperature=0)
model = init_chat_model("claude-sonnet-4-20250514", temperature=0)
```

## Tool Calling / Function Calling

```python
from langchain_core.tools import tool

@tool
def get_weather(location: str) -> str:
    """Get weather for a location."""
    return f"Sunny in {location}"

model_with_tools = model.bind_tools([get_weather])
response = model_with_tools.invoke("What's weather in Hanoi?")
# response.tool_calls -> [ToolCall(name="get_weather", args={...})]
```

## Structured Output

```python
from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(description="The person's age")

# Cách 1: with_structured_output
structured_model = model.with_structured_output(Person)
result = structured_model.invoke("John is 25 years old")
# result -> Person(name="John", age=25)

# Cách 2: Bind tools + parser
model_with_tools = model.bind_tools([Person])
```

## Streaming

```python
# Stream text chunks
for chunk in model.stream("Tell me a story"):
    print(chunk.content, end="")

# Stream với tool calls
async for event in model.astream_events("What's the weather?", version="v2"):
    if event["event"] == "on_chat_model_stream":
        print(event["data"]["chunk"].content, end="")
```

## Common Parameters

| Parameter | Ý Nghĩa |
|-----------|---------|
| `model` | Tên model (e.g., "gpt-4", "claude-3-opus") |
| `temperature` | Độ ngẫu nhiên (0-2, thường 0-1) |
| `max_tokens` | Số token tối đa trong response |
| `timeout` | Request timeout (giây) |
| `max_retries` | Số lần retry khi lỗi |
| `model_kwargs` | Extra params gửi thẳng tới provider |

## Best Practices

1. **Dùng `init_chat_model`** khi muốn code provider-agnostic
2. **Set `temperature=0`** cho các tác vụ deterministic (classification, extraction)
3. **Luôn dùng `with_structured_output`** khi cần output có cấu trúc
4. **Dùng `bind_tools` + `ToolMessage`** cho function calling
5. **Stream response** cho UX tốt hơn (không chờ full response)

## Trang Liên Quan

- [Prompts](prompts.md) — Prompt templates
- [Output Parsers](output-parsers.md) — Parse model output
- [Tools](tools.md) — Tool calling
- [Runnables](runnables.md) — Runnable interface
