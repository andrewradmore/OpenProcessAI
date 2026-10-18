# OpenProcessAI

**Turn business processes into evidence-backed process maps and human-approved AI agent specifications.**

OpenProcessAI is an open-source project designed to help organisations understand how work gets done, identify opportunities for automation, and design AI agents around real business processes.

The platform transforms business documents, written descriptions and interview notes into structured process maps. It links process steps to source evidence, identifies potential improvements, and generates proposed AI agent specifications for review.

## Objectives

- Map business processes from existing documentation.
- Identify activities, actors, decisions, inputs, outputs and dependencies.
- Link extracted information to supporting evidence.
- Highlight bottlenecks, duplication, manual work and automation opportunities.
- Generate structured AI agent specifications.
- Enable users to review, edit, approve and version outputs.
- Establish a secure foundation for future enterprise integrations.

## Core principles

1. Evidence before inference.
2. Human approval before agent execution.
3. Explicit uncertainty where information is missing.
4. Privacy and security by design.
5. Provider-independent AI architecture.
6. Traceable, versioned outputs.
7. Modular architecture that supports community contributions.

## MVP scope

The initial release will support:

1. Creating a process analysis project.
2. Uploading supported documents.
3. Extracting text and recording source references.
4. Generating an evidence-linked process graph.
5. Editing and validating process steps.
6. Identifying potential automation opportunities.
7. Generating a structured agent specification.
8. Reviewing and approving specifications.
9. Exporting process maps and agent specifications.

Agent execution, autonomous production changes and unrestricted access to external systems are outside the initial MVP.

## Proposed technology stack

- Frontend: Next.js and TypeScript.
- Backend: Python and FastAPI.
- Data validation: Pydantic.
- Database: PostgreSQL.
- Development storage: local filesystem or isolated object-storage adapter.
- AI integration: provider-independent model interface.
- Testing: Pytest and frontend unit/component tests.
- Deployment: Docker-based development environment.

Technology choices may be revised through documented architecture decisions.

## Documentation

See `docs/` for product requirements, architecture, API contracts, data models, AI design, security and the development roadmap.

## Getting involved

Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes. Security concerns should follow [SECURITY.md](SECURITY.md).

## Project status

Early development. The architecture and specifications are proposed foundations, not claims that all listed functionality has already been implemented.

## Licence

The project licence must be confirmed before publication. A placeholder `LICENSE` file is included; choose a licence such as MIT only after confirming that it matches your intended use.
