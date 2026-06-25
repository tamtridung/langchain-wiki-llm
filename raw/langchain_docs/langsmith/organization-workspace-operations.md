---
title: Organization and workspace operations reference
source: https://docs.langchain.com/langsmith/organization-workspace-operations.md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Organization and workspace operations reference

This page provides a comprehensive reference table of [workspace](/langsmith/administration-overview#workspaces) and [organization](/langsmith/administration-overview#organizations) operations and which roles can perform them.

The list includes API operations in LangSmith along with:

* Which system roles can perform each operation.
* The specific permission string required.
* Notes about partial access or special cases.

<Info>
  For an overview of LangSmith's RBAC system, role definitions, and permission concepts, refer to [Role-based access control](/langsmith/rbac).
</Info>

## Contents

| Organization-level operations                                                                                                                                                                                                                                                                               | Workspace-level operations                                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Core management:**<br />• [Organization settings](#organization-settings): Org info and configuration<br />• [Workspaces](#workspaces): Workspace management<br />• [Organization members](#organization-members): Member management<br />• [Roles and permissions](#roles-and-permissions): Custom roles | **Core resources:**<br />• [Projects](#projects): Organize traces and runs<br />• [Runs](#runs): Individual execution traces<br />• [Datasets](#datasets): Test datasets for evaluation<br />• [Examples](#examples): Individual dataset examples<br />• [Experiments](#experiments): Comparative experiments |
| **Security and authentication:**<br />• [SSO and authentication](#sso-and-authentication): Single sign-on setup<br />• [SCIM](#scim): Identity provisioning<br />• [Access policies](#access-policies): Attribute-based access control                                                                      | **Monitoring and analysis:**<br />• [Rules](#rules): Automated run rules<br />• [Alerts](#alerts): Alert rules for monitoring<br />• [Feedback](#feedback): Scores and labels on outputs<br />• [Annotation Queues](#annotation-queues): Human review queues<br />• [Charts](#charts): Custom visualizations  |
| **Billing and accounts:**<br />• [Billing and payments](#billing-and-payments): Subscription management<br />• [API keys](#api-keys): Org-level keys                                                                                                                                                        | **Development and configuration:**<br />• [Prompts](#prompts): Prompt templates (LangChain Hub)<br />• [Deployments](#deployments): Deployment configurations<br />• [MCP Servers](#mcp-servers): Model Context Protocol servers<br />• [Fleet](#fleet): Fleet admin operations                               |
| **Analytics:**<br />• [Charts and dashboards](#organization-charts-and-dashboards): Org-level visualizations<br />• [Usage and analytics](#usage-and-analytics): Usage tracking and TTL settings                                                                                                            | **Workspace management:**<br />• [Workspace settings](#workspace-settings-and-management): Members, settings<br />• [Tags](#tags): Metadata tagging system<br />• [Bulk Exports](#bulk-exports): Data export operations                                                                                       |

**Additional information:**

* [User-level operations](#user-level-operations): Operations for all authenticated users
* [Permission inheritance](#permission-inheritance): How roles inherit across org/workspaces

## Legend

* ✓ **Allowed**: User with this role can perform this action
* ✗ **Not Allowed**: User with this role cannot perform this action
* ⚠ **Partial**: User has limited access (see notes)

## Organization-level operations

<Info>
  Organization-level operations are controlled by organization roles, which are separate from the RBAC feature. Learn more in the [Role-based access control](/langsmith/rbac#organization-roles) guide.
</Info>

### Organization settings

| Operation                   | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   |
| --------------------------- | :-------: | :----------: | :------: | :--------: | --------------------- |
| View organization info      |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| View organization dashboard |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Update organization info    |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| View billing info           |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| View company info           |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Set company info            |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |

### Workspaces

Organization-level workspace management operations.

| Operation           | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   |
| ------------------- | :-------: | :----------: | :------: | :--------: | --------------------- |
| List all workspaces |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Create workspace    |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |

### Organization members

| Operation                       | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   | Notes                                                  |
| ------------------------------- | :-------: | :----------: | :------: | :--------: | --------------------- | ------------------------------------------------------ |
| View organization members       |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |                                                        |
| View active org members         |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |                                                        |
| View pending org members        |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |                                                        |
| Invite member to organization   |     ✓     |       ⚠      |     ✗    |      ✗     | `organization:manage` | Org Operator can only invite Org Users and Org Viewers |
| Invite members (batch)          |     ✓     |       ⚠      |     ✗    |      ✗     | `organization:manage` | Org Operator can only invite Org Users and Org Viewers |
| Add basic auth members          |     ✓     |       ⚠      |     ✗    |      ✗     | `organization:manage` | Org Operator can only add Org Users and Org Viewers    |
| Remove organization member      |     ✓     |       ⚠      |     ✗    |      ✗     | `organization:manage` | Org Operator cannot remove Org Admins                  |
| Update organization member role |     ✓     |       ⚠      |     ✗    |      ✗     | `organization:manage` | Org Operator can only modify Org Users and Org Viewers |
| Delete pending org member       |     ✓     |       ⚠      |     ✗    |      ✗     | `organization:manage` | Org Operator cannot delete pending Org Admin invites   |

### Roles and permissions

| Operation                  | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   |
| -------------------------- | :-------: | :----------: | :------: | :--------: | --------------------- |
| List organization roles    |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| List available permissions |     ✓     |       ✓      |     ✓    |      ✓     | N/A (user-level)      |
| Create custom role         |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Update custom role         |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Delete custom role         |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |

### SSO and authentication

| Operation                    | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   |
| ---------------------------- | :-------: | :----------: | :------: | :--------: | --------------------- |
| View SSO settings            |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Create SSO settings          |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Update SSO settings          |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Delete SSO settings          |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| View login methods           |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Update allowed login methods |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Set default SSO provision    |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |

### SCIM

System for Cross-domain Identity Management for user provisioning.

| Operation         | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   |
| ----------------- | :-------: | :----------: | :------: | :--------: | --------------------- |
| List SCIM tokens  |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Get SCIM token    |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Create SCIM token |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Update SCIM token |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Delete SCIM token |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |

### Access policies

Attribute-based access control (ABAC) policies for fine-grained permissions.

| Operation                    | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   |
| ---------------------------- | :-------: | :----------: | :------: | :--------: | --------------------- |
| List access policies         |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Get access policy            |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Create access policy         |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Delete access policy         |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Attach access policy to role |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |

### Billing and payments

| Operation                      | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   |
| ------------------------------ | :-------: | :----------: | :------: | :--------: | --------------------- |
| Create Stripe setup intent     |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Handle payment method creation |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Change payment plan            |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Create Stripe checkout session |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Confirm checkout completion    |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Create Stripe account links    |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |

### API keys

| Operation                                          | Org Admin | Org Operator | Org User | Org Viewer | Required Permission                                |
| -------------------------------------------------- | :-------: | :----------: | :------: | :--------: | -------------------------------------------------- |
| List org-scoped service keys                       |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`                                |
| Create org-scoped service key (workspace-scoped)\* |     ✓     |       ✓      |     ⚠    |      ✗     | `organization:pats:create`                         |
| Create org-scoped service key (org-wide)\*         |     ✓     |       ✗      |     ✗    |      ✗     | `organization:pats:create` + `organization:manage` |
| Update service key role                            |     ✓     |       ✗      |     ✗    |      ✗     | `organization:manage`                              |
| List personal access tokens (PATs)                 |     ✓     |       ✓      |     ✓    |      ✗     | `organization:read`                                |
| Create personal access token (PAT)                 |     ✓     |       ✓      |     ✓    |      ✗     | `organization:pats:create`                         |
| Delete personal access token (PAT)                 |     ✓     |       ✓      |     ✓    |      ✗     | `organization:read`                                |

<Note>
  \* Organization Operators and Organization Users can create workspace-scoped service keys only for workspaces where they are a Workspace Admin. Org-wide service keys require the Organization Admin role.
</Note>

### Organization charts and dashboards

| Operation                | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   |
| ------------------------ | :-------: | :----------: | :------: | :--------: | --------------------- |
| List org charts          |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Get org chart by ID      |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Create org chart         |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Update org chart         |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Delete org chart         |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Render org chart         |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Get org chart section    |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Create org chart section |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Update org chart section |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Delete org chart section |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Render org chart section |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |

### Usage and analytics

| Operation                                                            | Org Admin | Org Operator | Org User |      Org Viewer     | Required Permission   |
| -------------------------------------------------------------------- | :-------: | :----------: | :------: | :-----------------: | --------------------- |
| View organization usage                                              |     ✓     |       ✓      |     ✓    |          ✓          | `organization:read`   |
| [View granular billable usage](/langsmith/granular-usage)            |     ✓     |       ✓      |     ✓    | `organization:read` |                       |
| [Export granular usage as CSV](/langsmith/granular-usage#csv-export) |     ✓     |       ✓      |     ✓    | `organization:read` |                       |
| View workspace trace retention settings                              |     ✓     |       ✓      |     ✓    |          ✓          | `organization:read`   |
| Set workspace default trace tier (base/extended)                     |     ✓     |       ✓      |     ✗    |          ✗          | `organization:manage` |
| Set workspace extended retention duration (Enterprise)               |     ✓     |       ✓      |     ✗    |          ✗          | `organization:manage` |

## Workspace-level operations

These operations are controlled by [workspace-level roles and permissions](/langsmith/rbac#workspace-roles).

<Tip>
  To understand what each role means and their overall capabilities, refer to the [Role-based access control](/langsmith/rbac) guide.
</Tip>

### Projects

Projects organize traces and runs from your LLM applications.

| Operation                                          | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission              |
| -------------------------------------------------- | :-------------: | :--------------: | :--------------: | -------------------------------- |
| Create a new project                               |        ✓        |         ✗        |         ✗        | `projects:create`                |
| View project list                                  |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| View project details                               |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| View prebuilt dashboard                            |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| View project metadata (top K values)               |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| Update project metadata (name, description, tags)  |        ✓        |         ✓        |         ✗        | `projects:update`                |
| Increase project trace retention (base → extended) |        ✓        |         ✓        |         ✗        | `projects:increase-trace-tier`\* |
| Decrease project trace retention (extended → base) |        ✓        |         ✓        |         ✗        | `projects:decrease-trace-tier`\* |
| Create filter view                                 |        ✓        |         ✗        |         ✗        | `projects:create`                |
| View filter views                                  |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| View specific filter view                          |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| Update filter view                                 |        ✓        |         ✓        |         ✗        | `projects:update`                |
| Delete filter view                                 |        ✓        |         ✗        |         ✗        | `projects:delete`                |
| Delete a project                                   |        ✓        |         ✗        |         ✗        | `projects:delete`                |
| Delete multiple projects                           |        ✓        |         ✗        |         ✗        | `projects:delete`                |
| Get insights jobs (beta)                           |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| Get specific insights job (beta)                   |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| Create insights job (beta)                         |        ✓        |         ✓        |         ✓        | `projects:read` + `rules:create` |
| Update insights job (beta)                         |        ✓        |         ✓        |         ✗        | `projects:update`                |
| Delete insights job (beta)                         |        ✓        |         ✗        |         ✗        | `projects:delete`                |
| Get insights job configs (beta)                    |        ✓        |         ✓        |         ✓        | `rules:read`                     |
| Create insights job config (beta)                  |        ✓        |         ✓        |         ✗        | `rules:create`                   |
| Auto-generate insights job config (beta)           |        ✓        |         ✓        |         ✗        | `rules:create`                   |
| Update insights job config (beta)                  |        ✓        |         ✓        |         ✗        | `rules:update`                   |
| Delete insights job config (beta)                  |        ✓        |         ✓        |         ✗        | `rules:delete`                   |
| Get run cluster from insights job (beta)           |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| Get runs from insights job (beta)                  |        ✓        |         ✓        |         ✓        | `projects:read`                  |

<Note>
  \* `projects:increase-trace-tier` and `projects:decrease-trace-tier` are independent and can be granted separately in custom roles. For example, you can allow a role to decrease retention without allowing it to increase retention. If a user lacks both permissions, the retention settings UI is hidden entirely. If they have only one, the UI is partially enabled (the disallowed direction is disabled).
</Note>

### Runs

Individual execution traces and spans from your LLM applications.

| Operation                                                              | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| ---------------------------------------------------------------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| Send traces from SDK (includes single run, batch, multipart, and OTEL) |        ✓        |         ✓        |         ✗        | `runs:create`       |
| View a specific run                                                    |        ✓        |         ✓        |         ✓        | `runs:read`         |
| View thread preview                                                    |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Query/list runs                                                        |        ✓        |         ✓        |         ✓        | `runs:read`         |
| View run statistics                                                    |        ✓        |         ✓        |         ✓        | `runs:read`         |
| View grouped run statistics                                            |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Group runs by expression                                               |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Generate filter query from natural language                            |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Prefetch runs                                                          |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Update a run (PATCH)                                                   |        ✓        |         ✓        |         ✗        | `runs:create`       |
| View run sharing state                                                 |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Share a run publicly                                                   |        ✓        |         ✓        |         ✗        | `runs:share`        |
| Unshare a run                                                          |        ✓        |         ✓        |         ✗        | `runs:share`        |
| Delete runs by trace ID or metadata                                    |        ✓        |         ✗        |         ✗        | `runs:delete`       |

### Rules

Automated run rules that trigger actions based on run conditions.

| Operation               | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| ----------------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| List all run rules      |        ✓        |         ✓        |         ✓        | `rules:read`        |
| Create a run rule       |        ✓        |         ✓        |         ✗        | `rules:create`      |
| Update a run rule       |        ✓        |         ✓        |         ✗        | `rules:update`      |
| Delete a run rule       |        ✓        |         ✓        |         ✗        | `rules:delete`      |
| View rule logs          |        ✓        |         ✓        |         ✓        | `rules:read`        |
| Get last applied rule   |        ✓        |         ✓        |         ✓        | `rules:read`        |
| Manually trigger a rule |        ✓        |         ✓        |         ✗        | `rules:update`      |
| Trigger multiple rules  |        ✓        |         ✓        |         ✗        | `rules:update`      |

### Alerts

Alert rules for monitoring run conditions.

| Operation         | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| ----------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| Create alert rule |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Update alert rule |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Delete alert rule |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Get alert rule    |        ✓        |         ✓        |         ✓        | `runs:read`         |
| List alert rules  |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Test alert action |        ✓        |         ✓        |         ✓        | `runs:read`         |

### Datasets

Test datasets with examples for evaluation.

| Operation                                    | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission                                  |
| -------------------------------------------- | :-------------: | :--------------: | :--------------: | ---------------------------------------------------- |
| Create a dataset                             |        ✓        |         ✓        |         ✗        | `datasets:create`                                    |
| List datasets                                |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| View dataset details                         |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Update dataset metadata                      |        ✓        |         ✓        |         ✗        | `datasets:update`                                    |
| Delete a dataset                             |        ✓        |         ✗        |         ✗        | `datasets:delete`                                    |
| Upload CSV dataset                           |        ✓        |         ✓        |         ✗        | `datasets:create`                                    |
| Clone dataset                                |        ✓        |         ✓        |         ✗        | `datasets:update`                                    |
| Get dataset version                          |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Get dataset versions                         |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Diff dataset versions                        |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Update dataset version (tags)                |        ✓        |         ✓        |         ✗        | `datasets:update`                                    |
| Download dataset (OpenAI format)             |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Download dataset (OpenAI fine-tuning format) |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Download dataset (CSV)                       |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Download dataset (JSONL)                     |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| View dataset sharing state                   |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Share dataset publicly                       |        ✓        |         ✗        |         ✗        | `datasets:share`                                     |
| Unshare dataset                              |        ✓        |         ✗        |         ✗        | `datasets:share`                                     |
| Get index info                               |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Index dataset                                |        ✓        |         ✓        |         ✗        | `datasets:update`                                    |
| Sync dataset index                           |        ✓        |         ✓        |         ✗        | `datasets:update`                                    |
| Remove dataset index                         |        ✓        |         ✓        |         ✗        | `datasets:update`                                    |
| Search dataset                               |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Generate synthetic examples                  |        ✓        |         ✓        |         ✗        | `datasets:update`                                    |
| Get dataset splits                           |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Update dataset splits                        |        ✓        |         ✓        |         ✓        | `datasets:read`                                      |
| Run playground experiment (batch)            |        ✓        |         ⚠        |         ✗        | `prompts:read` + `datasets:read` + `projects:create` |
| Run playground experiment (stream)           |        ✓        |         ⚠        |         ✗        | `prompts:read` + `datasets:read` + `projects:create` |
| Run studio experiment                        |        ✓        |         ⚠        |         ✗        | `datasets:read` + `projects:create`                  |

<Note>
  Workspace Editors have partial access because they cannot create projects, which limits their ability to create new experiments.
</Note>

### Examples

Individual examples within datasets.

| Operation                       | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| ------------------------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| Count examples                  |        ✓        |         ✓        |         ✓        | `datasets:read`     |
| View a specific example         |        ✓        |         ✓        |         ✓        | `datasets:read`     |
| List examples                   |        ✓        |         ✓        |         ✓        | `datasets:read`     |
| Create a new example            |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| Create examples (bulk)          |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| Update a single example         |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| Update examples (bulk)          |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| Update examples (multipart)     |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| Upload examples from CSV        |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| Upload examples from JSONL      |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| Delete a single example         |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| Delete examples (bulk)          |        ✓        |         ✓        |         ✗        | `datasets:update`   |
| View examples with runs         |        ✓        |         ✓        |         ✓        | `datasets:read`     |
| View grouped examples with runs |        ✓        |         ✓        |         ✓        | `datasets:read`     |
| Validate a single example       |        ✓        |         ✓        |         ✓        | `datasets:read`     |
| Validate examples (bulk)        |        ✓        |         ✓        |         ✓        | `datasets:read`     |

### Experiments

Comparative experiments for evaluating LLM outputs.

| Operation                       | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission                                                       |
| ------------------------------- | :-------------: | :--------------: | :--------------: | ------------------------------------------------------------------------- |
| View comparative experiments    |        ✓        |         ✓        |         ✓        | `projects:read`                                                           |
| Create comparative experiment   |        ✓        |         ⚠        |         ✗        | `projects:create`                                                         |
| Delete comparative experiment   |        ✓        |         ✗        |         ✗        | `projects:delete`                                                         |
| View examples with runs         |        ✓        |         ✓        |         ✓        | `datasets:read`                                                           |
| View grouped examples with runs |        ✓        |         ✓        |         ✓        | `datasets:read`                                                           |
| View grouped experiments        |        ✓        |         ✓        |         ✓        | `datasets:read`                                                           |
| View feedback delta             |        ✓        |         ✓        |         ✓        | `datasets:read`                                                           |
| Upload experiment results       |        ✓        |         ⚠        |         ✗        | `datasets:create` + `datasets:update` + `projects:create` + `runs:create` |
| Get experiment view overrides   |        ✓        |         ✓        |         ✗        | `datasets:update`                                                         |
| Create experiment view override |        ✓        |         ✓        |         ✗        | `datasets:update`                                                         |
| Update experiment view override |        ✓        |         ✓        |         ✗        | `datasets:update`                                                         |
| Delete experiment view override |        ✓        |         ✓        |         ✗        | `datasets:update`                                                         |

<Note>
  Workspace Editors have partial access because they cannot create projects, which limits their ability to create new experiments.
</Note>

### Feedback

Scores, labels, and corrections on LLM outputs.

| Operation                                     | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| --------------------------------------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| List feedback formulas                        |        ✓        |         ✓        |         ✓        | `feedback:read`     |
| Get feedback formula                          |        ✓        |         ✓        |         ✓        | `feedback:read`     |
| Create feedback formula                       |        ✓        |         ✓        |         ✗        | `feedback:create`   |
| Update feedback formula                       |        ✓        |         ✓        |         ✗        | `feedback:update`   |
| Delete feedback formula                       |        ✓        |         ✓        |         ✗        | `feedback:delete`   |
| View specific feedback                        |        ✓        |         ✓        |         ✓        | `feedback:read`     |
| List feedbacks                                |        ✓        |         ✓        |         ✓        | `feedback:read`     |
| Create feedback                               |        ✓        |         ✓        |         ✗        | `feedback:create`   |
| Eagerly create feedback                       |        ✓        |         ✓        |         ✗        | `feedback:create`   |
| Update feedback                               |        ✓        |         ✓        |         ✗        | `feedback:update`   |
| Delete feedback                               |        ✓        |         ✓        |         ✗        | `feedback:delete`   |
| Batch ingest feedback                         |        ✓        |         ✓        |         ✗        | `feedback:create`   |
| Create feedback ingest token                  |        ✓        |         ✓        |         ✗        | `feedback:create`   |
| List feedback ingest tokens                   |        ✓        |         ✓        |         ✗        | `feedback:create`   |
| Create feedback with token (no auth required) |        ✓        |         ✓        |         ✓        | N/A (token-based)   |
| List feedback configs                         |        ✓        |         ✓        |         ✓        | `feedback:read`     |
| Create feedback config                        |        ✓        |         ✓        |         ✗        | `feedback:create`   |
| Update feedback config                        |        ✓        |         ✓        |         ✗        | `feedback:update`   |

### Annotation queues

Human review queues for LLM outputs.

| Operation                                   | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission        |
| ------------------------------------------- | :-------------: | :--------------: | :--------------: | -------------------------- |
| List annotation queues                      |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |
| Get annotation queue                        |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |
| Create annotation queue                     |        ✓        |         ✓        |         ✗        | `annotation-queues:create` |
| Update annotation queue                     |        ✓        |         ✓        |         ✗        | `annotation-queues:update` |
| Delete annotation queue                     |        ✓        |         ✗        |         ✗        | `annotation-queues:delete` |
| Populate annotation queue                   |        ✓        |         ✓        |         ✗        | `annotation-queues:update` |
| Get runs from queue                         |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |
| Get run from queue (by index)               |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |
| Get queues for run                          |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |
| Get queue total size                        |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |
| Get queue total archived                    |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |
| Get queue size                              |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |
| Add runs to queue                           |        ✓        |         ✓        |         ✗        | `annotation-queues:update` |
| Update run in queue                         |        ✓        |         ✓        |         ✗        | `annotation-queues:update` |
| Delete run from queue                       |        ✓        |         ✓        |         ✗        | `annotation-queues:update` |
| Delete runs from queue (bulk)               |        ✓        |         ✓        |         ✗        | `annotation-queues:update` |
| Create identity annotation queue run status |        ✓        |         ✓        |         ✗        | `annotation-queues:update` |
| Export archived runs                        |        ✓        |         ✓        |         ✓        | `annotation-queues:read`   |

### Prompts

Prompt templates and chains in the LangChain Hub.

| Operation               | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| ----------------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| List prompt repos       |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| View prompt repo        |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Create prompt repo      |        ✓        |         ✓        |         ✗        | `prompts:create`    |
| Fork prompt repo        |        ✓        |         ✓        |         ✗        | `prompts:create`    |
| Update prompt repo      |        ✓        |         ✓        |         ✗        | `prompts:update`    |
| Delete prompt repo      |        ✓        |         ✓        |         ✗        | `prompts:delete`    |
| List commits            |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| View commit             |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Push commit             |        ✓        |         ✓        |         ✗        | `prompts:update`    |
| List repo tags          |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Get all tags            |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Create tag              |        ✓        |         ✓        |         ✗        | `prompts:tag`       |
| Update tag              |        ✓        |         ✓        |         ✗        | `prompts:tag`       |
| Delete tag              |        ✓        |         ✓        |         ✗        | `prompts:tag`       |
| View events             |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| List comments           |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Create comment          |        ✓        |         ✓        |         ✗        | `prompts:read`      |
| Delete comment          |        ✓        |         ✓        |         ✗        | `prompts:read`      |
| Toggle like             |        ✓        |         ✓        |         ✗        | `prompts:read`      |
| Optimize prompt         |        ✓        |         ✓        |         ✗        | `prompts:update`    |
| List optimization jobs  |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Create optimization job |        ✓        |         ✓        |         ✗        | `prompts:create`    |
| Update optimization job |        ✓        |         ✓        |         ✗        | `prompts:update`    |
| Delete optimization job |        ✓        |         ✓        |         ✗        | `prompts:delete`    |
| Invoke prompt canvas    |        ✓        |         ✓        |         ✗        | `prompts:update`    |
| List quick actions      |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Create quick action     |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Delete quick action     |        ✓        |         ✓        |         ✓        | `prompts:read`      |
| Update quick action     |        ✓        |         ✓        |         ✓        | `prompts:read`      |

<Note>
  Some prompt operations support public access for shared prompts.
</Note>

### Charts

Custom visualizations and dashboards.

| Operation               | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| ----------------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| List charts             |        ✓        |         ✓        |         ✓        | `charts:read`       |
| Get chart by ID         |        ✓        |         ✓        |         ✓        | `charts:read`       |
| Create chart            |        ✓        |         ✓        |         ✗        | `charts:create`     |
| Update chart            |        ✓        |         ✓        |         ✗        | `charts:update`     |
| Delete chart            |        ✓        |         ✓        |         ✗        | `charts:delete`     |
| Render chart            |        ✓        |         ✓        |         ✓        | `charts:read`       |
| List chart sections     |        ✓        |         ✓        |         ✓        | `charts:read`       |
| Get chart section by ID |        ✓        |         ✓        |         ✓        | `charts:read`       |
| Create chart section    |        ✓        |         ✓        |         ✗        | `charts:create`     |
| Update chart section    |        ✓        |         ✓        |         ✗        | `charts:update`     |
| Delete chart section    |        ✓        |         ✓        |         ✗        | `charts:delete`     |
| Render chart section    |        ✓        |         ✓        |         ✓        | `charts:read`       |

### Deployments

[LangSmith Deployment](/langsmith/deployment) configurations.

| Operation         | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission  |
| ----------------- | :-------------: | :--------------: | :--------------: | -------------------- |
| Create deployment |        ✓        |         ✓        |         ✗        | `deployments:create` |
| View deployment   |        ✓        |         ✓        |         ✓        | `deployments:read`   |
| Update deployment |        ✓        |         ✓        |         ✗        | `deployments:update` |
| Delete deployment |        ✓        |         ✗        |         ✗        | `deployments:delete` |

### Workspace settings and management

| Operation                                                 | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission         |
| --------------------------------------------------------- | :-------------: | :--------------: | :--------------: | --------------------------- |
| View workspace info                                       |        ✓        |         ✓        |         ✓        | `workspaces:read`           |
| View workspace statistics                                 |        ✓        |         ✓        |         ✓        | `workspaces:read`           |
| Update workspace (name, description)                      |        ✓        |         ✗        |         ✗        | `workspaces:manage`         |
| Delete workspace                                          |        ✓        |         ✗        |         ✗        | `workspaces:manage`         |
| View workspace members                                    |        ✓        |         ✓        |         ✓        | `workspaces:read`           |
| View active workspace members                             |        ✓        |         ✓        |         ✓        | `workspaces:read`           |
| View pending workspace members                            |        ✓        |         ✓        |         ✓        | `workspaces:read`           |
| Add member to workspace                                   |        ✓        |         ✗        |         ✗        | `workspaces:manage-members` |
| Add members (batch)                                       |        ✓        |         ✗        |         ✗        | `workspaces:manage-members` |
| Update workspace member role                              |        ✓        |         ✗        |         ✗        | `workspaces:manage-members` |
| Remove workspace member                                   |        ✓        |         ✗        |         ✗        | `workspaces:manage-members` |
| Delete pending workspace member                           |        ✓        |         ✗        |         ✗        | `workspaces:manage-members` |
| View workspace trace retention settings                   |        ✓        |         ✓        |         ✓        | `workspaces:read`           |
| Update workspace extended retention duration (Enterprise) |        ✓        |         ✗        |         ✗        | `workspaces:manage`         |
| View usage limits                                         |        ✓        |         ✓        |         ✓        | `workspaces:read`           |
| View shared entities                                      |        ✓        |         ✓        |         ✓        | `workspaces:read`           |
| Bulk unshare entities                                     |        ✓        |         ✗        |         ✗        | `workspaces:manage`         |

### Tags

| Operation                       | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| ------------------------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| List tag keys                   |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Get tag key                     |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Create tag key                  |        ✓        |         ✗        |         ✗        | `workspaces:manage` |
| Update tag key                  |        ✓        |         ✗        |         ✗        | `workspaces:manage` |
| Delete tag key                  |        ✓        |         ✗        |         ✗        | `workspaces:manage` |
| List tag values                 |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Get tag value                   |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Create tag value                |        ✓        |         ✗        |         ✗        | `workspaces:manage` |
| Update tag value                |        ✓        |         ✗        |         ✗        | `workspaces:manage` |
| Delete tag value                |        ✓        |         ✗        |         ✗        | `workspaces:manage` |
| List tags                       |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| List tags for resource          |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| List tags for resources (batch) |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| List taggings                   |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Create tagging                  |        ✓        |         ✗        |         ✗        | `workspaces:manage` |
| Delete tagging                  |        ✓        |         ✗        |         ✗        | `workspaces:manage` |

### Bulk exports

| Operation                      | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission   |
| ------------------------------ | :-------------: | :--------------: | :--------------: | --------------------- |
| List bulk exports              |        ✓        |         ✓        |         ✓        | `bulk-exports:read`   |
| Get bulk export                |        ✓        |         ✓        |         ✓        | `bulk-exports:read`   |
| Get bulk export runs           |        ✓        |         ✓        |         ✓        | `bulk-exports:read`   |
| Get bulk export run            |        ✓        |         ✓        |         ✓        | `bulk-exports:read`   |
| Create bulk export             |        ✓        |         ✗        |         ✗        | `bulk-exports:manage` |
| Cancel bulk export             |        ✓        |         ✗        |         ✗        | `bulk-exports:manage` |
| Get bulk export destinations   |        ✓        |         ✓        |         ✓        | `bulk-exports:read`   |
| Get bulk export destination    |        ✓        |         ✓        |         ✓        | `bulk-exports:read`   |
| Create bulk export destination |        ✓        |         ✗        |         ✗        | `bulk-exports:manage` |
| Update bulk export destination |        ✓        |         ✗        |         ✗        | `bulk-exports:manage` |
| Get filtered export runs       |        ✓        |         ✓        |         ✓        | `bulk-exports:read`   |

<Tip>
  `bulk-exports:read` and `bulk-exports:manage` are dedicated permissions that allow you to grant export access via a [custom role](/langsmith/rbac#custom-roles) without granting the broader `workspaces:manage` scope. This is useful for security-team service keys that need to export traces but should not be able to manage workspaces, members, or secrets.
</Tip>

### MCP servers

Model Context Protocol servers for extended functionality.

| Operation         | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| ----------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| List MCP servers  |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Get MCP server    |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Create MCP server |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Update MCP server |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Delete MCP server |        ✓        |         ✓        |         ✓        | `workspaces:read`   |

### Fleet

[Fleet](/langsmith/fleet/index) workspace administration operations.

| Operation                               | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission        |
| --------------------------------------- | :-------------: | :--------------: | :--------------: | -------------------------- |
| View Fleet admin section (usage, spend) |        ✓        |         ✗        |         ✗        | `fleet:read-admin-config`  |
| Manage Fleet spend limits               |        ✓        |         ✗        |         ✗        | `fleet:write-admin-config` |

## User-level operations

These operations are available to all authenticated users and don't require specific workspace or organization permissions:

* View own user profile
* Update own user profile
* List organizations for user
* Create new organization
* List pending workspace invites
* Delete pending workspace invite
* Claim pending workspace invite
* List pending organization invites
* Delete pending organization invite
* Claim pending organization invite

## Permission inheritance

### Organization to workspace

* [Organization Admin](/langsmith/rbac#organization-admin) automatically has full permissions in all workspaces.
* [Organization Operator](/langsmith/rbac#organization-operator) only gets workspace access when explicitly added to workspaces with workspace-level roles (or to workspaces they create).
* [Organization User](/langsmith/rbac#organization-user) and [Organization Viewer](/langsmith/rbac#organization-viewer) only get workspace access when explicitly added to workspaces with workspace-level roles.

For detailed role definitions, refer to [Organization roles](/langsmith/rbac#organization-roles) and [Workspace roles](/langsmith/rbac#workspace-roles).

### Workspace role independence

* Users can have different workspace roles in different workspaces.
* A user might be a [Workspace Admin](/langsmith/rbac#workspace-admin) in one workspace and a [Workspace Viewer](/langsmith/rbac#workspace-viewer) in another.

***

<div className="source-links">
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/organization-workspace-operations.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
