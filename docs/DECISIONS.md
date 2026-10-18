# Architecture Decision Records

Record significant technical and product decisions here. For each decision include context, options considered, decision, consequences and date.

## ADR-001: Start with a modular monolith

**Status:** Proposed

**Context:** The MVP needs a small, testable architecture and does not yet have evidence that separate services are necessary.

**Decision:** Use a modular monolith with explicit domain boundaries.

**Consequences:** Simpler local development and deployment; modules must remain well separated to avoid a tightly coupled codebase.

## ADR-002: Keep agent execution out of the MVP

**Status:** Proposed

**Context:** Generated agents may create external side effects and require permission, monitoring and recovery controls.

**Decision:** The MVP generates and reviews specifications only. Approval does not execute an agent.

**Consequences:** Reduced initial capability but a safer development path and clearer acceptance criteria.

## ADR-003: Require evidence links for material process claims

**Status:** Proposed

**Context:** Users need to distinguish source-backed facts from model inference.

**Decision:** Store evidence references with process elements and automation opportunities; explicitly label unsupported assumptions.

**Consequences:** Additional schema and validation work, offset by greater reviewability and trust.

## Template for future decisions

### ADR-NNN: Short title

- **Status:** Proposed | Accepted | Superseded
- **Date:** YYYY-MM-DD
- **Context:**
- **Options considered:**
- **Decision:**
- **Consequences:**
