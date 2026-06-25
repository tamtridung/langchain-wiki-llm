---
tags: [langchain, concept, output-parsers]
created: 2026-06-25
updated: 2026-06-25
---

# Output Parsers — Parse Kết Quả Từ LLM

**Output Parsers** chịu trách nhiệm chuyển đổi output thô từ LLM (`AIMessage`) thành cấu trúc dữ liệu có thể sử dụng trong code.

## Các Parser Phổ Biến

### StrOutputParser — Lấy string thuần

```python
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
text = parser.invoke(ai_message)  # AIMessage -> str
# Đơn giản nhất, hay dùng nhất
```

### PydanticOutputParser — Parse thành Pydantic Model

```python
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class Joke(BaseModel):
    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline")
    rating: int = Field(description="How funny the joke is (1-10)")

parser = PydanticOutputParser(pydantic_object=Joke)

# Tích hợp với prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer with JSON matching this schema: {format_instructions}"),
    ("human", "{query}"),
]).partial(format_instructions=parser.get_format_instructions())

chain = prompt | model | parser
joke = chain.invoke({"query": "Tell me a programming joke"})
# joke.setup, joke.punchline, joke.rating
```

### JsonOutputParser — Parse JSON không schema

```python
from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()
result = parser.invoke('{"name": "John", "age": 30}')
# -> dict
```

### CommaSeparatedListOutputParser

```python
from langchain_core.output_parsers import CommaSeparatedListOutputParser

parser = CommaSeparatedListOutputParser()
result = parser.invoke("apple, banana, orange")
# -> ["apple", "banana", "orange"]
```

### DatetimeOutputParser

```python
from langchain_core.output_parsers import DatetimeOutputParser
from datetime import datetime

parser = DatetimeOutputParser()
result = parser.invoke("2024-12-25")
# -> datetime(2024, 12, 25)
```

## Custom Output Parser

```python
from langchain_core.output_parsers import BaseOutputParser

class MyParser(BaseOutputParser[dict]):
    def parse(self, text: str) -> dict:
        lines = text.strip().split("\n")
        result = {}
        for line in lines:
            key, value = line.split(": ", 1)
            result[key] = value
        return result

    @property
    def _type(self) -> str:
        return "my_parser"
```

## Auto-Fixing Parser

Khi LLM trả về format sai, parser có thể tự động sửa:

```python
from langchain_core.output_parsers import PydanticOutputParser
from langchain.output_parsers import RetryOutputParser, OutputFixingParser

# Tự động fix lỗi format
fixing_parser = OutputFixingParser.from_llm(
    parser=original_parser,
    llm=model
)

# Retry với prompt gốc
retry_parser = RetryOutputParser.from_llm(
    parser=original_parser,
    llm=model
)
```

## Best Practices

1. **Ưu tiên `with_structured_output`** (ChatModels) thay vì parser thủ công — nhanh hơn, ít lỗi hơn
2. **Dùng `PydanticOutputParser`** khi làm việc với model không support structured output
3. **Luôn include format instructions** trong prompt khi dùng parser
4. **Thêm `OutputFixingParser`** cho production — lỡ LLM trả sai format
5. **Custom parser** khi format đặc thù (CSV, log format, v.v.)

## So Sánh: Parser vs with_structured_output

| Tiêu Chí | PydanticOutputParser | with_structured_output |
|----------|---------------------|----------------------|
| Cách hoạt động | Instruct LLM viết JSON, parse sau | Dùng native tool calling/JSON mode |
| Tốc độ | Chậm hơn (cần sinh text + parse) | Nhanh hơn (native) |
| Độ tin cậy | Phụ thuộc instruction | Cao hơn (được provider support) |
| Model support | Mọi model | Chỉ model có function calling |
| Nên dùng khi | Model cũ, không support tool calling | Model mới (GPT-4, Claude 3+, Gemini) |

## Trang Liên Quan

- [Chat Models](chat-models.md) — Models sinh output
- [Prompts](prompts.md) — Prompt với format instructions
- [LCEL](lcel.md) — Kết hợp parser vào pipeline
