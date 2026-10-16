# Source change notes

Each source snapshot is identified by its full Git commit. ESPHome is pinned
separately in requirements.txt; these notes do not assign a version to Zooz
firmware or claim hardware validation.

## Development changes

- Require encrypted OTA using the API device PSK and reject password-only uploaders. Keep the existing key for migration; use the pinned CLI or USB recovery.

- Continuously compile both WROOM and S3 firmware configurations using disposable
  credentials, in addition to configuration validation and documentation tests.
- Check Python scripts and tests with Ruff error rules.
- Require automated tests and full firmware builds for relevant changes and
  document a concrete private security reporting and response process.

## Initial documented source, 2026-10-14

- Publish WROOM and S3 ESPHome Z-Wave proxy configurations and wiring guidance.
- Provide a connection-URL helper, synthetic tests and commissioning checklist.
- Record successful software builds with source hashes; physical commissioning
  remains pending as documented in docs/validation.md.
