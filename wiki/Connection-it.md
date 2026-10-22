# Collegamento e prima inclusione

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

[Documentazione ZAC93 + ESP32](Home-it.md) · [Diagnostica e ripristino](Troubleshooting-it.md)

Segui la [guida dettagliata all’hardware](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md), comprese le fotografie di riferimento con etichette. Seleziona esplicitamente WROOM o S3. Scollega l’alimentazione prima di collegare i cavi, verifica i nomi dei segnali e alimentazione e livelli logici a 3,3 V, e utilizza lo YAML esistente per quella scheda. Questa pagina non introduce un’altra piedinatura.

1. [Installa ESPHome sull’ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). Mantieni intatto il firmware dello ZAC93 e conserva privatamente i segreti locali.
2. [Collega Z-Wave JS UI al proxy nativo ESPHome, poi HA al suo WS Server](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). Sono due collegamenti distinti; la porta API dell’ESP32 non è la porta del server Z-Wave di HA. Un solo driver Z-Wave deve gestire il controller.
3. [Includi e osserva il sensore reale](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Segui la procedura di inclusione del sensore e completane l’intervista. La sola connettività API non conferma questo passaggio.
4. Registra versioni software, segnalazioni reali e lacune residue in un verbale privato di messa in servizio. Conserva NVM e chiavi di rete prima di migrazioni o aggiornamenti.

La guida HA contiene schermate esterne di riferimento con attribuzione; non documentano una realizzazione fisicamente messa in servizio qui. Leggi lo [stato di validazione](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) per capire la distinzione.
