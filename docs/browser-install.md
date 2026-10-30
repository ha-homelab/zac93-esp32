# Install from your browser

**[Open the USB installer](https://ha-homelab.github.io/zac93-esp32/).**
A desktop browser and a USB data cable are enough for the first installation.
There is no Python, PlatformIO or command-line flasher to install on your computer.
The installer downloads the selected release image and writes it directly to the ESP32.

The public image is **onboarding firmware**, not a working Z-Wave controller.
It configures Wi-Fi over USB and announces the board to ESPHome Device Builder.
Finish the encrypted application installation below before connecting the ZAC93.
This separation lets everyone use the same public download without distributing
Wi-Fi passwords, a shared API encryption key, or an unprotected Z-Wave bridge.

## Choose the physical board

- **WROOM:** an ESP32 DevKit with ESP32-WROOM-32/32D/32E and **4 MB flash**.
  The application uses TX GPIO17 and RX GPIO16. WROVER is not this profile.
- **S3:** an ESP32-S3-DevKitC-1 **N8, 8 MB flash**. Use its **USB-to-UART**
  connector for installation and Wi-Fi setup. The application uses TX GPIO17
  and RX GPIO18. N16, mini boards and alternate pinouts need a custom build.

The browser can identify the ESP chip family, but it cannot identify every
board, flash capacity or external wire. Check the module marking first.
**The target is the ESP32, never the Zooz ZAC93.** Keep the ZAC93 disconnected
through setup; its firmware and Z-Wave network are not part of this installer.

## Install and join Wi-Fi

1. Connect the ESP32 to the computer with a known USB **data** cable.
2. Open the installer in current desktop Chrome or Edge on Windows, macOS or
   Linux. Other browsers work only if they provide Web Serial; an unsupported
   browser shows an explanation instead of a functioning Connect button.
   iPhone/iPad browsers do not provide this USB installation path.
3. Verify the displayed release version and channel, select the exact board
   profile, then choose **Connect**.
   In the browser's permission dialog select only this board's serial port.
4. Choose **Install**. Read the erase warning: reinstalling can remove settings
   on that ESP32. Do not use this onboarding image as an update for a working
   controller unless you intend to replace its configuration.
5. Once installation completes, reset the board if prompted. Select your
   **2.4 GHz Wi-Fi** in the installer's Improv setup dialog. The credentials go
   to this board over the granted serial connection; they are not stored in
   this repository or compiled into the shared release image.
6. Close the installer's serial connection before another program opens it.

## Finish secure setup

1. In Home Assistant, open **ESPHome Device Builder**. The newly provisioned
   `zac93-wroom-…` or `zac93-s3-…` board should appear as a discovered device.
   Choose **Adopt/Take control**. The exact label can vary with Device Builder.
   Its import points to the matching release's application template.
2. Open the imported YAML and ensure it has a unique `api.encryption.key`
   for this device, together with your private Wi-Fi configuration. Do not
   assume adoption generated a key: ESPHome's importer can leave it unset.
   If it is absent, use **Copy/Regenerate** in the
   [ESPHome API guide](https://esphome.io/components/api/#configuration-variables)
   to generate a new 32-byte Base64 key in your browser, then add it to the
   imported YAML in Device Builder:

   ```yaml
   api:
     encryption:
       key: "PASTE_NEW_PER_DEVICE_KEY_HERE"
   ```

   Replace the placeholder with that new key; never reuse another board's key.
   The application template deliberately fails validation until a valid key
   overrides its placeholder. It uses the same key for encrypted ESPHome OTA.
   Validate the configuration before proceeding and keep the key private.
3. Choose **Install → Manual download → Factory format** (called **Modern format**
   in older versions; the complete factory
   image), then open [ESPHome Web](https://web.esphome.io/), connect to this
   board, choose **Install**, and select that downloaded `.factory.bin`.
   This second installation also happens in the browser. Device Builder does
   the compile; no local compiler or terminal is needed. The onboarding image
   deliberately has no OTA endpoint, so its first replacement is over USB.
4. Store the generated YAML/API key and downloaded image privately. This new
   image contains your configuration and must not be uploaded to a public
   release or issue. Disconnect USB before attaching the ZAC93 using the
   [wiring guide](hardware.md).
5. Restore power and follow [Z-Wave JS and Home Assistant setup](home-assistant.md).
   Confirm the encrypted connection and a live Z-Wave device response. A
   successful browser flash alone does not prove radio operation.

If discovery does not appear, wait for Wi-Fi to connect and check that Device
Builder can reach the same network. A release's source archive also contains
`firmware/esp32-wroom.yaml`, `firmware/esp32-s3.yaml`, `firmware/common.yaml` and
`firmware/radio.yaml`
for the [manual configuration path](firmware.md). Those files are an alternative,
not additional prerequisites for the browser route.

## Later updates

Update the adopted application in Device Builder using encrypted OTA; preserve
its name and API key. Stop Z-Wave JS for planned bridge maintenance, keep a
private network backup, and restart it after the bridge reconnects. Do not
reinstall the public onboarding image over an operational bridge merely to
obtain a newer release. The Zooz radio remains a separate update target.

## Troubleshooting

- **No Connect button:** use the HTTPS installer in a Web Serial capable desktop
  browser, outside an embedded preview. The browser feature check is authoritative.
- **No serial port:** use a data cable, another USB port, and the board maker's
  CP210x/CH340 driver if required. Linux may require membership in the serial
  device's group; log out/in after changing it. Do not run the browser as root.
- **Port busy:** close Device Builder logs, Arduino/PlatformIO monitors, other
  browser tabs and serial programs before reconnecting.
- **Connecting never completes:** hold **BOOT**, press/release **RESET/EN**,
  then release BOOT once connection begins. Follow the board's own bootloader
  instructions if its controls differ. Never short guessed pins.
- **Flash succeeds but Wi-Fi setup is absent:** reset normally, reconnect and
  use the same USB-to-UART port. The S3 native-USB connector is not the serial
  port used by this onboarding profile.
- **Wi-Fi fails:** use a 2.4 GHz network, verify the password, and avoid an
  enterprise network or captive portal. Improv can reconfigure Wi-Fi without
  erasing the board.
- **Wrong chip or profile:** stop and select the matching physical board.
  Do not override the chip mismatch or change the offset. Published factory
  images are complete merged images written at `0x0`; OTA/application-only
  images are not interchangeable with them.
- **Encrypted application will not connect:** verify its unique API key in
  Z-Wave JS and confirm the application, rather than onboarding firmware, is
  installed. Use [layered troubleshooting](troubleshooting.md).

## What a release contains

Browser firmware releases supply `zac93-wroom.factory.bin` and `zac93-s3.factory.bin`,
`SHA256SUMS`, `firmware-metadata.json` and the installer catalog. These are built
only from `firmware/factory/`; the build rejects secret references, OTA endpoints
and Z-Wave components there. CI checks both factory configurations and the
adopted application templates. Physical USB and Z-Wave acceptance remain a
separate [commissioning check](commissioning.md).

The installer is generated by the shared
[Venus OS CI Toolkit](https://github.com/victron-venus/venus-os-ci-toolkit)
using [ESP Web Tools](https://esphome.github.io/esp-web-tools/).

## Firmware source and licenses

Every published browser firmware release includes `firmware-sources.tar.gz`,
`FIRMWARE-SOURCES.md`, build metadata and SHA-256 checksums. The archive carries
the public configuration, build scripts, matching ESPHome package, license
notices and generated factory source. ESPHome runtime code retains GPLv3 and
its Python tooling retains MIT; ESP-IDF components retain their own licenses.
Only the temporary public factory builds enter this archive. Personal Device
Builder YAML, keys and application binaries must remain private.

## Maintainer: publish a browser firmware release

1. Merge the firmware changes and wait for the full **Check** and **Browser
   firmware** workflows to pass. The latter compiles both application profiles,
   builds both public factory images, and runs the shared installer validator
   before any release asset can be uploaded. It checks chip IDs, flash layout,
   catalog paths and hashes against the exact same firmware input directory.
2. Create a published, non-draft GitHub release whose tag points to that reviewed
   source. Use a prerelease for `beta`, `rc` or `nightly`; use a regular release
   for `stable`. An older source-only tag without the browser firmware files
   cannot be used. GitHub Pages must already be configured for Actions.
3. Run **Actions → Browser firmware → Run workflow** from the default branch.
   Enter the existing `tag` and matching `channel`. Leave `publish` and `deploy`
   off for a rehearsal, then inspect the workflow's installer artifact. These
   switches are off by default; a beta cannot automatically replace the public
   installer.
4. To publish that reviewed release, dispatch again with `publish: true` and
   `deploy: true`. The workflow rebuilds and validates the tagged source,
   attaches firmware/source/license/checksum assets, and publishes the page.
   Enabling `deploy` requires `publish`; merely creating a GitHub release does
   not run this workflow.
5. Verify the live page's version, channel and both board profiles, its manifest
   and binary URLs, and the release asset checksums. A successful build or page
   deployment does not replace a physical board acceptance test.

Release assets are immutable: the upload intentionally does not use
`--clobber`. If an asset already exists or publication was only partially
successful, inspect the failed run and the existing release before retrying;
do not overwrite previously published firmware. Changed firmware needs a new
release tag. The visible page contains one explicitly published channel at a
time, so replacing a stable page with a prerelease must be a deliberate choice.
