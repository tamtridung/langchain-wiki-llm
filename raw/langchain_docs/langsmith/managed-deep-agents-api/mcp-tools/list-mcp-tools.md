---
title: List MCP tools
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/mcp-tools/list-mcp-tools.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List MCP tools

> Return tools exposed by a registered MCP server. The API serves cached results when fresh; otherwise, it fetches tools from the remote MCP server and caches the response.



## OpenAPI

````yaml /langsmith/managed-deep-agents-openapi.json get /mcp/tools
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
  /mcp/tools:
    get:
      tags:
        - MCP tools
      summary: List MCP tools
      description: >-
        Return tools exposed by a registered MCP server. The API serves cached
        results when fresh; otherwise, it fetches tools from the remote MCP
        server and caches the response.
      operationId: listMcpTools
      parameters:
        - name: url
          in: query
          required: true
          description: Registered MCP server URL to fetch tools from.
          schema:
            type: string
            format: uri
        - name: oauth_provider_id
          in: query
          required: false
          description: OAuth provider ID for token-based MCP server auth.
          schema:
            type: string
        - name: force_refresh
          in: query
          required: false
          description: >-
            Skip cached tool definitions and fetch fresh tools from the MCP
            server.
          schema:
            type: boolean
            default: false
        - name: ls_user_id
          in: query
          required: false
          description: User ID override for service-key callers.
          schema:
            type: string
      responses:
        '200':
          description: MCP tools returned.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListMcpToolsResponse'
              examples:
                basic:
                  summary: Tools from a registered server
                  value:
                    tools:
                      - name: read_url_content
                        description: Read and extract content from a URL.
                        inputSchema:
                          type: object
                          properties:
                            url:
                              type: string
                          required:
                            - url
                    cached: true
                    fetched_at: '2026-06-01T20:50:32Z'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '502':
          $ref: '#/components/responses/BadGateway'
components:
  schemas:
    ListMcpToolsResponse:
      type: object
      properties:
        tools:
          type: array
          items:
            $ref: '#/components/schemas/McpTool'
          description: Tools exposed by the MCP server.
        cached:
          type: boolean
          description: Whether the response came from the MCP tools cache.
        fetched_at:
          type: string
          description: UTC timestamp when the tools were fetched from the MCP server.
    McpTool:
      type: object
      properties:
        name:
          type: string
          description: Tool name as exposed by the MCP server.
        description:
          type: string
          description: Human-readable tool description.
        inputSchema:
          type: object
          description: JSON schema for the tool input.
          additionalProperties: true
        annotations:
          type: object
          description: MCP tool annotations returned by the server.
          additionalProperties: true
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
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-Api-Key
      x-default: LANGSMITH_API_KEY

````