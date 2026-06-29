"""
Deep Agents — Python list of all links from the overview page
Source: https://docs.langchain.com/oss/python/deepagents/overview
Crawled: 2026-06-29
"""

from dataclasses import dataclass

# ──────────────────────────────────────────────
# 1. Simple list of URL strings
# ──────────────────────────────────────────────

DEEP_AGENTS_URLS = [
    # === Get Started ===
    "https://docs.langchain.com/oss/python/deepagents/overview",
    "https://docs.langchain.com/oss/python/deepagents/quickstart",
    "https://docs.langchain.com/oss/python/deepagents/customization",
    "https://docs.langchain.com/oss/python/deepagents/comparison",
    # === Deployment ===
    "https://docs.langchain.com/langsmith/managed-deep-agents-overview",
    "https://docs.langchain.com/oss/python/deepagents/going-to-production",
    # === Core Capabilities ===
    "https://docs.langchain.com/oss/python/deepagents/models",
    "https://docs.langchain.com/oss/python/deepagents/tools",
    "https://docs.langchain.com/oss/python/deepagents/context-engineering",
    "https://docs.langchain.com/oss/python/deepagents/multimodal",
    "https://docs.langchain.com/oss/python/deepagents/backends",
    "https://docs.langchain.com/oss/python/deepagents/subagents",
    "https://docs.langchain.com/oss/python/deepagents/async-subagents",
    "https://docs.langchain.com/oss/python/deepagents/human-in-the-loop",
    "https://docs.langchain.com/oss/python/deepagents/permissions",
    "https://docs.langchain.com/oss/python/deepagents/memory",
    "https://docs.langchain.com/oss/python/deepagents/skills",
    "https://docs.langchain.com/oss/python/deepagents/sandboxes",
    "https://docs.langchain.com/oss/python/deepagents/interpreters",
    "https://docs.langchain.com/oss/python/deepagents/profiles",
    "https://docs.langchain.com/oss/python/deepagents/event-streaming",
    "https://docs.langchain.com/oss/python/deepagents/streaming",
    "https://docs.langchain.com/oss/python/deepagents/rubric",
    # === Frontend ===
    "https://docs.langchain.com/oss/python/deepagents/frontend/overview",
    # === Protocols ===
    "https://docs.langchain.com/oss/python/deepagents/acp",
    # === Deep Agents Code ===
    "https://docs.langchain.com/oss/python/deepagents/code/overview",
    "https://docs.langchain.com/oss/python/deepagents/code/memory-and-skills",
    "https://docs.langchain.com/oss/python/deepagents/code/remote-sandboxes",
    "https://docs.langchain.com/oss/python/deepagents/code/subagents",
    "https://docs.langchain.com/oss/python/deepagents/code/providers",
    "https://docs.langchain.com/oss/python/deepagents/code/configuration",
    "https://docs.langchain.com/oss/python/deepagents/code/mcp-tools",
    "https://docs.langchain.com/oss/python/deepagents/code/data-locations",
]

# ──────────────────────────────────────────────
# 2. List of (category, name, url) tuples
# ──────────────────────────────────────────────

DEEP_AGENTS_LINKS = [
    # === Get Started ===
    ("get-started", "Overview",                          "https://docs.langchain.com/oss/python/deepagents/overview"),
    ("get-started", "Quickstart",                        "https://docs.langchain.com/oss/python/deepagents/quickstart"),
    ("get-started", "Customization",                     "https://docs.langchain.com/oss/python/deepagents/customization"),
    ("get-started", "Comparison with Claude Agent SDK",  "https://docs.langchain.com/oss/python/deepagents/comparison"),
    # === Deployment ===
    ("deployment", "Managed Deep Agents",                "https://docs.langchain.com/langsmith/managed-deep-agents-overview"),
    ("deployment", "Going to production",                "https://docs.langchain.com/oss/python/deepagents/going-to-production"),
    # === Core Capabilities ===
    ("core", "Models",                                   "https://docs.langchain.com/oss/python/deepagents/models"),
    ("core", "Tools",                                    "https://docs.langchain.com/oss/python/deepagents/tools"),
    ("core", "Context engineering",                      "https://docs.langchain.com/oss/python/deepagents/context-engineering"),
    ("core", "Multimodality",                             "https://docs.langchain.com/oss/python/deepagents/multimodal"),
    ("core", "Backends",                                 "https://docs.langchain.com/oss/python/deepagents/backends"),
    ("core", "Subagents",                                "https://docs.langchain.com/oss/python/deepagents/subagents"),
    ("core", "Async subagents",                          "https://docs.langchain.com/oss/python/deepagents/async-subagents"),
    ("core", "Human-in-the-loop",                        "https://docs.langchain.com/oss/python/deepagents/human-in-the-loop"),
    ("core", "Permissions",                              "https://docs.langchain.com/oss/python/deepagents/permissions"),
    ("core", "Memory",                                   "https://docs.langchain.com/oss/python/deepagents/memory"),
    ("core", "Skills",                                   "https://docs.langchain.com/oss/python/deepagents/skills"),
    ("core", "Sandboxes",                                "https://docs.langchain.com/oss/python/deepagents/sandboxes"),
    ("core", "Interpreters (Beta)",                      "https://docs.langchain.com/oss/python/deepagents/interpreters"),
    ("core", "Profiles (Beta)",                          "https://docs.langchain.com/oss/python/deepagents/profiles"),
    ("core", "Event streaming (Beta)",                   "https://docs.langchain.com/oss/python/deepagents/event-streaming"),
    ("core", "Streaming",                                "https://docs.langchain.com/oss/python/deepagents/streaming"),
    ("core", "Grading rubrics (Beta)",                   "https://docs.langchain.com/oss/python/deepagents/rubric"),
    # === Frontend ===
    ("frontend", "Frontend Overview",                    "https://docs.langchain.com/oss/python/deepagents/frontend/overview"),
    # === Protocols ===
    ("protocols", "Agent Client Protocol (ACP)",         "https://docs.langchain.com/oss/python/deepagents/acp"),
    ("protocols", "MCP with LangChain",                  "https://docs.langchain.com/oss/python/langchain/mcp"),
    ("protocols", "A2A with LangSmith",                  "https://docs.langchain.com/langsmith/server-a2a"),
    # === Deep Agents Code ===
    ("dcode", "Code Overview",                           "https://docs.langchain.com/oss/python/deepagents/code/overview"),
    ("dcode", "Memory and skills",                       "https://docs.langchain.com/oss/python/deepagents/code/memory-and-skills"),
    ("dcode", "Remote sandboxes",                        "https://docs.langchain.com/oss/python/deepagents/code/remote-sandboxes"),
    ("dcode", "Subagents",                               "https://docs.langchain.com/oss/python/deepagents/code/subagents"),
    ("dcode", "Model providers",                         "https://docs.langchain.com/oss/python/deepagents/code/providers"),
    ("dcode", "Configuration",                           "https://docs.langchain.com/oss/python/deepagents/code/configuration"),
    ("dcode", "MCP tools",                               "https://docs.langchain.com/oss/python/deepagents/code/mcp-tools"),
    ("dcode", "App data",                                "https://docs.langchain.com/oss/python/deepagents/code/data-locations"),
]

# ──────────────────────────────────────────────
# 3. Dataclass-based list
# ──────────────────────────────────────────────

@dataclass
class DeepAgentLink:
    """A single Deep Agents documentation link."""
    name: str
    url: str
    category: str

DEEP_AGENTS_DATACLASS = [
    DeepAgentLink("Overview",                          "https://docs.langchain.com/oss/python/deepagents/overview",                          "get-started"),
    DeepAgentLink("Quickstart",                        "https://docs.langchain.com/oss/python/deepagents/quickstart",                        "get-started"),
    DeepAgentLink("Customization",                     "https://docs.langchain.com/oss/python/deepagents/customization",                     "get-started"),
    DeepAgentLink("Comparison with Claude Agent SDK",  "https://docs.langchain.com/oss/python/deepagents/comparison",                        "get-started"),
    DeepAgentLink("Managed Deep Agents",               "https://docs.langchain.com/langsmith/managed-deep-agents-overview",                   "deployment"),
    DeepAgentLink("Going to production",               "https://docs.langchain.com/oss/python/deepagents/going-to-production",                "deployment"),
    DeepAgentLink("Models",                            "https://docs.langchain.com/oss/python/deepagents/models",                            "core"),
    DeepAgentLink("Tools",                             "https://docs.langchain.com/oss/python/deepagents/tools",                              "core"),
    DeepAgentLink("Context engineering",               "https://docs.langchain.com/oss/python/deepagents/context-engineering",                "core"),
    DeepAgentLink("Multimodality",                      "https://docs.langchain.com/oss/python/deepagents/multimodal",                         "core"),
    DeepAgentLink("Backends",                          "https://docs.langchain.com/oss/python/deepagents/backends",                            "core"),
    DeepAgentLink("Subagents",                         "https://docs.langchain.com/oss/python/deepagents/subagents",                          "core"),
    DeepAgentLink("Async subagents",                   "https://docs.langchain.com/oss/python/deepagents/async-subagents",                    "core"),
    DeepAgentLink("Human-in-the-loop",                 "https://docs.langchain.com/oss/python/deepagents/human-in-the-loop",                  "core"),
    DeepAgentLink("Permissions",                       "https://docs.langchain.com/oss/python/deepagents/permissions",                        "core"),
    DeepAgentLink("Memory",                            "https://docs.langchain.com/oss/python/deepagents/memory",                              "core"),
    DeepAgentLink("Skills",                            "https://docs.langchain.com/oss/python/deepagents/skills",                              "core"),
    DeepAgentLink("Sandboxes",                         "https://docs.langchain.com/oss/python/deepagents/sandboxes",                           "core"),
    DeepAgentLink("Interpreters (Beta)",                "https://docs.langchain.com/oss/python/deepagents/interpreters",                       "core"),
    DeepAgentLink("Profiles (Beta)",                    "https://docs.langchain.com/oss/python/deepagents/profiles",                           "core"),
    DeepAgentLink("Event streaming (Beta)",             "https://docs.langchain.com/oss/python/deepagents/event-streaming",                    "core"),
    DeepAgentLink("Streaming",                         "https://docs.langchain.com/oss/python/deepagents/streaming",                          "core"),
    DeepAgentLink("Grading rubrics (Beta)",             "https://docs.langchain.com/oss/python/deepagents/rubric",                             "core"),
    DeepAgentLink("Frontend Overview",                 "https://docs.langchain.com/oss/python/deepagents/frontend/overview",                  "frontend"),
    DeepAgentLink("Agent Client Protocol (ACP)",        "https://docs.langchain.com/oss/python/deepagents/acp",                               "protocols"),
    DeepAgentLink("MCP with LangChain",                 "https://docs.langchain.com/oss/python/langchain/mcp",                                 "protocols"),
    DeepAgentLink("A2A with LangSmith",                 "https://docs.langchain.com/langsmith/server-a2a",                                     "protocols"),
    DeepAgentLink("Code Overview",                     "https://docs.langchain.com/oss/python/deepagents/code/overview",                      "dcode"),
    DeepAgentLink("Memory and skills",                 "https://docs.langchain.com/oss/python/deepagents/code/memory-and-skills",             "dcode"),
    DeepAgentLink("Remote sandboxes",                  "https://docs.langchain.com/oss/python/deepagents/code/remote-sandboxes",              "dcode"),
    DeepAgentLink("Code Subagents",                    "https://docs.langchain.com/oss/python/deepagents/code/subagents",                     "dcode"),
    DeepAgentLink("Model providers",                   "https://docs.langchain.com/oss/python/deepagents/code/providers",                     "dcode"),
    DeepAgentLink("Configuration",                     "https://docs.langchain.com/oss/python/deepagents/code/configuration",                 "dcode"),
    DeepAgentLink("MCP tools",                         "https://docs.langchain.com/oss/python/deepagents/code/mcp-tools",                    "dcode"),
    DeepAgentLink("App data",                          "https://docs.langchain.com/oss/python/deepagents/code/data-locations",                "dcode"),
]

# ──────────────────────────────────────────────
# 4. Additional links from page content
# ──────────────────────────────────────────────

ADDITIONAL_LINKS = [
    ("llms.txt",                      "https://docs.langchain.com/llms.txt"),
    ("LangSmith signup",              "https://smith.langchain.com"),
    ("Observability quickstart",      "https://docs.langchain.com/langsmith/observability-quickstart"),
    ("deepagents (PyPI)",             "https://pypi.org/project/deepagents/"),
    ("LangChain",                     "https://docs.langchain.com/oss/python/langchain"),
    ("LangGraph",                     "https://docs.langchain.com/oss/python/langgraph"),
    ("Frameworks, runtimes, harnesses", "https://docs.langchain.com/oss/python/concepts/products"),
    ("Agent harness anchor",          "https://docs.langchain.com/oss/python/concepts/products#agent-harnesses-like-the-deep-agents-sdk"),
    ("create_agent",                  "https://docs.langchain.com/oss/python/langchain/agents"),
    ("LangGraph workflow",            "https://docs.langchain.com/oss/python/langgraph/overview"),
    ("MCP with LangChain",            "https://docs.langchain.com/oss/python/langchain/mcp"),
    ("API Reference",                 "https://reference.langchain.com/python/deepagents/"),
    # External
    ("GitHub (LangChain)",            "https://github.com/langchain-ai"),
    ("LangSmith Chat",                "https://chat.langchain.com/"),
    ("Agent Skills standard",         "https://agentskills.io/"),
    ("AGENTS.md spec",                "https://agents.md/"),
    ("Edit this page on GitHub",      "https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/overview.mdx"),
    ("File an issue",                 "https://github.com/langchain-ai/docs/issues/new/choose"),
    ("Deep Agents examples (GitHub)", "https://github.com/langchain-ai/deepagents/tree/main/examples"),
]

# ──────────────────────────────────────────────
# 5. Helper: group by category
# ──────────────────────────────────────────────

def group_by_category(links: list[tuple[str, str, str]]) -> dict[str, list[tuple[str, str]]]:
    """Group (category, name, url) tuples by category."""
    result: dict[str, list[tuple[str, str]]] = {}
    for cat, name, url in links:
        result.setdefault(cat, []).append((name, url))
    return result

if __name__ == "__main__":
    print(f"Total deep agents URLs: {len(DEEP_AGENTS_URLS)}")
    print(f"Total categorized links: {len(DEEP_AGENTS_LINKS)}")
    print(f"Total additional links: {len(ADDITIONAL_LINKS)}")
    print()
    print("=== By category ===")
    for cat, items in group_by_category(DEEP_AGENTS_LINKS).items():
        print(f"\n[{cat}]:")
        for name, url in items:
            print(f"  {name}: {url}")
