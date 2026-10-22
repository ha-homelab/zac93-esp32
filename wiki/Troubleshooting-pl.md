# Rozwiązywanie problemów i przywracanie

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

[Dokumentacja ZAC93 + ESP32](Home-pl.md) · [Połączenie i pierwsze dołączenie do sieci](Connection-pl.md)

Korzystaj z [głównego przewodnika rozwiązywania problemów](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md). Zacznij od pierwszej zawodzącej warstwy i zmieniaj jeden czynnik naraz:

1. **Zasilanie i okablowanie:** stabilność zasilania, wspólna masa, orientacja złącza i oznaczenia sygnałów. Odłącz zasilanie przed zmianą okablowania.
2. **Sieć:** host Z-Wave JS musi mieć dostęp do ESP32; wykrywanie multicast i odpowiedź ping nie weryfikują API.
3. **Szyfrowane API:** poprawny klucz, natywny transport i kodowanie URL. Nie wklejaj adresów połączenia do publicznych zgłoszeń.
4. **UART i radio:** kontroler musi zostać rozpoznany przez swój jedyny sterownik. Używaj udokumentowanej konfiguracji płytki, a nie układu pinów wywnioskowanego z niepowiązanego zdjęcia.
5. **Czujnik i HA:** odróżniaj dołączenie, interview i raportowanie od problemów WS Server i encji HA.

![Warstwy diagnostyczne](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

Przed aktualizacją wykonaj [procedury kopii zapasowej i konserwacji](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Reset fabryczny usuwa stan sieci i nie jest zwykłym sposobem naprawy błędów Wi-Fi, kluczy lub UART. Przywracanie kontrolera i aktualizacje radia przez to proxy nadal należą do [niezweryfikowanych elementów sprzętowych](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).

Zgłaszając problem, podaj identyfikację płytki, wersje, pierwszą zawodzącą warstwę i obserwacje po usunięciu danych wrażliwych. Przestrzegaj [zasad bezpieczeństwa](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md): bez kluczy Wi-Fi/API/OTA/Z-Wave, DSK, prywatnych adresów, surowych kopii zapasowych ani skompilowanego osobistego firmware.
