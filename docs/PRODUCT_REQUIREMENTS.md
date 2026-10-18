# Product Requirements Document

## 1. Product vision

OpenProcessAI helps people understand, document and improve business processes by converting fragmented operational knowledge into structured, evidence-backed process models and proposed AI agents.

## 2. Problem statement

Business processes are often distributed across policy documents, operating procedures, spreadsheets, emails and employee knowledge. Documentation may be incomplete or inconsistent; manual work and bottlenecks can be difficult to identify; and automation can be proposed before a process is understood or adequately controlled.

## 3. Target users

### Primary users
- Business analysts.
- Process improvement specialists.
- Automation and AI teams.
- IT architects.
- Operational managers.

### Secondary users
- Risk and compliance teams.
- Consultants.
- Enterprise transformation leaders.
- Open-source developers building extensions.

## 4. Core user journey

1. Create a project.
2. Define the business function and process under review.
3. Upload documents or provide a written description.
4. Review extracted text and source references.
5. Generate a draft process graph.
6. Correct process steps, relationships and decisions.
7. Review identified gaps and automation opportunities.
8. Generate an agent specification.
9. Review and approve or reject the specification.
10. Export the resulting artefacts.

## 5. Functional requirements

### FR-01: Project management
Users can create, view, update and archive process analysis projects.

### FR-02: Source ingestion
Users can submit supported documents and text descriptions. Unsupported formats must be rejected with a clear explanation.

### FR-03: Evidence management
Extracted claims must reference their source document and, where available, page, section or text-span location.

### FR-04: Process extraction
The system identifies candidate activities, actors, events, decisions, inputs, outputs and dependencies.

### FR-05: Process graph
The system represents process activities and their relationships as a structured graph.

### FR-06: Uncertainty management
The system distinguishes source-supported facts from inferred or unverified information.

### FR-07: Human editing
Users can correct, remove and add nodes, relationships and evidence references.

### FR-08: Opportunity analysis
The system identifies potential automation, simplification and control improvements, with a rationale and supporting evidence.

### FR-09: Agent specification
The system generates a structured proposal containing purpose, scope, inputs, outputs, tools, permissions, constraints and acceptance criteria.

### FR-10: Approval
Users can approve or reject an agent specification. Approval does not automatically enable execution.

### FR-11: Versioning
Changes to process graphs and agent specifications must be traceable.

### FR-12: Export
Users can export structured JSON and readable Markdown.

## 6. Non-functional requirements

- Validate all external input.
- Isolate project data between users and projects.
- Record material changes and approval decisions.
- Make AI provider integrations replaceable.
- Support automated testing.
- Avoid logging sensitive document content unnecessarily.
- Return understandable errors.
- Design for accessibility and maintainability.

## 7. MVP acceptance criteria

The MVP is acceptable when a user can:

1. Create a process project.
2. Submit a supported source document.
3. Inspect extracted content and evidence references.
4. Generate and edit a process graph.
5. Review automation opportunities.
6. Generate a schema-valid agent specification.
7. Approve or reject that specification.
8. Export the final artefacts.
9. Retrieve the project without losing its saved state.
10. Demonstrate through tests that approval does not trigger agent execution.

## 8. Out of scope for MVP

- Unattended production agents.
- Automatic changes to enterprise systems.
- Broad enterprise connector catalogues.
- Autonomous approval of high-impact decisions.
- Guaranteed correctness of AI-generated process maps.
- Full process-mining analytics from event logs.

## 9. Product success measures

Measure:
- Percentage of extracted steps accepted by reviewers.
- Evidence coverage of material process claims.
- Number of manual corrections per generated process.
- Percentage of generated specifications passing validation.
- Time required to produce a reviewed process map.
- Number and severity of security defects.
