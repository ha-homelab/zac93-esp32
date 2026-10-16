# Install and maintain ESPHome

[Home](../README.md) · [Hardware](hardware.md) · [Connect to HA](home-assistant.md)

**The target of these steps is the ESP32. Never flash an ESPHome binary to the ZAC93.** The ZAC93 retains the Zooz Serial API firmware.

## Prepare the configuration

Use a Python version supported by the pinned ESPHome release (Python 3.12 is used in CI):

```sh
git clone https://github.com/ha-homelab/zac93-esp32.git
cd zac93-esp32
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
cp firmware/secrets.example.yaml firmware/secrets.yaml
openssl rand -base64 32
```

Edit `firmware/secrets.yaml` locally. Put your 2.4 GHz Wi-Fi name/password in the first two fields, the generated Base64 value in `api_encryption_key`, which also authenticates encrypted OTA. Quote values in YAML. Use your editor's normal escaping if a password contains quote characters.

Keep `secrets.yaml` private. The API/OTA device key and Z-Wave network security keys are **separate kinds of secret**. Firmware binaries contain configuration secrets and should not be uploaded to issues or public releases either.

For an ESPHome Device Builder installation, copy `common.yaml`, the chosen board YAML and your private `secrets.yaml` into its configuration directory. Preserve the relative include, then validate and install the chosen board entry. Do not try to install `common.yaml` on its own.

## Select one board

WROOM:

```sh
esphome config firmware/esp32-wroom.yaml
esphome compile firmware/esp32-wroom.yaml
```

S3:

```sh
esphome config firmware/esp32-s3.yaml
esphome compile firmware/esp32-s3.yaml
```

For an S3 N16R8 module, first change `flash_size: 8MB` to `16MB`. Do not enable PSRAM merely because the module has it. An arbitrary S3 mini board may require a different board definition and GPIO selection.

## First USB installation

Use a USB **data** cable. On the S3 DevKitC-1, its USB-to-UART port is a straightforward initial flashing path. Select the port belonging to this ESP32; disconnect unrelated programmers if identification is ambiguous.

List serial ports:

```sh
python -m serial.tools.list_ports
```

Then install, replacing the example port and choosing the correct YAML:

```sh
esphome run firmware/esp32-wroom.yaml --device /dev/ttyUSB0
```

On macOS the port is commonly `/dev/cu.usbserial-…` or `/dev/cu.usbmodem…`; on Windows it is `COM…`. If automatic bootloader entry fails, use the board's BOOT/RESET procedure from Espressif's guide. Release BOOT after flashing and reset normally. **The ZAC93 can remain disconnected for this first installation.**

After Wi-Fi comes up, stop the log viewer with Ctrl-C. Disconnect USB, attach the ZAC93 as described in [hardware](hardware.md), and restore power.

## Why these settings exist

- `uart`: 115200 baud, 8 data bits, no parity, 1 stop bit; separate GPIOs avoid the usual programming console.
- `zwave_proxy`: native framing and local serial acknowledgements. No third-party stream-server component is required.
- `api.encryption`: encrypts the native API connection; the same key is used by Z-Wave JS.
- `api.reboot_timeout: 0s`: prevents a reboot solely because no API client is connected during setup. This does not disable every other watchdog or Wi-Fi recovery mechanism.
- `logger.baud_rate: 0`: disables serial log output. View application logs over the API. Boot ROM output can still exist on programming interfaces.
- `wifi.power_save_mode: none`: avoids Wi-Fi power-saving latency at the cost of extra power use.
- `ota.encryption: {}`: requires encrypted Noise OTA with the same 32-byte PSK as the API. Plaintext/password-only uploaders are rejected; use the pinned ESPHome CLI. An OTA password is neither needed nor accepted in this profile.

See the official [UART](https://esphome.io/components/uart/), [API](https://esphome.io/components/api/), [Z-Wave proxy](https://esphome.io/components/zwave_proxy/) and [OTA](https://esphome.io/components/ota/esphome/) documentation.

## Logs and later updates

```sh
esphome logs firmware/esp32-wroom.yaml --device zac93-wroom.local
esphome run firmware/esp32-wroom.yaml --device zac93-wroom.local
```

For S3, use `esp32-s3.yaml` and `zac93-s3.local`. A DHCP-reserved IP works if mDNS does not. The `run` command installs firmware and interrupts the bridge; plan updates when temporary loss of Z-Wave control is acceptable. Save the working configuration and Z-Wave backups first. Stop Z-Wave JS for a planned bridge update and restart it afterward.

Normal diagnostic API clients can coexist with the proxy connection, but **only one Z-Wave driver may own the radio stream**. Do not connect two Z-Wave JS instances while troubleshooting.

## Migrating from password-only OTA

This source revision changes OTA policy: `encryption: {}` reuses the API PSK,
requires encrypted transport, and removes the separate OTA-password verifier.
Keep the device's existing API key during this transition and use the pinned
ESPHome CLI. If the installed older firmware cannot negotiate encrypted OTA,
perform this update by USB instead; do not disable the new policy to force a
network upload. Afterward, clients without encryption support cannot update it.
Key rotation changes access to both API and OTA, so keep a private recovery copy
of the current key until the replacement firmware is accepted. USB recovery
remains available. CI compiles this policy but does not establish a live upgrade.
