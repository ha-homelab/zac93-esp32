# Verbinding en eerste opname in het netwerk

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

[Documentatie voor ZAC93 + ESP32](Home-nl.md) · [Probleemoplossing en herstel](Troubleshooting-nl.md)

Volg de uitgebreide [hardwarehandleiding](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md), inclusief de gelabelde referentiefoto’s. Kies expliciet WROOM of S3. Schakel de voeding uit voordat u draden aansluit, controleer de signaalnamen en de voeding en logische niveaus van 3,3 V, en gebruik de bestaande YAML voor die printplaat. Deze pagina introduceert geen andere pinindeling.

1. [Installeer ESPHome op de ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). Laat de ZAC93-firmware intact en houd lokale geheimen privé.
2. [Verbind Z-Wave JS UI met de native ESPHome-proxy en daarna HA met de bijbehorende WS Server](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). Dit zijn twee afzonderlijke verbindingen; de API-poort van de ESP32 is niet de poort van de Z-Wave-server voor HA. Laat precies één Z-Wave-driver verantwoordelijk zijn voor de controller.
3. [Neem de echte sensor op in het netwerk en observeer hem](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Volg de eigen opnameprocedure van de sensor en voltooi het interview. Alleen een werkende API-verbinding bevestigt deze stap niet.
4. Noteer softwareversies, echte meldingen en resterende hiaten in een privéverslag van de ingebruikname. Bewaar NVM en netwerksleutels vóór migraties of updates.

De HA-handleiding bevat externe referentieschermafbeeldingen met bronvermelding; ze vormen geen verslag van een hier fysiek in gebruik genomen installatie. Lees de [validatiestatus](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) voor dit onderscheid.
