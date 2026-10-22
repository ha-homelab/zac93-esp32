# Verbindung und erste Einbindung

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

[Dokumentation für ZAC93 + ESP32](Home-de.md) · [Fehlerbehebung und Wiederherstellung](Troubleshooting-de.md)

Folgen Sie der ausführlichen [Hardwareanleitung](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md), einschließlich der beschrifteten Referenzfotos. Wählen Sie ausdrücklich WROOM oder S3. Trennen Sie vor dem Verdrahten die Stromversorgung, prüfen Sie die Signalnamen sowie Versorgung und Logikpegel von 3,3 V, und verwenden Sie die vorhandene YAML-Datei dieser Platine. Diese Seite führt keine weitere Pinbelegung ein.

1. [Installieren Sie ESPHome auf dem ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). Lassen Sie die ZAC93-Firmware unverändert und bewahren Sie lokale Geheimnisse privat auf.
2. [Verbinden Sie Z-Wave JS UI mit dem nativen ESPHome-Proxy und anschließend HA mit dessen WS Server](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). Das sind zwei getrennte Verbindungen; der API-Port des ESP32 ist nicht der Port des Z-Wave-Servers für HA. Genau ein Z-Wave-Treiber darf für den Controller zuständig sein.
3. [Binden Sie den tatsächlichen Sensor ein und beobachten Sie ihn](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Befolgen Sie dessen eigene Einbindungsprozedur und schließen Sie sein Interview ab. Eine API-Verbindung allein bestätigt diesen Schritt nicht.
4. Halten Sie Softwareversionen, echte Meldungen und verbleibende Lücken in einem privaten Inbetriebnahmeprotokoll fest. Sichern Sie NVM und Netzwerkschlüssel vor Migrationen oder Aktualisierungen.

Die HA-Anleitung enthält externe Referenz-Screenshots mit Quellenangaben; sie dokumentieren keine hier physisch in Betrieb genommene Installation. Den Unterschied erläutert der [Validierungsstatus](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).
