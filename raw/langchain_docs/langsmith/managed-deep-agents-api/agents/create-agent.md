---
title: Create an agent
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/agents/create-agent.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an agent

> Create an agent with metadata, runtime configuration, and an optional file tree. Creation is atomic: either the agent is fully created or no state is persisted.



## OpenAPI

````yaml /langsmith/managed-deep-agents-openapi.json post /agents
openapi: 3.1.0
info:
  title: Managed Deep Agents API
  version: 0.1.0
  description: Create, configure, and run Managed Deep Agents.
servers:
  - url: https://api.smith.langchain.com/v1/deepagents
security:
  - apiKeyAuth: []
tags:
  - name: Agents
    description: Create and manage Managed Deep Agent resources.
  - name: Threads
    description: Create and inspect durable thread state.
  - name: Runs
    description: Start runs on Managed Deep Agent threads.
  - name: MCP servers
    description: Register MCP servers and store credentials referenced by agent tools.
  - name: MCP tools
    description: Discover tools exposed by registered MCP servers.
  - name: Auth sessions
    description: Start and poll OAuth authorization sessions for OAuth MCP servers.
paths:
  /agents:
    post:
      tags:
        - Agents
      summary: Create an agent
      description: >-
        Create an agent with metadata, runtime configuration, and an optional
        file tree. Creation is atomic: either the agent is fully created or no
        state is persisted.
      operationId: createManagedDeepAgent
      parameters:
        - $ref: '#/components/parameters/IncludeFiles'
        - $ref: '#/components/parameters/UserTimezone'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateAgentRequest'
            examples:
              basic:
                summary: Create a research assistant
                value:
                  name: research-assistant
                  description: >-
                    Research assistant that can search the web and summarize
                    sources.
                  permissions:
                    identity: personal
                    visibility: user
                  runtime:
                    model:
                      model_id: openai:gpt-5.5
                  instructions: >-
                    You are a careful research assistant. Search for sources,
                    keep notes, and return concise answers with citations.
                  tools:
                    tools:
                      - name: tavily_web_search
                        mcp_server_url: https://tools.langchain.com
                        mcp_server_name: Fleet
                        display_name: tavily_web_search
                    interrupt_config:
                      https://tools.langchain.com::tavily_web_search::Fleet: true
      responses:
        '201':
          description: Agent created.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Agent'
              examples:
                basic:
                  summary: Research assistant with one tool
                  value:
                    id: dfa71115-c971-4197-8f02-20826fbc6f40
                    name: research-assistant
                    description: >-
                      Research assistant that can search the web and summarize
                      sources.
                    owner_id: 33499cf9-4c02-49af-909d-b8f42e051eab
                    created_at: '2026-05-15T20:50:32.708302+00:00'
                    updated_at: '2026-05-15T20:50:32.708302+00:00'
                    permissions:
                      identity: personal
                      visibility: user
                      tenant_access_level: read
                    runtime:
                      model:
                        model_id: openai:gpt-5.5
                    revision: >-
                      13ac11f11da376e588cb84825ed88d05298f27aaaa90c6f694abf572f34161d9
                    instructions: >-
                      You are a careful research assistant. Search for sources,
                      keep notes, and return concise answers with citations.
                    tools:
                      tools:
                        - name: tavily_web_search
                          mcp_server_url: https://tools.langchain.com
                          mcp_server_name: Fleet
                          display_name: tavily_web_search
                      interrupt_config:
                        https://tools.langchain.com::tavily_web_search::Fleet: true
        '400':
          $ref: '#/components/responses/BadRequest'
        '403':
          $ref: '#/components/responses/Forbidden'
        '409':
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/UnprocessableEntity'
        '500':
          $ref: '#/components/responses/InternalServerError'
        '502':
          $ref: '#/components/responses/BadGateway'
        '503':
          $ref: '#/components/responses/ServiceUnavailable'
components:
  parameters:
    IncludeFiles:
      name: include_files
      in: query
      required: false
      description: >-
        Include the raw file map in the agent response. Accepted truthy values
        are `true` and `1`.
      schema:
        type: boolean
        default: false
    UserTimezone:
      name: X-User-Timezone
      in: header
      required: false
      description: >-
        IANA timezone name (for example, `America/Los_Angeles`) stamped into the
        agent's runtime configuration when the agent is created or updated. The
        runtime uses this timezone to inject a localized current-date line into
        the agent's system prompt, so the agent reasons about dates in the
        user's local time. Optional. Defaults to `UTC` when omitted; invalid
        values fall back to `UTC`.
      schema:
        type: string
        example: America/Los_Angeles
  schemas:
    CreateAgentRequest:
      type: object
      required:
        - name
      properties:
        name:
          type: string
          description: Human-readable agent name. Must not be blank.
        description:
          type: string
          description: Short agent description.
        permissions:
          $ref: '#/components/schemas/AgentPermissions'
        runtime:
          $ref: '#/components/schemas/AgentRuntime'
        instructions:
          type: string
          description: >-
            Deprecated alias for `system_prompt`. Accepted for backwards
            compatibility; `system_prompt` takes precedence when both are set.
        tools:
          $ref: '#/components/schemas/ToolsConfig'
        subagents:
          type: array
          description: >-
            Subagents. Each entry is written to `subagents/<name>/AGENTS.md`
            and, when provided, `subagents/<name>/tools.json`.
          items:
            $ref: '#/components/schemas/SubagentSpec'
        skills:
          type: array
          description: >-
            Inline skills. Each entry is written to `skills/<name>/SKILL.md` and
            supporting files.
          items:
            $ref: '#/components/schemas/SkillSpec'
        extras:
          type: object
          description: Caller-defined key-value metadata attached to the agent.
          additionalProperties: true
        files:
          $ref: '#/components/schemas/FileMap'
        backend:
          $ref: '#/components/schemas/AgentBackend'
        system_prompt:
          type: string
          description: >-
            Agent system prompt. Written to `AGENTS.md`. Preferred over
            deprecated `instructions` when both are provided.
        configurable:
          type: object
          description: >-
            Caller-defined runtime configuration merged into the agent config.
            Typed runtime fields win on key collision.
          additionalProperties: true
    Agent:
      allOf:
        - $ref: '#/components/schemas/AgentSummary'
        - type: object
          properties:
            revision:
              type: string
              description: Revision token for the latest file tree commit.
            instructions:
              type: string
              description: >-
                Deprecated alias echoed alongside `system_prompt` for backwards
                compatibility.
            tools:
              $ref: '#/components/schemas/ToolsConfig'
            subagents:
              type: array
              items:
                $ref: '#/components/schemas/SubagentSpec'
            skills:
              type: array
              items:
                $ref: '#/components/schemas/SkillSpec'
            files:
              $ref: '#/components/schemas/FileMap'
            system_prompt:
              type: string
              description: Agent system prompt parsed from `AGENTS.md`.
    AgentPermissions:
      type: object
      description: >-
        Agent visibility and sharing configuration. When omitted on create,
        defaults to personal identity, tenant visibility, and read tenant
        access.
      properties:
        identity:
          type: string
          enum:
            - personal
            - shared
          default: personal
          description: Agent identity scope.
        visibility:
          type: string
          enum:
            - tenant
            - user
          default: tenant
          description: Visibility scope for the agent.
        tenant_access_level:
          type: string
          enum:
            - read
            - run
            - write
          default: read
          description: Workspace access level.
        shared_users:
          $ref: '#/components/schemas/SharedUsers'
    AgentRuntime:
      type: object
      properties:
        model:
          $ref: '#/components/schemas/AgentModelConfig'
    ToolsConfig:
      type: object
      properties:
        tools:
          type: array
          description: MCP tools available to the agent. Serialized to `tools.json`.
          items:
            $ref: '#/components/schemas/ToolSpec'
        interrupt_config:
          type: object
          description: >-
            Per-tool interrupt rules. Keys are tool identifiers in the form
            `{mcp_server_url}::{tool_name}` (separator is two colons). The URL
            is normalized with any trailing slash stripped, so
            `https://tools.example.com` and `https://tools.example.com/` match
            the same tool. Additional `::`-separated components after the tool
            name (such as the MCP server display name) are accepted but ignored
            when matching. A bare tool name with no `::` is also accepted as a
            fallback. Values are booleans: `true` requires a human-in-the-loop
            interrupt before the tool runs; `false` allows it without interrupt.
            Use `{}` for no interrupts.
          additionalProperties:
            type: boolean
    SubagentSpec:
      type: object
      properties:
        name:
          type: string
          description: >-
            Subagent slug. Must be non-blank and may contain letters, numbers,
            spaces, underscores, or hyphens.
        description:
          type: string
          description: Short human-readable description.
        model_id:
          type: string
          description: Model ID for this subagent. Inherits the parent runtime when empty.
        instructions:
          type: string
          description: Subagent system prompt. Written to `subagents/<name>/AGENTS.md`.
        tools:
          $ref: '#/components/schemas/ToolsConfig'
    SkillSpec:
      type: object
      properties:
        type:
          type: string
          enum:
            - inline
          default: inline
          description: Skill discriminator. Only `inline` is supported.
        name:
          type: string
          description: >-
            Skill slug. Must be non-blank and may contain letters, numbers,
            spaces, underscores, or hyphens.
        description:
          type: string
          description: Short human-readable description shown to the agent.
        instructions:
          type: string
          description: Skill body. Written to `skills/<name>/SKILL.md`.
        files:
          type: object
          description: >-
            Supporting files keyed by relative path. Paths must be relative with
            no leading slash or `..` segment.
          additionalProperties:
            type: string
    FileMap:
      type: object
      description: >-
        Raw file map for paths not covered by typed fields. Keys are relative
        file paths. Setting a typed field and the corresponding `files` entry
        returns `422`.
      additionalProperties:
        $ref: '#/components/schemas/FileEntry'
    AgentBackend:
      type: object
      properties:
        type:
          type: string
          enum:
            - state
            - sandbox
          description: >-
            Execution backend type. Use `state` for state-only agents or
            `sandbox` for sandbox-backed agents.
          example: state
        sandbox_config:
          $ref: '#/components/schemas/SandboxConfig'
    AgentSummary:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        description:
          type: string
        owner_id:
          type: string
          format: uuid
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        permissions:
          $ref: '#/components/schemas/AgentPermissions'
        runtime:
          $ref: '#/components/schemas/AgentRuntime'
        extras:
          type: object
          additionalProperties: true
        access_level:
          type: string
          enum:
            - READ
            - RUN
            - WRITE
          description: Caller access level for this agent.
        is_owner:
          type: boolean
          description: Whether the authenticated caller owns this agent.
        backend:
          $ref: '#/components/schemas/AgentBackend'
    ErrorResponse:
      type: object
      properties:
        type:
          type: string
        code:
          type: string
        detail:
          type: string
        status:
          type: integer
    SharedUsers:
      type: object
      properties:
        read:
          type: array
          description: User IDs allowed to read the agent.
          items:
            type: string
        run:
          type: array
          description: User IDs allowed to run the agent.
          items:
            type: string
        update:
          type: array
          description: User IDs allowed to update the agent.
          items:
            type: string
    AgentModelConfig:
      type: object
      properties:
        model_id:
          type: string
          description: >-
            Model identifier used to run the agent. Use the form
            `{provider}:{model_name}` — for example, `openai:gpt-5.5` or
            `openai:gpt-5.4-mini`. Values without a colon are interpreted as
            references to a saved Playground configuration, not as direct model
            identifiers. See [Supported
            models](/langsmith/managed-deep-agents-overview#supported-models)
            for the recognized provider prefixes.
          example: openai:gpt-5.5
    ToolSpec:
      type: object
      properties:
        name:
          type: string
          description: Tool name as exposed by the MCP server.
        mcp_server_url:
          type: string
          format: uri
          description: URL of the MCP server hosting this tool.
        mcp_server_name:
          type: string
          description: Display name for the MCP server. Defaults to the URL when empty.
        display_name:
          type: string
          description: Display name for the tool. Defaults to the tool name when empty.
    FileEntry:
      type: object
      properties:
        type:
          type: string
          enum:
            - file
            - skill
          description: Entry discriminator. Defaults to `file` when omitted.
          example: file
        content:
          type: string
          description: >-
            File contents as a UTF-8 string. Must be empty when `type` is
            `skill`.
          example: |-
            # AGENTS.md

            You are a helpful agent.
        repo_handle:
          type: string
          description: Workspace skill repo handle. Required when `type` is `skill`.
          example: summarizer
        commit_id:
          type: string
          description: Optional pin to a specific skill commit. Defaults to latest.
    SandboxConfig:
      type: object
      properties:
        scope:
          type: string
          enum:
            - thread
            - agent
          description: >-
            Sandbox scope. Use `thread` for one sandbox per thread, or `agent`
            for one sandbox shared by the agent.
          example: thread
        snapshot_id:
          type: string
          description: Snapshot used when creating new sandbox-backed computers.
          example: 550e8400-e29b-41d4-a716-446655440000
        policy_ids:
          type: array
          description: Sandbox policies governing tool execution.
          items:
            type: string
        idle_ttl_seconds:
          type: integer
          description: Idle timeout after which an unused sandbox is paused, in seconds.
          example: 600
        delete_after_stop_seconds:
          type: integer
          description: Time after a sandbox is stopped before it is deleted, in seconds.
          example: 1200
  responses:
    BadRequest:
      description: Bad request.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          examples:
            missingRequiredField:
              summary: Required field missing
              value:
                type: https://docs.langchain.com/errors/missing_required_field
                code: missing_required_field
                detail: 'Set ''name'' to a non-empty string: ''name'' is required'
                status: 400
            invalidRequestBody:
              summary: Malformed JSON body
              value:
                type: https://docs.langchain.com/errors/invalid_request_body
                code: invalid_request_body
                detail: >-
                  Provide a valid JSON request body matching the documented
                  schema
                status: 400
    Forbidden:
      description: >-
        The authenticated identity does not have access to the resource or
        feature. The auth layer returns a simple `{"error": "Forbidden"}` body
        that does not match the structured `ErrorResponse` shape used by other
        4xx responses.
      content:
        application/json:
          schema:
            type: object
            properties:
              error:
                type: string
          examples:
            invalidApiKey:
              summary: API key is invalid or lacks workspace access
              value:
                error: Forbidden
    Conflict:
      description: Request conflicts with current resource state.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    UnprocessableEntity:
      description: Request is syntactically valid but failed validation.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalServerError:
      description: Internal server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    BadGateway:
      description: Upstream agent runtime error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          examples:
            upstreamAuthFailed:
              summary: >-
                Upstream runtime rejected the request (e.g. orphaned thread
                after agent deletion)
              value:
                type: https://docs.langchain.com/errors/upstream_auth_failed
                code: upstream_auth_failed
                detail: >-
                  Verify that the calling identity is authorized for this
                  organization: upstream agent runtime rejected the request
                status: 502
    ServiceUnavailable:
      description: Dependent service unavailable.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-Api-Key
      x-default: LANGSMITH_API_KEY

````