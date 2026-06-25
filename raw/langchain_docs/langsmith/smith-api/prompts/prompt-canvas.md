---
title: Prompt Canvas
source: https://docs.langchain.com/langsmith/smith-api/prompts/prompt-canvas.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Prompt Canvas



## OpenAPI

````yaml /langsmith/langsmith-platform-openapi.json post /api/v1/prompts/canvas
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
  /api/v1/prompts/canvas:
    post:
      tags:
        - prompts
      summary: Prompt Canvas
      operationId: prompt_canvas_api_v1_prompts_canvas_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PlaygroundPromptCanvasPayload'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
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
    PlaygroundPromptCanvasPayload:
      properties:
        messages:
          items:
            oneOf:
              - $ref: '#/components/schemas/AIMessage'
              - $ref: '#/components/schemas/HumanMessage'
              - $ref: '#/components/schemas/ChatMessage'
              - $ref: '#/components/schemas/SystemMessage'
              - $ref: '#/components/schemas/FunctionMessage'
              - $ref: '#/components/schemas/ToolMessage'
              - $ref: '#/components/schemas/AIMessageChunk'
              - $ref: '#/components/schemas/HumanMessageChunk'
              - $ref: '#/components/schemas/ChatMessageChunk'
              - $ref: '#/components/schemas/SystemMessageChunk'
              - $ref: '#/components/schemas/FunctionMessageChunk'
              - $ref: '#/components/schemas/ToolMessageChunk'
          type: array
          title: Messages
        highlighted:
          anyOf:
            - $ref: '#/components/schemas/Highlight'
            - type: 'null'
        artifact:
          anyOf:
            - $ref: '#/components/schemas/Artifact'
            - type: 'null'
        artifact_length:
          anyOf:
            - type: string
              enum:
                - shortest
                - short
                - long
                - longest
            - type: 'null'
          title: Artifact Length
        reading_level:
          anyOf:
            - type: string
              enum:
                - child
                - teenager
                - college
                - phd
            - type: 'null'
          title: Reading Level
        custom_action:
          anyOf:
            - type: string
            - type: 'null'
          title: Custom Action
        template_format:
          type: string
          enum:
            - f-string
            - mustache
          title: Template Format
        secrets:
          additionalProperties:
            type: string
          type: object
          title: Secrets
      type: object
      required:
        - messages
        - template_format
        - secrets
      title: PlaygroundPromptCanvasPayload
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    AIMessage:
      properties:
        content:
          anyOf:
            - type: string
            - items:
                anyOf:
                  - type: string
                  - additionalProperties: true
                    type: object
              type: array
          title: Content
        additional_kwargs:
          additionalProperties: true
          type: object
          title: Additional Kwargs
        response_metadata:
          additionalProperties: true
          type: object
          title: Response Metadata
        type:
          type: string
          const: ai
          title: Type
          default: ai
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
        tool_calls:
          items:
            $ref: '#/components/schemas/ToolCall'
          type: array
          title: Tool Calls
        invalid_tool_calls:
          items:
            $ref: '#/components/schemas/InvalidToolCall'
          type: array
          title: Invalid Tool Calls
        usage_metadata:
          anyOf:
            - $ref: '#/components/schemas/UsageMetadata'
            - type: 'null'
      additionalProperties: true
      type: object
      required:
        - content
      title: AIMessage
      description: |-
        Message from an AI.

        An `AIMessage` is returned from a chat model as a response to a prompt.

        This message represents the output of the model and consists of both
        the raw output as returned by the model and standardized fields
        (e.g., tool calls, usage metadata) added by the LangChain framework.
    HumanMessage:
      properties:
        content:
          anyOf:
            - type: string
            - items:
                anyOf:
                  - type: string
                  - additionalProperties: true
                    type: object
              type: array
          title: Content
        additional_kwargs:
          additionalProperties: true
          type: object
          title: Additional Kwargs
        response_metadata:
          additionalProperties: true
          type: object
          title: Response Metadata
        type:
          type: string
          const: human
          title: Type
          default: human
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
      additionalProperties: true
      type: object
      required:
        - content
      title: HumanMessage
      description: >-
        Message from the user.


        A `HumanMessage` is a message that is passed in from a user to the
        model.


        Example:
            ```python
            from langchain_core.messages import HumanMessage, SystemMessage

            messages = [
                SystemMessage(content="You are a helpful assistant! Your name is Bob."),
                HumanMessage(content="What is your name?"),
            ]

            # Instantiate a chat model and invoke it with the messages
            model = ...
            print(model.invoke(messages))
            ```
    ChatMessage:
      properties:
        content:
          anyOf:
            - type: string
            - items:
                anyOf:
                  - type: string
                  - additionalProperties: true
                    type: object
              type: array
          title: Content
        additional_kwargs:
          additionalProperties: true
          type: object
          title: Additional Kwargs
        response_metadata:
          additionalProperties: true
          type: object
          title: Response Metadata
        type:
          type: string
          const: chat
          title: Type
          default: chat
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
        role:
          type: string
          title: Role
      additionalProperties: true
      type: object
      required:
        - content
        - role
      title: ChatMessage
      description: Message that can be assigned an arbitrary speaker (i.e. role).
    SystemMessage:
      properties:
        content:
          anyOf:
            - type: string
            - items:
                anyOf:
                  - type: string
                  - additionalProperties: true
                    type: object
              type: array
          title: Content
        additional_kwargs:
          additionalProperties: true
          type: object
          title: Additional Kwargs
        response_metadata:
          additionalProperties: true
          type: object
          title: Response Metadata
        type:
          type: string
          const: system
          title: Type
          default: system
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
      additionalProperties: true
      type: object
      required:
        - content
      title: SystemMessage
      description: |-
        Message for priming AI behavior.

        The system message is usually passed in as the first of a sequence
        of input messages.

        Example:
            ```python
            from langchain_core.messages import HumanMessage, SystemMessage

            messages = [
                SystemMessage(content="You are a helpful assistant! Your name is Bob."),
                HumanMessage(content="What is your name?"),
            ]

            # Define a chat model and invoke it with the messages
            print(model.invoke(messages))
            ```
    FunctionMessage:
      properties:
        content:
          anyOf:
            - type: string
            - items:
                anyOf:
                  - type: string
                  - additionalProperties: true
                    type: object
              type: array
          title: Content
        additional_kwargs:
          additionalProperties: true
          type: object
          title: Additional Kwargs
        response_metadata:
          additionalProperties: true
          type: object
          title: Response Metadata
        type:
          type: string
          const: function
          title: Type
          default: function
        name:
          type: string
          title: Name
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
      additionalProperties: true
      type: object
      required:
        - content
        - name
      title: FunctionMessage
      description: >-
        Message for passing the result of executing a tool back to a model.


        `FunctionMessage` are an older version of the `ToolMessage` schema, and

        do not contain the `tool_call_id` field.


        The `tool_call_id` field is used to associate the tool call request with
        the

        tool call response. Useful in situations where a chat model is able

        to request multiple tool calls in parallel.
    ToolMessage:
      properties:
        content:
          anyOf:
            - type: string
            - items:
                anyOf:
                  - type: string
                  - additionalProperties: true
                    type: object
              type: array
          title: Content
        additional_kwargs:
          additionalProperties: true
          type: object
          title: Additional Kwargs
        response_metadata:
          additionalProperties: true
          type: object
          title: Response Metadata
        type:
          type: string
          const: tool
          title: Type
          default: tool
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
        tool_call_id:
          type: string
          title: Tool Call Id
        artifact:
          title: Artifact
        status:
          type: string
          enum:
            - success
            - error
          title: Status
          default: success
      additionalProperties: true
      type: object
      required:
        - content
        - tool_call_id
      title: ToolMessage
      description: >-
        Message for passing the result of executing a tool back to a model.


        `ToolMessage` objects contain the result of a tool invocation.
        Typically, the result

        is encoded inside the `content` field.


        `tool_call_id` is used to associate the tool call request with the tool
        call

        response. Useful in situations where a chat model is able to request
        multiple tool

        calls in parallel.


        Example:
            A `ToolMessage` representing a result of `42` from a tool call with id

            ```python
            from langchain_core.messages import ToolMessage

            ToolMessage(content="42", tool_call_id="call_Jja7J89XsjrOLA5r!MEOW!SL")
            ```

        Example:
            A `ToolMessage` where only part of the tool output is sent to the model
            and the full output is passed in to artifact.

            ```python
            from langchain_core.messages import ToolMessage

            tool_output = {
                "stdout": "From the graph we can see that the correlation between "
                "x and y is ...",
                "stderr": None,
                "artifacts": {"type": "image", "base64_data": "/9j/4gIcSU..."},
            }

            ToolMessage(
                content=tool_output["stdout"],
                artifact=tool_output,
                tool_call_id="call_Jja7J89XsjrOLA5r!MEOW!SL",
            )
            ```
    AIMessageChunk:
      properties:
        content:
          anyOf:
            - type: string
            - items:
                anyOf:
                  - type: string
                  - additionalProperties: true
                    type: object
              type: array
          title: Content
        additional_kwargs:
          additionalProperties: true
          type: object
          title: Additional Kwargs
        response_metadata:
          additionalProperties: true
          type: object
          title: Response Metadata
        type:
          type: string
          const: AIMessageChunk
          title: Type
          default: AIMessageChunk
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
        tool_calls:
          items:
            $ref: '#/components/schemas/ToolCall'
          type: array
          title: Tool Calls
        invalid_tool_calls:
          items:
            $ref: '#/components/schemas/InvalidToolCall'
          type: array
          title: Invalid Tool Calls
        usage_metadata:
          anyOf:
            - $ref: '#/components/schemas/UsageMetadata'
            - type: 'null'
        tool_call_chunks:
          items:
            $ref: '#/components/schemas/ToolCallChunk'
          type: array
          title: Tool Call Chunks
        chunk_position:
          anyOf:
            - type: string
              const: last
            - type: 'null'
          title: Chunk Position
      additionalProperties: true
      type: object
      required:
        - content
      title: AIMessageChunk
      description: Message chunk from an AI (yielded when streaming).
    HumanMessageChunk:
      properties:
        content:
          anyOf:
            - type: string
            - items:
                anyOf:
                  - type: string
                  - additionalProperties: true
                    type: object
              type: array
          title: Content
        additional_kwargs:
          additionalProperties: true
          type: object
          title: Additional Kwargs
        response_metadata:
          additionalProperties: true
          type: object
          title: Response Metadata
        type:
          type: string
          const: HumanMessageChunk
          title: Type
          default: HumanMessageChunk
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
      additionalProperties: true
      type: object
      required:
        - content
      title: HumanMessageChunk
      description: Human Message chunk.
    ChatMessageChunk:
      properties:
        content:
          anyOf:
            - type: string
            - items:
                anyOf:
                  - type: string
                  - additionalProperties: true
                    type: object
              type: array
          title: Content
        additional_kwargs:
          additionalProperties: true
          type: object
          title: Additional Kwargs
        response_metadata:
          additionalProperties: true
          type: object
          title: Response Metadata
        type:
          type: string
          const: ChatMessageChunk
          title: Type
          default: ChatMessageChunk
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
        role:
          type: string
          title: Role
      additionalProperties: true
      type: object
      required:
        - content
        - role
      title: ChatMessageChunk
      description: Chat Message chunk.
    SystemMessageChunk:
      properties:
        content:
          anyOf:
            - type: string
            - items:
                anyOf:
                  - type: string
                  - additionalProperties: true
                    type: object
              type: array
          title: Content
        additional_kwargs:
          additionalProperties: true
          type: object
          title: Additional Kwargs
        response_metadata:
          additionalProperties: true
          type: object
          title: Response Metadata
        type:
          type: string
          const: SystemMessageChunk
          title: Type
          default: SystemMessageChunk
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
      additionalProperties: true
      type: object
      required:
        - content
      title: SystemMessageChunk
      description: System Message chunk.
    FunctionMessageChunk:
      properties:
        content:
          anyOf:
            - type: string
            - items:
                anyOf:
                  - type: string
                  - additionalProperties: true
                    type: object
              type: array
          title: Content
        additional_kwargs:
          additionalProperties: true
          type: object
          title: Additional Kwargs
        response_metadata:
          additionalProperties: true
          type: object
          title: Response Metadata
        type:
          type: string
          const: FunctionMessageChunk
          title: Type
          default: FunctionMessageChunk
        name:
          type: string
          title: Name
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
      additionalProperties: true
      type: object
      required:
        - content
        - name
      title: FunctionMessageChunk
      description: Function Message chunk.
    ToolMessageChunk:
      properties:
        content:
          anyOf:
            - type: string
            - items:
                anyOf:
                  - type: string
                  - additionalProperties: true
                    type: object
              type: array
          title: Content
        additional_kwargs:
          additionalProperties: true
          type: object
          title: Additional Kwargs
        response_metadata:
          additionalProperties: true
          type: object
          title: Response Metadata
        type:
          type: string
          const: ToolMessageChunk
          title: Type
          default: ToolMessageChunk
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
        tool_call_id:
          type: string
          title: Tool Call Id
        artifact:
          title: Artifact
        status:
          type: string
          enum:
            - success
            - error
          title: Status
          default: success
      additionalProperties: true
      type: object
      required:
        - content
        - tool_call_id
      title: ToolMessageChunk
      description: Tool Message chunk.
    Highlight:
      properties:
        prompt_chunk_start_index:
          type: integer
          title: Prompt Chunk Start Index
        prompt_chunk_end_index:
          type: integer
          title: Prompt Chunk End Index
        prompt_chunk:
          type: string
          title: Prompt Chunk
        highlight_text:
          type: string
          title: Highlight Text
      type: object
      required:
        - prompt_chunk_start_index
        - prompt_chunk_end_index
        - prompt_chunk
        - highlight_text
      title: Highlight
    Artifact:
      properties:
        id:
          type: string
          title: Id
        contents:
          items:
            $ref: '#/components/schemas/ArtifactContent'
          type: array
          title: Contents
        current_content_index:
          type: integer
          title: Current Content Index
      type: object
      required:
        - id
        - contents
        - current_content_index
      title: Artifact
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
    ToolCall:
      properties:
        name:
          type: string
          title: Name
        args:
          additionalProperties: true
          type: object
          title: Args
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
        type:
          type: string
          const: tool_call
          title: Type
      type: object
      required:
        - name
        - args
        - id
      title: ToolCall
      description: |-
        Represents an AI's request to call a tool.

        Example:
            ```python
            {"name": "foo", "args": {"a": 1}, "id": "123"}
            ```

            This represents a request to call the tool named `'foo'` with arguments
            `{"a": 1}` and an identifier of `'123'`.

        !!! note "Factory function"

            `tool_call` may also be used as a factory to create a `ToolCall`. Benefits
            include:

            * Required arguments strictly validated at creation time
    InvalidToolCall:
      properties:
        type:
          type: string
          const: invalid_tool_call
          title: Type
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        args:
          anyOf:
            - type: string
            - type: 'null'
          title: Args
        error:
          anyOf:
            - type: string
            - type: 'null'
          title: Error
        index:
          anyOf:
            - type: integer
            - type: string
          title: Index
        extras:
          additionalProperties: true
          type: object
          title: Extras
      type: object
      required:
        - type
        - id
        - name
        - args
        - error
      title: InvalidToolCall
      description: |-
        Allowance for errors made by LLM.

        Here we add an `error` key to surface errors made during generation
        (e.g., invalid JSON arguments.)
    UsageMetadata:
      properties:
        input_tokens:
          type: integer
          title: Input Tokens
        output_tokens:
          type: integer
          title: Output Tokens
        total_tokens:
          type: integer
          title: Total Tokens
        input_token_details:
          $ref: '#/components/schemas/InputTokenDetails'
        output_token_details:
          $ref: '#/components/schemas/OutputTokenDetails'
      type: object
      required:
        - input_tokens
        - output_tokens
        - total_tokens
      title: UsageMetadata
      description: >-
        Usage metadata for a message, such as token counts.


        This is a standard representation of token usage that is consistent
        across models.


        Example:
            ```python
            {
                "input_tokens": 350,
                "output_tokens": 240,
                "total_tokens": 590,
                "input_token_details": {
                    "audio": 10,
                    "cache_creation": 200,
                    "cache_read": 100,
                },
                "output_token_details": {
                    "audio": 10,
                    "reasoning": 200,
                },
            }
            ```

        !!! warning "Behavior changed in `langchain-core` 0.3.9"

            Added `input_token_details` and `output_token_details`.

        !!! note "LangSmith SDK"

            The LangSmith SDK also has a `UsageMetadata` class. While the two share fields,
            LangSmith's `UsageMetadata` has additional fields to capture cost information
            used by the LangSmith platform.
    ToolCallChunk:
      properties:
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        args:
          anyOf:
            - type: string
            - type: 'null'
          title: Args
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
        index:
          anyOf:
            - type: integer
            - type: 'null'
          title: Index
        type:
          type: string
          const: tool_call_chunk
          title: Type
      type: object
      required:
        - name
        - args
        - id
        - index
      title: ToolCallChunk
      description: >-
        A chunk of a tool call (yielded when streaming).


        When merging `ToolCallChunk` objects (e.g., via
        `AIMessageChunk.__add__`), all

        string attributes are concatenated. Chunks are only merged if their
        values of

        `index` are equal and not `None`.


        Example:

        ```python

        left_chunks = [ToolCallChunk(name="foo", args='{"a":', index=0)]

        right_chunks = [ToolCallChunk(name=None, args="1}", index=0)]


        (
            AIMessageChunk(content="", tool_call_chunks=left_chunks)
            + AIMessageChunk(content="", tool_call_chunks=right_chunks)
        ).tool_call_chunks == [ToolCallChunk(name="foo", args='{"a":1}',
        index=0)]

        ```
    ArtifactContent:
      properties:
        index:
          type: integer
          title: Index
        content:
          type: string
          title: Content
      type: object
      required:
        - index
        - content
      title: ArtifactContent
    InputTokenDetails:
      properties:
        audio:
          type: integer
          title: Audio
        cache_creation:
          type: integer
          title: Cache Creation
        cache_read:
          type: integer
          title: Cache Read
      type: object
      title: InputTokenDetails
      description: >-
        Breakdown of input token counts.


        Does *not* need to sum to full input token count. Does *not* need to
        have all keys.


        Example:
            ```python
            {
                "audio": 10,
                "cache_creation": 200,
                "cache_read": 100,
            }
            ```

        May also hold extra provider-specific keys.


        !!! version-added "Added in `langchain-core` 0.3.9"
    OutputTokenDetails:
      properties:
        audio:
          type: integer
          title: Audio
        reasoning:
          type: integer
          title: Reasoning
      type: object
      title: OutputTokenDetails
      description: >-
        Breakdown of output token counts.


        Does *not* need to sum to full output token count. Does *not* need to
        have all keys.


        Example:
            ```python
            {
                "audio": 10,
                "reasoning": 200,
            }
            ```

        May also hold extra provider-specific keys.


        !!! version-added "Added in `langchain-core` 0.3.9"
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