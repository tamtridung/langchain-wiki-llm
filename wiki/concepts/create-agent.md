---
tags: [langchain, concept, core, agent]
created: 2026-06-25
updated: 2026-06-25
sources: [langsmith-evaluation, langsmith-production]
related: [concepts/agent-architectures, concepts/langgraph-overview, concepts/nodes-edges]
---

# create_agent — Agent Harness Cho LangChain

**`create_agent`** là hàm xây dựng agent minimal, highly configurable từ `langchain.agents`. Đây là cách đơn giản nhất để tạo agent trong LangChain v1 mới, không yêu cầu LangGraph.

## Import

```python
from langchain.agents import create_agent
```

## Cú Pháp Cơ Bản

```python
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_core.tools import tool

model = init_chat_model("claude-sonnet-4-6")

@tool
def get_weather(location: str) -> str:
    """Get weather for a location."""
    return f"Sunny, 32°C in {location}"

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful weather assistant.",
)

result = agent.invoke({"messages": [("human", "What's the weather in Hanoi?")]})
print(result["messages"][-1].content)
```

## Tham Số

```python
create_agent(
    model,                        # Chat model — string ("gpt-4o") hoặc BaseChatModel
    tools=[],                     # List tools — @tool, StructuredTool, hoặc MCP tools
    system_prompt=None,           # System message string
    prompt=None,                  # Prompt template (thay thế system_prompt nếu cần custom)
    middleware=None,              # List middleware để mở rộng behavior
    checkpointer=None,            # Optional: thêm persistence (MemorySaver, PostgresSaver...)
    name=None,                    # Tên agent — dùng cho tracing trên LangSmith
)
```

## State Schema

`create_agent` mặc định dùng `MessagesState` (tương đương LangGraph `MessagesState`):

```python
# State mặc định
class MessagesState(TypedDict):
    messages: Annotated[list, add_messages]
```

Input/Output đều là dict với key `"messages"`:

```python
# Input
agent.invoke({"messages": [("human", "Hello!")]})

# Output (result["messages"] chứa toàn bộ lịch sử)
result = agent.invoke({"messages": [("human", "What's my name?")]})
```

## Middleware

Middleware là cơ chế mở rộng của `create_agent`, cho phép can thiệp vào vòng lặp agent mà không cần sửa graph.

### Prebuilt Middleware

```python
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware

agent = create_agent(
    model=model,
    tools=[send_email, delete_user, get_weather],
    system_prompt="You are an admin assistant.",
    middleware=[
        HumanInTheLoopMiddleware(
            require_approval_for_tools=["send_email", "delete_user"]
        ),
    ],
)
```

### Các Middleware Có Sẵn

| Middleware | Mô tả |
|---|---|
| `HumanInTheLoopMiddleware` | Yêu cầu xác nhận trước khi gọi tool nhạy cảm |
| `RateLimitMiddleware` | Giới hạn số request |
| `GuardrailsMiddleware` | Kiểm tra input/output trước/sau khi agent chạy |
| `Custom middleware` | Tự implement middleware riêng |

### Custom Middleware

```python
from langchain.agents.middleware import BaseAgentMiddleware

class LoggingMiddleware(BaseAgentMiddleware):
    async def on_tool_start(self, tool_name: str, **kwargs):
        print(f"[LOG] Calling tool: {tool_name}")
    
    async def on_tool_end(self, tool_name: str, result: str, **kwargs):
        print(f"[LOG] Tool {tool_name} returned: {result[:50]}...")
```

## Checkpointing (Optional)

`create_agent` có thể thêm checkpointing nhưng **không built-in sẵn** như `create_react_agent`:

```python
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()

agent = create_agent(
    model=model,
    tools=[get_weather],
    checkpointer=memory,  # Thêm persistence
)

config = {"configurable": {"thread_id": "session-1"}}
agent.invoke(
    {"messages": [("human", "Hi, I'm John")]},
    config=config,
)
agent.invoke(
    {"messages": [("human", "What's my name?")]},
    config=config,
)
# → "Your name is John"
```

## Ví Dụ Nâng Cao

### Agent với MCP Tools

```python
from langchain.agents import create_agent
from langchain_mcp_adapters.tools import load_mcp_tools
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    async with streamablehttp_client(
        url="https://mcp-finance-agent.xxx.us.langgraph.app/mcp",
        headers={"X-Api-Key": "lsv2_pt_your_api_key"}
    ) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            
            agent = create_agent("gpt-5.5", tools)
            result = await agent.ainvoke({
                "messages": [("human", "What can the finance agent do?")]
            })
            print(result)
```

### Agent với Rate Limiter

```python
from langchain.agents import create_agent
from langchain_core.rate_limiters import InMemoryRateLimiter

rate_limiter = InMemoryRateLimiter(requests_per_second=0.08)

agent = create_agent(
    model=model,
    tools=[DuckDuckGoSearchRun(rate_limiter=rate_limiter)],
    system_prompt="You are a search assistant.",
)
```

### Multi-Agent với create_agent

```python
# Tạo nhiều agent chuyên biệt
qa_agent = create_agent(qa_llm, tools=[lookup_track, lookup_artist, lookup_album])
refund_agent = create_agent(refund_llm, tools=[process_refund, check_order])

# Dùng parent agent để routing (cần LangGraph cho multi-agent phức tạp)
# hoặc dùng function routing đơn giản
def route_to_agent(input_data):
    if "refund" in input_data["messages"][-1].content.lower():
        return refund_agent.invoke(input_data)
    return qa_agent.invoke(input_data)
```

## So Sánh: create_agent vs create_react_agent

| Tiêu chí | `create_agent` | `create_react_agent` |
|---|---|---|
| **Module** | `langchain.agents` | `langgraph.prebuilt` |
| **Phụ thuộc** | Chỉ `langchain` | Cần `langgraph` |
| **Middleware** | ✅ Built-in support | ❌ Không có |
| **Checkpointing** | Optional (pass `checkpointer`) | Built-in (`checkpointer` param) |
| **Interrupt/HIL** | Qua middleware | Built-in (`interrupt_before/after`) |
| **Streaming** | Cơ bản (`stream` events) | Chi tiết (modes, subgraphs) |
| **Time travel** | ❌ Không hỗ trợ | ✅ Hỗ trợ |
| **Subgraphs** | ❌ Không hỗ trợ | ✅ Hỗ trợ |
| **Độ phức tạp** | Thấp — 1 dòng tạo agent | Trung bình — cần compile graph |
| **Use case** | Prototype, agent đơn giản | Production, multi-turn, phức tạp |

> **Khi nào dùng `create_agent`?**
> - Bạn cần agent nhanh, đơn giản
> - Không cần persistence hoặc chỉ cần cơ bản
> - Muốn dùng middleware để mở rộng behavior
> - Prototype, MVP

> **Khi nào dùng `create_react_agent`?**
> - Cần checkpointing, HIL, time travel
> - Multi-agent, supervisor pattern
> - Streaming phức tạp (token, events, subgraphs)
> - Production deployment

## Tracing với LangSmith

`create_agent` tự động tích hợp tracing với LangSmith:

```python
import os
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = "lsv2_..."
os.environ["LANGSMITH_PROJECT"] = "my-agent"

# Agent sẽ tự động trace
agent = create_agent(model, tools, name="my-weather-agent")
agent.invoke({"messages": [("human", "Weather in Hanoi?")]})
```

Trên LangSmith, trace sẽ hiển thị với `ls_integration: "langchain_create_agent"`.

## Trang Liên Quan

- [Agent Architectures](agent-architectures.md) — Tổng quan các pattern agent
- [LangGraph Overview](langgraph-overview.md) — Khi nào cần nâng cấp lên LangGraph
- [create_react_agent trong Nodes & Edges](nodes-edges.md) — So sánh với LangGraph prebuilt
- [Tools](tools.md) — Định nghĩa tools cho agent
- [Middleware](../concepts/middleware.md) — (Nếu có) Chi tiết về middleware
