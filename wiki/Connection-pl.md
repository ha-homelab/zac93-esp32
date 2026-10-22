# Połączenie i pierwsze dołączenie do sieci

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

[Dokumentacja ZAC93 + ESP32](Home-pl.md) · [Rozwiązywanie problemów i przywracanie](Troubleshooting-pl.md)

Postępuj zgodnie ze szczegółowym [przewodnikiem sprzętowym](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md), w tym opisanymi zdjęciami referencyjnymi. Jawnie wybierz WROOM albo S3. Przed podłączaniem przewodów odłącz zasilanie, sprawdź nazwy sygnałów oraz zasilanie i poziomy logiczne 3,3 V, a następnie użyj istniejącego pliku YAML dla danej płytki. Ta strona nie wprowadza kolejnego układu pinów.

1. [Zainstaluj ESPHome na ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). Pozostaw firmware ZAC93 bez zmian i przechowuj lokalne sekrety prywatnie.
2. [Połącz Z-Wave JS UI z natywnym proxy ESPHome, a następnie HA z jego WS Server](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). To dwa odrębne połączenia; port API ESP32 nie jest portem serwera Z-Wave dla HA. Za kontroler musi odpowiadać dokładnie jeden sterownik Z-Wave.
3. [Dołącz rzeczywisty czujnik i obserwuj jego działanie](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Wykonaj procedurę dołączania właściwą dla czujnika i zakończ jego interview. Sama łączność z API nie potwierdza tego kroku.
4. Zapisz wersje oprogramowania, rzeczywiste raporty i pozostałe braki w prywatnym protokole uruchomienia. Zabezpiecz NVM i klucze sieci przed migracją lub aktualizacją.

Przewodnik HA zawiera zewnętrzne zrzuty referencyjne z podaniem źródeł; nie dokumentują one fizycznie uruchomionej tutaj instalacji. Różnicę wyjaśnia [status walidacji](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).
