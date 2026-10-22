# Připojení a první zařazení do sítě

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

[Dokumentace ZAC93 + ESP32](Home-cs.md) · [Řešení potíží a obnova](Troubleshooting-cs.md)

Postupujte podle podrobného [průvodce hardwarem](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md), včetně popsaných referenčních fotografií. Výslovně vyberte WROOM nebo S3. Před připojováním vodičů odpojte napájení, ověřte názvy signálů a napájení i logiku 3,3 V a použijte stávající YAML pro danou desku. Tato stránka nezavádí další zapojení pinů.

1. [Nainstalujte ESPHome do ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). Firmware ZAC93 ponechte nedotčený a místní tajné údaje uchovávejte soukromě.
2. [Připojte Z-Wave JS UI k nativní proxy ESPHome a poté HA k jejímu WS Serveru](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). Jde o dvě samostatná spojení; port API ESP32 není portem Z-Wave serveru pro HA. Za řadič musí odpovídat právě jeden ovladač Z-Wave.
3. [Zařaďte skutečný senzor do sítě a sledujte jej](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Dodržte postup zařazení daného senzoru a dokončete jeho interview. Samotné spojení s API tento krok nepotvrzuje.
4. Do soukromého záznamu o uvedení do provozu zapište verze softwaru, skutečná hlášení a zbývající mezery. Před migrací nebo aktualizací zachovejte NVM a síťové klíče.

Průvodce HA obsahuje externí referenční snímky obrazovky s uvedením zdrojů; nejde o snímkový záznam zde fyzicky zprovozněné sestavy. Rozdíl vysvětluje [stav ověření](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).
