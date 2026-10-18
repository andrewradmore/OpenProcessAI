# Technical Architecture

## 1. Architecture overview

Use a modular monolith for the MVP. Keep modules separated by responsibility without introducing unnecessary distributed services.

## 2. Components

### Frontend
Next.js and TypeScript.

Responsibilities: project management, source upload, evidence inspection, process graph visualisation and editing, opportunity review, agent specification review and export.

### API
FastAPI and Pydantic.

Responsibilities: request validation, authentication and authorisation, project and source management, workflow orchestration, graph validation, agent specification validation and audit events.

### Ingestion module
Validate file type and size; extract text from supported formats; preserve source metadata; create evidence records; and report extraction failures. Parsers must be isolated from API request handling.

### Process analysis module
Identify candidate process elements; generate relationships and decision branches; attach evidence references; identify missing information; and validate graph structure.

### AI provider module
Provide a common interface for supported models; apply structured-output schemas; handle timeouts and provider errors; support test doubles and deterministic test fixtures; and record model metadata without unnecessarily retaining prompts or source content.

### Agent specification module
Generate proposed agent definitions; validate scope and permissions; define expected inputs and outputs; define failure handling and escalation; and maintain version and approval status.

### Persistence module
Store projects, sources, evidence, graphs, specifications and audit events. Enforce project ownership and access rules. Provide transactional updates where needed.

## 3. Proposed request flow

1. The user uploads a document.
2. The API validates the request.
3. The ingestion module extracts text.
4. The evidence service stores source references.
5. The analysis module requests structured process extraction.
6. The graph validator checks nodes, relationships and evidence references.
7. The user reviews and edits the graph.
8. Opportunity analysis generates candidate improvements.
9. The specification generator produces an agent proposal.
10. The user reviews and approves or rejects it.
11. The application exports the approved artefact.

## 4. Dependency direction

The domain layer must not depend directly on a specific AI vendor, web framework or storage implementation.

Suggested logical modules:

- `projects`
- `sources`
- `evidence`
- `process_graph`
- `opportunities`
- `agent_specs`
- `approvals`
- `audit`
- `providers`
- `api`

## 5. Data flow and trust boundaries

Treat source documents as untrusted input. Uploaded content must never be interpreted as system instructions. Extracted content is evidence to analyse, not authority to override application policies.

All generated process elements must pass schema and reference validation before persistence. Any content passed to a model should be bounded, appropriately redacted where needed, and handled under a documented retention policy.

## 6. Failure handling

- Parser failure: report an actionable error.
- AI provider timeout: return a retryable failure where appropriate.
- Invalid model output: validate and retry within configured limits, then fail safely.
- Missing evidence: flag the claim for review.
- Invalid graph: reject the update and return validation errors.
- Permission failure: deny the operation.
- Approval failure: preserve the previous approved version.

## 7. Deployment model

Development: frontend development server, FastAPI application, PostgreSQL and local test storage.

Production readiness requires a separate review of identity, secrets, storage, network controls, backups, observability and deployment configuration.

## 8. Architecture decision

Start with a modular monolith. Split services only when measured scale, isolation or operational requirements justify the added complexity.
