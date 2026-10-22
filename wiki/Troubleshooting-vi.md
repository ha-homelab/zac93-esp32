# Khắc phục sự cố và khôi phục

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

[Tài liệu ZAC93 + ESP32](Home-vi.md) · [Kết nối và đưa vào mạng lần đầu](Connection-vi.md)

Dùng [hướng dẫn khắc phục sự cố chính thức](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md). Bắt đầu từ lớp đầu tiên bị lỗi và chỉ thay đổi một yếu tố mỗi lần:

1. **Nguồn và dây nối:** độ ổn định nguồn, mass chung, hướng đầu nối và nhãn tín hiệu. Ngắt nguồn trước khi thay đổi dây nối.
2. **Mạng:** máy chủ Z-Wave JS phải truy cập được ESP32; phát hiện multicast và phản hồi ping không xác minh API.
3. **API mã hóa:** khóa đúng, giao thức truyền gốc và mã hóa URL. Không dán URL kết nối vào báo cáo sự cố công khai.
4. **UART và vô tuyến:** bộ điều khiển phải được trình điều khiển duy nhất phụ trách nó nhận diện. Dùng cấu hình bo mạch được tài liệu hóa, không dùng sơ đồ chân suy ra từ một ảnh không liên quan.
5. **Cảm biến và HA:** phân biệt đưa vào mạng, interview và báo cáo với các vấn đề của WS Server và thực thể HA.

![Các lớp chẩn đoán](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

Làm theo [quy trình sao lưu và bảo trì](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md) trước khi cập nhật. Khôi phục cài đặt gốc xóa trạng thái mạng và không phải cách xử lý thông thường cho lỗi Wi-Fi, khóa hoặc UART. Khôi phục bộ điều khiển và cập nhật vô tuyến qua proxy này vẫn nằm trong [các hạng mục phần cứng chưa được xác minh](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).

Khi báo cáo sự cố, nêu danh tính bo mạch, phiên bản, lớp đầu tiên bị lỗi và các quan sát đã loại bỏ dữ liệu nhạy cảm. Tuân theo [hướng dẫn bảo mật](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md): không gửi khóa Wi-Fi/API/OTA/Z-Wave, DSK, địa chỉ riêng, bản sao lưu thô hoặc firmware cá nhân đã biên dịch.
