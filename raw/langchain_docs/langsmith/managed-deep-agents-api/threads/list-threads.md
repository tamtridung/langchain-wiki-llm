---
title: List threads
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/threads/list-threads.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List threads

> Return one page of recent threads for a Managed Deep Agent. Results are ordered by latest conversation activity.



## OpenAPI

````yaml /langsmith/managed-deep-agents-openapi.json get /threads
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
    get:
      tags:
        - Threads
      summary: List threads
      description: >-
        Return one page of recent threads for a Managed Deep Agent. Results are
        ordered by latest conversation activity.
      operationId: listManagedDeepAgentThreads
      parameters:
        - name: agent_id
          in: query
          required: true
          description: Managed Deep Agent ID.
          schema:
            type: string
            format: uuid
        - name: page_size
          in: query
          required: false
          description: Items per page. Defaults to 20.
          schema:
            type: integer
            minimum: 1
            maximum: 20
            default: 20
        - name: cursor
          in: query
          required: false
          description: Opaque pagination cursor returned by the previous list call.
          schema:
            type: string
        - name: status
          in: query
          required: false
          description: Filter to a single thread status.
          schema:
            type: string
            enum:
              - idle
              - busy
              - interrupted
              - error
        - name: is_pinned
          in: query
          required: false
          description: Filter by pinned state.
          schema:
            type: boolean
        - name: test_run
          in: query
          required: false
          description: >-
            Return test-run threads instead of non-test threads. Defaults to
            `false`.
          schema:
            type: boolean
            default: false
        - name: requires_attention
          in: query
          required: false
          description: >-
            Return only threads that need user action. Cannot be combined with
            `status`.
          schema:
            type: boolean
      responses:
        '200':
          description: Threads returned.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListThreadsResponse'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '502':
          $ref: '#/components/responses/BadGateway'
components:
  schemas:
    ListThreadsResponse:
      type: object
      properties:
        threads:
          type: array
          items:
            $ref: '#/components/schemas/ThreadSummary'
        next_cursor:
          type:
            - string
            - 'null'
          description: Cursor for the next page, or `null` when there are no more pages.
    ThreadSummary:
      allOf:
        - $ref: '#/components/schemas/Thread'
        - type: object
          properties:
            title:
              type: string
            has_interrupts:
              type: boolean
            state_updated_at:
              type: string
              format: date-time
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