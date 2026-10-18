# API Specification

Base path: `/api/v1`

This document defines the proposed API contract. Endpoints must be implemented and tested before being considered available. Authentication is assumed for protected endpoints; exact identity implementation remains an architecture decision.

## Projects

### `POST /projects`
Create a project.

Request example:
```json
{
  "name": "Accounts Payable Process",
  "description": "Review invoice handling"
}
```
Response: `201 Created` with the created project.

### `GET /projects`
List projects accessible to the current user.

### `GET /projects/{project_id}`
Retrieve project details, subject to authorisation.

### `PATCH /projects/{project_id}`
Update permitted project fields.

## Sources

### `POST /projects/{project_id}/sources`
Upload a supported source document. Enforce file-size limits, validate content, authorise project access and return a source identifier and processing status.

### `GET /projects/{project_id}/sources`
List sources belonging to the project.

### `GET /sources/{source_id}`
Retrieve source metadata and processing status, subject to project authorisation.

### `GET /sources/{source_id}/evidence`
Retrieve evidence segments extracted from a source.

## Process graphs

### `POST /projects/{project_id}/process-graphs/generate`
Request a draft graph from available project sources. This operation may be asynchronous in a later implementation. The response must make clear that the graph is an AI-generated draft.

### `GET /projects/{project_id}/process-graphs`
List graph versions.

### `GET /process-graphs/{graph_id}`
Retrieve a graph and its evidence references.

### `PUT /process-graphs/{graph_id}`
Save an edited graph after validating nodes, edges, project ownership and evidence references. Create a new version or use an explicit versioning policy; do not silently overwrite reviewed history.

## Opportunities

### `POST /projects/{project_id}/opportunities/generate`
Generate candidate process improvement opportunities with rationale, evidence, assumptions and risks.

### `GET /projects/{project_id}/opportunities`
List opportunities and their review status.

### `PATCH /opportunities/{opportunity_id}`
Update permitted review fields, such as accepted or rejected status.

## Agent specifications

### `POST /projects/{project_id}/agent-specifications/generate`
Generate a proposed specification from a reviewed process graph and selected opportunities.

### `GET /projects/{project_id}/agent-specifications`
List specifications and versions.

### `GET /agent-specifications/{specification_id}`
Retrieve a specification, subject to authorisation.

### `POST /agent-specifications/{specification_id}/submit-for-review`
Transition a draft specification into review, provided schema and policy checks pass.

### `POST /agent-specifications/{specification_id}/decision`
Record an approval or rejection for a specific immutable version.

Example request:
```json
{
  "decision": "rejected",
  "reason": "The exception-handling process needs further review."
}
```

Approval records a decision only. It must not execute an agent or initiate external side effects.

## Exports

### `GET /agent-specifications/{specification_id}/export?format=markdown`
Export a specification in a supported format. The implementation must authorise access and avoid exposing internal storage paths.

Supported initial formats: `markdown`, `json`.

## Error conventions

Use consistent HTTP status codes and a structured error body, for example:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The process graph contains an invalid evidence reference.",
    "details": []
  }
}
```

Do not return stack traces, secrets or sensitive document excerpts in production errors.

## API implementation requirements

- Validate requests and responses against explicit schemas.
- Authenticate and authorise every protected endpoint.
- Apply rate and resource limits to expensive operations.
- Make generation operations idempotent where practical.
- Define pagination for collection endpoints.
- Add contract tests for success, validation failure and unauthorised access.
- Publish an OpenAPI document from the implemented API, not merely this proposal.
