[Deep Agents Code](https://docs.langchain.com/oss/python/deepagents/code/overview)

Memory and Skills
=================

Copy page

Persistent memory, AGENTS.md files, and reusable skills for Deep Agents Code, including creation, discovery, and invocation.

Copy page

There are two primary ways to customize an agent in Deep Agents Code:

* **[Memory](#memory)**: `AGENTS.md` files and auto-saved memories that persist across sessions. Use memory for general coding style, preferences, and learned conventions.
* **[Skills](#skills)**: Reusable, on-demand capabilities that the agent discovers and reads only when relevant. Use skills for task-specific context such as workflows, best practices, and reference docs.

In practice, skills and memory sit on a spectrum. For more on when to use each, see [Skills, memory, and tools](/oss/python/deepagents/skills#skills-memory-and-tools).
Use `/remember` to explicitly prompt the agent to update its memory and skills from the current conversation.

Building a custom agent with the SDK? See [Memory](/oss/python/deepagents/memory) for programmatic memory backends.

[​](#memory) Memory
-------------------

### [​](#automatic-memory) Automatic memory

As you use the agent, it automatically stores information in `~/.deepagents/<agent_name>/memories/` as markdown files using a memory-first protocol:

1. **Research**: Searches memory for relevant context before starting tasks
2. **Response**: Checks memory when uncertain during execution
3. **Learning**: Automatically saves new information for future sessions

The agent organizes its memories by topic with descriptive filenames:

```
~/.deepagents/backend-dev/memories/
├── api-conventions.md
├── database-schema.md
└── deployment-process.md
```

When you teach the agent conventions:

```
dcode --agent backend-dev
> Our API uses snake_case and includes created_at/updated_at timestamps
```

It remembers for future sessions:

```
> Create a /users endpoint
# Applies conventions without prompting
```

### [​](#agents-md-files) AGENTS.md files

[`AGENTS.md` files](https://agents.md/) provide persistent context that is always loaded at session start:

* **Global**: `~/.deepagents/<agent_name>/AGENTS.md`—loaded every session.
* **Project**: `.deepagents/AGENTS.md` in any git project root—loaded when Deep Agents Code is run from within that project.

Both files are appended to the system prompt at startup.

### [​](#how-memory-works) How memory works

The agent may also read its memory files when answering project-specific questions or when you reference past work or patterns.
The agent updates `AGENTS.md` as you provide information on how it should behave, feedback on its work, or instructions to remember something.
It also updates its memory if it identifies patterns or preferences from your interactions.
To add more structured project knowledge in additional memory files, add them in `.deepagents/` and reference them in the `AGENTS.md` file.
You must reference additional files in the `AGENTS.md` file for the agent to be aware of them.
The additional files are not read on startup but the agent can reference and update them when needed.

### [​](#when-to-use-global-vs-project-agents-md) When to use global vs. project AGENTS.md

Use a global `AGENTS.md` (`~/.deepagents/agent/AGENTS.md`) for:

* Your personality, style, and universal coding preferences
* General tone and communication style
* Universal coding preferences (formatting, type hints, etc.)
* Tool usage patterns that apply everywhere
* Workflows and methodologies that don’t change per-project

Use a project `AGENTS.md` (`.deepagents/AGENTS.md` in project root) for:

* Project-specific context and conventions
* Project architecture and design patterns
* Coding conventions specific to this codebase
* Testing strategies and deployment processes
* Team guidelines and project structure

[​](#skills) Skills
-------------------

Skills package domain expertise, such as workflows, best practices, scripts, and reference docs, into reusable directories that the agent discovers and reads only when relevant.
Deep agent skills follow the [Agent Skills specification](https://agentskills.io/). For more on how skills work and how to write effective ones, see [Skills](/oss/python/deepagents/skills).
At startup, Deep Agents Code reads the name and description from each `SKILL.md` file’s frontmatter. When a task matches a skill’s description, the agent reads the skill file and follows its instructions. Discovery runs again on `/reload`.

### [​](#add-a-skill) Add a skill

1

Create a skill

```
# User skill (stored in ~/.deepagents/<agent_name>/skills/)
dcode skills create test-skill

# Project skill (stored in .deepagents/skills/)
dcode skills create test-skill --project
```

This generates:

```
skills/
└── test-skill
    └── SKILL.md
```

2

Edit SKILL.md

Open the generated `SKILL.md` and edit the file to include your instructions.

3

Add optional resources

Optionally add additional scripts or other resources to the `test-skill` folder. For more information, see [Usage](/oss/python/deepagents/skills#add-supporting-resources).

You can also copy existing skills directly to the agent’s folder:

```
mkdir -p ~/.deepagents/<agent_name>/skills
cp -r examples/skills/web-research ~/.deepagents/<agent_name>/skills/
```

### [​](#install-community-skills) Install community skills

You can use tools like Vercel’s [Skills CLI](https://github.com/vercel-labs/skills) to install community [Agent Skills](https://agentskills.io/) in your environment and make them available to your deep agents:

```
# Install a skill globally
npx skills add vercel-labs/agent-skills --skill web-design-guidelines -a deepagents -g -y

# List installed skills
npx skills ls -a deepagents -g
```

Global installs (`-g`) symlink skills into `~/.deepagents/agent/skills/`—the default agent’s user-level skills directory. Project-level installs (omit `-g`) place skills in `.deepagents/skills/` relative to the current directory, making them available to any agent running in that project regardless of agent name.

Global installs target the default `agent` directory only. If you use a custom-named agent, either use project-level installs or manually symlink the skill into `~/.deepagents/{your-agent}/skills/`.

### [​](#skill-discovery) Skill discovery

Skills are loaded from the following directories at startup:

```
~/.deepagents/<agent_name>/skills/
~/.agents/skills/
.deepagents/skills/
.agents/skills/
~/.claude/skills/          (experimental)
.claude/skills/            (experimental)
```

When duplicate skill names exist, later-precedence directories override earlier ones (see [App data](/oss/python/deepagents/code/data-locations#skills)).
For project-specific skills (under `.deepagents/skills/` or `.agents/skills/`), the project root is identified by a containing `.git` folder.

### [​](#invoke-a-skill-mid-session) Invoke a skill mid-session

Inside an interactive session, run a skill directly with the `/skill:<name>` slash command:

```
/skill:code-review
/skill:code-review review the auth module
```

The skill’s `SKILL.md` instructions are injected into the prompt along with any arguments you pass.

### [​](#launch-with-a-skill) Launch with a skill

The `--skill` flag invokes a skill immediately on launch, in either interactive (TUI) or non-interactive (headless) mode:

```
# Open the TUI and immediately run a skill
dcode --skill code-review

# Pass a request to the skill with -m
dcode --skill code-review -m 'review the auth module'

# Pipe content into a skill
cat diff.txt | dcode --skill code-review

# Pipe content and add a request
cat diff.txt | dcode --skill code-review -m 'focus on security'

# Run a skill headlessly
dcode --skill code-review -n 'review this patch'

# Quiet mode (only agent output on stdout)
dcode --skill code-review -n 'review this patch' -q
```

`--skill` with `--quiet` or `--no-stream` requires `-n` (non-interactive mode).

### [​](#list-skills) List skills

```
# List all user skills
dcode skills list

# List project skills
dcode skills list --project

# Get detailed info about a specific skill
dcode skills info test-skill
dcode skills info test-skill --project
```

---

[Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/code/memory-and-skills.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

YesNo

[Deep Agents Code

Previous](https://docs.langchain.com/oss/python/deepagents/code/overview)[Use remote sandboxes

Next](https://docs.langchain.com/oss/python/deepagents/code/remote-sandboxes)

Ctrl+I