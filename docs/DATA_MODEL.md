# Data Model

All entities require stable identifiers and timestamps where appropriate. This is a logical model; physical database migrations must be defined separately.

## Project
- `id`: UUID
- `name`: string
- `description`: optional string
- `status`: active | archived
- `created_by`: user identifier
- `created_at`: timestamp
- `updated_at`: timestamp

## SourceDocument
- `id`: UUID
- `project_id`: UUID
- `filename`: string
- `media_type`: string
- `content_hash`: string
- `storage_reference`: internal reference
- `processing_status`: pending | processing | complete | failed
- `created_at`: timestamp

Do not expose internal storage references as public download URLs.

## Evidence
- `id`: UUID
- `project_id`: UUID
- `source_document_id`: UUID
- `source_locator`: page, section or text-span reference
- `text_excerpt`: optional string
- `content_hash`: optional string
- `created_at`: timestamp

Evidence must refer to a source belonging to the same project.

## ProcessGraph
- `id`: UUID
- `project_id`: UUID
- `version`: integer
- `status`: draft | reviewed
- `nodes`: collection of process nodes
- `edges`: collection of process relationships
- `created_by`: user identifier
- `created_at`: timestamp

## ProcessNode
- `id`: UUID
- `type`: start | activity | decision | end | subprocess
- `name`: string
- `description`: optional string
- `actor`: optional string
- `inputs`: list
- `outputs`: list
- `evidence_ids`: list of Evidence identifiers
- `confidence`: optional bounded score
- `review_status`: unreviewed | accepted | corrected | rejected

Confidence scores are model estimates, not calibrated probabilities unless separately validated.

## ProcessEdge
- `id`: UUID
- `source_node_id`: UUID
- `target_node_id`: UUID
- `condition`: optional string
- `evidence_ids`: list of Evidence identifiers

Both endpoint nodes must exist in the same graph.

## AutomationOpportunity
- `id`: UUID
- `project_id`: UUID
- `title`: string
- `description`: string
- `opportunity_type`: automate | assist | simplify | control
- `evidence_ids`: list
- `assumptions`: list
- `risks`: list
- `review_status`: proposed | accepted | rejected

## AgentSpecification
- `id`: UUID
- `project_id`: UUID
- `version`: integer
- `name`: string
- `purpose`: string
- `scope`: object
- `inputs`: list
- `outputs`: list
- `tools`: list
- `permissions`: list
- `guardrails`: list
- `failure_handling`: list
- `acceptance_criteria`: list
- `evidence_ids`: list
- `status`: draft | in_review | approved | rejected | superseded
- `created_at`: timestamp

## ApprovalRecord
- `id`: UUID
- `agent_specification_id`: UUID
- `version`: integer
- `decision`: approved | rejected
- `reviewer_id`: user identifier
- `reason`: optional string
- `created_at`: timestamp

Approval applies to a specific immutable specification version.

## AuditEvent
- `id`: UUID
- `project_id`: UUID
- `actor_id`: optional user or service identifier
- `action`: string
- `resource_type`: string
- `resource_id`: UUID
- `timestamp`: timestamp
- `metadata`: structured, minimised object

Avoid storing credentials, access tokens or unnecessary document content in audit metadata.

## Integrity rules

1. Enforce project-level access.
2. Validate every evidence reference.
3. Prevent cross-project references.
4. Preserve approved versions.
5. Record material state changes.
6. Use transactions for multi-entity updates.
7. Define retention and deletion behaviour before production deployment.
