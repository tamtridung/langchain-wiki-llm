---
tags: [langchain, deep-agents, concept]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/deep-agents-code-overview, concepts/deep-agents-code-configuration, concepts/deep-agents-memory]
---

# Deep Agents Code — Data Locations

Nơi `dcode` lưu trữ configuration, sessions, memory, skills, và subagents.

## Directory Structure

```
~/.deepagents/
├── .state/
│   ├── sessions.db           # SQLite checkpoint DB
│   ├── history.jsonl         # Command history
│   ├── chatgpt-auth.json     # ChatGPT OAuth token
│   ├── auth.json             # Stored API keys
│   ├── mcp-tokens/           # MCP OAuth tokens
│   └── ...
└── {agent}/
    ├── AGENTS.md             # User customizations
    ├── skills/               # User-level skills
    │   └── {name}/SKILL.md
    ├── agents/               # Custom subagents
    │   └── {name}/AGENTS.md
    └── memories/             # Auto-saved memories
        ├── api-conventions.md
        └── database-schema.md

~/.agents/
└── skills/                   # Tool-agnostic skills

{project}/
├── AGENTS.md                 # Project instructions
├── .deepagents/
│   ├── AGENTS.md
│   ├── skills/
│   └── agents/
└── .agents/
    └── skills/
```

## What Goes Where

| Data | Location | R/W |
|------|----------|-----|
| Sessions | `~/.deepagents/.state/sessions.db` | R/W |
| Input history | `~/.deepagents/.state/history.jsonl` | R/W |
| ChatGPT OAuth | `~/.deepagents/.state/chatgpt-auth.json` | R/W |
| Base instructions | Package `default_agent_prompt.md` | R |
| User customizations | `~/.deepagents/{agent}/AGENTS.md` | R/W |
| Project instructions | `.deepagents/AGENTS.md` or `AGENTS.md` | R |
| User skills | `~/.deepagents/{agent}/skills/` | R/W |
| Shared skills | `~/.agents/skills/` | R |
| Project skills | `.deepagents/skills/` or `.agents/skills/` | R |
| Custom subagents | `~/.deepagents/{agent}/agents/` | R/W |
| Project subagents | `.deepagents/agents/` | R |

## Precedence Rules

### Skills (lowest → highest)
1. `~/.deepagents/{agent}/skills/` — User dcode
2. `~/.agents/skills/` — User tool-agnostic
3. `.deepagents/skills/` — Project dcode
4. `.agents/skills/` — Project tool-agnostic (cao nhất)

### Subagents (lowest → highest)
1. `~/.deepagents/{agent}/agents/` — User-level
2. `.deepagents/agents/` — Project-level (cao nhất)

### Instructions
All sources **combined** (not override):
1. Package base prompt (always)
2. `~/.deepagents/{agent}/AGENTS.md` (appended)
3. `.deepagents/AGENTS.md` (appended)
4. `AGENTS.md` at project root (appended)

## `.deepagents` vs `.agents`

| Directory | Purpose |
|-----------|---------|
| `.deepagents/` | dcode-specific features |
| `.agents/` | Tool-agnostic (share across AI CLIs) |

## Cleaning Up

| Action | Command |
|--------|---------|
| Reset all data | `rm -rf ~/.deepagents` |
| Clear sessions | `rm ~/.deepagents/.state/sessions.db*` |
| Clear API keys | `rm ~/.deepagents/.state/auth.json` |
| Clear MCP tokens | `rm -rf ~/.deepagents/.state/mcp-tokens` |
| Reset agent instructions | `dcode agents reset --agent {name}` |

## Trang Liên Quan

- [Deep Agents Code Overview](deep-agents-code-overview.md) — dcode CLI
- [Deep Agents Code Configuration](deep-agents-code-configuration.md) — config.toml
- [Deep Agents Memory](deep-agents-memory.md) — Memory systems
