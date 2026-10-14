# Hardware and wiring

[Home](../README.md) · [Firmware](firmware.md) · [Русский](guide-ru.md)

## Know which board you have

**WROOM reference:** an ESP32 DevKit fitted with ESP32-WROOM-32, 32D or 32E. The configuration uses GPIO17 for TX and GPIO16 for RX. These GPIOs are available on WROOM boards, but can be occupied by PSRAM on WROVER modules. Do not apply this pin map unchanged to WROVER. Refer to [Espressif's DevKitC guide](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html).

**S3 reference:** ESP32-S3-DevKitC-1 with N8/8 MB flash. GPIO17 is TX and GPIO18 is RX. For a different module, verify flash size and the board schematic before compiling; an N16R8 module needs a 16 MB flash setting. This application does not require PSRAM. Pins used by flash, PSRAM and native USB differ from classic ESP32. See [Espressif's S3-DevKitC-1 guide](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/user_guide_v1.1.html).

An ESP32 inside an existing AiDot device is not automatically equivalent to either development board: its power supply, exposed GPIOs and attached peripherals need a separate assessment.

## Identify the ZAC93 connector

![Logical ZAC93 pin map](../assets/diagrams/zac93-header.svg)

Numbering follows positions 1–10 of the compatible Raspberry Pi header. **This drawing is a signal map, not a view into the connector.** Turning the board over mirrors its apparent pin arrangement. Locate the actual `3V3`, `GND`, `RX` and `TX` markings before attaching wires. If the shipped board differs, stop and compare its documentation.

- Pin **1: 3V3**, the supply used here.
- Pin **6: GND**, the common ground used here. Pin 9 is also ground.
- Pin **8: RX**, the ZAC93 receive input; connect the ESP32 transmit output.
- Pin **10: TX**, the ZAC93 transmit output; connect the ESP32 receive input.
- Pins 2/4 are NC on the illustrated board; pins 3/5 are not used. Pin 7 is also unused by this design. Hardware v2 connects pin 7 to reset; older boards label it `PC01`. See the [Zooz hardware change log](https://www.support.getzooz.com/kb/article/1389-zac93-gpio-module-change-log/).

Some Raspberry Pi-oriented descriptions mention occupying the header's 5 V positions. That does **not** make 5 V a valid supply for this four-wire build. The [ZAC93 manual](https://www.getzooz.com/downloads/zooz-z-wave-800-series-long-range-gpio-module-zac93-LR-manual.pdf) specifies **3.3 V DC**.

### Real reference photographs

![ZAC93 underside with four wires and readable connector labels, by peterxian](https://community-assets.home-assistant.io/optimized/4X/8/0/3/803c7819cdbad99d5db946a631280949a75ac045_2_467x375.jpeg)

ZAC93 connector and four wires. Photo: **peterxian**, [original Home Assistant Community build, 2023](https://community.home-assistant.io/t/make-a-z-wave-to-wifi-bridge-with-esphome-stream-server-and-zooz-zac93-gpio/565913). This older board illustrates the signal labels; check your hardware revision.

![ESP32 side of the original four-wire build, by peterxian](https://community-assets.home-assistant.io/optimized/4X/8/c/f/8cff37fcc8c093b92ceba94e8199f4bb227f9501_2_370x500.jpeg)

ESP32 side of the same reference build. **Its UART0 GPIO1/3 wiring differs from our GPIO17/16 or GPIO17/18 wiring.** Use the drawings below for this repository's firmware. Wire colours in someone else's build are not pin identifiers. The original article also uses older raw TCP software; follow our native-proxy instructions instead.

![Zooz ZAC93 top side, showing its onboard antenna](https://hf-files-oregon.s3.amazonaws.com/hdpthesmartesthouse_kb_attachments/2023/04-25/0df30d1f-1f80-4f55-816c-acc0e0334ee6/image-20230425121602-1.png)

Product photograph: **Zooz**, [ZAC93 FAQ](https://www.support.getzooz.com/kb/article/1426-zac93-gpio-module-faqs/). The PCB antenna is already present. Keep it clear of metal and tightly bundled wiring. No antenna soldering is needed for the reference build.

## Variant A: ESP32-WROOM

![WROOM electrical wiring](../assets/diagrams/wiring-wroom.svg)

Connect 3V3 → pin 1; GND → pin 6; GPIO17 → pin 8; GPIO16 ← pin 10. Use [esp32-wroom.yaml](../firmware/esp32-wroom.yaml). `TX` and `RX` in this guide are always named from the local device's point of view, hence TX connects to RX.

## Variant B: ESP32-S3

![S3 electrical wiring](../assets/diagrams/wiring-s3.svg)

Connect 3V3 → pin 1; GND → pin 6; GPIO17 → pin 8; GPIO18 ← pin 10. Use [esp32-s3.yaml](../firmware/esp32-s3.yaml). Follow **GPIO numbers**, not the header's physical position or a label such as `D17` on an unrelated board.

## Assembly sequence

1. Read the module markings and select the correct configuration. Initially connect **only the ESP32** to USB and [install its firmware](firmware.md).
2. Unplug USB and all other power. Fit the four wires and check every endpoint against the diagram. Leave ZAC93 reset and all unused pins disconnected.
3. Inspect for reversed connectors, loose strands and shorts. With power off, use continuity mode if needed; never use continuity mode on a powered circuit.
4. Power the ESP32 through its USB connector. The ESP32 board's regulator supplies the ZAC93 from 3V3. Confirm the chosen regulator can support the additional load; an unspecified clone's regulator capacity is not guaranteed.
5. Carefully measure about 3.3 V between the ZAC93 supply and ground. Avoid bridging adjacent pins with a probe. Unplug immediately if a component becomes abnormally hot or the supply is wrong.
6. Secure both boards on an insulating mount with strain relief. Leave antenna areas exposed inside a nonmetallic enclosure. Continue with [Home Assistant setup](home-assistant.md).

Use one power source. Do not simultaneously drive the board's 3V3 pin from another supply while USB also powers it. If power is inadequate, redesign the supply deliberately with a common ground and no regulator backfeed. The [Espressif board guide](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html) describes its mutually exclusive power options.
