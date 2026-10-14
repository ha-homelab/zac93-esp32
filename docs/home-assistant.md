# Connect Z-Wave JS and Home Assistant

[Home](../README.md) · [Firmware](firmware.md) · [Troubleshooting](troubleshooting.md)

You need **one Z-Wave JS driver**, running continuously on a server. This guide uses **Z-Wave JS UI**, which combines that driver with a configuration and diagnostic interface. Its Home Assistant connection is a separate WebSocket server.

![Two different connection URLs](../assets/diagrams/connection-fields.svg)

- **6053:** ESP32 native ESPHome API, used by Z-Wave JS to reach the radio.
- **3000:** Z-Wave JS WebSocket server, used by Home Assistant.
- **8091:** default Z-Wave JS UI web interface for a standalone installation. An HA add-on/app can expose it through the HA sidebar instead.

These are different services. Do not paste the ESP32 URL into the Home Assistant Z-Wave server field. Do not expose these services directly to the public internet.

## 1. Install a single driver

### Home Assistant OS

Install **Z-Wave JS UI** from the Home Assistant Community Apps/add-on repository, then open its web interface. If you cannot find it, use the [upstream installation instructions](https://zwave-js.github.io/zwave-js-ui/#/getting-started/quick-start). Do not start the official Z-Wave JS app/add-on against this same controller at the same time. An existing driver for a *different* controller is a separate case.

### Home Assistant Container or k3s

Run Z-Wave JS UI as a separate persistent service using its [Docker installation guide](https://zwave-js.github.io/zwave-js-ui/#/getting-started/quick-start). The version checked when writing this guide was **11.24.3**. Pin a reviewed version rather than silently tracking `latest`.

Persist the application's `/usr/src/app/store` directory, allow the server to reach the ESP32 on TCP 6053, and let HA reach the server's enabled WebSocket port 3000. A network-attached ESP32 does **not** need a `/dev/ttyUSB*` mount in this container. In Kubernetes, use one active replica with persistent storage; do not allow a rolling update to leave two drivers using the same radio. Protect the UI with authentication and private network access.

The example `ws://zwave-js-ui:3000` works only if that service name resolves and is reachable **from Home Assistant's container/pod**. Across namespaces, use the appropriate service FQDN. On separate machines use the server's private DNS name or IP. `localhost` inside HA normally means HA's own network namespace, not another container or the ESP32.

## 2. Set the native ESPHome serial connection

Reserve the ESP32's address in DHCP, or use a hostname that resolves from the driver host. Run the supplied helper on a trusted terminal:

```sh
python3 scripts/connection_url.py zac93-wroom.local
```

For S3 use `zac93-s3.local`. Enter the API encryption key when prompted. The helper prints a **private** URL in this form:

```text
esphome://zac93-wroom.local:6053?key=ENCODED_API_KEY
```

Paste the whole URL into **Z-Wave JS UI → Settings → Z-Wave → Serial Port**. It is normal that a network URL is entered into a field named Serial Port. Save the configuration. The query parameter is `key`, and Base64 characters `+`, `/` and `=` must be URL encoded. The [Z-Wave JS ESPHome connection documentation](https://github.com/zwave-js/zwave-js/blob/master/docs/usage/esphome-connection.md) defines this transport.

![Reference screenshot: location of Z-Wave JS UI Serial Port field](https://tube0013.github.io/tube_gateways/assets/zwave-js-serial-config.png)

Screenshot: [TubesZB setup guide](https://tube0013.github.io/tube_gateways/getting-started/z-wave/). **This screenshot still displays a legacy `tcp://…:6639` value. It is included only to locate the field. Replace that value with the encrypted `esphome://…:6053?key=…` URL above.** It is not a screenshot of this project or your network.

## 3. Configure the Z-Wave network

For a **new, empty network**, generate security keys using Z-Wave JS UI's key-generation controls. Keep all generated keys in a secure backup. If you are migrating an existing network, preserve its keys and controller backup instead of generating replacements.

Choose **USA/US** for a matching US/CA/MX ZAC93 and North American end devices; wording can vary with the driver version. Confirm the controller identity, firmware, region and Home ID appear and the driver becomes ready before attempting inclusion. Do not guess the firmware version from the order date.

Enable the **WS Server** under the UI's Home Assistant settings, normally on port **3000**. MQTT is not needed for HA's native Z-Wave integration; leave its gateway disabled unless you have a separate reason to use it. The expected end result is one ready driver and one server reachable from HA. Refer to [Z-Wave JS UI documentation](https://zwave-js.github.io/zwave-js-ui/#/homeassistant/homeassistant-official).

## 4. Connect Home Assistant

In **Settings → Devices & services → Add integration**, find **Z-Wave** (called Z-Wave JS in some versions). Choose the custom/existing-server path. Do not ask the wizard to install a second driver.

![Home Assistant Z-Wave setup: Custom installation](https://tube0013.github.io/tube_gateways/assets/zwave-setup-1.png)

Choose **Custom installation**. Screenshot: [TubesZB](https://tube0013.github.io/tube_gateways/getting-started/z-wave/).

![Home Assistant: uncheck the Supervisor add-on option](https://tube0013.github.io/tube_gateways/assets/zwave-setup-2.png)

Uncheck **Use the Z-Wave Supervisor add-on** when you already run Z-Wave JS UI. Screenshot: [TubesZB](https://tube0013.github.io/tube_gateways/getting-started/z-wave/).

![Home Assistant: existing Z-Wave server URL field](https://tube0013.github.io/tube_gateways/assets/zwave-setup-3.png)

Enter the actual server URL in this field. The screenshot's `ws://localhost:3000` is an example, not a universally correct address. For the common HA OS community add-on, the hostname is often `a0d7b954-zwavejsui`; verify yours on the app/add-on information page. A separate container/service might use `ws://zwave-js-ui:3000`. Screenshot: [TubesZB](https://tube0013.github.io/tube_gateways/getting-started/z-wave/).

After submission, HA should display the controller. If the UI has devices but HA does not, diagnose the WebSocket connection before re-including anything. See [Home Assistant's official integration guide](https://www.home-assistant.io/integrations/zwave_js/).

## 5. Add an end device

1. Start **Add device / inclusion** from the Z-Wave integration or Z-Wave JS UI.
2. Put the sensor into inclusion using its own manual. For a battery sensor, use fresh batteries and keep it awake as the manufacturer specifies until the interview completes.
3. If requested, verify the DSK/PIN printed on that device. Do not substitute a code from another device.
4. Confirm its model and exposed values; then trigger a real event and watch HA's state/history.

For a Monoprice P/N 15902 PIR, this is a **Z-Wave** inclusion workflow, not ZHA, Zigbee pairing or Matter commissioning. Do not assume an older PIR supports SmartStart or Long Range. A device that still belongs to a previous network may need the documented exclusion procedure before inclusion; a controller factory reset is not the appropriate fix.

## 6. Add optional bridge diagnostics

Add the ESP32 separately through HA's **ESPHome** integration using its hostname/IP and the **raw** API encryption key from `secrets.yaml` (not the URL-encoded version). This exposes Wi-Fi signal, uptime, ESPHome version and API status. It does not duplicate the Z-Wave sensor entities.

`ESPHome API Connected = on` only means a native API client is connected. **It does not prove that ZAC93 replies over UART or that a PIR's radio reports arrive.** Confirm those in Z-Wave JS and in the real sensor's HA state.
