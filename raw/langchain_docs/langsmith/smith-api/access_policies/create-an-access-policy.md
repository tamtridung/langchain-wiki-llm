---
title: Create an access policy
source: https://docs.langchain.com/langsmith/smith-api/access_policies/create-an-access-policy.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an access policy

> Creates a new access policy.



## OpenAPI

````yaml /langsmith/langsmith-platform-openapi.json post /v1/platform/orgs/current/access-policies
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
  /v1/platform/orgs/current/access-policies:
    post:
      tags:
        - access_policies
      summary: Create an access policy
      description: Creates a new access policy.
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/authz_internal.CreateAccessPolicyPayload'
      responses:
        '201':
          description: Access policy created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/authz_internal.AccessPolicyCreateResponse'
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/abac.ErrorResponse'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/abac.ErrorResponse'
        '404':
          description: Role not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/abac.ErrorResponse'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/abac.ErrorResponse'
        '503':
          description: Service unavailable
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/abac.ErrorResponse'
      security:
        - API Key: []
        - Organization ID: []
        - Bearer Auth: []
components:
  schemas:
    authz_internal.CreateAccessPolicyPayload:
      type: object
      properties:
        condition_groups:
          type: array
          items:
            $ref: '#/components/schemas/authz_internal.ConditionGroup'
        description:
          type: string
        effect:
          type: string
        name:
          type: string
        role_ids:
          description: if present, attach to the specified roles
          type: array
          items:
            type: string
    authz_internal.AccessPolicyCreateResponse:
      type: object
      properties:
        id:
          type: string
    abac.ErrorResponse:
      type: object
      properties:
        error:
          type: string
          example: 'Invalid request: missing required fields'
    authz_internal.ConditionGroup:
      type: object
      properties:
        conditions:
          type: array
          items:
            $ref: '#/components/schemas/authz_internal.Condition'
        permission:
          $ref: '#/components/schemas/authz_internal.Permission'
        resource_type:
          type: string
    authz_internal.Condition:
      type: object
      properties:
        attribute_key:
          type: string
        attribute_name:
          $ref: '#/components/schemas/authz_internal.AbacAttributeName'
        attribute_value:
          type: string
        operator:
          $ref: '#/components/schemas/authz_internal.AbacOperator'
    authz_internal.Permission:
      type: string
      enum:
        - annotation-queues:create
        - annotation-queues:delete
        - annotation-queues:read
        - annotation-queues:update
        - charts:create
        - charts:delete
        - charts:read
        - charts:update
        - datasets:create
        - datasets:delete
        - datasets:read
        - datasets:share
        - datasets:tag-on-create
        - datasets:update
        - deployments:create
        - deployments:delete
        - deployments:read
        - deployments:update
        - feedback:create
        - feedback:delete
        - feedback:read
        - feedback:update
        - experiments:run
        - issues:create
        - issues:delete
        - issues:read
        - issues:update
        - projects:create
        - projects:delete
        - projects:read
        - projects:tag-on-create
        - projects:update
        - projects:increase-trace-tier
        - projects:decrease-trace-tier
        - prompts:create
        - prompts:delete
        - prompts:read
        - prompts:tag-on-create
        - prompts:update
        - prompts:share
        - rules:create
        - rules:delete
        - rules:read
        - rules:update
        - rules:configure-retention
        - runs:create
        - runs:read
        - runs:share
        - runs:delete
        - sandboxes:create
        - sandboxes:delete
        - sandboxes:read
        - sandboxes:tag-on-create
        - sandboxes:update
        - sandboxes:exec
        - workspaces:manage-members
        - workspaces:manage-secrets
        - workspaces:manage
        - workspaces:manage-model-configs
        - workspaces:read
        - alerts:create
        - alerts:update
        - alerts:delete
        - alerts:read
        - bulk-exports:read
        - bulk-exports:manage
        - mcp-servers:create
        - mcp-servers:delete
        - mcp-servers:invoke
        - mcp-servers:read
        - mcp-servers:update
        - gateway:invoke
        - fleet:read-admin-config
        - fleet:write-admin-config
        - organization:pats:create
        - organization:read
        - organization:manage
      x-enum-varnames:
        - AnnotationQueuesCreate
        - AnnotationQueuesDelete
        - AnnotationQueuesRead
        - AnnotationQueuesUpdate
        - ChartsCreate
        - ChartsDelete
        - ChartsRead
        - ChartsUpdate
        - DatasetsCreate
        - DatasetsDelete
        - DatasetsRead
        - DatasetsShare
        - DatasetsTagOnCreate
        - DatasetsUpdate
        - DeploymentsCreate
        - DeploymentsDelete
        - DeploymentsRead
        - DeploymentsUpdate
        - FeedbackCreate
        - FeedbackDelete
        - FeedbackRead
        - FeedbackUpdate
        - ExperimentsRun
        - IssuesCreate
        - IssuesDelete
        - IssuesRead
        - IssuesUpdate
        - ProjectsCreate
        - ProjectsDelete
        - ProjectsRead
        - ProjectsTagOnCreate
        - ProjectsUpdate
        - ProjectsIncreaseTraceTier
        - ProjectsDecreaseTraceTier
        - PromptsCreate
        - PromptsDelete
        - PromptsRead
        - PromptsTagOnCreate
        - PromptsUpdate
        - PromptsShare
        - RulesCreate
        - RulesDelete
        - RulesRead
        - RulesUpdate
        - RulesConfigureRetention
        - RunsCreate
        - RunsRead
        - RunsShare
        - RunsDelete
        - SandboxesCreate
        - SandboxesDelete
        - SandboxesRead
        - SandboxesTagOnCreate
        - SandboxesUpdate
        - SandboxesExec
        - WorkspacesManageMembers
        - WorkspacesManageSecrets
        - WorkspacesManage
        - WorkspacesManageModelConfigs
        - WorkspacesRead
        - AlertsCreate
        - AlertsUpdate
        - AlertsDelete
        - AlertsRead
        - BulkExportsRead
        - BulkExportsManage
        - McpServersCreate
        - McpServersDelete
        - McpServersInvoke
        - McpServersRead
        - McpServersUpdate
        - GatewayInvoke
        - FleetReadAdminConfig
        - FleetWriteAdminConfig
        - OrganizationPATsCreate
        - OrganizationRead
        - OrganizationManage
    authz_internal.AbacAttributeName:
      type: string
      enum:
        - resource_tag_key
      x-enum-varnames:
        - AbacAttributeNameResourceTagKey
    authz_internal.AbacOperator:
      type: string
      enum:
        - equals
        - not_equals
        - equals_ignore_case
        - not_equals_ignore_case
        - matches
        - not_matches
        - equals_if_exists
        - not_equals_if_exists
        - equals_ignore_case_if_exists
        - not_equals_ignore_case_if_exists
        - matches_if_exists
        - not_matches_if_exists
      x-enum-varnames:
        - AbacOperatorEquals
        - AbacOperatorNotEquals
        - AbacOperatorEqualsIgnoreCase
        - AbacOperatorNotEqualsIgnoreCase
        - AbacOperatorMatches
        - AbacOperatorNotMatches
        - AbacOperatorEqualsIfExists
        - AbacOperatorNotEqualsIfExists
        - AbacOperatorEqualsIgnoreCaseIfExists
        - AbacOperatorNotEqualsIgnoreCaseIfExists
        - AbacOperatorMatchesIfExists
        - AbacOperatorNotMatchesIfExists
  securitySchemes:
    API Key:
      type: apiKey
      in: header
      name: X-API-Key
    Organization ID:
      type: apiKey
      in: header
      name: X-Organization-Id
    Bearer Auth:
      type: http
      description: >-
        Bearer tokens are used to authenticate from the UI. Must also specify
        x-tenant-id or x-organization-id (for org scoped apis).
      scheme: bearer

````