# Testing Strategy

## 1. Principles

Test deterministic behaviour independently from model behaviour. Use mock providers for most automated tests and a controlled evaluation set for model-specific checks.

## 2. Unit tests

Cover:
- Schema validation.
- Graph node and edge integrity.
- Evidence reference validation.
- Project ownership rules.
- Agent specification validation.
- Versioning and approval state transitions.
- Export serialisation.

## 3. Integration tests

Cover:
- Project creation and retrieval.
- Source upload and parsing.
- Evidence persistence.
- Graph generation using a mock provider.
- Graph editing and version retrieval.
- Opportunity generation and review.
- Specification review and approval recording.
- Access denial across project boundaries.

## 4. Security tests

Include:
- Oversized and malformed uploads.
- Misleading file extensions.
- Path traversal attempts.
- Cross-project identifier access.
- Malicious document text and prompt injection.
- Invalid or unexpected model outputs.
- Secret leakage checks.
- Attempts to execute actions through approval endpoints.

## 5. End-to-end tests

A core end-to-end scenario should create a project, upload a test document, inspect evidence, generate a graph, edit a node, create an opportunity, generate a specification, record a decision and export the artefact.

Assert that no external action is performed at any point.

## 6. Evaluation dataset

Maintain versioned, sanitised example processes with expected nodes, relationships and evidence locations. Avoid committing confidential customer documents or personal data.

## 7. Release gates

A release should not proceed if:
- Critical tests fail.
- Cross-project access isolation is broken.
- Generated outputs can bypass schema validation.
- Approval triggers execution.
- Secrets are committed.
- Material security findings remain unresolved without documented acceptance.
