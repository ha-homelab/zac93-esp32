# Probleemoplossing en herstel

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

[Documentatie voor ZAC93 + ESP32](Home-nl.md) · [Verbinding en eerste opname in het netwerk](Connection-nl.md)

Gebruik de [leidende handleiding voor probleemoplossing](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md). Begin bij de eerste falende laag en verander steeds één factor:

1. **Voeding en bedrading:** stabiele voeding, gemeenschappelijke massa, connectorrichting en signaallabels. Schakel de voeding uit voordat u bedrading verandert.
2. **Netwerk:** de Z-Wave-JS-host moet de ESP32 kunnen bereiken; multicastdetectie en een pingantwoord controleren de API niet.
3. **Versleutelde API:** juiste sleutel, native transport en URL-codering. Plaats geen verbindings-URL’s in openbare issues.
4. **UART en radio:** de controller moet door zijn enige driver worden herkend. Gebruik de gedocumenteerde printplaatconfiguratie, geen pinindeling afgeleid van een niet-gerelateerde foto.
5. **Sensor en HA:** onderscheid opname, interview en rapportage van problemen met WS Server en HA-entiteiten.

![Diagnoselagen](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

Volg vóór updates de [back-up- en onderhoudsprocedures](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Een fabrieksreset wist de netwerkstatus en is geen normale oplossing voor wifi-, sleutel- of UART-fouten. Controllerherstel en radio-updates via deze proxy behoren nog steeds tot de [niet-geverifieerde hardwarepunten](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).

Vermeld bij een probleemmelding de identiteit van de printplaat, versies, de eerste falende laag en waarnemingen waaruit gevoelige gegevens zijn verwijderd. Volg de [beveiligingsrichtlijnen](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md): geen wifi-/API-/OTA-/Z-Wave-sleutels, DSK’s, privéadressen, onbewerkte back-ups of gecompileerde persoonlijke firmware.
