# Řešení potíží a obnova

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

[Dokumentace ZAC93 + ESP32](Home-cs.md) · [Připojení a první zařazení do sítě](Connection-cs.md)

Použijte [hlavní průvodce řešením potíží](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md). Začněte u první selhávající vrstvy a měňte vždy jen jeden faktor:

1. **Napájení a vodiče:** stabilita napájení, společná zem, orientace konektoru a označení signálů. Před změnou zapojení odpojte napájení.
2. **Síť:** hostitel Z-Wave JS musí dosáhnout na ESP32; multicastové vyhledání ani odpověď na ping nejsou ověřením API.
3. **Šifrované API:** správný klíč, nativní přenos a kódování URL. Nevkládejte adresy připojení do veřejných hlášení problémů.
4. **UART a rádio:** řadič musí rozpoznat jeho jediný ovladač. Použijte zdokumentovanou konfiguraci desky, nikoli zapojení odvozené z nesouvisející fotografie.
5. **Senzor a HA:** oddělte zařazení, interview a hlášení od problémů WS Serveru a entit HA.

![Diagnostické vrstvy](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

Před aktualizacemi dodržte [postupy zálohování a údržby](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Obnovení továrního nastavení smaže stav sítě a není běžným řešením chyb Wi-Fi, klíčů nebo UART. Obnova řadiče a aktualizace rádia přes tuto proxy stále patří mezi [neověřené hardwarové body](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).

Při hlášení problému uveďte identitu desky, verze, první selhávající vrstvu a pozorování zbavená citlivých údajů. Dodržujte [bezpečnostní pokyny](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md): žádné klíče Wi-Fi/API/OTA/Z-Wave, DSK, soukromé adresy, nezpracované zálohy ani zkompilovaný osobní firmware.
