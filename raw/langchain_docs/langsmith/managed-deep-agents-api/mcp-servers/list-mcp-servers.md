---
title: List MCP servers
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/mcp-servers/list-mcp-servers.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List MCP servers

> List MCP servers registered in the caller's workspace.



## OpenAPI

````yaml /langsmith/managed-deep-agents-openapi.json get /mcp-servers
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
    get:
      tags:
        - MCP servers
      summary: List MCP servers
      description: List MCP servers registered in the caller's workspace.
      operationId: listMcpServers
      responses:
        '200':
          description: List of registered MCP servers.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListMcpServersResponse'
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
    ListMcpServersResponse:
      type: array
      description: List of MCP servers in the caller's workspace.
      items:
        $ref: '#/components/schemas/McpServer'
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