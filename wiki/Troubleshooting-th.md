# การแก้ปัญหาและการกู้คืน

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

[เอกสาร ZAC93 + ESP32](Home-th.md) · [การเชื่อมต่อและการเพิ่มเข้าร่วมเครือข่ายครั้งแรก](Connection-th.md)

ใช้[คู่มือการแก้ปัญหาหลัก](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md) เริ่มจากชั้นแรกที่ทำงานผิดพลาดและเปลี่ยนทีละปัจจัย:

1. **ไฟเลี้ยงและสายไฟ:** ความเสถียรของไฟเลี้ยง กราวด์ร่วม ทิศทางขั้วต่อ และป้ายสัญญาณ ตัดไฟก่อนเปลี่ยนการเดินสาย
2. **เครือข่าย:** โฮสต์ Z-Wave JS ต้องเข้าถึง ESP32 ได้ การค้นหาแบบมัลติคาสต์และการตอบ ping ไม่ใช่การตรวจสอบ API
3. **API ที่เข้ารหัส:** คีย์ที่ถูกต้อง การส่งข้อมูลแบบเนทีฟ และการเข้ารหัส URL อย่าวาง URL การเชื่อมต่อใน issue สาธารณะ
4. **UART และวิทยุ:** ไดรเวอร์ที่รับผิดชอบเพียงตัวเดียวต้องระบุคอนโทรลเลอร์ได้ ใช้การกำหนดค่าบอร์ดตามเอกสาร ไม่ใช่ผังขาที่คาดเดาจากภาพอื่นที่ไม่เกี่ยวข้อง
5. **เซ็นเซอร์และ HA:** แยกปัญหาการเพิ่มเข้าร่วมเครือข่าย การ interview และการรายงาน ออกจากปัญหา WS Server และเอนทิตีของ HA

![ชั้นการวินิจฉัย](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

ทำตาม[ขั้นตอนสำรองข้อมูลและบำรุงรักษา](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md) ก่อนอัปเดต การรีเซ็ตเป็นค่าโรงงานลบสถานะเครือข่ายและไม่ใช่วิธีแก้ปกติสำหรับข้อผิดพลาด Wi-Fi คีย์ หรือ UART การกู้คืนคอนโทรลเลอร์และอัปเดตวิทยุผ่านพร็อกซีนี้ยังอยู่ใน[รายการฮาร์ดแวร์ที่ยังไม่ได้ตรวจสอบ](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md)

เมื่อรายงานปัญหา ให้ระบุข้อมูลระบุตัวบอร์ด เวอร์ชัน ชั้นแรกที่ผิดพลาด และข้อสังเกตที่ลบข้อมูลอ่อนไหวแล้ว ทำตาม[คำแนะนำด้านความปลอดภัย](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md): ห้ามเผยแพร่คีย์ Wi-Fi/API/OTA/Z-Wave, DSK, ที่อยู่ส่วนตัว, ข้อมูลสำรองดิบ หรือเฟิร์มแวร์ส่วนตัวที่คอมไพล์แล้ว
