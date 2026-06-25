---
title: Create a thread
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/threads/create-thread.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a thread

> Create a thread bound to a Managed Deep Agent. Use the returned thread ID to start runs.



## OpenAPI

````yaml /langsmith/managed-deep-agents-openapi.json post /threads
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
  /threads:
    post:
      tags:
        - Threads
      summary: Create a thread
      description: >-
        Create a thread bound to a Managed Deep Agent. Use the returned thread
        ID to start runs.
      operationId: createManagedDeepAgentThread
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateThreadRequest'
            examples:
              basic:
                summary: Create a thread for an agent
                value:
                  agent_id: 11111111-1111-1111-1111-111111111111
                  options:
                    test_run: false
                    skip_memory_write_protection: false
      responses:
        '201':
          description: Thread created.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Thread'
              examples:
                basic:
                  summary: Thread bound to an agent
                  value:
                    id: 019e2d67-ff4d-7251-bce5-dfdec8e1991b
                    agent_id: ''
                    status: idle
                    metadata:
                      is_test_run: false
                      ls_user_id: 33499cf9-4c02-49af-909d-b8f42e051eab
                      skip_memory_write_protection: false
                      tenant_id: ebbaf2eb-769b-4505-aca2-d11de10372a4
                    created_at: '2026-05-15T20:50:50.832351+00:00'
                    updated_at: '2026-05-15T20:50:50.832351+00:00'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '409':
          $ref: '#/components/responses/Conflict'
        '502':
          $ref: '#/components/responses/BadGateway'
components:
  schemas:
    CreateThreadRequest:
      type: object
      required:
        - agent_id
      properties:
        agent_id:
          type: string
          format: uuid
          description: Managed Deep Agent ID.
        options:
          $ref: '#/components/schemas/CreateThreadOptions'
        thread_id:
          type: string
          format: uuid
          description: Optional caller-supplied thread ID.
        if_exists:
          type: string
          enum:
            - do_nothing
            - raise
          description: Behavior when `thread_id` already exists.
        metadata:
          type: object
          description: Thread metadata.
          additionalProperties: true
    Thread:
      type: object
      properties:
        id:
          type: string
          format: uuid
        agent_id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - idle
            - busy
            - interrupted
            - error
        metadata:
          type: object
          additionalProperties: true
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
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