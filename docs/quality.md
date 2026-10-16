# Quality and security evidence

The Check workflow runs unit tests, Ruff, documentation checks and ESPHome compilation for both supported boards using disposable synthetic secrets. The pinned ESPHome validator also rejects a short API key and an incompatible password/encryption combination. Git history is scanned with Gitleaks. [Validation evidence](validation.md) distinguishes actual compiler results from still-required physical commissioning.

Failures and substantive review findings must be resolved before merge. Automated results are bounded evidence, not proof that every defect is absent. No full-function coverage percentage, complete secure-design assurance case or independent maintenance continuity is claimed.

The primary maintainer personally confirmed knowledge of secure-design principles and common Python/network vulnerabilities. The maintainer also confirms no bug, enhancement or vulnerability reports outside GitHub in the preceding 12 months. These are human attestations, not test results; public issue history and current security findings must also be checked when refreshing the assessment.

See [governance](../GOVERNANCE.md), [conduct](../CODE_OF_CONDUCT.md), [roadmap](../ROADMAP.md) and [security policy](../SECURITY.md).

The [compiler dependency assessment](compiler-dependency-assessment.md) records known Starlette advisories in the pinned build environment. Its conclusion applies to Python 3.12 command-line config/compile/serial-upload usage, not PlatformIO Home or ESPHome dashboard.
