# MVP Development Roadmap

This roadmap is an initial sequence, not a promise of delivery dates. Complete each stage with tests and review before moving to the next.

## Stage 0 — Repository and engineering baseline

- [ ] Confirm project name, licence and contribution model.
- [ ] Create repository structure and issue templates.
- [ ] Add Python and frontend project scaffolding.
- [ ] Configure formatting, linting and tests.
- [ ] Add environment-variable example files without secrets.
- [ ] Add CI for linting and tests.

**Exit criteria:** a clean checkout can be set up from documented instructions and automated checks run successfully.

## Stage 1 — Domain schemas

- [ ] Define project, source, evidence, process graph and agent specification schemas.
- [ ] Define enumerations and validation rules.
- [ ] Add schema tests and example fixtures.
- [ ] Define versioning and migration conventions.

**Exit criteria:** valid examples pass and invalid references or structures are rejected.

## Stage 2 — Source ingestion

- [ ] Implement project creation.
- [ ] Implement upload validation and supported file types.
- [ ] Extract text and source metadata.
- [ ] Create evidence records with stable source locators.
- [ ] Add size limits, error handling and safe storage.

**Exit criteria:** users can upload a supported document and inspect extracted text with source references.

## Stage 3 — Process graph generation

- [ ] Define the provider interface.
- [ ] Implement a mock provider for tests.
- [ ] Generate structured process nodes and edges.
- [ ] Validate evidence links and graph integrity.
- [ ] Represent uncertainty and unsupported assumptions.
- [ ] Persist and retrieve graph versions.

**Exit criteria:** a source can produce a validated draft graph with traceable evidence.

## Stage 4 — Review and editing

- [ ] Render the process graph.
- [ ] Support node and edge edits.
- [ ] Display supporting evidence.
- [ ] Validate edits before saving.
- [ ] Record material changes.

**Exit criteria:** a reviewer can correct the graph and retrieve the saved version.

## Stage 5 — Opportunity analysis

- [ ] Identify candidate automation and simplification opportunities.
- [ ] Attach evidence and assumptions.
- [ ] Capture risks, dependencies and human-control needs.
- [ ] Allow users to accept or reject suggestions.

**Exit criteria:** every displayed opportunity has a rationale and an explicit review status.

## Stage 6 — Agent specification and approval

- [ ] Define the agent specification schema.
- [ ] Generate specifications from reviewed process steps.
- [ ] Validate tools, permissions, inputs and outputs.
- [ ] Define failure handling and escalation.
- [ ] Implement immutable versioned approvals.
- [ ] Ensure approval cannot launch execution.

**Exit criteria:** a reviewer can approve or reject a versioned specification without triggering external actions.

## Stage 7 — Export, hardening and release

- [ ] Export Markdown and JSON.
- [ ] Add end-to-end tests.
- [ ] Test access isolation and malicious document inputs.
- [ ] Add dependency and secret scanning.
- [ ] Review retention and deletion behaviour.
- [ ] Publish setup instructions and known limitations.

**Exit criteria:** the MVP acceptance criteria in the product requirements are demonstrably met.

## Prioritisation rule

Prefer evidence integrity, safe defaults and a complete end-to-end user journey over adding many integrations or enabling autonomous execution early.
