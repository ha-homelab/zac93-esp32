# Conexión y primera inclusión

<!-- language-navigation:start -->
<p dir="ltr">
<a href="Connection.md" lang="en" dir="ltr">English</a> ·
<a href="Connection-ar.md" lang="ar" dir="rtl">العربية</a> ·
<a href="Connection-bn.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="Connection-cs.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="Connection-de.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="Connection-es.md" lang="es" dir="ltr">Español</a> ·
<a href="Connection-fa.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="Connection-fr.md" lang="fr" dir="ltr">Français</a> ·
<a href="Connection-he.md" lang="he" dir="rtl">עברית</a> ·
<a href="Connection-hi.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="Connection-id.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="Connection-it.md" lang="it" dir="ltr">Italiano</a> ·
<a href="Connection-ja.md" lang="ja" dir="ltr">日本語</a> ·
<a href="Connection-ko.md" lang="ko" dir="ltr">한국어</a> ·
<a href="Connection-nl.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="Connection-pl.md" lang="pl" dir="ltr">Polski</a> ·
<a href="Connection-pt.md" lang="pt" dir="ltr">Português</a> ·
<a href="Connection-ru.md" lang="ru" dir="ltr">Русский</a> ·
<a href="Connection-th.md" lang="th" dir="ltr">ไทย</a> ·
<a href="Connection-tr.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="Connection-uk.md" lang="uk" dir="ltr">Українська</a> ·
<a href="Connection-vi.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="Connection-zh-Hans.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="Connection-zh-Hant.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Documentación de ZAC93 + ESP32](Home-es.md) · [Diagnóstico y recuperación](Troubleshooting-es.md)

Sigue la [guía detallada de hardware](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md), incluidas las fotografías de referencia etiquetadas. Selecciona expresamente WROOM o S3. Desconecta la alimentación antes de conectar cables, verifica los nombres de las señales y la alimentación y lógica de 3,3 V, y utiliza el YAML existente de esa placa. Esta página no introduce otro mapa de pines.

1. [Instala ESPHome en el ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). Conserva intacto el firmware del ZAC93 y mantén privados los secretos locales.
2. [Conecta Z-Wave JS UI al proxy nativo de ESPHome y después HA a su WS Server](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). Son dos conexiones distintas; el puerto API del ESP32 no es el puerto del servidor Z-Wave de HA. Mantén exactamente un controlador Z-Wave a cargo del dispositivo controlador.
3. [Incluye y observa el sensor real](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Sigue el procedimiento de inclusión del propio sensor y completa su entrevista. La conectividad API por sí sola no confirma este paso.
4. Registra versiones de software, informes reales y carencias pendientes en un registro privado de puesta en servicio. Conserva la NVM y las claves de red antes de migraciones o actualizaciones.

La guía de HA contiene capturas externas de referencia con atribución; no documentan una instalación puesta físicamente en servicio aquí. Consulta el [estado de validación](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) para entender la distinción.
