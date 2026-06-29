---
tags: [langchain, deep-agents, concept]
created: 2026-06-29
updated: 2026-06-29
sources: [deep-agents-sdk]
related: [concepts/deep-agents-memory, concepts/deep-agents-context-engineering, concepts/deep-agents-overview]
---

# Deep Agents — Skills System

**Skills** package domain expertise — workflows, best practices, scripts, reference docs — vào reusable directories. Agent dùng **progressive disclosure**: chỉ đọc metadata lúc startup, đọc full instructions khi cần.

## Progressive Disclosure

Skills load theo 3 levels:

| Level | What loads | When |
|-------|------------|------|
| **1. Metadata** | `name` + `description` từ SKILL.md frontmatter | Agent startup, cho mọi skill |
| **2. Instructions** | Full SKILL.md body | Khi skill được invoked |
| **3. Resources** | Supporting files (`scripts/`, `references/`, `assets/`) | Khi instructions reference |

## Structure

```
skills/
└── langgraph-docs/
    ├── SKILL.md          # Required: frontmatter + instructions
    ├── scripts/          # Optional: executable code
    ├── references/       # Optional: reference docs
    └── assets/           # Optional: assets
```

### SKILL.md Format

```markdown
---
name: langgraph-docs
description: Use this skill for requests related to LangGraph to fetch relevant documentation.
---

# langgraph-docs

## Instructions

1. Fetch https://docs.langchain.com/llms.txt
2. Identify 2-4 relevant pages
3. Fetch and synthesize
```

### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique skill name |
| `description` | Yes | What skill does + when to use (keywords!) |

## Usage trong SDK

```python
from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend

backend = FilesystemBackend(root_dir="./my-project")
agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    backend=backend,
    skills=["./my-project/skills/"],
)
```

## Write Effective Skills

- **Keep frontmatter concise** — mọi skill's frontmatter được add vào system prompt
- **SKILL.md body < 5,000 tokens**
- **Write specific descriptions** — tell agent both *what* and *when*
- **Differentiate overlapping skills** — consolidate nếu quá giống

```markdown
# Good
description: >-
  Extract text and tables from PDF files, fill PDF forms, and merge
  multiple PDFs. Use when working with PDF documents.

# Bad
description: Helps with PDFs.
```

## Skills in Deep Agents Code (dcode CLI)

```bash
# Create skill
dcode skills create test-skill
dcode skills create test-skill --project  # Project-level

# List skills
dcode skills list
dcode skills list --project

# Invoke mid-session
/skill:code-review
/skill:code-review review the auth module

# Launch with skill
dcode --skill code-review
```

### Skill Discovery Paths

```
~/.deepagents/<agent_name>/skills/     # User-level
~/.agents/skills/                       # Tool-agnostic
.deepagents/skills/                     # Project-level
.agents/skills/                         # Project tool-agnostic
~/.claude/skills/ (experimental)
.claude/skills/ (experimental)
```

## Community Skills

```bash
npx skills add vercel-labs/agent-skills --skill web-design-guidelines -a deepagents -g -y
```

## Trang Liên Quan

- [Deep Agents Memory](deep-agents-memory.md) — Memory (always-loaded context)
- [Deep Agents Context Engineering](deep-agents-context-engineering.md) — Context management
- [Deep Agents Customization](deep-agents-customization.md) — Skills parameter
