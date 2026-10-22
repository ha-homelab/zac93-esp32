# Диагностика и восстановление

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

[Документация ZAC93 + ESP32](Home-ru.md) · [Подключение и первое включение в сеть](Connection-ru.md)

Основные документы: [русская инструкция](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/guide-ru.md) и [подробная диагностика](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md). Идите от первого неработающего слоя и меняйте по одному фактору:

1. **Питание и проводка:** стабильность, общая земля, ориентация разъёма, маркировка сигналов. Переподключайте провода только без питания.
2. **Сеть:** доступ к ESP32 должен быть именно с хоста Z-Wave JS. Обнаружение mDNS и ответ ping не доказывают работу API.
3. **Зашифрованный API:** верный ключ, штатный транспорт и URL-кодирование. URL с ключом нельзя публиковать в issue.
4. **UART и радио:** единственный драйвер должен определить контроллер. Используйте конфигурацию конкретной платы, не переносите распиновку с посторонней фотографии.
5. **Датчик и HA:** отдельно проверяйте inclusion/interview/отчёты и отдельно WS Server с сущностями HA.

![Слои диагностики](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

До обновления следуйте [плану резервирования](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Factory reset стирает состояние сети; это не обычный способ исправить Wi-Fi, ошибку API-ключа или UART. Восстановление контроллера и обновление радиопрошивки через этот proxy ещё входят в [непроверенные аппаратные пункты](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).

В issue указывайте модель платы, версии, первый неработающий слой и обезличенные наблюдения. По [правилам безопасности](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md) нельзя публиковать Wi-Fi/API/OTA/Z-Wave ключи, DSK, приватные адреса, сырые резервные копии и личные собранные прошивки.
