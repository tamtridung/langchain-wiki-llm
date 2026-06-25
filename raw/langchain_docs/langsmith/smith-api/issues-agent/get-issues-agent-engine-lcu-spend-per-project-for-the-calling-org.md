---
title: Get issues-agent (Engine) LCU spend per project for the calling org
source: https://docs.langchain.com/langsmith/smith-api/issues-agent/get-issues-agent-engine-lcu-spend-per-project-for-the-calling-org.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get issues-agent (Engine) LCU spend per project for the calling org

> Returns one flat row per (tenant, session) pair in the
caller's organization that has Engine spend in the
window, each carrying its workspace name, project
(session) name, and Engine LCU spend. The caller groups
rows by tenant for display and sums the `lcu_total`
field across items for the org-wide total (the UI tile
does both). The window defaults to the current calendar
month (UTC) and can be overridden with `start` and `end`
(RFC 3339, capped at 31 days). Hours where the rate card
did not price a (provider, model) pair are excluded from
each row's `lcu_total` and surfaced as
`lcu_unpriced_row_count` so callers can detect billing
coverage gaps without inflating the spend number.



## OpenAPI

````yaml /langsmith/langsmith-platform-openapi.json get /issues-agent/lcu-spend
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
  /issues-agent/lcu-spend:
    get:
      tags:
        - issues-agent
      summary: Get issues-agent (Engine) LCU spend per project for the calling org
      description: |-
        Returns one flat row per (tenant, session) pair in the
        caller's organization that has Engine spend in the
        window, each carrying its workspace name, project
        (session) name, and Engine LCU spend. The caller groups
        rows by tenant for display and sums the `lcu_total`
        field across items for the org-wide total (the UI tile
        does both). The window defaults to the current calendar
        month (UTC) and can be overridden with `start` and `end`
        (RFC 3339, capped at 31 days). Hours where the rate card
        did not price a (provider, model) pair are excluded from
        each row's `lcu_total` and surfaced as
        `lcu_unpriced_row_count` so callers can detect billing
        coverage gaps without inflating the spend number.
      parameters:
        - description: >-
            Inclusive window start, RFC 3339. Defaults to first instant of
            current calendar month (UTC).
          name: start
          in: query
          schema:
            type: string
            title: Start
        - description: >-
            Exclusive window end, RFC 3339. Defaults to first instant of next
            calendar month (UTC).
          name: end
          in: query
          schema:
            type: string
            title: End
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/issues_agent_usage.LCUSpendResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/issues_agent_usage.LCUSpendErrorResponse'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/issues_agent_usage.LCUSpendErrorResponse'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/issues_agent_usage.LCUSpendErrorResponse'
      security:
        - API Key: []
        - Tenant ID: []
        - Bearer Auth: []
components:
  schemas:
    issues_agent_usage.LCUSpendResponse:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/issues_agent_usage.LCUSpendItem'
        organization_id:
          type: string
        period_end:
          type: string
        period_start:
          type: string
        resolved_monthly_spend_limit_lcu:
          description: >-
            ResolvedMonthlySpendLimitLCU is the effective monthly LCU spend
            limit enforced for

            this org — the minimum of the finance, plan, and admin layers — or
            null when

            unlimited. Surfaced so the UI can render spend against the true
            enforced limit

            rather than the admin layer alone. Serialized as a string for
            NUMERIC precision.
          type: string
    issues_agent_usage.LCUSpendErrorResponse:
      type: object
      properties:
        error:
          type: string
    issues_agent_usage.LCUSpendItem:
      type: object
      properties:
        lcu_total:
          type: string
        lcu_unpriced_row_count:
          type: integer
        session_id:
          type: string
        session_name:
          type: string
        tenant_id:
          type: string
        tenant_name:
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