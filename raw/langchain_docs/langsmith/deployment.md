---
title: LangSmith Deployment
source: https://docs.langchain.com/langsmith/deployment.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# LangSmith Deployment

> Deploy and manage agents with durable execution, real-time streaming, and horizontal scaling.

LangSmith Deployment is a workflow orchestration runtime purpose-built for agent workloads. It provides the managed infrastructure agents need to run reliably in production at scale, supporting the full lifecycle from local development to deployment.

## Deployable products

LangSmith Deployment is framework-agnostic which means you can deploy agents built with:

<CardGroup cols={2}>
  <Card title="Deep Agents" cta="Open quickstart" href="/langsmith/managed-deep-agents-overview" icon="robot">
    Create, run, and operate Managed Deep Agents through the private preview API.
  </Card>

  <Card title="LangGraph (and LangChain)" cta="Open quickstart" href="/langsmith/deployment-quickstart" icon="chart-dots-3">
    Use the LangGraph CLI and app templates to deploy a LangGraph application to LangSmith.
  </Card>

  <Card title="Google ADK" cta="View guide" href="/langsmith/deploy-google-adk" icon="google">
    Deploy Google Agent Development Kit (ADK) agent as a LangGraph with the `deployments-wrap-sdk` package.
  </Card>

  <Card title="Other frameworks" cta="View guide" href="/langsmith/deploy-other-frameworks" icon="packages">
    Deploy Claude Agent SDK, Strands, CrewAI, AutoGen, and other agent frameworks with the Functional API or `deployments-wrap-sdk`.
  </Card>
</CardGroup>

## Deployment environments

You can run the same [Agent Server](/langsmith/agent-server) runtime in several hosting models. A **standalone server** is the lightest option: you run containers yourself without the LangSmith [control plane](/langsmith/control-plane). For managed deployments through the UI and APIs, use **Cloud** or **Self-hosted** (full platform in your infrastructure).

<CardGroup cols={2}>
  <Card title="Cloud" cta="View guide" href="/langsmith/deploy-to-cloud" icon="cloud">
    Fully managed by LangChain, running on AWS and GCP. Create deployments from GitHub in the LangSmith UI or with [`langgraph deploy`](/langsmith/cli#deploy). Requires a [Plus plan or above](https://www.langchain.com/pricing).
  </Card>

  <Card title="Standalone server" cta="View guide" href="/langsmith/deploy-standalone-server" icon="server">
    Deploy Agent Server with Docker, Compose, or Kubernetes. Bring your own PostgreSQL, Redis, and LangSmith license; no control plane. Optional [LangSmith tracing](/langsmith/observability) to Cloud or a self-hosted instance.
  </Card>

  <Card title="Self-hosted" cta="View guide" href="/langsmith/self-hosted" icon="buildings">
    Run the full LangSmith platform, including the control plane and data plane, in your cloud (for example on Kubernetes). Requires [Enterprise plan](https://www.langchain.com/pricing). Integrates observability, evaluation, and agent deployment in one private stack.
  </Card>

  <Card title="Frameworks and platforms" cta="View guides" href="/langsmith/deploy-frameworks-and-platforms" icon="code">
    Deploy an Agent Server to LangSmith, Next.js, SvelteKit, Nuxt, Cloudflare Workers, Deno Deploy, and more. Full-stack examples with streaming UI and thread history.

    <div className="not-prose mt-4 grid grid-cols-6 items-center justify-items-center gap-2 border-t border-gray-200 pt-4 dark:border-gray-700">
      <span className="inline-flex h-8 w-8 items-center justify-center">
        <img className="h-5 w-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/langchain.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=b910ed9cd0b6b8adb4b6da400882e92c" alt="LangSmith" width="65" height="65" data-path="images/providers/light/langchain.svg" />
      </span>

      <span className="inline-flex h-8 w-8 items-center justify-center">
        <img className="h-5 w-5" src="https://mintcdn.com/langchain-5e9cc07a/h9vvRKKSgCSjvd_Y/images/providers/light/nextjs.svg?fit=max&auto=format&n=h9vvRKKSgCSjvd_Y&q=85&s=4f3336e9534db50f25f87173a41322d5" alt="Next.js" width="24" height="24" data-path="images/providers/light/nextjs.svg" />
      </span>

      <span className="inline-flex h-8 w-8 items-center justify-center">
        <img className="h-5 w-5" src="https://mintcdn.com/langchain-5e9cc07a/h9vvRKKSgCSjvd_Y/images/providers/light/svelte.svg?fit=max&auto=format&n=h9vvRKKSgCSjvd_Y&q=85&s=07e7e35c40e4522f739feea9ef3e33b7" alt="SvelteKit" width="24" height="24" data-path="images/providers/light/svelte.svg" />
      </span>

      <span className="inline-flex h-8 w-8 items-center justify-center">
        <img className="h-5 w-5" src="https://mintcdn.com/langchain-5e9cc07a/h9vvRKKSgCSjvd_Y/images/providers/light/nuxt.svg?fit=max&auto=format&n=h9vvRKKSgCSjvd_Y&q=85&s=5d965ed1f93f51ac604e66b935a65368" alt="Nuxt" width="24" height="24" data-path="images/providers/light/nuxt.svg" />
      </span>

      <span className="inline-flex h-8 w-8 items-center justify-center">
        <img className="h-5 w-5" src="https://mintcdn.com/langchain-5e9cc07a/h9vvRKKSgCSjvd_Y/images/providers/light/cloudflare.svg?fit=max&auto=format&n=h9vvRKKSgCSjvd_Y&q=85&s=ae129fcbfc78ccaece42b1c4d3699311" alt="Cloudflare Workers" width="24" height="24" data-path="images/providers/light/cloudflare.svg" />
      </span>

      <span className="inline-flex h-8 w-8 items-center justify-center">
        <img className="h-5 w-5" src="https://mintcdn.com/langchain-5e9cc07a/Tz8fh3A43FeUPf69/images/providers/light/deno.svg?fit=max&auto=format&n=Tz8fh3A43FeUPf69&q=85&s=8d213b0000104542fcaa7ab160595224" alt="Deno Deploy" width="24" height="24" data-path="images/providers/light/deno.svg" />
      </span>
    </div>
  </Card>
</CardGroup>

Same runtime, same APIs. What changes is who manages the infrastructure.
For a feature-level comparison and infrastructure setup, see [Platform setup](/langsmith/platform-setup).

## Build on the Agent Server runtime

Once deployed, agents work with [Agent Server](/langsmith/assistants)'s execution model: **assistants** for configuration, **threads** for state, and **runs** for workloads. For capabilities, tutorials, server customization, and operations, see [Develop agents](/langsmith/develop-agents-overview).

<Card title="Find and fix failures with Engine" icon="https://mintcdn.com/langchain-5e9cc07a/oHF6ZolKSFmH17u5/images/brand/engine-icon-dark.png?fit=max&auto=format&n=oHF6ZolKSFmH17u5&q=85&s=739a487161804691a14c36c2768d278d" href="/langsmith/engine-overview" arrow="true" width="196" height="196" data-path="images/brand/engine-icon-dark.png">
  Once agents are in production, use LangSmith Engine to detect recurring failures in their traces, diagnose root causes, and resolve them.
</Card>

***

<div className="source-links">
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deployment.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
