---
title: Get Server Info
source: https://docs.langchain.com/langsmith/smith-api/info/get-server-info.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Server Info

> Get information about the current deployment of LangSmith.



## OpenAPI

````yaml /langsmith/langsmith-platform-openapi.json get /api/v1/info
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
  /api/v1/info:
    get:
      tags:
        - info
      summary: Get Server Info
      description: Get information about the current deployment of LangSmith.
      operationId: get_server_info_api_v1_info_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/InfoGetResponse'
components:
  schemas:
    InfoGetResponse:
      properties:
        version:
          type: string
          title: Version
        git_sha:
          anyOf:
            - type: string
            - type: 'null'
          title: Git Sha
        license_expiration_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: License Expiration Time
        batch_ingest_config:
          $ref: '#/components/schemas/BatchIngestConfig'
          default:
            use_multipart_endpoint: true
            scale_up_qsize_trigger: 1000
            scale_up_nthreads_limit: 16
            scale_down_nempty_trigger: 4
            size_limit: 100
            size_limit_bytes: 20971520
        instance_flags:
          additionalProperties: true
          type: object
          title: Instance Flags
        customer_info:
          anyOf:
            - $ref: '#/components/schemas/CustomerInfo'
            - type: 'null'
      type: object
      required:
        - version
      title: InfoGetResponse
      description: The LangSmith server info.
    BatchIngestConfig:
      properties:
        use_multipart_endpoint:
          type: boolean
          title: Use Multipart Endpoint
          default: true
        scale_up_qsize_trigger:
          type: integer
          title: Scale Up Qsize Trigger
          default: 1000
        scale_up_nthreads_limit:
          type: integer
          title: Scale Up Nthreads Limit
          default: 16
        scale_down_nempty_trigger:
          type: integer
          title: Scale Down Nempty Trigger
          default: 4
        size_limit:
          type: integer
          title: Size Limit
          default: 100
        size_limit_bytes:
          type: integer
          title: Size Limit Bytes
          default: 20971520
      type: object
      title: BatchIngestConfig
      description: Batch ingest config.
    CustomerInfo:
      properties:
        customer_id:
          type: string
          title: Customer Id
        customer_name:
          type: string
          title: Customer Name
      type: object
      required:
        - customer_id
        - customer_name
      title: CustomerInfo
      description: Customer info.

````