---
tags: [langchain, deep-agents, concept]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/deep-agents-overview, concepts/deep-agents-customization, concepts/chat-models]
---

# Deep Agents — Profiles (HarnessProfile & ProviderProfile)

Profiles cho phép bạn package configuration áp dụng khi một provider hoặc model cụ thể được chọn — system prompt tweaks, tool overrides, excluded middleware, v.v.

## Harness Profiles

`HarnessProfile` điều chỉnh prompt assembly, tool visibility, middleware, và subagent defaults sau khi chat model đã được khởi tạo.

```python
from deepagents import HarnessProfile, register_harness_profile

register_harness_profile(
    "openai:gpt-5.5",
    HarnessProfile(
        system_prompt_suffix="Respond in under 100 words.",
        excluded_tools={"execute"},
        excluded_middleware={"SummarizationMiddleware"},
    ),
)
```

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `base_system_prompt` | `string` | Replace base Deep Agents system prompt |
| `system_prompt_suffix` | `string` | Append text to assembled prompt |
| `tool_description_overrides` | `Mapping[str, str]` | Override tool descriptions |
| `excluded_tools` | `frozenset[str]` | Remove tools from visible set |
| `excluded_middleware` | `frozenset` | Strip middleware from default stack |
| `extra_middleware` | `Sequence` | Append middleware |
| `general_purpose_subagent` | `GeneralPurposeSubagentProfile` | Disable/rename/re-prompt GP subagent |

### Provider Profiles

`ProviderProfile` chỉ áp dụng khi bạn pass `provider:model` string (không áp dụng với preconfigured model instance):

```python
from deepagents import ProviderProfile, register_provider_profile

# Provider-wide: mọi openai model đều temperature=0
register_provider_profile("openai", ProviderProfile(init_kwargs={"temperature": 0}))

# Model-level: gpt-5.5 thêm reasoning_effort
register_provider_profile(
    "openai:gpt-5.5",
    ProviderProfile(init_kwargs={"reasoning_effort": "medium"}),
)
```

### Registration Keys

| Key Format | Scope | Example |
|------------|-------|---------|
| `"openai"` | Provider-level — mọi model từ provider | `"openai"`, `"anthropic"` |
| `"openai:gpt-5.5"` | Model-level — specific model | `"openai:gpt-5.5"` |

Provider-level và model-level merge khi resolve. Unset fields inherit từ provider profile.

### Merge Semantics

| Field | Behavior |
|-------|----------|
| `base_system_prompt`, `system_prompt_suffix` | New wins |
| `tool_description_overrides` | Merge per key |
| `excluded_tools`, `excluded_middleware` | Set union |
| `extra_middleware` | Merge by name |
| `general_purpose_subagent` | Merge field-wise |
| `init_kwargs` | Dict merge, new wins |

### Load từ Config Files

```python
import yaml
from deepagents import HarnessProfileConfig, register_harness_profile

with open("openai.yaml") as f:
    config = HarnessProfileConfig.from_dict(yaml.safe_load(f))

register_harness_profile("openai", config)
```

### Built-in Profiles

Deep Agents ships built-in harness profiles cho OpenAI và Anthropic (Claude) models.

## Trang Liên Quan

- [Deep Agents Overview](deep-agents-overview.md) — Tổng quan Deep Agents SDK
- [Deep Agents Customization](deep-agents-customization.md) — `create_deep_agent` parameters
- [Chat Models](chat-models.md) — Supported models & integrations
