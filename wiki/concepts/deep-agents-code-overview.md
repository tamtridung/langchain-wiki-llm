---
tags: [langchain, deep-agents, concept]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/deep-agents-overview, concepts/deep-agents-code-configuration, concepts/sandboxes]
---

# Deep Agents Code (`dcode`) — CLI Coding Agent

**Deep Agents Code** (`dcode`) là open-source terminal coding agent built on Deep Agents SDK. Nó làm việc với bất kỳ LLM nào hỗ trợ tool calling và hỗ trợ switching providers/models mid-session.

## Quickstart

```bash
# Install
curl -LsSf https://langch.in/dcode | bash

# Launch
dcode

# With specific model
dcode --model anthropic:claude-opus-4-8
dcode --model openai:gpt-5.5
```

## Capabilities

- **File operations** — read, write, edit files
- **Shell execution** — run tests, build, manage dependencies
- **Remote sandboxes** — run tools remotely (LangSmith, AgentCore, Daytona, Modal, Runloop, Vercel)
- **Web search** — Tavily-powered
- **Task planning & tracking** — `write_todos`
- **Subagents** — delegate via `AGENTS.md` files
- **Memory** — persistent markdown files, auto-saved
- **Context compaction** — summarize older messages, offload to storage
- **Human-in-the-loop** — approval cho sensitive operations
- **Skills** — reusable capabilities
- **MCP tools** — external Model Context Protocol servers
- **Tracing** — LangSmith observability

## Built-in Tools

| Tool | Description | HITL |
|------|-------------|------|
| `ls` | List files | — |
| `read_file` | Read file (multimodal) | — |
| `write_file` | Create/overwrite | Required |
| `edit_file` | Targeted edits | Required |
| `glob` | Find files by pattern | — |
| `grep` | Search text in files | — |
| `execute` | Shell commands (local/sandbox) | Required |
| `web_search` | Tavily search | Required |
| `fetch_url` | Fetch URL → markdown | Required |
| `task` | Delegate to subagents | Required |
| `ask_user` | Ask user questions | — |
| `compact_conversation` | Summarize & offload | Mixed |
| `write_todos` | Task planning | — |
| `get_current_thread_id` | Get thread ID for LangSmith | — |

## CLI Flags

| Flag | Description |
|------|-------------|
| `-a, --agent NAME` | Named agent with separate memory |
| `-M, --model MODEL` | Specific model (`provider:model`) |
| `-r, --resume [ID]` | Resume session |
| `-m, --message TEXT` | Initial prompt (non-interactive) |
| `-n, --non-interactive TEXT` | Headless mode |
| `-y, --auto-approve` | Skip HITL prompts |
| `-S, --shell-allow-list LIST` | Auto-approve shell commands |
| `--sandbox TYPE` | Remote sandbox for execution |
| `--mcp-config PATH` | Explicit MCP config |
| `--no-mcp` | Disable MCP |
| `--skill NAME` | Invoke skill at startup |
| `--startup-cmd CMD` | Shell command before first prompt |
| `--max-turns N` | Cap agentic turns (non-interactive) |
| `--timeout SECONDS` | Wall-clock timeout (non-interactive) |
| `-q, --quiet` | Clean output for piping |
| `--acp` | Run as ACP server |
| `--update` | Check for updates |

## CLI Commands

| Command | Description |
|---------|-------------|
| `dcode agents list` | List agents |
| `dcode agents reset --agent NAME` | Clear agent memory |
| `dcode skills list [--project]` | List skills |
| `dcode skills create NAME` | Create skill |
| `dcode skills info NAME` | Show skill details |
| `dcode threads list` | List sessions |
| `dcode threads delete ID` | Delete session |
| `dcode mcp login NAME` | OAuth login for MCP |
| `dcode config show` | Show effective config |
| `dcode config get <key>` | Get specific config value |
| `dcode auth list` | List provider credentials |
| `dcode update` | Check for updates |

## Non-Interactive Mode

```bash
# Run single task, exit
dcode -n "Create a Python script that prints Hello World"

# Pipe content
git diff | dcode -n "Review these changes"

# With auto-approve
dcode -n "Run tests" -y

# With shell allow list
dcode -n "Install deps and run tests" -S "recommended"
```

## Trang Liên Quan

- [Deep Agents Code Configuration](deep-agents-code-configuration.md) — config.toml, credentials
- [Deep Agents Code Data Locations](deep-agents-code-data-locations.md) — Directory structure
- [Deep Agents Overview](deep-agents-overview.md) — Deep Agents SDK overview
- [Sandboxes](sandboxes.md) — Remote sandbox backends
