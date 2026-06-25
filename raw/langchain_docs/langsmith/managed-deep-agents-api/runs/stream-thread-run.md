---
title: Stream a thread run
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/runs/stream-thread-run.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Stream a thread run

> Start a run on a thread and stream output as server-sent events. The request must use `agent_id`; `assistant_id` is reserved for server-side forwarding and is rejected.



## OpenAPI

````yaml /langsmith/managed-deep-agents-openapi.json post /threads/{thread_id}/runs/stream
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
  /threads/{thread_id}/runs/stream:
    post:
      tags:
        - Runs
      summary: Stream a thread run
      description: >-
        Start a run on a thread and stream output as server-sent events. The
        request must use `agent_id`; `assistant_id` is reserved for server-side
        forwarding and is rejected.
      operationId: streamManagedDeepAgentThreadRun
      parameters:
        - $ref: '#/components/parameters/ThreadID'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/StreamRunRequest'
            examples:
              basic:
                summary: Stream updates
                value:
                  agent_id: 11111111-1111-1111-1111-111111111111
                  input:
                    messages:
                      - role: user
                        content: >-
                          Research recent approaches to agent memory and
                          summarize the main tradeoffs.
                  stream_mode:
                    - updates
                  stream_subgraphs: true
                  user_timezone: America/Los_Angeles
      responses:
        '200':
          description: Server-sent event stream.
          content:
            text/event-stream:
              schema:
                type: string
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
  parameters:
    ThreadID:
      name: thread_id
      in: path
      required: true
      description: Thread ID.
      schema:
        type: string
  schemas:
    StreamRunRequest:
      type: object
      required:
        - agent_id
        - input
      properties:
        agent_id:
          type: string
          format: uuid
          description: >-
            Managed Deep Agent ID. The server forwards this upstream as
            `assistant_id`.
        input:
          type: object
          required:
            - messages
          description: >-
            Run input state. Include `messages` for chat input; additional
            properties are forwarded as graph input state.
          properties:
            messages:
              type: array
              minItems: 1
              description: Input messages for the run.
              items:
                $ref: '#/components/schemas/Message'
          additionalProperties: true
        stream_mode:
          type: array
          description: Stream modes to return.
          items:
            type: string
            enum:
              - values
              - updates
              - messages-tuple
        stream_subgraphs:
          type: boolean
          description: Whether to stream subgraph events.
        user_timezone:
          type: string
          description: >-
            IANA timezone name (for example, `America/Los_Angeles`) for this
            run. The runtime uses it to inject a localized current-date line
            into the agent's system prompt, so the agent reasons about dates in
            the user's local time. Optional. Defaults to the timezone stamped on
            the agent (or `UTC` if none was set); invalid values fall back to
            `UTC`.
          example: America/Los_Angeles
      additionalProperties: true
    Message:
      type: object
      properties:
        role:
          type: string
          enum:
            - user
            - assistant
            - system
            - tool
        content:
          type: string
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