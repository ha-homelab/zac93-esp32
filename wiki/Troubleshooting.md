# Troubleshooting and recovery

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

[ZAC93 + ESP32 documentation](Home.md) · [Connection and first inclusion](Connection.md)

Use the [canonical troubleshooting guide](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md). Work from the first failing layer, changing one factor at a time:

1. **Power and wiring:** supply stability, common ground, connector orientation and signal labels. Disconnect power before changing wiring.
2. **Network:** the Z-Wave JS host must reach the ESP32; multicast discovery and a ping reply are not API verification.
3. **Encrypted API:** correct key, native transport and URL encoding. Do not paste connection URLs into public issues.
4. **UART and radio:** the controller must be identified by its single driver. Use the documented board configuration, not a pin map inferred from an unrelated photo.
5. **Sensor and HA:** distinguish inclusion/interview/reporting from WS Server and HA entity problems.

![Diagnostic layers](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

Follow [backup and maintenance procedures](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md) before updates. Factory reset erases network state and is not a normal remedy for Wi-Fi, key or UART errors. Controller restoration and radio updates through this proxy remain among the [unverified hardware items](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).

When reporting an issue, include board identity, versions, the first failing layer and redacted observations. Follow [security guidance](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md): no Wi-Fi/API/OTA/Z-Wave keys, DSKs, private addresses, raw backups or compiled personal firmware.
