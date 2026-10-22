# Koneksi dan penyertaan pertama

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

[Dokumentasi ZAC93 + ESP32](Home-id.md) · [Pemecahan masalah dan pemulihan](Troubleshooting-id.md)

Ikuti [panduan perangkat keras terperinci](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md), termasuk foto referensi berlabel. Pilih WROOM atau S3 secara eksplisit. Putuskan daya sebelum menyambungkan kabel, periksa nama sinyal serta catu daya dan logika 3,3 V, lalu gunakan YAML yang sudah ada untuk papan tersebut. Halaman ini tidak memperkenalkan pemetaan pin lain.

1. [Pasang ESPHome pada ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). Biarkan firmware ZAC93 tetap utuh dan simpan rahasia lokal secara privat.
2. [Hubungkan Z-Wave JS UI ke proksi ESPHome native, lalu HA ke WS Server-nya](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). Ini adalah dua koneksi terpisah; port API ESP32 bukan port server Z-Wave untuk HA. Pastikan tepat satu driver Z-Wave bertanggung jawab atas pengontrol.
3. [Sertakan dan amati sensor yang sebenarnya](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Ikuti prosedur penyertaan milik sensor dan selesaikan proses interview-nya. Konektivitas API saja tidak mengonfirmasi langkah ini.
4. Catat versi perangkat lunak, laporan nyata, dan kekurangan yang tersisa dalam catatan komisioning privat. Simpan NVM dan kunci jaringan sebelum migrasi atau pembaruan.

Panduan HA memuat tangkapan layar referensi eksternal dengan atribusi; ini bukan rekaman tangkapan layar dari rakitan yang telah dikomisioning secara fisik di sini. Baca [status validasi](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) untuk memahami perbedaannya.
