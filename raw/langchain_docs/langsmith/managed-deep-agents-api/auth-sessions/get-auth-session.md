---
title: Get an authorization session
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/auth-sessions/get-auth-session.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get an authorization session

> Return the current status of an in-flight authorization session. Use `wait_seconds` to long-poll until the session completes or the wait window expires.



## OpenAPI

````yaml /langsmith/managed-deep-agents-openapi.json get /auth-sessions/{session_id}
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
  /auth-sessions/{session_id}:
    get:
      tags:
        - Auth sessions
      summary: Get an authorization session
      description: >-
        Return the current status of an in-flight authorization session. Use
        `wait_seconds` to long-poll until the session completes or the wait
        window expires.
      operationId: getAuthSession
      parameters:
        - name: session_id
          in: path
          required: true
          description: Authorization session ID.
          schema:
            type: string
        - name: wait_seconds
          in: query
          required: false
          description: Long-poll window in seconds. Defaults to 1. Maximum is 25.
          schema:
            type: integer
            minimum: 1
            maximum: 25
            default: 1
      responses:
        '200':
          description: Authorization session status returned.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetAuthSessionResponse'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '502':
          $ref: '#/components/responses/BadGateway'
components:
  schemas:
    GetAuthSessionResponse:
      type: object
      properties:
        id:
          type: string
        status:
          $ref: '#/components/schemas/AuthSessionStatus'
    AuthSessionStatus:
      type: string
      enum:
        - PENDING
        - COMPLETED
        - CONNECTION_REQUIRED
        - TOKEN_EXPIRED
      description: Current authorization session status.
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