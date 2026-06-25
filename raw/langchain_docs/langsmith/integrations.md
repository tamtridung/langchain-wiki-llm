---
title: Integrations
source: https://docs.langchain.com/langsmith/integrations.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrations

[LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-integrations) provides integrations for a growing set of popular [LLM providers](#llm-providers) and [agent frameworks](#agent-frameworks) as well as [Deep Agents](/oss/python/deepagents/overview), [LangChain](/oss/python/langchain/overview), and [LangGraph](/oss/python/langgraph/overview). For setup and usage, refer to the guides listed on this page.

## LLM providers

<div className="grid grid-cols-1 md:grid-cols-3 gap-3">
  <a href="/langsmith/trace-bedrock" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/bedrock.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=d6fc326f6c429075add5a742c87d12b1" alt="" width="65" height="65" data-path="images/providers/light/bedrock.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/bedrock.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=dc593829dc9ff5ad061f991e08bbebc8" alt="" width="65" height="65" data-path="images/providers/dark/bedrock.svg" />

    <span className="font-semibold">Amazon Bedrock</span>
  </a>

  <a href="/langsmith/trace-anthropic" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/anthropic.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=f681e2a9025c2e1104d4260c6b27d638" alt="" width="65" height="65" data-path="images/providers/light/anthropic.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/anthropic.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=02fc4a5cd4c124dbec46869777a15f34" alt="" width="65" height="65" data-path="images/providers/dark/anthropic.svg" />

    <span className="font-semibold">Anthropic</span>
  </a>

  <a href="/langsmith/trace-deepseek" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/deepseek.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=5a11e956e2ba24fd746aebd929ee1a5e" alt="" width="65" height="65" data-path="images/providers/light/deepseek.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/deepseek.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=0cb62f13b3b37e89c35060913ca67515" alt="" width="65" height="65" data-path="images/providers/dark/deepseek.svg" />

    <span className="font-semibold">DeepSeek</span>
  </a>

  <a href="/langsmith/trace-with-google-gemini" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/gemini.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=486f57c43a26c9661700c37d0f575c05" alt="" width="65" height="65" data-path="images/providers/light/gemini.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/gemini.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=6436cb2ebecd9119e486f81fb2fdd360" alt="" width="65" height="65" data-path="images/providers/dark/gemini.svg" />

    <span className="font-semibold">Google Gemini</span>
  </a>

  <a href="/langsmith/trace-litellm" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/TiT87b4RAoWyIOkQ/images/providers/light/litellm.svg?fit=max&auto=format&n=TiT87b4RAoWyIOkQ&q=85&s=3c70d2b1a246ead959c54869ecf39a74" alt="" width="24" height="24" data-path="images/providers/light/litellm.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/bCVgrm_X3ggdZ1m0/images/providers/dark/litellm.svg?fit=max&auto=format&n=bCVgrm_X3ggdZ1m0&q=85&s=bf0caf761551eb218517adc898493c9e" alt="" width="24" height="24" data-path="images/providers/dark/litellm.svg" />

    <span className="font-semibold">LiteLLM</span>
  </a>

  <a href="/langsmith/trace-with-mistral" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/mistral.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=2b060bfbf269ab1b7f41f3a835f7a0b6" alt="" width="65" height="65" data-path="images/providers/light/mistral.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/mistral.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=59bde8ab2250b2ba2deaa84b74a66e1b" alt="" width="65" height="65" data-path="images/providers/dark/mistral.svg" />

    <span className="font-semibold">Mistral</span>
  </a>

  <a href="/langsmith/trace-openai" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=fb29ba01edf0644930f3eda68ab6c0c2" alt="" width="65" height="67" data-path="images/providers/light/openai.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=ad31e0e26cb456a8fa3cddea3bac876e" alt="" width="65" height="67" data-path="images/providers/dark/openai.svg" />

    <span className="font-semibold">OpenAI</span>
  </a>

  <a href="/langsmith/trace-with-openai-compatible" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=fb29ba01edf0644930f3eda68ab6c0c2" alt="" width="65" height="67" data-path="images/providers/light/openai.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=ad31e0e26cb456a8fa3cddea3bac876e" alt="" width="65" height="67" data-path="images/providers/dark/openai.svg" />

    <span className="font-semibold">OpenAI-compatible APIs</span>
  </a>
</div>

<Callout icon="arrows-transfer-down" color="#4F46E5" iconType="regular">
  **Using LangChain?** LangChain provides a unified interface to 100+ LLM providers, which allows you to switch between models by setting environment variables. [Initialize a model](/oss/python/langchain/models#initialize-a-model) and LangSmith will automatically trace your application.
</Callout>

## Agent frameworks

<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
  <a href="/langsmith/trace-with-autogen" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/autogen.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=4000da450d02b72ba1115c3dcdc2fde4" alt="" width="65" height="65" data-path="images/providers/light/autogen.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/autogen.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=74a63bfa8fc60eb3fb25b2c4f4f820b4" alt="" width="65" height="65" data-path="images/providers/dark/autogen.svg" />

    <span className="font-semibold">AutoGen</span>
  </a>

  <a href="/langsmith/trace-claude-agent-sdk" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/claude.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=d3cae2da0f353a45594f57b7f2382aba" alt="" width="65" height="65" data-path="images/providers/light/claude.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/claude.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=44d1be6c97663a8cd1d4408083011bd9" alt="" width="65" height="65" data-path="images/providers/dark/claude.svg" />

    <span className="font-semibold">Claude Agent SDK</span>
  </a>

  <a href="/langsmith/trace-with-crewai" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/crewai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=5f262e7fa86dc071770356a652ddee8f" alt="" width="65" height="65" data-path="images/providers/light/crewai.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/crewai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=dc6b523c974b2c63e0b21c70c29ed4b6" alt="" width="65" height="65" data-path="images/providers/dark/crewai.svg" />

    <span className="font-semibold">CrewAI</span>
  </a>

  <a href="/langsmith/trace-deep-agents" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/8njVp3mXF3LrAS1d/images/brand/docs-favicon.png?fit=max&auto=format&n=8njVp3mXF3LrAS1d&q=85&s=a61c2b4666f558992e1fd44750b08465" alt="" width="650" height="650" data-path="images/brand/docs-favicon.png" />

    <span className="font-semibold">Deep Agents</span>
  </a>

  <a href="/langsmith/trace-with-google-adk" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/googleadk.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=b89f56d14d3d07aed99317fe34b20828" alt="" width="65" height="65" data-path="images/providers/light/googleadk.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/googleadk.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=2b3b327124dd6113be499c6e0c927cda" alt="" width="65" height="65" data-path="images/providers/dark/googleadk.svg" />

    <span className="font-semibold">Google ADK</span>
  </a>

  <a href="/langsmith/trace-with-langchain" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/8njVp3mXF3LrAS1d/images/brand/docs-favicon.png?fit=max&auto=format&n=8njVp3mXF3LrAS1d&q=85&s=a61c2b4666f558992e1fd44750b08465" alt="" width="650" height="650" data-path="images/brand/docs-favicon.png" />

    <span className="font-semibold">LangChain</span>
  </a>

  <a href="/langsmith/trace-with-langgraph" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/8njVp3mXF3LrAS1d/images/brand/docs-favicon.png?fit=max&auto=format&n=8njVp3mXF3LrAS1d&q=85&s=a61c2b4666f558992e1fd44750b08465" alt="" width="650" height="650" data-path="images/brand/docs-favicon.png" />

    <span className="font-semibold">LangGraph</span>
  </a>

  <a href="/langsmith/trace-with-mastra" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/mastra.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=4a14d6600d2b99a511b09271f9a5b57e" alt="" width="65" height="65" data-path="images/providers/light/mastra.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/mastra.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=afe3e7535919bd2332229f31d119a6a4" alt="" width="65" height="65" data-path="images/providers/dark/mastra.svg" />

    <span className="font-semibold">Mastra</span>
  </a>

  <a href="/langsmith/trace-with-microsoft-agent-framework" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/microsoft.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=9189910834f230f7f94115d88e7ec4bf" alt="" width="65" height="65" data-path="images/providers/light/microsoft.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/microsoft.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=36998a752a161152e010bc2c9b421567" alt="" width="65" height="65" data-path="images/providers/dark/microsoft.svg" />

    <span className="font-semibold">Microsoft Agent Framework</span>
  </a>

  <a href="/langsmith/trace-with-openai-agents-sdk" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=fb29ba01edf0644930f3eda68ab6c0c2" alt="" width="65" height="67" data-path="images/providers/light/openai.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=ad31e0e26cb456a8fa3cddea3bac876e" alt="" width="65" height="67" data-path="images/providers/dark/openai.svg" />

    <span className="font-semibold">OpenAI Agents</span>
  </a>

  <a href="/langsmith/trace-with-opentelemetry" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/opentelemetry.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=84b763868676d132f14cc4055525c34d" alt="" width="65" height="65" data-path="images/providers/light/opentelemetry.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/opentelemetry.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=3eaddab2003804357fcad1a7a8d09f35" alt="" width="65" height="65" data-path="images/providers/dark/opentelemetry.svg" />

    <span className="font-semibold">OpenTelemetry</span>
  </a>

  <a href="/langsmith/trace-with-pydantic-ai" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/z7oQGiHwXv52HwOy/images/providers/light/pydanticai.svg?fit=max&auto=format&n=z7oQGiHwXv52HwOy&q=85&s=0c399e2c9d65c77eeb5644d3d7f2dca5" alt="" width="65" height="65" data-path="images/providers/light/pydanticai.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/pydanticai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=808e787a6f78fc14508f9c6336ac9a6a" alt="" width="65" height="65" data-path="images/providers/dark/pydanticai.svg" />

    <span className="font-semibold">PydanticAI</span>
  </a>

  <a href="/langsmith/trace-with-semantic-kernel" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/microsoft.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=9189910834f230f7f94115d88e7ec4bf" alt="" width="65" height="65" data-path="images/providers/light/microsoft.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/microsoft.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=36998a752a161152e010bc2c9b421567" alt="" width="65" height="65" data-path="images/providers/dark/microsoft.svg" />

    <span className="font-semibold">Semantic Kernel</span>
  </a>

  <a href="/langsmith/trace-with-strands-agents" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/bedrock.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=d6fc326f6c429075add5a742c87d12b1" alt="" width="65" height="65" data-path="images/providers/light/bedrock.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/bedrock.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=dc593829dc9ff5ad061f991e08bbebc8" alt="" width="65" height="65" data-path="images/providers/dark/bedrock.svg" />

    <span className="font-semibold">Strands Agents</span>
  </a>

  <a href="/langsmith/trace-with-vercel-ai-sdk" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/z7oQGiHwXv52HwOy/images/providers/light/vercel.svg?fit=max&auto=format&n=z7oQGiHwXv52HwOy&q=85&s=76a0a441ec1730cb68635a19a2a29032" alt="" width="65" height="65" data-path="images/providers/light/vercel.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/vercel.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=7fa15293664e1da6c5fa1319ae0182ec" alt="" width="65" height="65" data-path="images/providers/dark/vercel.svg" />

    <span className="font-semibold">Vercel AI SDK</span>
  </a>
</div>

## Voice AI frameworks

<div className="grid grid-cols-1 md:grid-cols-2 gap-3">
  <a href="/langsmith/trace-openai-realtime" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=fb29ba01edf0644930f3eda68ab6c0c2" alt="" width="65" height="67" data-path="images/providers/light/openai.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=ad31e0e26cb456a8fa3cddea3bac876e" alt="" width="65" height="67" data-path="images/providers/dark/openai.svg" />

    <span className="font-semibold">OpenAI Realtime</span>
  </a>

  <a href="/langsmith/trace-gemini-live" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/gemini.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=486f57c43a26c9661700c37d0f575c05" alt="" width="65" height="65" data-path="images/providers/light/gemini.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/gemini.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=6436cb2ebecd9119e486f81fb2fdd360" alt="" width="65" height="65" data-path="images/providers/dark/gemini.svg" />

    <span className="font-semibold">Gemini Live</span>
  </a>

  <a href="/langsmith/trace-with-livekit" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/livekit.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=e8c6fd5de3893374c7b2b57c68f97de8" alt="" width="65" height="65" data-path="images/providers/light/livekit.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/livekit.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=b98d4d6fbaf0100df180f3e3ee54ca4e" alt="" width="65" height="65" data-path="images/providers/dark/livekit.svg" />

    <span className="font-semibold">Livekit</span>
  </a>

  <a href="/langsmith/trace-with-pipecat" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/pipecat.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=91517611a27adb6cde1a46a81c76233d" alt="" width="65" height="65" data-path="images/providers/light/pipecat.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/pipecat.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=9fde2f2d7a0acaadd3977e693efb5f45" alt="" width="65" height="65" data-path="images/providers/dark/pipecat.svg" />

    <span className="font-semibold">Pipecat</span>
  </a>
</div>

## Developer tools

<div className="grid grid-cols-1 md:grid-cols-3 gap-3">
  <a href="/langsmith/trace-claude-code" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/claude.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=d3cae2da0f353a45594f57b7f2382aba" alt="" width="65" height="65" data-path="images/providers/light/claude.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/claude.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=44d1be6c97663a8cd1d4408083011bd9" alt="" width="65" height="65" data-path="images/providers/dark/claude.svg" />

    <span className="font-semibold">Claude Code</span>
  </a>

  <a href="/langsmith/trace-with-codex" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=fb29ba01edf0644930f3eda68ab6c0c2" alt="" width="65" height="67" data-path="images/providers/light/openai.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/openai.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=ad31e0e26cb456a8fa3cddea3bac876e" alt="" width="65" height="67" data-path="images/providers/dark/openai.svg" />

    <span className="font-semibold">OpenAI Codex</span>
  </a>

  <a href="/langsmith/trace-with-opencode" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/oO5HjFJbtRKTB5uq/images/providers/light/opencode.svg?fit=max&auto=format&n=oO5HjFJbtRKTB5uq&q=85&s=25a9d6bd2ec68f699ff7d461b2922dad" alt="" width="300" height="300" data-path="images/providers/light/opencode.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/h08KbTOE2npCZz51/images/providers/dark/opencode.svg?fit=max&auto=format&n=h08KbTOE2npCZz51&q=85&s=10a4c9f2cbe6791ff5db75dd47468483" alt="" width="300" height="300" data-path="images/providers/dark/opencode.svg" />

    <span className="font-semibold">OpenCode</span>
  </a>

  <a href="/langsmith/trace-with-instructor" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/light/instructor.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=d9e2a38d8afcb3f166057e835d4717a7" alt="" width="65" height="65" data-path="images/providers/light/instructor.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/instructor.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=66789d39507bfb7f5643bd8528814fd0" alt="" width="65" height="65" data-path="images/providers/dark/instructor.svg" />

    <span className="font-semibold">Instructor</span>
  </a>

  <a href="/langsmith/trace-with-n8n" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/r98TU0ib_rpHFZca/images/providers/light/n8n.svg?fit=max&auto=format&n=r98TU0ib_rpHFZca&q=85&s=4fa6a6e73885330613947815c52d1499" alt="" width="24" height="24" data-path="images/providers/light/n8n.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/r98TU0ib_rpHFZca/images/providers/dark/n8n.svg?fit=max&auto=format&n=r98TU0ib_rpHFZca&q=85&s=be61c5d6a46d7e493363fdc98e309374" alt="" width="24" height="24" data-path="images/providers/dark/n8n.svg" />

    <span className="font-semibold">n8n</span>
  </a>

  <a href="/langsmith/trace-with-pi" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/4TrOZZ3BK2K-YJOg/images/providers/light/pi.svg?fit=max&auto=format&n=4TrOZZ3BK2K-YJOg&q=85&s=a7b450733e32c31c1052067940c4ad48" alt="" width="65" height="65" data-path="images/providers/light/pi.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/8wWwqzGtryixR6uX/images/providers/dark/pi.svg?fit=max&auto=format&n=8wWwqzGtryixR6uX&q=85&s=4aa58d2d70e82fa82018e3110c56dbad" alt="" width="65" height="65" data-path="images/providers/dark/pi.svg" />

    <span className="font-semibold">Pi</span>
  </a>

  <a href="/langsmith/trace-with-temporal" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/z7oQGiHwXv52HwOy/images/providers/light/temporal.svg?fit=max&auto=format&n=z7oQGiHwXv52HwOy&q=85&s=3c34b851e1be36297688e71ece797843" alt="" width="65" height="65" data-path="images/providers/light/temporal.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/ZPKed1feKJ8F6LVo/images/providers/dark/temporal.svg?fit=max&auto=format&n=ZPKed1feKJ8F6LVo&q=85&s=a7bffaafd90d667487c6e9f8822fb08d" alt="" width="65" height="65" data-path="images/providers/dark/temporal.svg" />

    <span className="font-semibold">Temporal</span>
  </a>

  <a href="/langsmith/trace-with-vscode-copilot" className="flex items-center justify-center gap-1.5 p-2 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600 no-underline ">
    <img className="block dark:hidden w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/VoDejLXW9qn9e7mU/images/providers/light/vscode.svg?fit=max&auto=format&n=VoDejLXW9qn9e7mU&q=85&s=15987426cb92b1921d8d41f902df02ac" alt="" width="24" height="24" data-path="images/providers/light/vscode.svg" />

    <img className="hidden dark:block w-5 h-5" src="https://mintcdn.com/langchain-5e9cc07a/dfo4A1rdxUTEZYH_/images/providers/dark/vscode.svg?fit=max&auto=format&n=dfo4A1rdxUTEZYH_&q=85&s=5b71dcc502cbb7b56fd8e4dfda561021" alt="" width="24" height="24" data-path="images/providers/dark/vscode.svg" />

    <span className="font-semibold">VS Code Copilot</span>
  </a>
</div>

***

<div className="source-links">
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/integrations.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
