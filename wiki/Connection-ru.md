# Подключение и первое включение в сеть

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

[Документация ZAC93 + ESP32](Home-ru.md) · [Диагностика и восстановление](Troubleshooting-ru.md)

Начните с [полной русской инструкции](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/guide-ru.md) и [фотографий/схем](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md). Явно выберите WROOM или S3. Перед соединением проводов отключите питание, сверьте маркировку сигналов и питание/логику 3,3 В. Используйте существующий YAML выбранной платы; эта страница не вводит новую распиновку.

1. [Установите ESPHome на ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). ZAC93 сохраняет свою прошивку, личные секреты остаются вне публикации.
2. [Соедините Z-Wave JS UI с ESPHome proxy, а HA — с WS Server](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). Это два отдельных соединения: порт API ESP32 не является портом сервера Z-Wave для HA. Только один Z-Wave-драйвер должен владеть контроллером.
3. Выполните inclusion по инструкции датчика, завершите interview и подтвердите реальный отчёт датчика. Одного статуса API connected недостаточно.
4. Заполните [список приёмки](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md), сохраните версии, наблюдения и незавершённые проверки приватно. До миграций и обновлений сохраните NVM и ключи сети.

Скриншоты в подробной инструкции — подписанные внешние примеры. Они не подтверждают физическую приёмку этого проекта. Актуальное разделение выполненных и ожидаемых проверок находится в [журнале валидации](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).
