---
title: Bulk update threads
source: https://docs.langchain.com/langsmith/managed-deep-agents-api/threads/bulk-update-threads.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk update threads

> Apply one thread update payload to multiple threads. Returns one result per thread in request order.



## OpenAPI

````yaml /langsmith/managed-deep-agents-openapi.json post /threads/bulk-modify
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
  /threads/bulk-modify:
    post:
      tags:
        - Threads
      summary: Bulk update threads
      description: >-
        Apply one thread update payload to multiple threads. Returns one result
        per thread in request order.
      operationId: bulkUpdateManagedDeepAgentThreads
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BulkUpdateThreadsRequest'
      responses:
        '200':
          description: Bulk update results returned.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BulkUpdateThreadsResponse'
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
    BulkUpdateThreadsRequest:
      type: object
      required:
        - thread_ids
        - data
      properties:
        thread_ids:
          type: array
          items:
            type: string
          maxItems: 50
        data:
          $ref: '#/components/schemas/UpdateThreadRequest'
    BulkUpdateThreadsResponse:
      type: object
      properties:
        results:
          type: array
          items:
            $ref: '#/components/schemas/BulkUpdateThreadResult'
    UpdateThreadRequest:
      type: object
      properties:
        title:
          type: string
        metadata:
          type: object
          additionalProperties: true
      additionalProperties: true
    BulkUpdateThreadResult:
      type: object
      properties:
        id:
          type: string
          format: uuid
        status:
          type: string
          enum:
            - success
            - failure
        error_code:
          type: string
        message:
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