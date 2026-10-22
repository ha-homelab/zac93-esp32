# Diagnostica e ripristino

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

[Documentazione ZAC93 + ESP32](Home-it.md) · [Collegamento e prima inclusione](Connection-it.md)

Utilizza la [guida di riferimento alla diagnostica](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md). Parti dal primo livello che presenta un errore, modificando un solo fattore alla volta:

1. **Alimentazione e cablaggio:** stabilità dell’alimentazione, massa comune, orientamento dei connettori ed etichette dei segnali. Scollega l’alimentazione prima di modificare il cablaggio.
2. **Rete:** l’host Z-Wave JS deve raggiungere l’ESP32; il rilevamento multicast e una risposta al ping non verificano l’API.
3. **API cifrata:** chiave corretta, trasporto nativo e codifica URL. Non incollare URL di connessione nelle issue pubbliche.
4. **UART e radio:** il controller deve essere identificato dal suo unico driver. Usa la configurazione documentata della scheda, non una piedinatura dedotta da una foto non pertinente.
5. **Sensore e HA:** distingui inclusione, intervista e rapporti dai problemi del WS Server e delle entità HA.

![Livelli diagnostici](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

Segui le [procedure di backup e manutenzione](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md) prima degli aggiornamenti. Il ripristino di fabbrica cancella lo stato della rete e non è un rimedio normale agli errori Wi-Fi, di chiave o UART. Il ripristino del controller e gli aggiornamenti radio tramite questo proxy restano tra gli [aspetti hardware non verificati](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).

Quando segnali un problema, indica l’identità della scheda, le versioni, il primo livello in errore e osservazioni prive di dati riservati. Segui le [indicazioni di sicurezza](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md): niente chiavi Wi-Fi/API/OTA/Z-Wave, DSK, indirizzi privati, backup grezzi o firmware personale compilato.
