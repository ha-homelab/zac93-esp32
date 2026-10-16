# Related offline tools

[English home](../README.md) · [Русская главная](../README.ru.md) · [Deutsch](../README.de.md) · [Español](../README.es.md) · [Wiki](../wiki/Home.md)

These repositories complement a documented installation. They are separate tools with separate installation requirements. None connects this ZAC93, validates a pinout, performs inclusion, measures RF range or substitutes for the [physical commissioning checklist](commissioning.md). Use synthetic or reviewed, redacted input; do not copy HA diagnostics, network keys or controller backups into a public repository.

## Entity migration plans

[ha-entity-migrations](https://github.com/ha-homelab/ha-entity-migrations) plans changes from explicit hardware/channel/role records and supplied JSON configuration snapshots. It distinguishes references that follow a household role from references that follow a physical channel. This is relevant if a newly included Z-Wave device replaces another device while the old one is reused elsewhere.

The first release is offline and read-only: it reports candidate edits and unresolved references, never applies them to HA. A ready result covers only the supplied files. Dynamic templates and unsupported input formats cannot be treated as proof that all references have migrated. Record the Z-Wave inclusion and actual entity IDs first; then prepare the migration input privately.

## Measurement contracts

[ha-meter-contracts](https://github.com/ha-homelab/ha-meter-contracts) checks declared meter topology, measurement meaning, units, freshness and overlap. It is relevant when an included meter exposes several views of the same measurement or a shared power total must not be labelled as a single load.

Declared topology and a valid sample are not electrical calibration. Do not infer that a controller, socket or battery sensor measures energy solely because it exists in HA. Review that device's documented capabilities and real observations before writing a contract.

## Home Assistant scenario tests

[ha-scenario-tests](https://github.com/ha-homelab/ha-scenario-tests) runs a restricted synthetic scenario format through a pinned real Home Assistant automation/script engine. It can assert ordered service calls, forbidden calls and synthetic final states for logic intended to consume a Z-Wave sensor.

It does not import arbitrary production configuration, connect to the radio, emulate RF failures or prove production timer duration from a short accelerated example. Consult that project's supported Python version and validation record. Keep device commissioning and logic testing as separate evidence.

## Recorded voice scenarios

[assist-scenario-lab](https://github.com/ha-homelab/assist-scenario-lab) evaluates bounded recorded voice evidence and can import a single exported HA pipeline event array. Protocol completion, intent correctness, observed action and audibility are distinct checks.

Use it if a voice command will operate a newly included device: a successful service request alone does not prove that a lamp changed or speech was audible. This is an offline evaluator, not a voice satellite, automatic acoustic measurement tool or Z-Wave integration. Review exported identifiers even though the import adapter discards pipeline payloads.

## По-русски

- **[Миграции сущностей](https://github.com/ha-homelab/ha-entity-migrations):** явный план переноса роли на новое устройство с сохранением различия между ролью и физическим выходом. JSON-снимки и политики задаются пользователем; изменения не применяются, динамические ссылки требуют ручного разбора.
- **[Контракты измерений](https://github.com/ha-homelab/ha-meter-contracts):** проверка заявленного охвата счётчика, единиц, свежести и двойного учёта. Проверка схемы не заменяет измерение и калибровку.
- **[Сценарии HA](https://github.com/ha-homelab/ha-scenario-tests):** ограниченные синтетические сценарии в реальном закреплённом движке автоматизаций HA. Это проверка логики, а не радио, датчика или реального двадцатиминутного интервала.
- **[Голосовые испытания](https://github.com/ha-homelab/assist-scenario-lab):** раздельная оценка завершения протокола, смысла команды, наблюдаемого действия и слышимого ответа по предоставленным записям. Автоматически физический результат не подтверждается.

Все четыре проекта дополняют документацию. Они не переводят статус этого ZAC93 из «аппаратная проверка ожидается» в «проверено». Для этого нужны реальные наблюдения и заполненный [список приёмки](commissioning.md).
