[Get started](https://docs.langchain.com/oss/python/deepagents/quickstart)

Comparison with Claude Agent SDK
================================

Copy page

Compare LangChain Deep Agents with the Claude Agent SDK to choose the right tool for your use case.

Copy page

This page explains how [LangChain Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) compares to the [Claude Agent SDK](https://platform.anthropic.com/docs/en/agent-sdk/overview). Both are harnesses for building custom agents, but they make different tradeoffs around execution environments, deployment, and vendor coupling.

Deep Agents is used in production by [OpenSWE](https://github.com/langchain-ai/open-swe) and [LangSmith Fleet](https://docs.langchain.com/langsmith/fleet/index).

[​](https://docs.langchain.com/oss/python/deepagents/comparison#at-a-glance) At a glance
----------------------------------------------------------------------------------------

|  | **Deep Agents** | **Claude Agent SDK** |
| --- | --- | --- |
| **Where the agent runs** | Inside a sandbox, or outside a sandbox executing commands remotely | Inside a sandbox |
| **Execution backend** | Pluggable: [local, virtual filesystem, remote sandbox, or custom](https://docs.langchain.com/oss/python/deepagents/backends) | Local filesystem of the sandbox it runs in |
| **Model provider** | Any (Anthropic, OpenAI, Google, 100+ others) | Claude (Anthropic, Bedrock, Vertex, Azure) |
| **Per-provider/model tuning** | [Harness profiles](https://docs.langchain.com/oss/python/deepagents/profiles) (beta): declarative bundles of system prompt, tool, middleware, and subagent tweaks, registered per provider or specific model | Configure in code at each model call site |
| **Deployment** | [Managed Deep Agents](https://docs.langchain.com/langsmith/managed-deep-agents-overview) in LangSmith, or self-host a [standalone image](https://docs.langchain.com/langsmith/deploy-standalone-server) via [`langgraph build`](https://docs.langchain.com/langsmith/cli#build) | [Self-host](https://code.claude.com/docs/en/agent-sdk/hosting). You build the server, auth, and streaming layer. [Claude managed agents](https://platform.claude.com/docs/en/managed-agents/overview) is a separate product |
| **Multi-tenancy** | [Built-in](https://docs.langchain.com/oss/python/deepagents/going-to-production#multi-tenancy): scoped threads, per-user sandboxes, RBAC | Build it yourself |
| **License** | MIT | MIT (Claude Code itself is proprietary) |

[​](https://docs.langchain.com/oss/python/deepagents/comparison#main-differences) Main differences
--------------------------------------------------------------------------------------------------

### [​](https://docs.langchain.com/oss/python/deepagents/comparison#agent-and-execution-environment) Agent and execution environment

There are [two patterns for connecting agents to sandboxes](https://www.langchain.com/blog/the-two-patterns-by-which-agents-connect-sandboxes): running the agent *inside* the sandbox, or running the agent outside and **using the sandbox as a tool**.
The Claude Agent SDK only supports the first. Your agent runs inside a sandbox and executes tools against the sandbox’s local filesystem. Anthropic’s hosted model [Claude managed agents](https://platform.claude.com/docs/en/managed-agents/overview) use a decoupled model, which reflects where production agent architectures are heading.
Deep Agents supports both, and lets you pick a [backend](https://docs.langchain.com/oss/python/deepagents/backends#quickstart) to wire them together. In practice, this means you can:

* Run the agent inside a sandbox (same model as Claude Agent SDK).
* Run the agent in a long-lived container and [use a remote sandbox as a tool](https://www.langchain.com/blog/the-two-patterns-by-which-agents-connect-sandboxes), executing commands over the network.
* Swap in a virtual filesystem for tests, or a custom backend for your own infrastructure.

### [​](https://docs.langchain.com/oss/python/deepagents/comparison#multi-tenancy) Multi-tenancy

When you productionize your application, you generally expose it to many end users and must isolate the environment for each user.
In Claude Agent SDK, the SDK ties the agent to its sandbox. To give each user an isolated execution environment, you must build an API wrapper that spins up a sandbox per user, tracks which sandbox belongs to whom, and tears it down afterwards.
Deep Agents handles this directly: configure a sandbox [per user or per assistant](https://docs.langchain.com/oss/python/deepagents/going-to-production#lifecycle) in the harness, with scoped threads, run history, and [RBAC](https://docs.langchain.com/oss/python/deepagents/going-to-production#team-access-control-rbac) included. If you use [LangSmith Sandbox](https://docs.langchain.com/langsmith/sandbox-auth-proxy), you also get an auth proxy out of the box so end users can call third-party APIs from the sandbox without you provisioning credentials per user.

### [​](https://docs.langchain.com/oss/python/deepagents/comparison#a-production-agent-server) A production agent server

To expose a [self-hosted Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/hosting) app to end users, you write your own HTTP/WebSocket or SSE server that invokes the agent, streams tokens back, and manages conversation threads. That server is yours to build, operate, and secure.
Deep Agents deployments include an [agent server](https://docs.langchain.com/langsmith/agent-server) out of the box: streaming endpoints, thread management, run history, webhooks, and [authentication](https://docs.langchain.com/langsmith/auth).

### [​](https://docs.langchain.com/oss/python/deepagents/comparison#managed-cloud-or-self-hosted) Managed cloud or self-hosted

Claude Agent SDK deployments are [self-hosted](https://code.claude.com/docs/en/agent-sdk/hosting). The SDK and [Claude managed agents](https://platform.claude.com/docs/en/managed-agents/overview) are separate products. Code written against the SDK does not deploy directly to the managed offering.
Deep agents run in two modes without code changes:

* **Managed:** create, run, and operate deep agents with [Managed Deep Agents](https://docs.langchain.com/langsmith/managed-deep-agents-overview) in LangSmith.
* **Self-hosted:** run [`langgraph build`](https://docs.langchain.com/langsmith/cli#build) to produce a [standalone Docker image](https://docs.langchain.com/langsmith/deploy-standalone-server) you can deploy anywhere.

For a managed agent platform that works across any model provider, use [LangSmith Fleet](https://docs.langchain.com/langsmith/fleet/index). [Claude managed agents](https://platform.claude.com/docs/en/managed-agents/overview) is limited to the Anthropic ecosystem.

### [​](https://docs.langchain.com/oss/python/deepagents/comparison#llm) LLM

Claude Agent SDK execution bundles the model, backend, and deployment and optimizes support between all three.
With Deep Agents, you pick the model provider, the execution backend, and the deployment target independently. By choosing this harness you retain maximum flexibility in your choice of model and infrastructure.

### [​](https://docs.langchain.com/oss/python/deepagents/comparison#ecosystems) Ecosystems

The Claude Agent SDK is purpose-built for Claude and Anthropic’s product surface. Deep Agents integrates with the broader LangChain ecosystem, including LangSmith for observability, evaluation, and deployment, and works across any model provider.

[​](https://docs.langchain.com/oss/python/deepagents/comparison#summary) Summary
--------------------------------------------------------------------------------

* **Choose Deep Agents** if you want model and infrastructure flexibility, built-in multi-tenant deployment, and the option to run managed or self-hosted without code changes.
* **Choose Claude Agent SDK** if you are already invested in the Anthropic ecosystem and wish to self-host and build the API, auth, and multi-tenant layers yourself.

**Notice a mistake?**We drafted this comparison on April 16th, 2026. If products have changed, please [file an issue](https://github.com/langchain-ai/docs/issues).

---

[Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/comparison.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

YesNo

[Customize Deep Agents

Previous](https://docs.langchain.com/oss/python/deepagents/customization)[Changelog

Next](https://docs.langchain.com/oss/python/deepagents/changelog-py)

Ctrl+I