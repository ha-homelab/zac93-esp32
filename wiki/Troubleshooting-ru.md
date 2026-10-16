# Диагностика и восстановление

[Главная](https://github.com/ha-homelab/zac93-esp32/wiki/Home-ru) · [English](https://github.com/ha-homelab/zac93-esp32/wiki/Troubleshooting) · [Подключение](https://github.com/ha-homelab/zac93-esp32/wiki/Connection-ru)

Основные документы: [русская инструкция](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/guide-ru.md) и [подробная диагностика](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md). Идите от первого неработающего слоя и меняйте по одному фактору:

1. **Питание и проводка:** стабильность, общая земля, ориентация разъёма, маркировка сигналов. Переподключайте провода только без питания.
2. **Сеть:** доступ к ESP32 должен быть именно с хоста Z-Wave JS. Обнаружение mDNS и ответ ping не доказывают работу API.
3. **Зашифрованный API:** верный ключ, штатный транспорт и URL-кодирование. URL с ключом нельзя публиковать в issue.
4. **UART и радио:** единственный драйвер должен определить контроллер. Используйте конфигурацию конкретной платы, не переносите распиновку с посторонней фотографии.
5. **Датчик и HA:** отдельно проверяйте inclusion/interview/отчёты и отдельно WS Server с сущностями HA.

![Слои диагностики](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

До обновления следуйте [плану резервирования](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Factory reset стирает состояние сети; это не обычный способ исправить Wi-Fi, ошибку API-ключа или UART. Восстановление контроллера и обновление радиопрошивки через этот proxy ещё входят в [непроверенные аппаратные пункты](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).

В issue указывайте модель платы, версии, первый неработающий слой и обезличенные наблюдения. По [правилам безопасности](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md) нельзя публиковать Wi-Fi/API/OTA/Z-Wave ключи, DSK, приватные адреса, сырые резервные копии и личные собранные прошивки.
