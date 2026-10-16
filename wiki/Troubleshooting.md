# Troubleshooting and recovery

[Home](Home.md) · [Русский](Troubleshooting-ru.md) · [Connection](Connection.md)

Use the [canonical troubleshooting guide](../docs/troubleshooting.md). Work from the first failing layer, changing one factor at a time:

1. **Power and wiring:** supply stability, common ground, connector orientation and signal labels. Disconnect power before changing wiring.
2. **Network:** the Z-Wave JS host must reach the ESP32; multicast discovery and a ping reply are not API verification.
3. **Encrypted API:** correct key, native transport and URL encoding. Do not paste connection URLs into public issues.
4. **UART and radio:** the controller must be identified by its single driver. Use the documented board configuration, not a pin map inferred from an unrelated photo.
5. **Sensor and HA:** distinguish inclusion/interview/reporting from WS Server and HA entity problems.

![Diagnostic layers](../assets/diagrams/diagnostic-ladder.svg)

Follow [backup and maintenance procedures](../docs/commissioning.md) before updates. Factory reset erases network state and is not a normal remedy for Wi-Fi, key or UART errors. Controller restoration and radio updates through this proxy remain among the [unverified hardware items](../docs/validation.md).

When reporting an issue, include board identity, versions, the first failing layer and redacted observations. Follow [security guidance](../SECURITY.md): no Wi-Fi/API/OTA/Z-Wave keys, DSKs, private addresses, raw backups or compiled personal firmware.
