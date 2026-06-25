---
title: List snapshots
source: https://docs.langchain.com/langsmith/smith-api/sandboxes/list-snapshots.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List snapshots

> List sandbox snapshots for the authenticated tenant, with optional filtering, sorting, and pagination.



## OpenAPI

````yaml /langsmith/langsmith-platform-openapi.json get /v2/sandboxes/snapshots
openapi: 3.1.0
info:
  title: LangSmith
  description: >+
    The LangSmith API is used to programmatically create and manage LangSmith
    resources.


    ## Host

    https://api.smith.langchain.com


    ## Authentication

    To authenticate with the LangSmith API, set the `X-Api-Key` header

    to a valid [LangSmith API
    key](https://docs.langchain.com/langsmith/create-account-api-key#create-an-api-key).

  version: 0.1.0
servers:
  - url: /
security: []
tags:
  - name: run
    x-group: Tracing
  - name: runs
    x-group: Tracing
  - name: sessions
    x-group: Tracing
  - name: tracer-sessions
    x-group: Tracing
  - name: datasets
    x-group: Datasets
  - name: examples
    x-group: Datasets
  - name: evaluators
    x-group: Evaluation
  - name: experiment-view-overrides
    x-group: Evaluation
  - name: experiments
    x-group: Evaluation
  - name: annotation-queues
    x-group: Feedback & Annotation
  - name: annotation_queues
    x-group: Feedback & Annotation
  - name: feedback
    x-group: Feedback & Annotation
  - name: feedback-configs
    x-group: Feedback & Annotation
  - name: alert_rules
    x-group: Monitoring
  - name: bulk-exports
    x-group: Monitoring
  - name: charts
    x-group: Monitoring
  - name: commits
    x-group: Prompts & Playground
  - name: directories
    x-group: Prompts & Playground
  - name: hub_environments
    x-group: Prompts & Playground
  - name: playground-settings
    x-group: Prompts & Playground
  - name: prompt-webhooks
    x-group: Prompts & Playground
  - name: prompts
    x-group: Prompts & Playground
  - name: tag-transitions
    x-group: Prompts & Playground
  - name: comments
    x-group: Prompt Hub
  - name: likes
    x-group: Prompt Hub
  - name: optimization-jobs
    x-group: Prompt Hub
  - name: ownerships
    x-group: Prompt Hub
  - name: repos
    x-group: Prompt Hub
  - name: settings
    x-group: Prompt Hub
  - name: tags
    x-group: Prompt Hub
  - name: integrations
    x-group: Integrations & Tools
  - name: mcp
    x-group: Integrations & Tools
  - name: mcp_vendors
    x-group: Integrations & Tools
  - name: oauth
    x-group: Integrations & Tools
  - name: tools
    x-group: Integrations & Tools
  - name: gateway-policies
    x-group: LLM Gateway
  - name: sandboxes
    x-group: Sandboxes
  - name: issues
    x-group: Issues
  - name: issues-agent
    x-group: Issues
  - name: Organizations
    x-group: Administration
  - name: SCIM Tokens
    x-group: Administration
  - name: TTL Settings
    x-group: Administration
  - name: access_policies
    x-group: Administration
  - name: api-key
    x-group: Administration
  - name: audit-logs
    x-group: Administration
  - name: auth
    x-group: Administration
  - name: aws_marketplace
    x-group: Administration
  - name: data_planes
    x-group: Administration
  - name: me
    x-group: Administration
  - name: orgs
    x-group: Administration
  - name: service-accounts
    x-group: Administration
  - name: tenant
    x-group: Administration
  - name: ttl-settings
    x-group: Administration
  - name: usage-limits
    x-group: Administration
  - name: workspaces
    x-group: Administration
  - name: ace
    x-group: System
  - name: backfills
    x-group: System
  - name: features
    x-group: System
  - name: info
    x-group: System
  - name: model-price-map
    x-group: System
  - name: public
    x-group: System
  - name: fleet secrets
  - name: fleet tenants
  - name: fleet users
paths:
  /v2/sandboxes/snapshots:
    get:
      tags:
        - sandboxes
      summary: List snapshots
      description: >-
        List sandbox snapshots for the authenticated tenant, with optional
        filtering, sorting, and pagination.
      parameters:
        - description: Maximum number of results
          name: limit
          in: query
          schema:
            default: 50
            type: integer
            title: Limit
        - description: Pagination offset
          name: offset
          in: query
          schema:
            type: integer
            default: 0
            title: Offset
        - description: Filter by name substring
          name: name_contains
          in: query
          schema:
            type: string
            title: Name Contains
        - description: Filter by status (building, ready, failed, deleting)
          name: status
          in: query
          schema:
            type: string
            title: Status
        - description: Filter by creator identity. Only 'me' is supported.
          name: created_by
          in: query
          schema:
            type: string
            title: Created By
        - description: Sort column (name, status, created_at)
          name: sort_by
          in: query
          schema:
            default: created_at
            type: string
            title: Sort By
        - description: Sort direction (asc, desc)
          name: sort_direction
          in: query
          schema:
            default: desc
            type: string
            title: Sort Direction
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.SnapshotListResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.ErrorResponse'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.ErrorResponse'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.ErrorResponse'
      security:
        - API Key: []
        - Tenant ID: []
        - Bearer Auth: []
components:
  schemas:
    sandboxes.SnapshotListResponse:
      type: object
      properties:
        offset:
          type: integer
        snapshots:
          type: array
          items:
            $ref: '#/components/schemas/sandboxes.SnapshotResponse'
    sandboxes.ErrorResponse:
      type: object
      properties:
        detail:
          type: object
          properties:
            error:
              type: string
            error_id:
              type: string
            message:
              type: string
    sandboxes.SnapshotResponse:
      type: object
      properties:
        created_at:
          type: string
        created_by:
          type: string
        docker_image:
          type: string
        fs_capacity_bytes:
          type: integer
        fs_used_bytes:
          type: integer
        id:
          type: string
        image_digest:
          type: string
        memory_snapshot_size_bytes:
          description: >-
            MemorySnapshotSizeBytes is non-nil iff the snapshot was captured
            with

            VM memory state. A non-nil value is the canonical signal that this

            snapshot can warm-restore from memory; nil means rootfs only.
          type: integer
        name:
          type: string
        registry_id:
          type: string
        source_sandbox_id:
          type: string
        status:
          type: string
        status_message:
          type: string
        updated_at:
          type: string
  securitySchemes:
    API Key:
      type: apiKey
      in: header
      name: X-API-Key
    Tenant ID:
      type: apiKey
      in: header
      name: X-Tenant-Id
    Bearer Auth:
      type: http
      description: >-
        Bearer tokens are used to authenticate from the UI. Must also specify
        x-tenant-id or x-organization-id (for org scoped apis).
      scheme: bearer

````