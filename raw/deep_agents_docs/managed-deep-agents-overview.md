[Managed Deep Agents](https://docs.langchain.com/langsmith/managed-deep-agents-overview)

Managed Deep Agents
===================

Copy page

Overview of Managed Deep Agents private beta features, workflows, and limits.

Copy page

Managed Deep Agents is a hosted runtime for creating, running, and operating deep agents in LangSmith. Use it to run durable, long-running agents without standing up your own agent server.
It pairs the [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) harness with managed infrastructure: durable runs, [LangSmith sandboxes](https://docs.langchain.com/langsmith/sandboxes), thread state, MCP tools, file trees, traces, and agent revisions.

Managed Deep Agents is in **private beta**, available on [LangSmith Cloud](https://docs.langchain.com/langsmith/cloud) in the US region only. [Join the waitlist](https://www.langchain.com/langsmith-managed-deep-agents-waitlist) to request access.

The recommended workflow is:

1. Create or edit a local Managed Deep Agents project.
2. Keep the default backend or opt into a LangSmith sandbox backend.
3. Connect MCP tools when the agent needs external capabilities.
4. Deploy the project to Managed Deep Agents.
5. Run the agent with the Python or TypeScript SDK.
6. Inspect traces, files, tool calls, runtime state, and revisions in LangSmith.

[​](https://docs.langchain.com/langsmith/managed-deep-agents-overview#follow-the-workflow) Follow the workflow
--------------------------------------------------------------------------------------------------------------

[Quickstart
----------

Deploy a first agent with the CLI, then run it from code.](https://docs.langchain.com/langsmith/managed-deep-agents-quickstart)

[Connect tools
-------------

Register static-header or OAuth MCP servers and reference their tools from agents.](https://docs.langchain.com/langsmith/managed-deep-agents-mcp)

[Deploy an agent
---------------

Create or update Managed Deep Agents with the CLI, SDK, or REST API.](https://docs.langchain.com/langsmith/managed-deep-agents-deploy)

[Run an agent
------------

Create threads and stream Managed Deep Agent runs with the SDK or REST API.](https://docs.langchain.com/langsmith/managed-deep-agents-invoke)

[SDKs
----

Use the Python, TypeScript, and React SDKs for Managed Deep Agents.](https://docs.langchain.com/langsmith/managed-deep-agents-sdk)

[CLI reference
-------------

Review all deploy commands, project files, flags, and validation rules.](https://docs.langchain.com/langsmith/managed-deep-agents-cli)

[API reference
-------------

Review common REST commands and generated endpoint reference pages.](https://docs.langchain.com/langsmith/managed-deep-agents-api)

[​](https://docs.langchain.com/langsmith/managed-deep-agents-overview#use-managed-deep-agents) Use Managed Deep Agents
----------------------------------------------------------------------------------------------------------------------

Use Managed Deep Agents to:

* Create and manage deep agents from local project files.
* Run long-running agents without standing up a custom agent server.
* Give each thread or agent isolated LangSmith sandbox resources for code execution, filesystem work, and long-running tasks.
* Stream runs and persist thread state.
* Use a managed file tree for instructions, skills, subagents, tools, and runtime files.
* Register workspace-level MCP servers, including OAuth MCP servers, and list their available tools.
* Inspect traces and agent behavior in LangSmith.

You can also deploy Deep Agents with a standard [LangSmith Deployment](https://docs.langchain.com/langsmith/deployment-quickstart). Use that path when you need custom application code, custom routes, advanced authentication, full Agent Server APIs, stronger isolation controls, or maximum scalability.

[​](https://docs.langchain.com/langsmith/managed-deep-agents-overview#created-resources) Created resources
----------------------------------------------------------------------------------------------------------

When you create a Managed Deep Agent, LangSmith provisions:

* A Managed Deep Agent resource.
* A separate [LangSmith tracing project](https://docs.langchain.com/langsmith/observability-concepts#projects) for the agent.
* A [Context Hub](https://docs.langchain.com/langsmith/use-the-context-hub) agent repo that stores the managed file tree.

It does not create a LangSmith Deployment.
Managed Deep Agent runs are traced in the separate tracing project created for the agent. Open traces in LangSmith to inspect user inputs, final responses, model calls, tool calls, subagent activity, files, and runtime state created during the run.
The Context Hub agent repo stores the managed file tree for the agent, including instructions, skills, subagents, and tool configuration.

[​](https://docs.langchain.com/langsmith/managed-deep-agents-overview#langsmith-sandbox-backends) LangSmith sandbox backends
----------------------------------------------------------------------------------------------------------------------------

Managed Deep Agents projects generated by `deepagents-cli>=0.2.2` use the `state` backend:

```
{
  "backend": {
    "type": "state"
  }
}
```

LangSmith sandboxes are isolated environments for operations such as running code and interacting with a filesystem without affecting your main infrastructure. In Managed Deep Agents, they give agents a managed runtime for long-running work while LangSmith handles the underlying sandbox lifecycle.
Choose the backend that matches your scope:

* `state`: applies no sandbox-specific backend behavior.
* `sandbox` with `sandbox_config.scope: "thread"`: scopes sandbox resources to each thread.
* `sandbox` with `sandbox_config.scope: "agent"`: scopes the sandbox to the agent rather than to individual threads.

For standalone sandbox concepts, see the [LangSmith sandboxes overview](https://docs.langchain.com/langsmith/sandboxes). For Managed Deep Agents configuration fields and validation rules, see [Deploy an agent](https://docs.langchain.com/langsmith/managed-deep-agents-deploy#choose-a-backend) and the [CLI reference](https://docs.langchain.com/langsmith/managed-deep-agents-cli#project-file-reference).

[​](https://docs.langchain.com/langsmith/managed-deep-agents-overview#limits-and-notes) Limits and notes
--------------------------------------------------------------------------------------------------------

Operational notes that apply during private beta. Behavior may change before general availability.

### [​](https://docs.langchain.com/langsmith/managed-deep-agents-overview#stable-deploy-experience) Stable deploy experience

Managed Deep Agents deploy is available through the beta CLI release during private beta. The stable Deep Agents deploy experience continues to work until Managed Deep Agents reaches public beta and the deploy command switches to the new behavior.

### [​](https://docs.langchain.com/langsmith/managed-deep-agents-overview#supported-models) Supported models

Pass model identifiers in the form `{provider}:{model_id}`. For example, `openai:gpt-5.5`. The runtime resolves models with `init_chat_model`, so any provider that `init_chat_model` supports is usable from Managed Deep Agents. See [Supported providers and models](https://docs.langchain.com/oss/python/langchain/models#supported-providers-and-models) for the current list.
Values without a colon are interpreted as references to a saved Playground configuration rather than as model identifiers. Always supply the full `{provider}:{model_id}` form when configuring a model directly.

### [​](https://docs.langchain.com/langsmith/managed-deep-agents-overview#thread-retention) Thread retention

Threads have no retention window or per-workspace cap during private beta. Create as many as you need. Existing threads remain accessible for the duration of the beta.

### [​](https://docs.langchain.com/langsmith/managed-deep-agents-overview#rate-limits-and-quotas) Rate limits and quotas

The Managed Deep Agents endpoints do not enforce per-key, per-workspace, or per-agent request rate limits during private beta.

### [​](https://docs.langchain.com/langsmith/managed-deep-agents-overview#agent-limits) Agent limits

Free LangSmith workspaces are limited to one Managed Deep Agent. Paid LangSmith plans can create unlimited agents. When a free workspace is already at its limit, `deepagents deploy` and `POST /v1/deepagents/agents` fail with `HTTP 409` and a message to delete the existing agent or upgrade your plan.

### [​](https://docs.langchain.com/langsmith/managed-deep-agents-overview#delete-agents) Delete agents

`DELETE /v1/deepagents/agents/{agent_id}` does not cascade to threads. Threads created against a deleted agent remain queryable but cannot start new runs. Track and delete threads explicitly when you want to clean them up.

### [​](https://docs.langchain.com/langsmith/managed-deep-agents-overview#api-stability) API stability

Routes live under `/v1/deepagents`, but the surface is in private beta and may change before general availability. Breaking changes are communicated to beta customers directly through the contact provided when access was granted.

### [​](https://docs.langchain.com/langsmith/managed-deep-agents-overview#support-and-feedback) Support and feedback

Beta access includes direct support. The contact for bug reports and feature requests is included in the email you receive when access is granted.

[​](https://docs.langchain.com/langsmith/managed-deep-agents-overview#private-beta-scope) Private beta scope
------------------------------------------------------------------------------------------------------------

Managed Deep Agents is available on LangSmith Cloud in the US region only during private beta. Self-hosted and Hybrid deployments are not supported, and EU and other regions are planned after general availability.
The API also does not mirror every LangSmith Deployment endpoint in private beta. A Managed Deep Agent is not a LangSmith Deployment.


---

[Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

YesNo

[Cloud platform features

Previous](https://docs.langchain.com/langsmith/cloud-platform-features)[Managed Deep Agents quickstart

Next](https://docs.langchain.com/langsmith/managed-deep-agents-quickstart)

Ctrl+I