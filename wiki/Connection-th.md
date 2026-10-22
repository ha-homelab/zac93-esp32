# การเชื่อมต่อและการเพิ่มเข้าร่วมเครือข่ายครั้งแรก

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

[เอกสาร ZAC93 + ESP32](Home-th.md) · [การแก้ปัญหาและการกู้คืน](Troubleshooting-th.md)

ทำตาม[คู่มือฮาร์ดแวร์โดยละเอียด](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md) รวมถึงภาพอ้างอิงที่มีป้ายกำกับ เลือก WROOM หรือ S3 อย่างชัดเจน ตัดไฟก่อนต่อสาย ตรวจสอบชื่อสัญญาณ รวมถึงไฟเลี้ยงและระดับลอจิก 3.3 V แล้วใช้ YAML ที่มีอยู่ของบอร์ดนั้น หน้านี้ไม่ได้กำหนดผังขาอีกชุดหนึ่ง

1. [ติดตั้ง ESPHome บน ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md) คงเฟิร์มแวร์ของ ZAC93 ไว้ตามเดิม และเก็บข้อมูลลับในเครื่องไว้เป็นส่วนตัว
2. [เชื่อมต่อ Z-Wave JS UI กับพร็อกซี ESPHome แบบเนทีฟ แล้วเชื่อมต่อ HA กับ WS Server ของมัน](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md) นี่คือการเชื่อมต่อแยกกันสองส่วน พอร์ต API ของ ESP32 ไม่ใช่พอร์ตเซิร์ฟเวอร์ Z-Wave ของ HA ให้มีไดรเวอร์ Z-Wave เพียงตัวเดียวรับผิดชอบคอนโทรลเลอร์
3. [เพิ่มเซ็นเซอร์จริงเข้าร่วมเครือข่ายและสังเกตการทำงาน](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md) ทำตามขั้นตอนเพิ่มอุปกรณ์ของเซ็นเซอร์นั้นและดำเนินการ interview ให้เสร็จ การเชื่อมต่อ API ได้เพียงอย่างเดียวไม่ยืนยันขั้นตอนนี้
4. บันทึกเวอร์ชันซอฟต์แวร์ รายงานจริง และสิ่งที่ยังขาดไว้ในบันทึกการทดสอบเริ่มใช้งานแบบส่วนตัว เก็บรักษา NVM และคีย์เครือข่ายก่อนย้ายระบบหรืออัปเดต

คู่มือ HA มีภาพหน้าจออ้างอิงจากภายนอกพร้อมระบุแหล่งที่มา ไม่ใช่บันทึกภาพหน้าจอของชุดฮาร์ดแวร์ที่ผ่านการทดสอบเริ่มใช้งานจริงที่นี่ อ่าน[สถานะการตรวจสอบ](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) เพื่อทำความเข้าใจความแตกต่าง
