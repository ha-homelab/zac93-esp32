# Kết nối và đưa vào mạng lần đầu

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

[Tài liệu ZAC93 + ESP32](Home-vi.md) · [Khắc phục sự cố và khôi phục](Troubleshooting-vi.md)

Làm theo [hướng dẫn phần cứng chi tiết](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md), bao gồm các ảnh tham khảo có chú thích. Chọn rõ WROOM hoặc S3. Ngắt nguồn trước khi nối dây, kiểm tra tên tín hiệu cùng nguồn cấp và mức logic 3,3 V, rồi dùng YAML hiện có của đúng bo mạch đó. Trang này không đưa ra sơ đồ chân khác.

1. [Cài ESPHome trên ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). Giữ nguyên firmware ZAC93 và bảo mật các bí mật cục bộ.
2. [Kết nối Z-Wave JS UI với proxy ESPHome gốc, sau đó nối HA với WS Server của nó](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). Đây là hai kết nối riêng biệt; cổng API của ESP32 không phải cổng máy chủ Z-Wave dành cho HA. Chỉ để đúng một trình điều khiển Z-Wave phụ trách bộ điều khiển.
3. [Đưa cảm biến thật vào mạng và theo dõi nó](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Làm theo quy trình đưa vào mạng của chính cảm biến và hoàn tất quá trình interview. Chỉ kết nối được API chưa xác nhận bước này.
4. Ghi phiên bản phần mềm, báo cáo thực tế và các thiếu sót còn lại vào hồ sơ chạy thử riêng tư. Giữ lại NVM và khóa mạng trước khi di chuyển hoặc cập nhật.

Hướng dẫn HA có các ảnh chụp màn hình tham khảo bên ngoài được ghi nguồn; đó không phải hồ sơ ảnh của một cấu hình đã được chạy thử vật lý tại đây. Đọc [trạng thái xác thực](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) để hiểu sự khác biệt.
