---
tags: [langchain, deep-agents, concept]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/managed-deep-agents, concepts/deep-agents-customization, concepts/deep-agents-profiles]
---

# Deep Agents SDK — Tổng Quan

**Deep Agents** là thư viện Python mã nguồn mở (`deepagents`) để xây dựng AI agent production-grade. Nó cung cấp **harness** — một framework có sẵn planning, filesystem tools, subagent delegation, memory, skills, middleware stack, và pluggable backends — bạn chỉ cần kết nối model, tools, và system prompt.

## Cài Đặt

```bash
pip install deepagents tavily-python
```

## Quickstart: Agent Nghiên Cứu

```python
import os
from typing import Literal
from tavily import TavilyClient
from deepagents import create_deep_agent

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search"""
    return tavily_client.search(query, max_results=max_results,
                                include_raw_content=include_raw_content, topic=topic)

research_instructions = """You are an expert researcher..."""

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    tools=[internet_search],
    system_prompt=research_instructions,
)

result = agent.invoke({"messages": [{"role": "user", "content": "What is LangGraph?"}]})
print(result["messages"][-1].content)
```

## Harness Architecture

Khi bạn gọi `create_deep_agent()`, agent tự động:

1. **Plans approach** — dùng `write_todos` để break down task
2. **Conducts research** — gọi tools bạn cung cấp (search, APIs, databases)
3. **Manages context** — dùng filesystem tools để offload large results
4. **Spawns subagents** — delegate subtasks qua `task` tool
5. **Synthesizes** — compile findings thành response

### Default Middleware Stack

```
PlanningMiddleware          → Hướng dẫn dùng write_todos
LocalContextMiddleware      → CWD & project info (CLI only)
MemoryMiddleware            → AGENTS.md + memory files
SkillsMiddleware            → Progressive disclosure skills
FilesystemMiddleware        → ls/read_file/write_file/edit_file/glob/grep
SubAgentMiddleware          → task tool delegation
HumanInTheLoopMiddleware    → interrupt_on approvals (khi configured)
SummarizationMiddleware     → Context compaction & offloading
PatchToolCallsMiddleware    → Repair message history khi interrupted
```

### Built-in Tools

| Tool | Description | Human-in-the-Loop |
|------|-------------|-------------------|
| `ls` | List files | — |
| `read_file` | Read với multimodal support (image, audio, video, PDF) | — |
| `write_file` | Create/overwrite | Required |
| `edit_file` | String replacement edits | Required |
| `glob` | Find files by pattern | — |
| `grep` | Search text in files | — |
| `execute` | Shell commands (sandbox backends only) | Required |
| `web_search` | Tavily search | Required |
| `fetch_url` | Fetch URL → markdown | Required |
| `task` | Delegate work to subagents | Required |
| `ask_user` | Ask user questions | — |
| `compact_conversation` | Summarize & offload | Mixed |
| `write_todos` | Task planning | — |

## Models

Specify models in `provider:model` format: `google_genai:gemini-3.5-flash`, `openai:gpt-5.5`, `anthropic:claude-sonnet-4-6`.

### Suggested Models (eval-tested)

| Provider | Models | Overall Score |
|----------|--------|---------------|
| Google | `gemini-3.5-flash`, `gemini-3.1-pro-preview` | 82% |
| OpenAI | `gpt-5.5`, `gpt-5.4` | 80% |
| Anthropic | `claude-opus-4-8`, `claude-opus-4-7` | 80% |
| Open-weight | `GLM-5.2`, `Kimi-K2.7`, `MiniMax-M3` | 77-81% |

### Model Parameters

```python
from langchain.chat_models import init_chat_model

model = init_chat_model(
    model="google_genai:gemini-3.5-flash",
    thinking_level="medium",
)
agent = create_deep_agent(model=model)
```

### Runtime Model Selection

Dùng middleware để swap model tại runtime:

```python
from langchain.agents.middleware import wrap_model_call

@wrap_model_call
def configurable_model(request, handler):
    model_name = request.runtime.context.model
    model = init_chat_model(model_name)
    return handler(request.override(model=model))

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    middleware=[configurable_model],
    context_schema=Context,
)
```

## So Sánh Nhanh: Deep Agents vs Claude Agent SDK

| Tiêu Chí | Deep Agents | Claude Agent SDK |
|----------|-------------|------------------|
| Model provider | Any (100+) | Claude-only |
| Execution backend | Pluggable (VFS, local, sandbox, custom) | Sandbox local filesystem |
| Deployment | Managed + Self-hosted (Docker) | Self-hosted (build server) |
| Multi-tenancy | Built-in (RBAC, per-user sandboxes) | Build yourself |
| License | MIT | MIT |

## Trang Liên Quan

- [Deep Agents Customization](deep-agents-customization.md) — Toàn bộ tham số `create_deep_agent`
- [Deep Agents Backends](deep-agents-backends.md) — Filesystem backends
- [Deep Agents Profiles](deep-agents-profiles.md) — Harness & provider profiles
- [Managed Deep Agents](managed-deep-agents.md) — Hosted runtime trên LangSmith
- [Deep Agents Memory](deep-agents-memory.md) — Long-term memory systems
