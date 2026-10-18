# AI and Agent Design

## 1. Design objective

Use AI to accelerate process discovery and agent design while keeping outputs reviewable, evidence-linked and bounded by explicit permissions.

## 2. Provider abstraction

Define an internal provider interface that supports:
- Structured generation against a schema.
- Model and provider identification.
- Configurable timeout and retry policy.
- Usage metadata where available.
- Mock implementations for automated tests.

Business logic should not call a vendor SDK directly.

## 3. Evidence-grounded extraction

For each extracted process element, retain:
- The proposed claim.
- Source document identifier.
- Source locator where available.
- Supporting evidence identifiers.
- Whether the element is extracted, inferred or unverified.
- Review status.

Do not invent evidence locations. If a claim cannot be supported, label it as an assumption or request clarification.

## 4. Process graph validation

Validate that:
- Node and edge identifiers are unique within a graph.
- Edge endpoints exist.
- Evidence references exist and belong to the same project.
- Required fields are present.
- Decision branches can carry explicit conditions.
- The graph is serialisable and conforms to the declared schema.

Graph validation does not prove that the business process is correct; human review remains necessary.

## 5. Opportunity generation

Each opportunity should include:
- Name and description.
- Target process step or steps.
- Opportunity category: automate, assist, simplify or control.
- Supporting evidence.
- Assumptions and unknowns.
- Expected benefit hypothesis.
- Risks, dependencies and control considerations.
- Review status.

Avoid presenting speculative financial benefits as established facts.

## 6. Agent specification contract

Every proposed agent specification should define:
- Name and purpose.
- Explicit scope and out-of-scope actions.
- Trigger and required inputs.
- Expected outputs.
- Permitted tools and operations.
- Permissions and data access boundaries.
- Guardrails and prohibited actions.
- Human escalation conditions.
- Error handling and recovery behaviour.
- Logging and audit requirements.
- Acceptance tests and measurable success criteria.
- Evidence and assumptions supporting the design.

## 7. Human approval

Approval is a review state, not permission to run an agent. Execution must remain disabled in the MVP. Any later execution capability requires a separate threat model, permission model, operational controls and explicit design decision.

Approved versions must be immutable. Material edits create a new version requiring a new review.

## 8. Prompt injection and untrusted content

Uploaded files, extracted text and retrieved content are untrusted data. They may contain instructions intended to manipulate a model.

Controls should include:
- Clear separation between trusted instructions and source content.
- No direct execution of instructions found in documents.
- Strict structured output schemas.
- Tool access disabled during extraction unless specifically required.
- Evidence and policy validation outside the model.
- Adversarial tests using malicious document content.

## 9. Evaluation

Build a small, versioned evaluation set containing representative processes and edge cases. Measure:
- Node extraction precision and recall where labels are available.
- Evidence-link validity.
- Unsupported-claim rate.
- Graph schema pass rate.
- Reviewer correction rate.
- Agent specification schema and policy pass rates.

Record model, prompt and schema versions for reproducibility. Do not describe confidence scores as calibrated probabilities unless calibration has been evaluated.
