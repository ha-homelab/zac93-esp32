# Security and private diagnostics

Do not publish real `secrets.yaml` files, compiled firmware, full private connection URLs, Wi-Fi credentials, API/OTA keys, Z-Wave network keys, device DSKs or NVM/controller backups. Public examples use placeholders and documentation addresses.

Run the native API, driver and management UI on a trusted private network. Do not forward ports 6053, 3000 or 8091 from the internet. Protect the management UI and backups. An encrypted ESPHome API connection does not automatically secure every other management service.

Report a suspected vulnerability using the repository's private vulnerability reporting option if enabled. If it is unavailable, open an issue requesting a private contact **without including exploit details or credentials**. Rotate any accidentally disclosed key and remove the affected public material; deleting a file from the latest commit alone does not erase its history.
