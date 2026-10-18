# Contributing to OpenProcessAI

Thank you for considering a contribution.

## Before starting

- Read the README and relevant documents in `docs/`.
- For significant changes, open an issue describing the problem and proposed approach before beginning work.
- Avoid introducing dependencies without a clear benefit.
- Never include credentials, customer data, confidential documents or personal data in issues, tests or pull requests.

## Contribution principles

- Keep changes focused and reviewable.
- Add tests for new behaviour and bug fixes.
- Update documentation when behaviour, schemas or APIs change.
- Preserve evidence traceability for process claims.
- Keep AI-provider-specific code behind provider interfaces.
- Do not enable agent execution or external side effects without an explicit design review and human-approval controls.

## Pull requests

A pull request should include:

1. The problem being solved.
2. A summary of the implementation.
3. Tests run and their results.
4. Documentation or migration impacts.
5. Security and privacy considerations.

## Proposed development checks

- Formatting and linting.
- Type checking where applicable.
- Unit and integration tests.
- Schema validation tests.
- Dependency and secret scanning.

These checks should be automated in CI as the codebase develops.
