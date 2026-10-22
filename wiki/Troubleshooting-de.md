# Fehlerbehebung und Wiederherstellung

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

[Dokumentation für ZAC93 + ESP32](Home-de.md) · [Verbindung und erste Einbindung](Connection-de.md)

Verwenden Sie die [maßgebliche Anleitung zur Fehlerbehebung](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md). Beginnen Sie bei der ersten fehlerhaften Schicht und ändern Sie jeweils nur einen Faktor:

1. **Stromversorgung und Verdrahtung:** stabile Versorgung, gemeinsame Masse, Steckerausrichtung und Signalbeschriftungen. Trennen Sie die Stromversorgung vor Änderungen an der Verdrahtung.
2. **Netzwerk:** Der Z-Wave-JS-Host muss den ESP32 erreichen; Multicast-Erkennung und eine Ping-Antwort prüfen nicht die API.
3. **Verschlüsselte API:** korrekter Schlüssel, nativer Transport und URL-Kodierung. Veröffentlichen Sie keine Verbindungs-URLs in öffentlichen Issues.
4. **UART und Funk:** Der einzige zuständige Treiber muss den Controller erkennen. Verwenden Sie die dokumentierte Platinenkonfiguration, keine aus einem fremden Foto abgeleitete Pinbelegung.
5. **Sensor und HA:** Unterscheiden Sie Einbindung, Interview und Meldungen von Problemen mit WS Server und HA-Entitäten.

![Diagnoseschichten](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

Befolgen Sie vor Aktualisierungen die [Sicherungs- und Wartungsverfahren](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Ein Werksreset löscht den Netzwerkzustand und ist keine übliche Lösung für WLAN-, Schlüssel- oder UART-Fehler. Die Wiederherstellung des Controllers und Funkaktualisierungen über diesen Proxy gehören weiterhin zu den [ungeprüften Hardwarepunkten](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).

Geben Sie bei einer Fehlermeldung die Platinenidentität, Versionen, die erste fehlerhafte Schicht und bereinigte Beobachtungen an. Beachten Sie die [Sicherheitsrichtlinien](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md): keine WLAN-/API-/OTA-/Z-Wave-Schlüssel, DSKs, privaten Adressen, rohen Sicherungen oder kompilierten persönlichen Firmwaredateien.
