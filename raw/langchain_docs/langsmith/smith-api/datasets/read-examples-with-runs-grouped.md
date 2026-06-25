---
title: Read Examples With Runs Grouped
source: https://docs.langchain.com/langsmith/smith-api/datasets/read-examples-with-runs-grouped.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Examples With Runs Grouped

> Fetch examples for a dataset, and fetch the runs for each example if they are associated with the given session_ids.



## OpenAPI

````yaml /langsmith/langsmith-platform-openapi.json post /api/v1/datasets/{dataset_id}/group/runs
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
  /api/v1/datasets/{dataset_id}/group/runs:
    post:
      tags:
        - datasets
      summary: Read Examples With Runs Grouped
      description: >-
        Fetch examples for a dataset, and fetch the runs for each example if
        they are associated with the given session_ids.
      operationId: >-
        read_examples_with_runs_grouped_api_v1_datasets__dataset_id__group_runs_post
      parameters:
        - name: dataset_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Dataset Id
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/QueryGroupedExamplesWithRuns'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GroupedExamplesWithRunsResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - API Key: []
        - Tenant ID: []
        - Bearer Auth: []
components:
  schemas:
    QueryGroupedExamplesWithRuns:
      properties:
        session_ids:
          items:
            type: string
            format: uuid
          type: array
          maxItems: 10
          minItems: 1
          title: Session Ids
        offset:
          type: integer
          minimum: 0
          title: Offset
          default: 0
        limit:
          type: integer
          maximum: 20
          minimum: 1
          title: Limit
          default: 10
        preview:
          type: boolean
          title: Preview
          default: false
        group_by:
          $ref: '#/components/schemas/GroupExampleRunsByField'
        metadata_key:
          type: string
          title: Metadata Key
        per_group_limit:
          type: integer
          maximum: 10
          minimum: 1
          title: Per Group Limit
          default: 5
        filters:
          anyOf:
            - additionalProperties:
                items:
                  type: string
                type: array
              propertyNames:
                format: uuid
              type: object
            - type: 'null'
          title: Filters
      type: object
      required:
        - session_ids
        - group_by
        - metadata_key
      title: QueryGroupedExamplesWithRuns
    GroupedExamplesWithRunsResponse:
      properties:
        groups:
          items:
            $ref: '#/components/schemas/ExampleGroupWithSessions'
          type: array
          title: Groups
      type: object
      required:
        - groups
      title: GroupedExamplesWithRunsResponse
      description: >-
        Response for grouped comparison view of dataset examples.


        Returns dataset examples grouped by a run metadata value (e.g.,
        model='gpt-4').

        Optional filters are applied to all runs before grouping.


        Shows:

        - Which examples were executed with each metadata value

        - Per-session aggregate statistics for runs on those examples

        - The actual example data with their associated runs


        Used for comparing how different sessions performed on the same set of
        examples.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    GroupExampleRunsByField:
      type: string
      enum:
        - run_metadata
        - example_metadata
      title: GroupExampleRunsByField
    ExampleGroupWithSessions:
      properties:
        filter:
          type: string
          title: Filter
        count:
          anyOf:
            - type: integer
            - type: 'null'
          title: Count
        total_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Total Tokens
        total_cost:
          anyOf:
            - type: string
            - type: 'null'
          title: Total Cost
        min_start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Min Start Time
        max_start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Max Start Time
        latency_p50:
          anyOf:
            - type: number
            - type: 'null'
          title: Latency P50
        latency_p99:
          anyOf:
            - type: number
            - type: 'null'
          title: Latency P99
        feedback_stats:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Feedback Stats
        group_key:
          anyOf:
            - type: string
            - type: integer
            - type: number
          title: Group Key
        sessions:
          items:
            $ref: '#/components/schemas/GroupedRunsSessionStats'
          type: array
          title: Sessions
        examples:
          items:
            $ref: '#/components/schemas/ExampleWithRunsCH'
          type: array
          title: Examples
        example_count:
          type: integer
          title: Example Count
        prompt_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Prompt Tokens
        completion_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Completion Tokens
        prompt_cost:
          anyOf:
            - type: string
            - type: 'null'
          title: Prompt Cost
        completion_cost:
          anyOf:
            - type: string
            - type: 'null'
          title: Completion Cost
        error_rate:
          anyOf:
            - type: number
            - type: 'null'
          title: Error Rate
      type: object
      required:
        - filter
        - group_key
        - sessions
        - examples
        - example_count
      title: ExampleGroupWithSessions
      description: >-
        Group of examples with a specific metadata value across multiple
        sessions.


        Extends RunGroupBase with:

        - group_key: metadata value that defines this group

        - sessions: per-session stats for runs matching this metadata value

        - examples: shared examples across all sessions (intersection logic)
                    with flat array of runs (each run has session_id field for frontend to determine column)
        - example_count: unique example count (pagination-aware, same across all
        sessions due to intersection)


        Inherited from RunGroupBase:

        - filter: metadata filter for this group (e.g., "and(eq(is_root, true),
        and(eq(metadata_key, 'model'), eq(metadata_value, 'gpt-4')))")

        - count: total run count across all sessions (includes duplicate runs)

        - total_tokens, total_cost: aggregate across sessions

        - min_start_time, max_start_time: time range across sessions

        - latency_p50, latency_p99: aggregate latency stats across sessions

        - feedback_stats: weighted average feedback across sessions


        Additional aggregate stats:

        - prompt_tokens, completion_tokens: separate token counts

        - prompt_cost, completion_cost: separate costs

        - error_rate: average error rate
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    GroupedRunsSessionStats:
      properties:
        start_time:
          type: string
          format: date-time
          title: Start Time
        end_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: End Time
        extra:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Extra
        name:
          type: string
          title: Name
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
        default_dataset_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Default Dataset Id
        reference_dataset_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Reference Dataset Id
        trace_tier:
          anyOf:
            - $ref: '#/components/schemas/TraceTier'
            - type: 'null'
        id:
          type: string
          format: uuid
          title: Id
        run_count:
          anyOf:
            - type: integer
            - type: 'null'
          title: Run Count
        latency_p50:
          anyOf:
            - type: number
            - type: 'null'
          title: Latency P50
        latency_p99:
          anyOf:
            - type: number
            - type: 'null'
          title: Latency P99
        first_token_p50:
          anyOf:
            - type: number
            - type: 'null'
          title: First Token P50
        first_token_p99:
          anyOf:
            - type: number
            - type: 'null'
          title: First Token P99
        total_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Total Tokens
        prompt_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Prompt Tokens
        completion_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Completion Tokens
        total_cost:
          anyOf:
            - type: string
            - type: 'null'
          title: Total Cost
        prompt_cost:
          anyOf:
            - type: string
            - type: 'null'
          title: Prompt Cost
        completion_cost:
          anyOf:
            - type: string
            - type: 'null'
          title: Completion Cost
        tenant_id:
          type: string
          format: uuid
          title: Tenant Id
        last_run_start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Last Run Start Time
        last_run_start_time_live:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Last Run Start Time Live
        feedback_stats:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Feedback Stats
        session_feedback_stats:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Session Feedback Stats
        run_facets:
          anyOf:
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
          title: Run Facets
        error_rate:
          anyOf:
            - type: number
            - type: 'null'
          title: Error Rate
        streaming_rate:
          anyOf:
            - type: number
            - type: 'null'
          title: Streaming Rate
        test_run_number:
          anyOf:
            - type: integer
            - type: 'null'
          title: Test Run Number
        experiment_progress:
          anyOf:
            - $ref: '#/components/schemas/ExperimentProgress'
            - type: 'null'
        example_count:
          anyOf:
            - type: integer
            - type: 'null'
          title: Example Count
        filter:
          type: string
          title: Filter
        min_start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Min Start Time
        max_start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Max Start Time
      type: object
      required:
        - id
        - tenant_id
        - filter
      title: GroupedRunsSessionStats
      description: >-
        TracerSession stats filtered to runs matching a specific metadata value.


        Extends TracerSession with:

        - example_count: unique examples (vs run_count = total runs including
        duplicates)

        - filter: ClickHouse filter for fetching runs in this session/group

        - min/max_start_time: time range for runs in this session/group
    ExampleWithRunsCH:
      properties:
        outputs:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Outputs
        dataset_id:
          type: string
          format: uuid
          title: Dataset Id
        source_run_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Source Run Id
        metadata:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Metadata
        inputs:
          additionalProperties: true
          type: object
          title: Inputs
        created_at:
          type: string
          format: date-time
          title: Created At
        id:
          type: string
          format: uuid
          title: Id
        name:
          type: string
          title: Name
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
        attachment_urls:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Attachment Urls
        runs:
          items:
            $ref: '#/components/schemas/RunSchemaComparisonView'
          type: array
          title: Runs
      type: object
      required:
        - dataset_id
        - inputs
        - id
        - name
        - runs
      title: ExampleWithRunsCH
      description: >-
        Example schema with list of runs from ClickHouse.


        For non-grouped endpoint (/datasets/{dataset_id}/runs): runs from single
        session.

        For grouped endpoint (/datasets/{dataset_id}/group/runs): flat array of
        runs from

        all sessions, where each run has a session_id field for frontend to
        determine column placement.
    TraceTier:
      type: string
      enum:
        - longlived
        - shortlived
      title: TraceTier
    ExperimentProgress:
      properties:
        expected_run_count:
          type: integer
          title: Expected Run Count
        run_progress:
          type: number
          title: Run Progress
        evaluator_progress:
          additionalProperties:
            type: number
          type: object
          title: Evaluator Progress
      type: object
      required:
        - expected_run_count
        - run_progress
        - evaluator_progress
      title: ExperimentProgress
    RunSchemaComparisonView:
      properties:
        name:
          type: string
          title: Name
        inputs:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Inputs
        inputs_preview:
          anyOf:
            - type: string
            - type: 'null'
          title: Inputs Preview
        run_type:
          $ref: '#/components/schemas/RunTypeEnum'
        start_time:
          type: string
          format: date-time
          title: Start Time
        end_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: End Time
        extra:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Extra
        error:
          anyOf:
            - type: string
            - type: 'null'
          title: Error
        execution_order:
          type: integer
          minimum: 1
          title: Execution Order
          default: 1
        serialized:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Serialized
        outputs:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Outputs
        outputs_preview:
          anyOf:
            - type: string
            - type: 'null'
          title: Outputs Preview
        parent_run_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Parent Run Id
        manifest_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Manifest Id
        manifest_s3_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Manifest S3 Id
        events:
          anyOf:
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
          title: Events
        tags:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Tags
        inputs_s3_urls:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Inputs S3 Urls
        outputs_s3_urls:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Outputs S3 Urls
        s3_urls:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: S3 Urls
        trace_id:
          type: string
          format: uuid
          title: Trace Id
        dotted_order:
          anyOf:
            - type: string
            - type: 'null'
          title: Dotted Order
        trace_min_start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Trace Min Start Time
        trace_max_start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Trace Max Start Time
        id:
          type: string
          format: uuid
          title: Id
        session_id:
          type: string
          format: uuid
          title: Session Id
        reference_example_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Reference Example Id
        total_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Total Tokens
        prompt_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Prompt Tokens
        completion_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Completion Tokens
        first_token_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: First Token Time
        total_cost:
          anyOf:
            - type: string
            - type: 'null'
          title: Total Cost
        prompt_cost:
          anyOf:
            - type: string
            - type: 'null'
          title: Prompt Cost
        completion_cost:
          anyOf:
            - type: string
            - type: 'null'
          title: Completion Cost
        status:
          type: string
          title: Status
        feedback_stats:
          anyOf:
            - additionalProperties:
                additionalProperties: true
                type: object
              type: object
            - type: 'null'
          title: Feedback Stats
        app_path:
          anyOf:
            - type: string
            - type: 'null'
          title: App Path
      type: object
      required:
        - name
        - run_type
        - trace_id
        - id
        - session_id
        - status
      title: RunSchemaComparisonView
      description: Run schema for comparison view.
    RunTypeEnum:
      type: string
      enum:
        - tool
        - chain
        - llm
        - retriever
        - embedding
        - prompt
        - parser
      title: RunTypeEnum
      description: Enum for run types.
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