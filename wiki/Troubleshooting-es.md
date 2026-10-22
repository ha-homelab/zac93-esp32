# Diagnóstico y recuperación

<!-- language-navigation:start -->
<p dir="ltr">
<a href="Troubleshooting.md" lang="en" dir="ltr">English</a> ·
<a href="Troubleshooting-ar.md" lang="ar" dir="rtl">العربية</a> ·
<a href="Troubleshooting-bn.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="Troubleshooting-cs.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="Troubleshooting-de.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="Troubleshooting-es.md" lang="es" dir="ltr">Español</a> ·
<a href="Troubleshooting-fa.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="Troubleshooting-fr.md" lang="fr" dir="ltr">Français</a> ·
<a href="Troubleshooting-he.md" lang="he" dir="rtl">עברית</a> ·
<a href="Troubleshooting-hi.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="Troubleshooting-id.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="Troubleshooting-it.md" lang="it" dir="ltr">Italiano</a> ·
<a href="Troubleshooting-ja.md" lang="ja" dir="ltr">日本語</a> ·
<a href="Troubleshooting-ko.md" lang="ko" dir="ltr">한국어</a> ·
<a href="Troubleshooting-nl.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="Troubleshooting-pl.md" lang="pl" dir="ltr">Polski</a> ·
<a href="Troubleshooting-pt.md" lang="pt" dir="ltr">Português</a> ·
<a href="Troubleshooting-ru.md" lang="ru" dir="ltr">Русский</a> ·
<a href="Troubleshooting-th.md" lang="th" dir="ltr">ไทย</a> ·
<a href="Troubleshooting-tr.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="Troubleshooting-uk.md" lang="uk" dir="ltr">Українська</a> ·
<a href="Troubleshooting-vi.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="Troubleshooting-zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="Troubleshooting-zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Documentación de ZAC93 + ESP32](Home-es.md) · [Conexión y primera inclusión](Connection-es.md)

Utiliza la [guía principal de diagnóstico](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md). Empieza por la primera capa que falle y cambia un solo factor cada vez:

1. **Alimentación y cableado:** estabilidad de la alimentación, masa común, orientación del conector y etiquetas de señales. Desconecta la alimentación antes de modificar el cableado.
2. **Red:** el host de Z-Wave JS debe alcanzar el ESP32; el descubrimiento multicast y una respuesta a ping no verifican la API.
3. **API cifrada:** clave correcta, transporte nativo y codificación de URL. No pegues las URL de conexión en incidencias públicas.
4. **UART y radio:** el único controlador de software responsable debe identificar el dispositivo controlador. Usa la configuración documentada de la placa, no un mapa de pines deducido de una foto ajena.
5. **Sensor y HA:** distingue la inclusión, entrevista y emisión de informes de los problemas del WS Server y de las entidades de HA.

![Capas de diagnóstico](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

Sigue los [procedimientos de copia de seguridad y mantenimiento](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md) antes de actualizar. Un restablecimiento de fábrica borra el estado de la red y no es una solución habitual a errores de Wi-Fi, claves o UART. La restauración del controlador y las actualizaciones de radio mediante este proxy siguen entre los [aspectos de hardware no verificados](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).

Al comunicar una incidencia, incluye la identidad de la placa, las versiones, la primera capa que falla y observaciones con los datos sensibles eliminados. Sigue las [indicaciones de seguridad](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md): no publiques claves Wi-Fi/API/OTA/Z-Wave, DSK, direcciones privadas, copias de seguridad sin procesar ni firmware personal compilado.
