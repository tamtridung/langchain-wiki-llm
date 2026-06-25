---
title: Start an authorization session
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/auth-sessions/start-auth-session.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Start an authorization session

> Start an OAuth authorization session for the caller. If the user is already authorized, the response can be completed immediately. Otherwise, the response includes a verification URL that the user must visit to complete authorization.



## OpenAPI

````yaml /langsmith/managed-deep-agents-openapi.json post /auth-sessions
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
  /auth-sessions:
    post:
      tags:
        - Auth sessions
      summary: Start an authorization session
      description: >-
        Start an OAuth authorization session for the caller. If the user is
        already authorized, the response can be completed immediately.
        Otherwise, the response includes a verification URL that the user must
        visit to complete authorization.
      operationId: startAuthSession
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateAuthSessionRequest'
            examples:
              oauth:
                summary: Start an OAuth session for an MCP server provider
                value:
                  provider_id: github-tools-provider
                  scopes:
                    - repo
                  strategy: REUSE
      responses:
        '200':
          description: Existing token reused; no new session created.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateAuthSessionResponse'
        '201':
          description: >-
            New pending session created; visit `verification_url` to complete
            authorization.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateAuthSessionResponse'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '502':
          $ref: '#/components/responses/BadGateway'
components:
  schemas:
    CreateAuthSessionRequest:
      type: object
      required:
        - provider_id
        - scopes
        - strategy
      properties:
        provider_id:
          type: string
          description: >-
            OAuth provider ID returned by the MCP OAuth provider registration
            endpoint.
        scopes:
          type: array
          items:
            type: string
          description: OAuth scopes to request.
        strategy:
          $ref: '#/components/schemas/AuthSessionStrategy'
        agent_id:
          type: string
          description: Optional agent ID to associate with the session.
        token_id:
          type: string
          description: Optional token ID to reuse or update.
        is_default:
          type: boolean
          description: >-
            Whether the resulting token should be the default token for this
            provider.
    CreateAuthSessionResponse:
      type: object
      properties:
        id:
          type: string
          description: Authorization session ID. Present for pending sessions.
        provider_id:
          type: string
        status:
          $ref: '#/components/schemas/AuthSessionStatus'
        verification_url:
          type: string
          format: uri
          description: >-
            URL the user must visit to complete authorization. Present when
            status is `PENDING`.
        token:
          type: string
          description: >-
            Token identifier or token payload returned when authorization is
            already complete. Treat this value as sensitive.
        metadata:
          type: object
          additionalProperties: true
    AuthSessionStrategy:
      type: string
      enum:
        - REUSE
        - CREATE
      description: >-
        `REUSE` returns an existing valid token when possible. `CREATE` starts a
        fresh authorization session.
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