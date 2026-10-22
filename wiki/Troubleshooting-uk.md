# Діагностика та відновлення

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

[Документація ZAC93 + ESP32](Home-uk.md) · [Підключення та перше включення до мережі](Connection-uk.md)

Використовуйте [основний посібник із діагностики](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md). Починайте з першого несправного рівня та змінюйте лише один чинник за раз:

1. **Живлення та проводи:** стабільність живлення, спільна земля, орієнтація роз’єму й підписи сигналів. Перед зміною проводки вимкніть живлення.
2. **Мережа:** хост Z-Wave JS повинен мати доступ до ESP32; multicast-виявлення та відповідь на ping не перевіряють API.
3. **Зашифрований API:** правильний ключ, нативний транспорт і кодування URL. Не вставляйте URL підключення в публічні issue.
4. **UART і радіо:** контролер має визначити його єдиний драйвер. Використовуйте задокументовану конфігурацію плати, а не схему контактів, виведену зі сторонньої фотографії.
5. **Датчик і HA:** відрізняйте включення, опитування та звіти від проблем WS Server і сутностей HA.

![Рівні діагностики](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

Перед оновленнями дотримуйтеся [процедур резервування та обслуговування](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Скидання до заводських налаштувань стирає стан мережі й не є звичайним способом виправлення помилок Wi-Fi, ключів або UART. Відновлення контролера й оновлення радіопрошивки через цей проксі досі належать до [неперевірених апаратних пунктів](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).

Повідомляючи про проблему, зазначте ідентифікацію плати, версії, перший несправний рівень і спостереження без конфіденційних даних. Дотримуйтеся [правил безпеки](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md): жодних ключів Wi-Fi/API/OTA/Z-Wave, DSK, приватних адрес, необроблених резервних копій або скомпільованих особистих прошивок.
