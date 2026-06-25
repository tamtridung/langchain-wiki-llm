---
title: List agents
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/agents/list-agents.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List agents

> Return Managed Deep Agents owned by the authenticated user. System-created default agents are excluded.



## OpenAPI

````yaml /langsmith/managed-deep-agents-openapi.json get /agents
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
    get:
      tags:
        - Agents
      summary: List agents
      description: >-
        Return Managed Deep Agents owned by the authenticated user.
        System-created default agents are excluded.
      operationId: listManagedDeepAgents
      parameters:
        - name: page_size
          in: query
          required: false
          description: Items per page. Defaults to 20. Maximum is 100.
          schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 20
        - name: cursor
          in: query
          required: false
          description: Opaque pagination cursor from a previous response.
          schema:
            type: string
        - name: name
          in: query
          required: false
          description: Substring filter on agent name.
          schema:
            type: string
        - name: sort_by
          in: query
          required: false
          description: Field to sort by.
          schema:
            type: string
            enum:
              - created_at
              - updated_at
              - name
            default: updated_at
        - name: sort_order
          in: query
          required: false
          description: Sort order.
          schema:
            type: string
            enum:
              - asc
              - desc
            default: desc
      responses:
        '200':
          description: Agents returned.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListAgentsResponse'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '500':
          $ref: '#/components/responses/InternalServerError'
        '502':
          $ref: '#/components/responses/BadGateway'
        '503':
          $ref: '#/components/responses/ServiceUnavailable'
components:
  schemas:
    ListAgentsResponse:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/AgentSummary'
        next_cursor:
          type:
            - string
            - 'null'
          description: Cursor for the next page, or `null` when there are no more pages.
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
    Unauthorized:
      description: >-
        Authentication required. The auth layer returns a simple `{"error":
        "Unauthorized"}` body that does not match the structured `ErrorResponse`
        shape used by other 4xx responses.
      content:
        application/json:
          schema:
            type: object
            properties:
              error:
                type: string
          examples:
            missingApiKey:
              summary: No `X-Api-Key` header supplied
              value:
                error: Unauthorized
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