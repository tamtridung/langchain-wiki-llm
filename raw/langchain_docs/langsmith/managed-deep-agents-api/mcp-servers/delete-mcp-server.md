---
title: Delete an MCP server
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/mcp-servers/delete-mcp-server.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete an MCP server

> Delete an MCP server. The call is idempotent: deleting a non-existent server returns `204`. After deletion, agents whose tools reference this server's URL will no longer have the stored headers attached at invocation time.



## OpenAPI

````yaml /langsmith/managed-deep-agents-openapi.json delete /mcp-servers/{mcp_server_id}
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
  /mcp-servers/{mcp_server_id}:
    delete:
      tags:
        - MCP servers
      summary: Delete an MCP server
      description: >-
        Delete an MCP server. The call is idempotent: deleting a non-existent
        server returns `204`. After deletion, agents whose tools reference this
        server's URL will no longer have the stored headers attached at
        invocation time.
      operationId: deleteMcpServer
      parameters:
        - $ref: '#/components/parameters/McpServerID'
      responses:
        '204':
          description: MCP server deleted.
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
        '502':
          $ref: '#/components/responses/BadGateway'
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
  schemas:
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
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-Api-Key
      x-default: LANGSMITH_API_KEY

````