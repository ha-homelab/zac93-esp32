# Pemecahan masalah dan pemulihan

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

[Dokumentasi ZAC93 + ESP32](Home-id.md) · [Koneksi dan penyertaan pertama](Connection-id.md)

Gunakan [panduan pemecahan masalah utama](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md). Mulailah dari lapisan pertama yang gagal dan ubah satu faktor setiap kali:

1. **Daya dan pengkabelan:** kestabilan catu daya, ground bersama, orientasi konektor, dan label sinyal. Putuskan daya sebelum mengubah pengkabelan.
2. **Jaringan:** host Z-Wave JS harus dapat menjangkau ESP32; penemuan multicast dan balasan ping bukan verifikasi API.
3. **API terenkripsi:** kunci yang benar, transport native, dan pengodean URL. Jangan tempelkan URL koneksi ke issue publik.
4. **UART dan radio:** pengontrol harus dikenali oleh satu-satunya driver yang menanganinya. Gunakan konfigurasi papan yang didokumentasikan, bukan pemetaan pin yang disimpulkan dari foto yang tidak terkait.
5. **Sensor dan HA:** bedakan penyertaan, interview, dan pelaporan dari masalah WS Server dan entitas HA.

![Lapisan diagnostik](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

Ikuti [prosedur pencadangan dan pemeliharaan](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md) sebelum pembaruan. Reset pabrik menghapus status jaringan dan bukan solusi biasa untuk kesalahan Wi-Fi, kunci, atau UART. Pemulihan pengontrol dan pembaruan radio melalui proksi ini masih termasuk [hal-hal perangkat keras yang belum diverifikasi](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).

Saat melaporkan masalah, sertakan identitas papan, versi, lapisan pertama yang gagal, dan hasil pengamatan yang sudah disunting untuk menghapus data sensitif. Ikuti [panduan keamanan](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md): jangan sertakan kunci Wi-Fi/API/OTA/Z-Wave, DSK, alamat privat, cadangan mentah, atau firmware pribadi hasil kompilasi.
