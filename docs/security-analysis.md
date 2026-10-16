# Security-analysis scope

CodeQL and repository secret scans remain enabled. Two narrowly reviewed data
flows require context when interpreting a generic sensitive-data rule:

- `validate_configs.py` creates fresh random values solely as disposable compiler
  inputs. They do not authenticate any real device. The file is mode 0600 inside
  a mode-0700 temporary directory, removed when validation ends; failure output
  redacts even these synthetic values. This is not storage of a user's password.
- `connection_url.py` is an explicit private URL formatter. It reads the user's
  API key through `getpass`, then emits exactly a warning and the requested
  credential-bearing URL for private configuration. It has no application/event
  log, telemetry or network request. The CLI regression checks this exact output
  contract. Do not invoke it in recorded terminals, paste its output into issues,
  or place the resulting URL into public logs.

These rationales apply only to these exact flows. They do not exempt general
password storage, logging, compiler output or other future call sites.
