---
title: Update an agent
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/agents/update-agent.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an agent

> Update the specified agent. Top-level scalar fields merge field-by-field. Nested objects such as `runtime`, `permissions`, `tools`, `subagents`, `skills`, and `extras` are replaced in full when provided. Providing file-tree fields such as `instructions`, `tools`, `subagents`, `skills`, or `files` creates a new file tree commit.



## OpenAPI

````yaml /langsmith/managed-deep-agents-openapi.json patch /agents/{agent_id}
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
  /agents/{agent_id}:
    patch:
      tags:
        - Agents
      summary: Update an agent
      description: >-
        Update the specified agent. Top-level scalar fields merge
        field-by-field. Nested objects such as `runtime`, `permissions`,
        `tools`, `subagents`, `skills`, and `extras` are replaced in full when
        provided. Providing file-tree fields such as `instructions`, `tools`,
        `subagents`, `skills`, or `files` creates a new file tree commit.
      operationId: updateManagedDeepAgent
      parameters:
        - $ref: '#/components/parameters/AgentID'
        - $ref: '#/components/parameters/IncludeFiles'
        - $ref: '#/components/parameters/UserTimezone'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateAgentRequest'
            examples:
              updateInstructions:
                summary: Update instructions and tools
                value:
                  description: >-
                    Research assistant that searches the web, reads URLs, and
                    summarizes sources.
                  instructions: >-
                    You are a careful research assistant. Search for sources,
                    read relevant pages, keep notes, and return concise answers
                    with citations.
                  tools:
                    tools:
                      - name: tavily_web_search
                        mcp_server_url: https://tools.langchain.com
                        mcp_server_name: Fleet
                        display_name: tavily_web_search
                      - name: read_url_content
                        mcp_server_url: https://tools.langchain.com
                        mcp_server_name: Fleet
                        display_name: read_url_content
                    interrupt_config:
                      https://tools.langchain.com::tavily_web_search::Fleet: true
                      https://tools.langchain.com::read_url_content::Fleet: false
      responses:
        '200':
          description: Agent updated.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Agent'
        '400':
          $ref: '#/components/responses/BadRequest'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '422':
          $ref: '#/components/responses/UnprocessableEntity'
        '500':
          $ref: '#/components/responses/InternalServerError'
components:
  parameters:
    AgentID:
      name: agent_id
      in: path
      required: true
      description: Managed Deep Agent ID.
      schema:
        type: string
        format: uuid
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
    UpdateAgentRequest:
      type: object
      description: Sparse update payload. Omitted fields are left unchanged.
      properties:
        name:
          type: string
          description: Updated agent name.
        description:
          type: string
          description: Updated agent description.
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
            Updated subagent definitions. Replaces the existing subagents field
            in full.
          items:
            $ref: '#/components/schemas/SubagentSpec'
        skills:
          type: array
          description: Updated inline skills. Replaces the existing skills field in full.
          items:
            $ref: '#/components/schemas/SkillSpec'
        extras:
          type: object
          description: >-
            Updated caller-defined metadata. Replaces the existing extras field
            in full.
          additionalProperties: true
        files:
          $ref: '#/components/schemas/FileMap'
        backend:
          $ref: '#/components/schemas/AgentBackend'
        system_prompt:
          type: string
          description: >-
            Updated agent system prompt. Written to `AGENTS.md`. Preferred over
            deprecated `instructions` when both are provided.
        configurable:
          type: object
          description: >-
            Updated caller-defined runtime configuration. Typed runtime fields
            win on key collision.
          additionalProperties: true
        deleted_paths:
          type: array
          description: Relative file paths to remove from the file tree.
          items:
            type: string
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
    NotFound:
      description: Resource not found.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          examples:
            agentNotFound:
              summary: Unknown agent ID
              value:
                type: https://docs.langchain.com/errors/agent_not_found
                code: agent_not_found
                detail: >-
                  Verify the agent ID and that the calling identity has access:
                  agent not found
                status: 404
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
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-Api-Key
      x-default: LANGSMITH_API_KEY

````