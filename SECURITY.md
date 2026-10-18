# Security Policy

## Scope

OpenProcessAI processes business documents and may generate proposed automation designs. Security issues can expose confidential business information or create unsafe automation recommendations.

## Reporting a vulnerability

Do not publish exploitable details, credentials, customer data or proof-of-concept material containing sensitive information in a public issue. Until a private reporting channel is configured, contact the repository owner through a verified private channel and share only the minimum information needed to reproduce the issue.

## Security expectations

- Treat uploaded documents and extracted text as untrusted input.
- Enforce authentication and project-level authorisation on every protected operation.
- Validate file type, size and content before processing.
- Keep secrets out of source control, logs and examples.
- Use least-privilege access for services and integrations.
- Do not allow document content to override system or application policies.
- Require human approval before any future agent can perform consequential actions.
- Log security-relevant events while minimising sensitive payloads.
- Pin and review dependencies; apply security updates promptly.

## Current status

This document describes intended practices. Controls must be implemented and tested before the application is considered production-ready.
