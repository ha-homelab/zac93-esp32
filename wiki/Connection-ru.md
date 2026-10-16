# Подключение и первое включение в сеть

[Главная](https://github.com/ha-homelab/zac93-esp32/wiki/Home-ru) · [English](https://github.com/ha-homelab/zac93-esp32/wiki/Connection) · [Диагностика](https://github.com/ha-homelab/zac93-esp32/wiki/Troubleshooting-ru)

Начните с [полной русской инструкции](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/guide-ru.md) и [фотографий/схем](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md). Явно выберите WROOM или S3. Перед соединением проводов отключите питание, сверьте маркировку сигналов и питание/логику 3,3 В. Используйте существующий YAML выбранной платы; эта страница не вводит новую распиновку.

1. [Установите ESPHome на ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). ZAC93 сохраняет свою прошивку, личные секреты остаются вне публикации.
2. [Соедините Z-Wave JS UI с ESPHome proxy, а HA — с WS Server](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). Это разные соединения с разными портами. Только один Z-Wave-драйвер должен владеть контроллером.
3. Выполните inclusion по инструкции датчика, завершите interview и подтвердите реальный отчёт датчика. Одного статуса API connected недостаточно.
4. Заполните [список приёмки](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md), сохраните версии, наблюдения и незавершённые проверки приватно. До миграций и обновлений сохраните NVM и ключи сети.

Скриншоты в подробной инструкции — подписанные внешние примеры. Они не подтверждают физическую приёмку этого проекта. Актуальное разделение выполненных и ожидаемых проверок находится в [журнале валидации](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).
