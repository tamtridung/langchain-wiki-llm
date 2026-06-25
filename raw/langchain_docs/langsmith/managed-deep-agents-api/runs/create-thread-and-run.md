---
title: Create a thread and start a run
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/runs/create-thread-and-run.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a thread and start a run

> Create a thread bound to `agent_id` and start a run on it in one call. Run kwargs are passed through; thread-creation flags go in the optional `thread` envelope.



## OpenAPI

````yaml /langsmith/managed-deep-agents-openapi.json post /threads/runs
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
  /threads/runs:
    post:
      tags:
        - Runs
      summary: Create a thread and start a run
      description: >-
        Create a thread bound to `agent_id` and start a run on it in one call.
        Run kwargs are passed through; thread-creation flags go in the optional
        `thread` envelope.
      operationId: createManagedDeepAgentThreadAndRun
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateThreadAndRunRequest'
      responses:
        '200':
          description: Run returned.
          content:
            application/json:
              schema:
                type: object
                additionalProperties: true
        '201':
          description: Run created.
          content:
            application/json:
              schema:
                type: object
                additionalProperties: true
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          $ref: '#/components/responses/Conflict'
        '422':
          $ref: '#/components/responses/UnprocessableEntity'
        '502':
          $ref: '#/components/responses/BadGateway'
components:
  schemas:
    CreateThreadAndRunRequest:
      type: object
      required:
        - agent_id
      properties:
        agent_id:
          type: string
          description: Managed Deep Agent ID.
          example: 11111111-1111-1111-1111-111111111111
        thread:
          $ref: '#/components/schemas/CreateThreadAndRunThread'
      additionalProperties: true
    CreateThreadAndRunThread:
      type: object
      properties:
        thread_id:
          type: string
          format: uuid
        if_exists:
          type: string
          enum:
            - do_nothing
            - raise
        metadata:
          type: object
          additionalProperties: true
        options:
          $ref: '#/components/schemas/CreateThreadOptions'
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
    CreateThreadOptions:
      type: object
      properties:
        test_run:
          type: boolean
          description: Marks the thread as a test run, filtered out of usage and analytics.
        skip_memory_write_protection:
          type: boolean
          default: false
          description: >-
            Controls whether the runtime pauses for human approval before the
            agent writes to long-term memory on this thread. By default
            (`false`), the runtime raises a human-in-the-loop interrupt when the
            agent tries to write or edit files in its memory directory, so the
            user can approve or reject the write before it persists. Set to
            `true` to bypass that interrupt and let memory writes proceed
            immediately — useful for headless or unattended runs.
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