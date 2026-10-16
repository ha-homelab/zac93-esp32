# Device security profile

The supplied firmware requires a 32-byte random PSK for both the ESPHome native
API and OTA. Generate it with `openssl rand -base64 32`; do not invent a human
password or publish the resulting firmware. `ota.encryption: {}` requires Noise
transport and rejects uploaders without encryption support. It reuses the API
PSK; there is no project-managed user-password verifier. Wi-Fi credentials are
recoverable outbound credentials and Z-Wave network keys are separately managed
by the user's controller.

The pinned ESPHome implementation uses its published Noise protocol and FLOSS
crypto implementation. Key lengths and primitives come from ESPHome; this
repository does not implement a replacement cipher. Config validation and full
builds use disposable random keys. These prove source compatibility, not
physical commissioning or resistance to extraction from an unprotected device.
See [firmware maintenance](firmware.md) for upgrade and recovery.
