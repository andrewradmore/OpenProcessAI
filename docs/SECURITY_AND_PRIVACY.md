# Security and Privacy Requirements

## 1. Data classification

Uploaded business documents may contain confidential information, personal data, trade secrets or regulated data. Treat source material as sensitive unless the deployment owner has established otherwise.

## 2. Access control

- Require authentication for private projects.
- Enforce project-level authorisation on every read and write.
- Prevent identifiers from being used to access another user's resources.
- Use least privilege for application services and future integrations.
- Do not rely on frontend checks as the sole security control.

## 3. File handling

- Enforce file size and type limits.
- Validate file content rather than trusting filename extensions alone.
- Store uploads outside public web roots.
- Generate internal storage identifiers.
- Consider malware scanning for production deployments.
- Avoid processing macros or active content.
- Apply resource limits to parsers.

## 4. AI provider data handling

Before enabling an external model provider, document what data is sent, the provider's retention and training terms, regional processing options, and any contractual requirements. Provide configuration to disable external model calls where possible.

Do not send more source content than required for the task. Redact or minimise personal data when feasible.

## 5. Secrets and configuration

- Keep credentials in environment variables or a managed secret store.
- Commit only safe `.env.example` files.
- Rotate exposed credentials immediately.
- Never log access tokens, API keys or full sensitive prompts.

## 6. Audit and retention

Record security-relevant actions, approval decisions and material changes. Minimise payload content in logs. Define retention, deletion, export and backup behaviour before production deployment.

## 7. Agent safety

The MVP must not execute generated agents. If execution is introduced later, require:
- Explicit allowlisted tools and operations.
- Scoped credentials and least privilege.
- Human confirmation for consequential actions.
- Rate limits, budgets and timeouts.
- Idempotency and rollback strategy where possible.
- Monitoring, audit and emergency disable controls.
- Threat modelling and security review.

## 8. Compliance

This document is an engineering baseline, not a claim of legal or regulatory compliance. Deployment owners must assess applicable privacy, data protection, records management and sector-specific obligations.
