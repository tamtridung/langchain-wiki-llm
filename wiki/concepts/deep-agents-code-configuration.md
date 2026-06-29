---
tags: [langchain, deep-agents, concept]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/deep-agents-code-overview, concepts/deep-agents-code-data-locations, concepts/chat-models]
---

# Deep Agents Code — Configuration

Cấu hình `dcode` nằm trong `~/.deepagents/`.

## Config Files

| File | Format | Purpose |
|------|--------|---------|
| `config.toml` | TOML | Model defaults, provider settings, themes |
| `.env` | Dotenv | API keys, secrets |
| `hooks.json` | JSON | Lifecycle event hooks |
| `.mcp.json` | JSON | MCP server definitions |

## Inspect Configuration

```bash
# Show effective config (with sources)
dcode config show

# List all available options
dcode config list

# Get specific value
dcode config get interpreter.memory_limit_mb

# Show config file paths
dcode config path
```

Mỗi option resolve theo thứ tự: `DEEPAGENTS_CODE_` env var → canonical env var → `config.toml` → built-in default.

## Provider Credentials

### /auth (Recommended)

```bash
# Mở credential manager trong session
/auth
```

Labels: `[stored]` (saved via /auth), `[env: VARNAME]` (from env), `[missing]` (no key).

### dcode auth (Shell)

```bash
# List providers
dcode auth list

# Store key (from stdin)
echo "$ANTHROPIC_API_KEY" | dcode auth set anthropic

# Store key from env var
dcode auth set openai --from-env OPENAI_API_KEY

# Remove key
dcode auth remove anthropic

# Show store path
dcode auth path
```

### Environment Variables

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."

# Scope to dcode only
export DEEPAGENTS_CODE_OPENAI_API_KEY="sk-..."
```

### Key Resolution Order

1. `DEEPAGENTS_CODE_`-prefixed env var (highest)
2. App-stored key (via `/auth`)
3. Plain provider env var (lowest)

### Enable Web Search (Tavily)

```bash
# Via /auth
/auth → select Tavily → paste key

# Via env var
export TAVILY_API_KEY="tvly-..."
```

## Provider Reference (dcode)

| Provider | Package | Env Var |
|----------|---------|---------|
| OpenAI | `langchain-openip` | `OPENAI_API_KEY` |
| OpenAI (Codex) | `langchain-openip` | Sign in with ChatGPT |
| Azure OpenAI | `langchain-openip` | `AZURE_OPENAI_API_KEY` |
| Anthropic | `langchain-anthropic` | `ANTHROPIC_API_KEY` |
| Google Gemini | `langchain-google-genai` | `GOOGLE_API_KEY` |
| Baseten | `langchain-baseten` | `BASETEN_API_KEY` |
| AWS Bedrock | `langchain-aws` | `AWS_ACCESS_KEY_ID` |
| HuggingFace | `langchain-huggingface` | `HUGGINGFACEHUB_API_TOKEN` |
| Ollama | `langchain-ollama` | `OLLAMA_API_KEY` |
| Groq | `langchain-groq` | `GROQ_API_KEY` |
| Fireworks | `langchain-fireworks` | `FIREWORKS_API_KEY` |
| Mistral AI | `langchain-mistralai` | `MISTRAL_API_KEY` |
| DeepSeek | `langchain-deepseek` | `DEEPSEEK_API_KEY` |
| OpenRouter | `langchain-openrouter` | `OPENROUTER_API_KEY` |
| LiteLLM | `langchain-litellm` | Per-provider |

### Sign in with ChatGPT

```bash
/auth → select openai_codex → browser sign-in → Codex models appear
```

## Model Resolution (dcode)

Khi launch, model resolve theo thứ tự:
1. `--model` flag
2. `[models].default` trong config.toml
3. `[models].recent` (auto-saved từ `/model`)
4. Environment auto-detection: `OPENAI_API_KEY` → `ANTHROPIC_API_KEY` → `GOOGLE_API_KEY`

## MCP Configuration

Xem [MCP](mcp.md) cho details về `.mcp.json` format.

## Trang Liên Quan

- [Deep Agents Code Overview](deep-agents-code-overview.md) — dcode CLI
- [Deep Agents Code Data Locations](deep-agents-code-data-locations.md) — Directory structure
- [MCP](mcp.md) — MCP tools
- [Chat Models](chat-models.md) — Supported models
