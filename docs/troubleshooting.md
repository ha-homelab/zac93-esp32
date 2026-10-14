# Troubleshooting and diagnostics

[Home](../README.md) · [HA setup](home-assistant.md) · [Commissioning record](commissioning.md)

![Five diagnostic layers](../assets/diagrams/diagnostic-ladder.svg)

Work down the drawing. A successful earlier layer does not validate later ones. In particular, ping, an ESPHome connection, a lit ZAC93 LED and a ready Z-Wave driver are four different observations.

## 1. No ESP32 boot, repeated resets or brownout

- Disconnect power before touching wiring. Check for a shifted ZAC93 connector, a short and reversed supply/ground.
- Try a known-good short USB cable and adequate power source. A charge-only cable cannot flash firmware.
- Check the 3.3 V rail at the ZAC93, including during startup. A lit LED does not establish a stable supply. Never solve a brownout by feeding 5 V into ZAC93.
- Confirm the exact board/flash configuration. A WROVER or arbitrary S3 clone is not guaranteed to match these examples.
- If the ESP32 works with the ZAC93 disconnected, inspect the added wiring and regulator capacity before reconnecting.

## 2. ESP32 boots but cannot be found

Check the router's DHCP leases and the configured 2.4 GHz SSID/password. Use a DHCP reservation for a stable endpoint. Hostnames ending in `.local` depend on mDNS, which may not cross VLANs or container networks. Test from the **driver's network**, not just a laptop on a different Wi-Fi segment.

Read-only checks below use `192.0.2.10`, a documentation placeholder. Replace it with the actual ESP32 address:

```sh
ping -c 3 192.0.2.10
nc -vz -w 3 192.0.2.10 6053
```

ICMP can be blocked even when the service is reachable. Successful TCP connection proves only that a port is open, not that API authentication or the radio works. `nc` flags vary by platform. Do not send arbitrary text or serial commands into the port.

Check routing, VLAN client isolation and firewall rules. The driver needs TCP 6053 to the ESP32. The HA server needs TCP 3000 to the Z-Wave JS server. Your management browser needs access to the UI; it does not need public internet port forwarding.

## 3. TCP works, but API authentication fails

- Recreate the URL using [connection_url.py](../scripts/connection_url.py). It must start with `esphome://`, use `?key=`, and encode the Base64 key.
- Compare the raw key against the one actually compiled into the ESP32. Editing `secrets.yaml` without installing firmware does not change the device's key.
- Check for a pasted space, newline, or a `+` decoded as a space. Do not paste the full URL in a public bug report.
- Use a current compatible Z-Wave JS / Z-Wave JS UI version with ESPHome transport support. The repository's checked software versions are in the [validation record](validation.md).

To read ESPHome logs using the same local configuration:

```sh
esphome logs firmware/esp32-wroom.yaml --device 192.0.2.10
```

For S3, substitute its YAML. A successful log connection proves the network/API layer. It still does not prove UART communication. Because this project disables serial logging, the absence of application logs on the USB programming port is expected.

## 4. API connects, but Z-Wave JS cannot identify the controller

This commonly points to UART wiring, radio power or a competing driver:

1. Stop any second Z-Wave JS instance. One controller must have one owner.
2. Power off. Confirm **ESP32 TX → ZAC93 RX pin 8** and **ESP32 RX ← ZAC93 TX pin 10**, with shared ground and 3.3 V power.
3. Confirm the physical GPIOs match the selected YAML: WROOM TX17/RX16; S3 TX17/RX18. Do not follow the old reference photo's GPIO1/3 routing.
4. Check for GPIOs occupied by board peripherals/PSRAM. Keep the data wires short and avoid loose breadboard contacts.
5. Keep the supplied UART parameters: **115200 / 8N1**, no RTS/CTS wiring. Do not attach another UART consumer or console to these pins.
6. Restart the bridge and its single driver after correcting the issue. Look for controller identity and successful driver initialization. Exact log wording changes by release.

If more evidence is needed, a **3.3 V-compatible logic analyzer**, used by someone familiar with it, can observe TX/RX without driving them. Traffic from ESP32 with no reply on ZAC93 TX narrows the issue to the module, power or wiring; replies present but rejected suggest framing/transport/firmware issues. Do not connect a 5 V UART transmitter, short TX to ground, or interpret raw binary output as text.

No controller reset is needed to diagnose these transport failures.

## 5. Driver ready, but the sensor does not appear or update

- Verify matching radio regions. The controller being online does not make a different-region end device compatible.
- Confirm inclusion is active and use the device's documented procedure. For a previously paired device, use exclusion as documented, then re-include.
- Wake battery devices for the interview. A sleeping node is not necessarily failed. Repeated interviews while it sleeps will not help.
- Move the test sensor nearer for initial inclusion; later test it in its final location. Classic mesh coverage and Long Range are different modes, with different device requirements.
- Inspect the node's interview status and values in Z-Wave JS UI. Trigger motion and wait for the sensor's configured clear/retrigger interval. Then compare the HA entity state/history.
- If Z-Wave JS sees the event but HA does not, inspect HA's WebSocket integration connection and whether the relevant entity is disabled.

Do not change multiple radio parameters at once. Keep a record of each change and the resulting event timestamps.

## Z-Wave JS UI works, but HA cannot connect

Enable the WS Server and verify TCP 3000 from HA's network. Use the service hostname/IP, not the ESP32 hostname. The UI's HTTP port 8091 is not the WebSocket server port. `localhost` inside a container is usually not the other service. In k3s, check Service selectors, ready endpoints, network policy and that only one driver replica is active.

Read the Home Assistant Z-Wave integration diagnostics and the driver log for the same time interval. Redact credentials before sharing. Do not install a second driver as a connectivity test.

## ZAC93 LED or button seems wrong

LED behavior varies with ZAC93 firmware: Zooz changed it in version 2.10. Compare your actual version with the [vendor change log](https://www.support.getzooz.com/kb/article/1389-zac93-gpio-module-change-log/), not an older photo. The white board button is not a general-purpose inclusion/reset button in this guide. Network inclusion and controller reset are host-software operations; see the [vendor FAQ](https://www.support.getzooz.com/kb/article/1426-zac93-gpio-module-faqs/).

## Information to collect for a useful issue

- Exact ESP32 board/module, flash size, ZAC93 hardware and radio firmware versions.
- The chosen YAML filename, ESPHome version and Z-Wave JS UI/driver versions.
- Clear, powered-off photos of both wire endpoints and connector labels.
- Which of the five layers passes, the first failure, and a short redacted log excerpt.
- Whether the failure changes with a known-good supply/cable or after stopping duplicate drivers.

Keep API keys, Wi-Fi secrets, network keys, DSKs, NVM files and full private connection URLs out of public issues. See [SECURITY.md](../SECURITY.md).
