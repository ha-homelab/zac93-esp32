# Security and private diagnostics

Do not publish real `secrets.yaml` files, compiled firmware, full private connection URLs, Wi-Fi credentials, API/OTA keys, Z-Wave network keys, device DSKs or NVM/controller backups. Public examples use placeholders and documentation addresses.

Install [Gitleaks](https://github.com/gitleaks/gitleaks) and enable the tracked local hooks after cloning:

```sh
git config core.hooksPath .githooks
```

The pre-commit hook checks staged blobs; the pre-push hook scans Git history. Both redact detected values. CI repeats the file policy and a full-history Gitleaks scan, including custom ESPHome API-key and connection-URL patterns. GitHub secret scanning and push protection are also enabled. `.gitignore` alone is not a security boundary: forced or already-tracked files can bypass it, so the publication check rejects them independently.

Hooks are local and must be enabled in each clone. CI runs after a branch has reached GitHub, so keep the pre-push check enabled. These controls reduce accidental disclosure; no scanner recognizes every possible secret. Review staged changes and keep private operating data outside this repository.

Run the native API, driver and management UI on a trusted private network. Do not forward ports 6053, 3000 or 8091 from the internet. Protect the management UI and backups. An encrypted ESPHome API connection does not automatically secure every other management service.

Report a suspected vulnerability using the repository's private vulnerability reporting option if enabled. If it is unavailable, open an issue requesting a private contact **without including exploit details or credentials**. Rotate any accidentally disclosed key and remove the affected public material; deleting a file from the latest commit alone does not erase its history.
