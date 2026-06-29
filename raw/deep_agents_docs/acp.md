[Protocols](https://docs.langchain.com/oss/python/deepagents/acp)

Agent Client Protocol (ACP)
===========================

Copy page

Expose Deep Agents over the Agent Client Protocol (ACP) to integrate with code editors and IDEs.

Copy page

[Agent Client Protocol (ACP)](https://agentclientprotocol.com/get-started/introduction) standardizes communication between coding agents and code editors or IDEs.
With the ACP protocol, you can make use of your custom deep agents with any ACP-compatible client, allowing your code editor to provide project context and receive rich updates.

ACP is designed for agent-editor integrations. If you want your agent to call tools hosted by external servers, see [Model Context Protocol (MCP)](https://docs.langchain.com/oss/python/langchain/mcp).

[​](https://docs.langchain.com/oss/python/deepagents/acp#quickstart) Quickstart
-------------------------------------------------------------------------------

Install the ACP integration package:

pip

uv

```
pip install deepagents-acp
```

Then expose a deep agent over ACP.
This starts an ACP server in stdio mode (it reads requests from stdin and writes responses to stdout). In practice, you usually run this as a command launched by an ACP client (for example, your editor), which then communicates with the server over stdio.

```
import asyncio

from acp import run_agent
from deepagents import create_deep_agent
from langgraph.checkpoint.memory import MemorySaver

from deepagents_acp.server import AgentServerACP


async def main() -> None:
    agent = create_deep_agent(
        model="google_genai:gemini-3.5-flash",
        # You can customize your deep agent here: set a custom prompt,
        # add your own tools, attach middleware, or compose subagents.
        system_prompt="You are a helpful coding assistant",
        checkpointer=MemorySaver(),
    )

    server = AgentServerACP(agent)
    await run_agent(server)


if __name__ == "__main__":
    asyncio.run(main())
```

[Example coding agent
--------------------

The `deepagents-acp` package includes an example coding agent with filesystem and shell that you can run out of the box.](https://github.com/langchain-ai/deepagents/blob/main/libs/acp/examples/demo_agent.py)

[​](https://docs.langchain.com/oss/python/deepagents/acp#clients) Clients
-------------------------------------------------------------------------

Deep agents work anywhere you can run an ACP agent server. Some notable ACP clients include:

* [Zed](https://zed.dev/docs/ai/external-agents)
* [JetBrains IDEs](https://www.jetbrains.com/help/ai-assistant/acp.html)
* Visual Studio Code (via [vscode-acp](https://github.com/formulahendry/vscode-acp))
* Neovim (via ACP-compatible plugins)

### [​](https://docs.langchain.com/oss/python/deepagents/acp#zed) Zed

The `deepagents` repo includes [a demo ACP entrypoint](https://github.com/langchain-ai/deepagents/blob/main/libs/acp/run_demo_agent.sh) you can register with [Zed](https://zed.dev/docs/ai/external-agents):

1. Clone the `deepagents` repo and install dependencies:

```
git clone https://github.com/langchain-ai/deepagents.git
cd deepagents/libs/acp
uv sync --all-groups
chmod +x run_demo_agent.sh
```

2. Configure credentials for the demo agent:

```
cp .env.example .env
```

Then set `ANTHROPIC_API_KEY` in `.env`.

3. Configure your ACP agent server command in Zed’s `settings.json`:

```
{
  "agent_servers": {
    "DeepAgents": {
      "type": "custom",
      "command": "/your/absolute/path/to/deepagents/libs/acp/run_demo_agent.sh"
    }
  }
}
```

4. Open Zed’s Agents panel and start a Deep Agents thread.

### [​](https://docs.langchain.com/oss/python/deepagents/acp#toad) Toad

If you want to run an ACP agent server as a local dev tool, you can use [Toad](https://github.com/batrachianai/toad) to manage the process.

```
uv tool install -U batrachian-toad

toad acp "python path/to/your_server.py" .
# or
toad acp "uv run python path/to/your_server.py" .
```

See the upstream ACP docs for protocol details and editor support:

* Introduction: <https://agentclientprotocol.com/get-started/introduction>
* Clients/editors: <https://agentclientprotocol.com/get-started/clients>

---

[Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/acp.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

YesNo

[Sandbox

Previous](https://docs.langchain.com/oss/python/deepagents/frontend/sandbox)[Model Context Protocol

Next](https://docs.langchain.com/oss/python/deepagents/mcp)

Ctrl+I