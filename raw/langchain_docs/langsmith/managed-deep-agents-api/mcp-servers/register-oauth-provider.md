---
title: Register per-user MCP OAuth provider
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/mcp-servers/register-oauth-provider.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Register per-user MCP OAuth provider

> Discovers and registers an OAuth provider for the authenticated user against a Deep Agents MCP server configured with per-user dynamic client mode. Idempotent when a mapping already exists.



## OpenAPI

````yaml /langsmith/managed-deep-agents-openapi.json post /mcp-servers/{mcp_server_id}/oauth-provider
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
  /mcp-servers/{mcp_server_id}/oauth-provider:
    post:
      tags:
        - MCP servers
      summary: Register per-user MCP OAuth provider
      description: >-
        Discovers and registers an OAuth provider for the authenticated user
        against a Deep Agents MCP server configured with per-user dynamic client
        mode. Idempotent when a mapping already exists.
      operationId: registerMcpOAuthProvider
      parameters:
        - $ref: '#/components/parameters/McpServerID'
      requestBody:
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RegisterMcpOAuthProviderRequest'
            examples:
              empty:
                summary: Infer the user from the authenticated request
                value: {}
      responses:
        '200':
          description: OAuth provider registered or returned.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RegisterMcpOAuthProviderResponse'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '500':
          $ref: '#/components/responses/InternalServerError'
        '503':
          $ref: '#/components/responses/ServiceUnavailable'
components:
  parameters:
    McpServerID:
      name: mcp_server_id
      in: path
      required: true
      description: MCP server ID.
      schema:
        type: string
        format: uuid
  schemas:
    RegisterMcpOAuthProviderRequest:
      type: object
      properties:
        ls_user_id:
          type: string
          description: >-
            Deprecated. User identity is inferred from the authenticated request
            when available.
    RegisterMcpOAuthProviderResponse:
      type: object
      properties:
        oauth_provider_id:
          type: string
          description: OAuth provider ID to use when starting an authorization session.
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
    InternalServerError:
      description: Internal server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
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