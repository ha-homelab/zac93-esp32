# Validation record

[Home](../README.md) · [Hardware acceptance checklist](commissioning.md)

## Software checks — 2026-10-14

Both supplied board configurations passed `esphome config` and a full compilation with **ESPHome 2026.9.1 / ESP-IDF**. Disposable credentials were supplied outside the public repository. The compiled YAML source files were compared byte-for-byte with the published files.

- **ESP32-WROOM:** compilation successful; reported static RAM **45,216 / 180,736 bytes**, flash **756,275 / 1,835,008 bytes**.
- **ESP32-S3 N8:** compilation successful; reported static RAM **100,239 / 341,760 bytes**, flash **749,535 / 3,932,160 bytes**.
- The three URL-helper tests passed, covering URL-encoded Base64, IPv6 and rejection of invalid inputs.
- Both configurations also passed through the repository's disposable-credential validation script.
- All six SVG diagrams were rendered in Chromium and visually inspected. Reference photographs and all four external UI screenshots were inspected; differences from this design are captioned.
- The 26 distinct external documentation/image URLs present at the time of inspection returned HTTP 200. This is an availability check, not a guarantee about future pages or every URL fragment.
- Local Markdown target checks and SVG XML parsing passed. The GitHub Actions workflow passed `actionlint`.

Flash/RAM figures describe these builds, not measured runtime consumption or an electrical power budget. Different credentials, compiler releases or configuration changes may change them. CI validates configurations and documentation; it does not perform a hardware test or publish firmware containing credentials.

## Source fingerprints

These identify the YAML used for the initial successful builds:

```text
496365c64e7b36288e72318157f37533b4dc09b886d3dd862835e864e66074c0  firmware/common.yaml
938043be5b1331eef66d83d1a1e95b3bfcd76b261633d0ab603db8c39d74c37b  firmware/esp32-wroom.yaml
2d359e37889ec4846d5f83f26097e73f1c7a6c5375ab8709028f56f7ffd1c8d5  firmware/esp32-s3.yaml
```

## Hardware checks — pending

The ZAC93 was ordered when this guide was prepared. **No physical test of this repository's WROOM or S3 assembly is claimed.** The following remain unverified here:

- Supply headroom and stability on the actual ESP32 board.
- ZAC93 serial initialization through each selected GPIO pair.
- Real inclusion and reports from a Monoprice 15902 or other end device.
- End-to-end operation with the user's Home Assistant installation.
- Radio range, Long Range inclusion, reconnection under Wi-Fi outages and long-term uptime.
- Controller NVM restoration and ZAC93 OTW firmware updates through the proxy.

The wiring design is based on the cited module/board documentation and first-hand reference build, while the transport is supported by ESPHome and Z-Wave JS. Compilation validates software integration, not the physical assembly. Record the actual commissioning outcome using the [checklist](commissioning.md).
