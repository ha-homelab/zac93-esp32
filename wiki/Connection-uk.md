# Підключення та перше включення до мережі

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

[Документація ZAC93 + ESP32](Home-uk.md) · [Діагностика та відновлення](Troubleshooting-uk.md)

Дотримуйтеся докладного [посібника з апаратної частини](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md), зокрема підписаних довідкових фотографій. Явно оберіть WROOM або S3. Перед під’єднанням проводів вимкніть живлення, перевірте назви сигналів, живлення й логічні рівні 3,3 В та використовуйте наявний YAML саме цієї плати. Ця сторінка не запроваджує іншої схеми контактів.

1. [Установіть ESPHome на ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). Залиште прошивку ZAC93 незмінною та зберігайте локальні секрети приватно.
2. [Підключіть Z-Wave JS UI до нативного проксі ESPHome, а потім HA до його WS Server](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). Це два окремі з’єднання; порт API ESP32 не є портом сервера Z-Wave для HA. За контролер має відповідати рівно один драйвер Z-Wave.
3. [Включіть до мережі реальний датчик і спостерігайте за ним](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Виконайте власну процедуру включення датчика та завершіть його опитування (interview). Самого з’єднання з API для підтвердження цього кроку недостатньо.
4. Занотуйте версії ПЗ, реальні звіти та невирішені питання в приватному протоколі введення в експлуатацію. Перед міграціями або оновленнями збережіть NVM і ключі мережі.

Посібник HA містить зовнішні довідкові знімки екрана із зазначенням джерел; це не фотофіксація фізично введеної тут в експлуатацію збірки. Різницю пояснює [стан перевірки](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).
