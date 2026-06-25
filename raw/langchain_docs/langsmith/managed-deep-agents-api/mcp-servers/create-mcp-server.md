---
title: Register an MCP server
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/mcp-servers/create-mcp-server.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Register an MCP server

> Register an MCP server in the caller's workspace. Static-header servers can include credential headers. OAuth servers should set `auth_type=oauth` and `oauth_mode=per_user_dynamic_client`, then register an OAuth provider and start an auth session before use.



## OpenAPI

````yaml /langsmith/managed-deep-agents-openapi.json post /mcp-servers
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
  /mcp-servers:
    post:
      tags:
        - MCP servers
      summary: Register an MCP server
      description: >-
        Register an MCP server in the caller's workspace. Static-header servers
        can include credential headers. OAuth servers should set
        `auth_type=oauth` and `oauth_mode=per_user_dynamic_client`, then
        register an OAuth provider and start an auth session before use.
      operationId: createMcpServer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateMcpServerRequest'
            examples:
              basic:
                summary: Register Tavily's hosted MCP server with a bearer credential
                value:
                  name: tavily
                  url: https://mcp.tavily.com/mcp/
                  headers:
                    - key: Authorization
                      value: Bearer tvly-...
              oauth:
                summary: Register an OAuth MCP server
                value:
                  name: github-tools
                  url: https://example.com/mcp
                  auth_type: oauth
                  oauth_mode: per_user_dynamic_client
      responses:
        '201':
          description: MCP server registered.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/McpServer'
              examples:
                basic:
                  summary: Newly registered Tavily MCP server
                  value:
                    id: 5b6f6a2b-2c95-4f0f-9c2b-7c3a3e4f8d11
                    tenant_id: 33499cf9-4c02-49af-909d-b8f42e051eab
                    name: tavily
                    url: https://mcp.tavily.com/mcp/
                    headers:
                      - key: Authorization
                        value: Bearer tvly-...
                    auth_type: ''
                    oauth_mode: ''
                    created_at: '2026-05-20T20:50:32.708302+00:00'
                    updated_at: '2026-05-20T20:50:32.708302+00:00'
                    mcp_vendor_id: null
                    vendor_id: null
                    external_system_id: null
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
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
  schemas:
    CreateMcpServerRequest:
      type: object
      required:
        - name
        - url
      properties:
        name:
          type: string
          description: Human-readable name for the MCP server.
        url:
          type: string
          format: uri
          description: MCP server URL. Must be a valid HTTPS endpoint.
        headers:
          type: array
          items:
            $ref: '#/components/schemas/McpServerHeader'
          description: >-
            Credential headers attached to every invocation of this MCP server.
            Omitted from response bodies when the caller lacks invoke permission
            on the server.
        auth_type:
          $ref: '#/components/schemas/AuthType'
        oauth_provider_id:
          type:
            - string
            - 'null'
          format: uuid
          description: Optional OAuth provider ID for legacy shared OAuth providers.
        oauth_mode:
          $ref: '#/components/schemas/OAuthMode'
        vendor_id:
          type: string
          description: Optional vendor identifier for catalog grouping.
        external_system_id:
          type: string
          description: Optional opaque external system identifier.
    McpServer:
      type: object
      properties:
        id:
          type: string
          format: uuid
        tenant_id:
          type: string
          format: uuid
        name:
          type: string
        url:
          type: string
          format: uri
        headers:
          type: array
          items:
            $ref: '#/components/schemas/McpServerHeader'
          description: >-
            Credential headers attached to every invocation of this MCP server.
            Omitted from response bodies when the caller lacks invoke permission
            on the server.
        auth_type:
          $ref: '#/components/schemas/AuthType'
        oauth_provider_id:
          type:
            - string
            - 'null'
          format: uuid
          description: >-
            OAuth provider ID for legacy shared OAuth providers, when
            configured.
        oauth_mode:
          $ref: '#/components/schemas/OAuthMode'
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        mcp_vendor_id:
          type:
            - string
            - 'null'
        vendor_id:
          type:
            - string
            - 'null'
        external_system_id:
          type:
            - string
            - 'null'
        can_invoke:
          type: boolean
          description: >-
            Whether the caller has invoke permission on this server. Omitted
            when ambient permissions already imply invoke.
    McpServerHeader:
      type: object
      required:
        - key
        - value
      description: A single header attached to MCP server invocations.
      properties:
        key:
          type: string
          description: Header name (for example, `Authorization`).
        value:
          type: string
          description: Header value. May contain secrets such as bearer tokens.
    AuthType:
      type: string
      enum:
        - headers
        - oauth
      description: Authentication scheme used by the MCP server.
    OAuthMode:
      type: string
      enum:
        - legacy_shared_provider
        - per_user_dynamic_client
      description: OAuth mode used by an OAuth MCP server.
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