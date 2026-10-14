# Commissioning, backups and maintenance

[Home](../README.md) · [Diagnostics](troubleshooting.md) · [Validation evidence](validation.md)

This is an **uncompleted commissioning checklist**, not a report of hardware tests. Fill it in after the ordered module arrives. Keep private addresses and keys in a private record.

## First installation

- [ ] Record the ESP32 module marking, flash size and board revision.
- [ ] Record the ZAC93 region, hardware revision and observed radio firmware.
- [ ] Photograph both wire endpoints while powered off; check connector orientation.
- [ ] Confirm 3.3 V at ZAC93 and a shared ground.
- [ ] Confirm stable ESP32 boot and address from the driver host.
- [ ] Confirm native API authentication using the configured key.
- [ ] Confirm Z-Wave JS reads controller identity, firmware, Home ID and region.
- [ ] Confirm exactly one driver owns the controller.
- [ ] Include one test sensor and complete its interview.
- [ ] Observe a real sensor event in Z-Wave JS and then in HA.
- [ ] Test the battery sensor again after it sleeps and wakes.
- [ ] Test in the intended final location before relying on an automation.
- [ ] Restart the bridge once; verify the existing network and entities reconnect without re-pairing.
- [ ] Save controller and application backups; document where they are stored privately.

For any test that does not pass, record the observation rather than marking the whole assembly as working.

## What to back up

Save **both** the controller's NVM backup and the Z-Wave JS UI persistent store/settings, including its security keys. Save the ESPHome YAML plus a private copy of `secrets.yaml` separately. A Home Assistant backup is useful too, but verify whether it actually contains the external driver's store. A k3s service's PVC is not automatically included in an HA backup.

Use Z-Wave JS UI's NVM backup controls where supported and its application backup/export features. Store copies encrypted and outside the host. Treat NVM, key exports and DSK information as private; do not attach them to this public repository. Restore compatibility depends on controller/SDK versions: follow the current [Z-Wave JS UI backup and restore documentation](https://zwave-js.github.io/zwave-js-ui/#/usage/backup) before a restore. Do not test a restore casually on a working network.

## Update two firmware domains separately

**ESP32:** compile the selected YAML, retain working settings, and install via ESPHome USB/OTA. Plan for a bridge interruption. This updates the network proxy, not the ZAC93 radio firmware.

**ZAC93:** use only the appropriate Zooz OTW firmware and the vendor's procedure for that hardware/region. Back up first and provide stable power throughout. As checked on **2026-10-14**, Zooz's [change log](https://www.support.getzooz.com/kb/article/1389-zac93-gpio-module-change-log/) lists **2.30 / SDK 7.24.2**. That is a reference version, not a claim about the shipped module. The log documents a version-number/product-type correction in 2.20 after 2.10; follow Zooz's recovery/update guidance if an update rejects an older image/version instead of forcing an unrelated binary.

Do not assume the ESPHome proxy path supports every controller bootloader/OTW workflow. Verify current tool and transport support; if necessary use Zooz's documented direct connection for maintenance. This project has **not** tested radio firmware updates over the proxy.

## Reset is not restart

Restarting the ESP32 or driver should preserve the Z-Wave network. A **controller factory reset erases that network's controller state** and can require recovery or re-inclusion. It is not a remedy for a wrong API key, wrong port, crossed UART wiring or a sleeping battery sensor. Perform one only as an intentional network replacement with a recovery plan.

## Operational limitations

This assembly depends on ESP32 power, Wi-Fi, routing, a running Z-Wave JS server and HA. It adds a network dependency compared with a local USB controller. Keep the reference bridge focused on Z-Wave before adding Bluetooth scanning or other high-load tasks. No uptime, RF range, LR behavior, power budget or failure-recovery guarantee is implied by a successful compile.
