---
tags: [langchain, deep-agents, concept]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/deep-agents-overview, concepts/deep-agents-async-subagents, concepts/multi-agent]
---

# Deep Agents — Subagents

Subagents cho phép supervisor agent delegate tasks mà không cần tự xử lý từng bước.

## Synchronous Subagents (Mặc định)

Subagents chạy đồng bộ — supervisor block cho đến khi subagent hoàn thành.

### Dictionary Spec

```python
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    subagents=[
        {
            "name": "researcher",
            "description": "Researches topics thoroughly",
            "system_prompt": "You are a thorough researcher...",
        },
    ],
)
```

### CompiledSubAgent (Full Control)

```python
from deepagents import CompiledSubAgent, create_deep_agent

subagent = CompiledSubAgent(
    name="researcher",
    model="openai:gpt-5.5",
    system_prompt="You are a researcher.",
    tools=[search_tool],
    interrupt_on={"write_file": True},
)

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    subagents=[subagent],
)
```

### General-Purpose Subagent

Mặc định, Deep Agents tạo một **general-purpose subagent** cho mọi task delegation. Bạn có thể:

- **Override** — đặt subagent khác cùng tên `"general-purpose"`
- **Disable** — dùng `GeneralPurposeSubagentProfile(enabled=False)`
- **Thay đổi model** — dùng cheaper model cho delegation

```python
register_harness_profile(
    "openai",
    HarnessProfile(
        general_purpose_subagent=GeneralPurposeSubagentProfile(enabled=False),
    ),
)
```

## Subagents trong Deep Agents Code

Subagents được định nghĩa qua `AGENTS.md` files với YAML frontmatter:

```yaml
---
name: researcher
description: Research topics on the web before writing content
model: anthropic:claude-haiku-4-5-20251001
---
You are a research assistant with access to web search.
```

### Data Locations

```
~/.deepagents/{agent}/agents/{name}/AGENTS.md    # User-level
.deepagents/agents/{name}/AGENTS.md               # Project-level (higher precedence)
```

### Cost-Efficient Subagents

Override general-purpose subagent với model rẻ hơn:

```yaml
---
name: general-purpose
description: General-purpose agent for research and multi-step tasks
model: anthropic:claude-haiku-4-5-20251001
---
```

## Running Without Subagents

Để chạy agent không có `task` tool: set `general_purpose_subagent.enabled=False` và không pass subagents.

## Trang Liên Quan

- [Deep Agents Async Subagents](deep-agents-async-subagents.md) — Background, non-blocking subagents
- [Multi-Agent](multi-agent.md) — Multi-agent patterns
- [Deep Agents Overview](deep-agents-overview.md) — Tổng quan Deep Agents
