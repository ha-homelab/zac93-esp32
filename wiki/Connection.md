# Connection and first inclusion

[Home](https://github.com/ha-homelab/zac93-esp32/wiki/Home) · [Русский](https://github.com/ha-homelab/zac93-esp32/wiki/Connection-ru) · [Troubleshooting](https://github.com/ha-homelab/zac93-esp32/wiki/Troubleshooting)

Follow the detailed [hardware guide](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md), including the labelled reference photographs. Select WROOM or S3 explicitly. Disconnect power before connecting wires, verify signal names and 3.3-V supply/logic, and use that board's existing YAML. This page does not introduce another pin map.

1. [Install ESPHome on the ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). Keep the ZAC93 firmware intact and retain local secrets privately.
2. [Connect Z-Wave JS UI to the native ESPHome proxy, then HA to its WS Server](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). These are two separate connections; the ESP32's API port is not HA's Z-Wave server port. Keep exactly one Z-Wave driver responsible for the controller.
3. [Include and observe the actual sensor](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Follow the sensor's own inclusion procedure and complete its interview. API connectivity alone does not confirm this step.
4. Record software versions, real reports and remaining gaps in a private commissioning record. Preserve NVM and network keys before migration or updates.

The HA guide contains attributed external reference screenshots; it is not a screenshot record of a physically commissioned build here. Read the [validation status](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) for the distinction.
