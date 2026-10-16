# ZAC93 + ESP32 → Home Assistant

[English](README.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Fuentes de la wiki](wiki/Home.md)

Guía ilustrada para construir un controlador Z-Wave local con **Zooz ZAC93**, **ESP32-WROOM o ESP32-S3**, el proxy Z-Wave nativo de ESPHome y un servidor Z-Wave JS.

**Estado de verificación:** el hardware está pedido y la puesta en servicio física está pendiente. Las pruebas de software no demuestran todavía la alimentación, el alcance ni la inclusión de dispositivos. El [registro de validación](docs/validation.md) distingue lo comprobado de lo pendiente. Esta guía de entrada en español complementa las referencias detalladas en inglés y la [guía rusa](docs/guide-ru.md).

![Arquitectura del sistema](assets/diagrams/architecture.svg)

El ESP32 aporta la conexión de red. El ZAC93 aporta la radio Z-Wave y conserva su firmware Zooz. Home Assistant se conecta al servidor Z-Wave JS. Añadir el ESP32 a la integración ESPHome por separado no incorpora por sí solo los dispositivos Z-Wave.

## Material y conexiones

Para dispositivos norteamericanos, elegir el [ZAC93 US/CA/MX](https://www.thesmartesthouse.com/products/zooz-800-series-z-wave-long-range-gpio-module-zac93-lr). Las regiones del controlador y del dispositivo deben coincidir. La antena está integrada; no hace falta una externa. Un sensor Z-Wave Plus antiguo no adquiere Long Range por usar este controlador. El precio fechado del README inglés es histórico, no una oferta actual.

También hacen falta una placa ESP32 adecuada, cuatro cables cortos aislados, cable USB de datos, alimentación USB suficiente y soporte o caja no conductores. Los diseños de referencia son **ESP32-WROOM-32/32D/32E** y **ESP32-S3-DevKitC-1 N8**. Para otras placas hay que comprobar su esquema y capacidad flash.

Estas son las cuatro conexiones del diseño **WROOM**:

- ESP32 **3V3 → contacto 1 del ZAC93, 3V3**.
- ESP32 **GND → contacto 6 del ZAC93, GND**.
- ESP32 **GPIO17 / TX → contacto 8 del ZAC93 / RX**.
- ESP32 **GPIO16 / RX ← contacto 10 del ZAC93 / TX**.

En el diseño **S3**, solo cambia la entrada RX del ESP32 a **GPIO18**. Usar el archivo correspondiente: [WROOM](firmware/esp32-wroom.yaml) o [S3](firmware/esp32-s3.yaml). No trasladar automáticamente el esquema WROOM a un WROVER: GPIO16/17 pueden estar ocupados por PSRAM.

![Conexiones WROOM](assets/diagrams/wiring-wroom.svg)

![Conexiones S3](assets/diagrams/wiring-s3.svg)

**La alimentación y los niveles UART del ZAC93 son de 3,3 V. No conectarlo a 5 V ni a VIN.** Desconectar el USB antes de cablear. Los dibujos son mapas eléctricos, no plantillas de orientación mecánica válidas para cualquier placa. Comprobar las marcas y las [fotografías de referencia comentadas](docs/hardware.md): al girar la placa, la disposición se ve invertida. Dejar libres los contactos no utilizados y no aplicar una segunda alimentación simultánea a 3V3.

## Preparar el ESP32

ESPHome se instala en el **ESP32**, nunca en el ZAC93. La configuración usa **ESPHome 2026.9.1**, fijado en [requirements.txt](requirements.txt). La CI usa Python 3.12.

```sh
git clone https://github.com/ha-homelab/zac93-esp32.git
cd zac93-esp32
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
cp firmware/secrets.example.yaml firmware/secrets.yaml
openssl rand -base64 32
openssl rand -hex 24
```

Editar `firmware/secrets.yaml` con los datos de la red Wi-Fi de 2,4 GHz, el valor Base64 generado en `api_encryption_key` y la segunda contraseña aleatoria en `ota_password`. No publicar este archivo ni los binarios compilados. La clave API, la contraseña OTA y las claves de seguridad de la red Z-Wave cumplen funciones distintas.

Para WROOM, validar, compilar e identificar el puerto real:

```sh
esphome config firmware/esp32-wroom.yaml
esphome compile firmware/esp32-wroom.yaml
python -m serial.tools.list_ports
esphome run firmware/esp32-wroom.yaml --device /dev/ttyUSB0
```

Sustituir `/dev/ttyUSB0` por el puerto de la placa. Para S3 usar `esp32-s3.yaml` en esos comandos. El diseño S3 de referencia tiene 8 MB flash; identificar otra variante antes de cambiar ese valor. El ZAC93 puede permanecer desconectado durante la primera instalación. Después, quitar USB, conectar los cuatro cables y volver a alimentar. La [guía de firmware](docs/firmware.md) explica BOOT/RESET, Device Builder y OTA.

## Conectar Home Assistant

1. **Preparar un servidor Z-Wave JS.** Z-Wave JS UI ofrece la interfaz de configuración. En HA OS puede funcionar como aplicación/add-on comunitario; en Container/k3s, como servicio separado con almacenamiento persistente para `/usr/src/app/store`. Un solo controlador de software debe usar la radio a la vez.
2. **Conectar el servidor con el ESP32.** El servidor necesita acceder al puerto TCP 6053 del ESP32. Reservar una dirección DHCP ayuda a mantenerla estable. Ejecutar `python3 scripts/connection_url.py zac93-wroom.local`: pide la clave API sin mostrarla y genera una URL `esphome://` correctamente codificada. Para S3 usar `zac93-s3.local`. Pegar la URL secreta en **Z-Wave JS UI → Settings → Z-Wave → Serial Port**. No sustituirla por la antigua receta `tcp://…:6639`.
3. **Conectar HA con el servidor.** Activar **WS Server** en Z-Wave JS UI, normalmente TCP 3000. En HA añadir la integración Z-Wave con instalación personalizada y la dirección del servidor, por ejemplo `ws://zwave-js-ui:3000`. Es un nombre DNS ilustrativo, no una dirección universal. Aquí no se introduce la dirección del ESP32. MQTT no es necesario para esta integración.
4. **Incluir el sensor.** Iniciar inclusion en HA o Z-Wave JS UI y seguir el manual del sensor. Mantener despiertos los dispositivos de batería durante el interview. Si pertenecían a otra red, puede ser necesario un exclusion normal antes de incluirlos. No restablecer todo el controlador por este motivo.

![Capas de conexión](assets/diagrams/connection-fields.svg)

La [guía detallada de HA](docs/home-assistant.md) contiene capturas externas identificadas como referencia. En una red nueva y vacía, generar y guardar las claves Z-Wave. Al migrar una red existente, conservar sus claves y NVM. Una conexión API de ESPHome activa no demuestra que la radio ni los informes del sensor funcionen.

## Diagnóstico y copias de seguridad

![Secuencia de diagnóstico](assets/diagrams/diagnostic-ladder.svg)

- **Alimentación inestable:** comprobar cable, masa común, orientación y 3,3 V. No intentar resolverlo alimentando el ZAC93 a 5 V.
- **ESP32 visible, API desconectada:** comprobar el acceso desde el servidor Z-Wave JS y la clave/codificación de URL. mDNS puede no atravesar VLAN.
- **API conectada, controlador ausente:** cortar la alimentación y revisar TX/RX y GPIO. UART usa 115200/8N1. Descartar un segundo proceso Z-Wave JS compitiendo por la radio.
- **Controlador visible, sensor ausente:** comprobar región, batería, inclusión/exclusión e interview. Si los valores llegan a Z-Wave JS UI pero no a HA, revisar WS Server e integración HA.

La [guía de problemas](docs/troubleshooting.md) desarrolla cada capa. Registrar los ensayos físicos con la [lista de puesta en servicio](docs/commissioning.md). Guardar de forma privada NVM, almacenamiento de Z-Wave JS UI con las claves de red, configuración ESPHome y secretos. Un factory reset borra el estado de la red; no equivale a reiniciar. La actualización del firmware de radio y la restauración a través de este proxy siguen sin comprobarse físicamente aquí.

## Herramientas offline y contribuciones

Las [cuatro herramientas complementarias](docs/community-tools.md) revisan cambios de roles, contratos de medición, escenarios HA sintéticos y evidencias grabadas de asistentes de voz. Ninguna sustituye la puesta en servicio de la radio. Las [fuentes de la wiki](wiki/Home.md) facilitan la navegación hacia las guías canónicas.

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_docs.py
python3 scripts/render_diagrams.py
git diff --exit-code -- assets/diagrams
```

[Contribuir](CONTRIBUTING.md), [seguridad](SECURITY.md), [fuentes y créditos](docs/sources.md), [licencia MIT](LICENSE). Las fotografías y capturas de terceros mantienen sus derechos y no representan un montaje verificado en este repositorio.
