---
tags: [langchain, deep-agents, concept]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/deep-agents-memory, concepts/deep-agents-skills, concepts/deep-agents-subagents]
---

# Deep Agents — Context Engineering

Context engineering là cung cấp đúng thông tin và tools ở đúng format để agent hoàn thành task reliably.

## Types of Context

| Context Type | What You Control | Scope |
|-------------|-----------------|-------|
| **Input context** | System prompt, memory, skills | Static, applied each run |
| **Runtime context** | Per-run config (user IDs, API keys) | Per run, propagates to subagents |
| **Context compression** | Built-in offloading + summarization | Automatic |
| **Context isolation** | Subagents quarantine heavy work | Per subagent |
| **Long-term memory** | Persistent storage (StoreBackend) | Cross-conversation |

## Input Context

### System Prompt

```python
agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    system_prompt="You are a research assistant. Always cite sources.",
)
```

Dùng `@dynamic_prompt` cho context-aware instructions:

```python
from deepagents import dynamic_prompt

@dynamic_prompt
def build_prompt(runtime):
    user_prefs = runtime.store.get(("prefs",), "style")
    return f"User prefers {user_prefs}. Be concise."
```

### Memory (Always Loaded)

```python
agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    memory=["/project/AGENTS.md", "~/.deepagents/preferences.md"],
)
```

### Skills (Progressive Disclosure)

```python
agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    skills=["/skills/research/", "/skills/web-search/"],
)
```

### Tool Prompts

Tool descriptions từ tool schema được gửi đến model. Write good descriptions:

```python
@tool(parse_docstring=True)
def search_orders(user_id: str, status: str, limit: int = 10) -> str:
    """Search for user orders by status.
    Use this when user asks about order history.
    Args:
        user_id: Unique identifier
        status: 'pending', 'shipped', or 'delivered'
        limit: Max results
    """
```

## Runtime Context

Pass per-run data qua `context=` parameter:

```python
from dataclasses import dataclass
from deepagents import create_deep_agent
from langchain.tools import tool, ToolRuntime

@dataclass
class Context:
    user_id: str
    api_key: str

@tool
def fetch_user_data(query: str, runtime: ToolRuntime[Context]) -> str:
    """Fetch data for current user."""
    user_id = runtime.context.user_id
    return f"Data for user {user_id}: {query}"

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    tools=[fetch_user_data],
    context_schema=Context,
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "Get my activity"}]},
    context=Context(user_id="user-123", api_key="sk-..."),
)
```

Runtime context **propagates to all subagents**.

## Context Compression

### Offloading

- Tool results > threshold → tự động lưu vào backend, thay bằng reference
- Chỉ đếm text tokens (không ảnh hưởng images/media)

### Summarization

- Khi context window gần đầy → summarize messages cũ
- Image/audio/video blocks trong range summarized → không carry forward
- Original conversation vẫn được lưu vào filesystem

### Isolation với Subagents

Dùng subagents để quarantine heavy work — chỉ trả kết quả về supervisor, giữ context main agent gọn.

## Custom State Schema

```python
from typing import TypedDict
from deepagents import DeepAgentState

class MyState(DeepAgentState):
    custom_field: str

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    state_schema=MyState,
)
```

## Trang Liên Quan

- [Deep Agents Memory](deep-agents-memory.md) — Long-term memory
- [Deep Agents Skills](deep-agents-skills.md) — Skills (progressive disclosure)
- [Deep Agents Subagents](deep-agents-subagents.md) — Context isolation với subagents
