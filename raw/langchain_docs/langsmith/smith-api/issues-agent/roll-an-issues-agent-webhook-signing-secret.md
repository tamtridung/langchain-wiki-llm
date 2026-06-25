---
title: Roll an issues agent webhook signing secret
source: https://docs.langchain.com/langsmith/smith-api/issues-agent/roll-an-issues-agent-webhook-signing-secret.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Roll an issues agent webhook signing secret

> Replaces the signing secret for the given issues agent webhook and returns the
updated webhook. Future deliveries are signed with the new secret immediately.



## OpenAPI

````yaml /langsmith/langsmith-platform-openapi.json post /v1/platform/sessions/{session_id}/issues-agent/webhooks/{id}/roll-secret
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
  /v1/platform/sessions/{session_id}/issues-agent/webhooks/{id}/roll-secret:
    post:
      tags:
        - issues-agent
      summary: Roll an issues agent webhook signing secret
      description: >-
        Replaces the signing secret for the given issues agent webhook and
        returns the

        updated webhook. Future deliveries are signed with the new secret
        immediately.
      parameters:
        - description: Tracer session ID (UUID)
          name: session_id
          in: path
          required: true
          schema:
            type: string
        - description: Webhook ID (UUID)
          name: id
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
                $ref: >-
                  #/components/schemas/tracer_session_issues_agent_webhooks.IssuesAgentWebhook
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                additionalProperties:
                  type: string
                type: object
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                additionalProperties:
                  type: string
                type: object
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                additionalProperties:
                  type: string
                type: object
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                additionalProperties:
                  type: string
                type: object
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                additionalProperties:
                  type: string
                type: object
      security:
        - API Key: []
        - Tenant ID: []
        - Bearer Auth: []
components:
  schemas:
    tracer_session_issues_agent_webhooks.IssuesAgentWebhook:
      type: object
      properties:
        created_at:
          type: string
        event_types:
          items:
            type: string
          type: array
        headers:
          type: object
        id:
          type: string
        organization_id:
          description: >-
            OrganizationID is derived from the tenant on fetch (no stored
            column); the

            row carries it so Slack delivery can address the org-scoped install.
          type: string
        session_id:
          type: string
        severity_threshold:
          $ref: '#/components/schemas/tracer_session_issues.Severity'
        signing_secret:
          type: string
        slack_channel_id:
          description: >-
            Delivery target is either a URL or a Slack channel. SlackTeamID is
            the

            channel's workspace (which install to send through).
          type: string
        slack_team_id:
          type: string
        tenant_id:
          type: string
        updated_at:
          type: string
        url:
          type: string
    tracer_session_issues.Severity:
      type: integer
      enum:
        - 0
        - 1
        - 2
        - 3
      x-enum-varnames:
        - SeverityUrgent
        - SeverityHigh
        - SeverityMed
        - SeverityLow
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