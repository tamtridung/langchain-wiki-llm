---
title: Get a sandbox
source: https://docs.langchain.com/langsmith/smith-api/sandboxes/get-a-sandbox.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a sandbox

> Retrieve a sandbox by name. Stale provisioning sandboxes are auto-failed.



## OpenAPI

````yaml /langsmith/langsmith-platform-openapi.json get /v2/sandboxes/boxes/{name}
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
  /v2/sandboxes/boxes/{name}:
    get:
      tags:
        - sandboxes
      summary: Get a sandbox
      description: >-
        Retrieve a sandbox by name. Stale provisioning sandboxes are
        auto-failed.
      parameters:
        - description: Sandbox display name
          name: name
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sandboxes.SandboxResponse'
        '404':
          description: Not Found
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
        - X-Service-Key: []
components:
  schemas:
    sandboxes.SandboxResponse:
      type: object
      properties:
        created_at:
          type: string
        created_by:
          type: string
        dataplane_url:
          type: string
        delete_after_stop_seconds:
          type: integer
        fs_capacity_bytes:
          type: integer
        id:
          type: string
        idle_ttl_seconds:
          type: integer
        mem_bytes:
          type: integer
        mount_config:
          $ref: '#/components/schemas/sandboxes.SandboxMountConfig'
        name:
          type: string
        proxy_config:
          $ref: '#/components/schemas/sandboxes.ProxyConfig'
        size_class:
          type: string
        snapshot_id:
          type: string
        status:
          type: string
        status_message:
          type: string
        stopped_at:
          type: string
        updated_at:
          type: string
        updated_by:
          type: string
        vcpus:
          type: integer
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
    sandboxes.SandboxMountConfig:
      type: object
      properties:
        auth:
          $ref: '#/components/schemas/sandboxes.SandboxMountAuthConfig'
        mounts:
          type: array
          items:
            $ref: '#/components/schemas/sandboxapi.MountSpec'
    sandboxes.ProxyConfig:
      type: object
      properties:
        access_control:
          $ref: '#/components/schemas/sandboxes.AccessControl'
        callbacks:
          type: array
          items:
            $ref: '#/components/schemas/sandboxes.Callback'
        no_proxy:
          items:
            type: string
          type: array
        rules:
          type: array
          items:
            $ref: '#/components/schemas/sandboxes.ProxyRule'
    sandboxes.SandboxMountAuthConfig:
      type: object
      properties:
        aws:
          $ref: '#/components/schemas/sandboxes.SandboxAWSMountAuthConfig'
        gcp:
          $ref: '#/components/schemas/sandboxes.SandboxGCPMountAuthConfig'
    sandboxapi.MountSpec:
      type: object
      required:
        - id
        - mount_path
        - type
      properties:
        cache:
          $ref: '#/components/schemas/sandboxapi.MountCacheSpec'
        gcs:
          $ref: '#/components/schemas/sandboxapi.GCSMountSpec'
        git:
          $ref: '#/components/schemas/sandboxapi.GitMountSpec'
        id:
          type: string
          maxLength: 64
        mount_path:
          type: string
        read_only:
          type: boolean
        s3:
          $ref: '#/components/schemas/sandboxapi.S3MountSpec'
        type:
          enum:
            - s3
            - gcs
            - git
          allOf:
            - $ref: '#/components/schemas/sandboxapi.MountKind'
      discriminator:
        mapping:
          s3:
            $ref: '#/components/schemas/sandboxapi.S3BucketMountSpec'
          gcs:
            $ref: '#/components/schemas/sandboxapi.GCSBucketMountSpec'
          git:
            $ref: '#/components/schemas/sandboxapi.GitRepoMountSpec'
        propertyName: type
      oneOf:
        - $ref: '#/components/schemas/sandboxapi.S3BucketMountSpec'
        - $ref: '#/components/schemas/sandboxapi.GCSBucketMountSpec'
        - $ref: '#/components/schemas/sandboxapi.GitRepoMountSpec'
    sandboxes.AccessControl:
      type: object
      properties:
        allow_list:
          items:
            type: string
          type: array
        deny_list:
          items:
            type: string
          type: array
    sandboxes.Callback:
      type: object
      required:
        - match_hosts
        - ttl_seconds
        - url
      properties:
        full_request:
          type: boolean
        match_hosts:
          type: array
          minItems: 1
          items:
            type: string
        request_headers:
          type: array
          items:
            $ref: '#/components/schemas/sandboxes.ProxyHeader'
        ttl_seconds:
          type: integer
          maximum: 3600
          minimum: 60
        url:
          type: string
    sandboxes.ProxyRule:
      type: object
      required:
        - name
      properties:
        aws:
          $ref: '#/components/schemas/sandboxes.ProxyAWSConfig'
        enabled:
          type: boolean
        gcp:
          $ref: '#/components/schemas/sandboxes.ProxyGCPConfig'
        headers:
          type: array
          items:
            $ref: '#/components/schemas/sandboxes.ProxyHeader'
        match_hosts:
          description: >-
            MatchHosts is only accepted for header injection rules. Provider
            auth

            rules use built-in host matching.
          type: array
          items:
            type: string
        match_paths:
          items:
            type: string
          type: array
        name:
          type: string
        type:
          type: string
    sandboxes.SandboxAWSMountAuthConfig:
      type: object
      required:
        - access_key_id
        - secret_access_key
      properties:
        access_key_id:
          $ref: '#/components/schemas/sandboxes.ProxySecretValue'
        secret_access_key:
          $ref: '#/components/schemas/sandboxes.ProxySecretValue'
    sandboxes.SandboxGCPMountAuthConfig:
      type: object
      required:
        - service_account_json
      properties:
        service_account_json:
          $ref: '#/components/schemas/sandboxes.ProxySecretValue'
    sandboxapi.MountCacheSpec:
      type: object
      properties:
        max_size_bytes:
          type: integer
          minimum: 0
        writeback_seconds:
          type: integer
          minimum: 0
    sandboxapi.GCSMountSpec:
      type: object
      required:
        - bucket
      properties:
        bucket:
          type: string
        prefix:
          type: string
    sandboxapi.GitMountSpec:
      type: object
      required:
        - remote_url
      properties:
        ref:
          $ref: '#/components/schemas/sandboxapi.GitMountRefSpec'
        refresh_interval_seconds:
          type: integer
          minimum: 1
        remote_url:
          type: string
    sandboxapi.S3MountSpec:
      type: object
      required:
        - bucket
        - endpoint_url
        - region
      properties:
        bucket:
          type: string
        endpoint_url:
          type: string
        path_style:
          type: boolean
        prefix:
          type: string
        region:
          type: string
    sandboxapi.MountKind:
      type: string
      enum:
        - s3
        - gcs
        - git
      x-enum-varnames:
        - MountKindS3
        - MountKindGCS
        - MountKindGit
    sandboxapi.S3BucketMountSpec:
      type: object
      required:
        - id
        - mount_path
        - type
        - s3
      properties:
        cache:
          $ref: '#/components/schemas/sandboxapi.MountCacheSpec'
        id:
          type: string
          maxLength: 64
        mount_path:
          type: string
        read_only:
          type: boolean
        s3:
          $ref: '#/components/schemas/sandboxapi.S3MountSpec'
        type:
          enum:
            - s3
          allOf:
            - $ref: '#/components/schemas/sandboxapi.MountKind'
      not:
        anyOf:
          - required:
              - gcs
          - required:
              - git
    sandboxapi.GCSBucketMountSpec:
      type: object
      required:
        - id
        - mount_path
        - type
        - gcs
      properties:
        cache:
          $ref: '#/components/schemas/sandboxapi.MountCacheSpec'
        gcs:
          $ref: '#/components/schemas/sandboxapi.GCSMountSpec'
        id:
          type: string
          maxLength: 64
        mount_path:
          type: string
        read_only:
          type: boolean
        type:
          enum:
            - gcs
          allOf:
            - $ref: '#/components/schemas/sandboxapi.MountKind'
      not:
        anyOf:
          - required:
              - s3
          - required:
              - git
    sandboxapi.GitRepoMountSpec:
      type: object
      required:
        - id
        - mount_path
        - type
        - git
      properties:
        git:
          $ref: '#/components/schemas/sandboxapi.GitMountSpec'
        id:
          type: string
          maxLength: 64
        mount_path:
          type: string
        read_only:
          type: boolean
        type:
          enum:
            - git
          allOf:
            - $ref: '#/components/schemas/sandboxapi.MountKind'
      not:
        anyOf:
          - required:
              - s3
          - required:
              - gcs
    sandboxes.ProxyHeader:
      type: object
      required:
        - name
        - type
      properties:
        is_set:
          type: boolean
        name:
          type: string
        type:
          enum:
            - plaintext
            - opaque
            - workspace_secret
          allOf:
            - $ref: '#/components/schemas/sandboxes.HeaderType'
        value:
          type: string
    sandboxes.ProxyAWSConfig:
      type: object
      required:
        - access_key_id
        - secret_access_key
      properties:
        access_key_id:
          $ref: '#/components/schemas/sandboxes.ProxySecretValue'
        secret_access_key:
          $ref: '#/components/schemas/sandboxes.ProxySecretValue'
    sandboxes.ProxyGCPConfig:
      type: object
      required:
        - scopes
        - service_account_json
      properties:
        scopes:
          type: array
          minItems: 1
          items:
            type: string
        service_account_json:
          $ref: '#/components/schemas/sandboxes.ProxySecretValue'
    sandboxes.ProxySecretValue:
      type: object
      required:
        - type
      properties:
        is_set:
          type: boolean
        type:
          enum:
            - plaintext
            - opaque
            - workspace_secret
          allOf:
            - $ref: '#/components/schemas/sandboxes.HeaderType'
        value:
          type: string
    sandboxapi.GitMountRefSpec:
      type: object
      required:
        - name
        - type
      properties:
        name:
          type: string
        type:
          type: string
          enum:
            - branch
            - tag
    sandboxes.HeaderType:
      type: string
      enum:
        - plaintext
        - opaque
        - workspace_secret
      x-enum-varnames:
        - HeaderTypePlaintext
        - HeaderTypeOpaque
        - HeaderTypeWorkspaceSecret
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