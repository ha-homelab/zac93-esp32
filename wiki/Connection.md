# Connection and first inclusion

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

[ZAC93 + ESP32 documentation](Home.md) · [Troubleshooting and recovery](Troubleshooting.md)

Follow the detailed [hardware guide](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md), including the labelled reference photographs. Select WROOM or S3 explicitly. Disconnect power before connecting wires, verify signal names and 3.3-V supply/logic, and use that board's existing YAML. This page does not introduce another pin map.

1. [Install ESPHome on the ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). Keep the ZAC93 firmware intact and retain local secrets privately.
2. [Connect Z-Wave JS UI to the native ESPHome proxy, then HA to its WS Server](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). These are two separate connections; the ESP32's API port is not HA's Z-Wave server port. Keep exactly one Z-Wave driver responsible for the controller.
3. [Include and observe the actual sensor](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Follow the sensor's own inclusion procedure and complete its interview. API connectivity alone does not confirm this step.
4. Record software versions, real reports and remaining gaps in a private commissioning record. Preserve NVM and network keys before migration or updates.

The HA guide contains attributed external reference screenshots; it is not a screenshot record of a physically commissioned build here. Read the [validation status](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) for the distinction.
