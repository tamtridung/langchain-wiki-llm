---
tags: [langchain, concept, tools]
created: 2026-06-25
updated: 2026-06-25
---

# Tools — Cho LLM Gọi Function Bên Ngoài

**Tools** là cách LangChain cho phép LLM tương tác với thế giới bên ngoài — gọi APIs, truy vấn database, thực thi code, v.v. Tools dựa trên cơ chế **function/tool calling** của các model providers.

## Định Nghĩa Tool

### Cách 1: `@tool` Decorator (Khuyến nghị)

```python
from langchain_core.tools import tool

@tool
def get_weather(location: str) -> str:
    """Get the current weather for a location.
    
    Args:
        location: The city and state, e.g. 'Hanoi, Vietnam'
    """
    # Gọi weather API ở đây
    return f"Sunny, 32°C in {location}"

# Docstring và type hints tự động sinh JSON schema
```

### Cách 2: `StructuredTool`

```python
from langchain_core.tools import StructuredTool

def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

tool = StructuredTool.from_function(
    func=multiply,
    name="multiply",
    description="Multiply two integers together",
)
```

### Cách 3: `BaseTool` Class

```python
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

class CalculatorInput(BaseModel):
    a: int = Field(description="First number")
    b: int = Field(description="Second number")

class CalculatorTool(BaseTool):
    name: str = "calculator"
    description: str = "Add two numbers"
    args_schema: type[BaseModel] = CalculatorInput

    def _run(self, a: int, b: int) -> str:
        return str(a + b)
```

## Bind Tools vào Model

```python
# Bind tools -> model tự quyết định khi nào gọi tool
model_with_tools = model.bind_tools([get_weather, calculator])

# Hoặc tools từ langchain-community
from langchain_community.tools import DuckDuckGoSearchRun
search = DuckDuckGoSearchRun()
model_with_tools = model.bind_tools([search])
```

## Tool Calling Flow

```
User: "What's weather in Hanoi and 5+3?"
                │
                ▼
     model.bind_tools([get_weather, calculator])
                │
                ▼
       AIMessage với tool_calls:
       [ToolCall(name="get_weather", args={"location": "Hanoi"}),
        ToolCall(name="calculator", args={"a": 5, "b": 3})]
                │
                ▼
     Gọi tools, nhận kết quả
                │
                ▼
       ToolMessage("Sunny, 32°C")
       ToolMessage("8")
                │
                ▼
     Model tổng hợp câu trả lời cuối
```

## Full Tool Calling Pattern

```python
from langchain_core.messages import HumanMessage, ToolMessage

tools = [get_weather, calculator]
model_with_tools = model.bind_tools(tools)

messages = [HumanMessage("What's weather in Hanoi? Also 5+3=?")]
response = model_with_tools.invoke(messages)
# response.tool_calls -> danh sách tool cần gọi

# Gọi tools và append kết quả
for tool_call in response.tool_calls:
    tool = {t.name: t for t in tools}[tool_call["name"]]
    result = tool.invoke(tool_call["args"])
    messages.append(ToolMessage(result, tool_call_id=tool_call["id"]))

# Model tổng hợp kết quả
final = model_with_tools.invoke(messages)
```

## Toolkits — Bộ Tools Theo Chủ Đề

```python
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///chinook.db")
toolkit = SQLDatabaseToolkit(db=db, llm=model)
tools = toolkit.get_tools()
# Gồm: list_tables, schema, query_checker, execute_query, ...
```

## Built-in Tools Phổ Biến

| Tool | Mô Tả |
|------|-------|
| `DuckDuckGoSearchRun` | Web search |
| `ArxivQueryRun` | Tìm kiếm academic papers |
| `WikipediaQueryRun` | Tra cứu Wikipedia |
| `YouTubeSearchTool` | Tìm kiếm YouTube |
| `FileManagementToolkit` | Đọc/ghi file |
| `PythonREPLTool` | Thực thi Python code |

## Best Practices

1. **Function calling > Prompt-based** — Dùng `bind_tools()` thay vì instruct model viết JSON
2. **Mô tả tool rõ ràng** — LLM quyết định dùng tool nào dựa trên description
3. **Parameter names có nghĩa** — `location` tốt hơn `param1`
4. **Validate input** — Dùng Pydantic schema để LLM biết format đúng
5. **Giới hạn số lượng tools** — 5-10 tools mỗi lần gọi là tốt nhất

## Trang Liên Quan

- [Chat Models](chat-models.md) — Tool calling với model
- [Agent Architectures](agent-architectures.md) — Agent dùng tools tự động
- [Runnables](runnables.md) — Tool cũng là Runnable
