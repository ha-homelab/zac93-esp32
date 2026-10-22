# عیب‌یابی و بازیابی

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

[مستندات ZAC93 + ESP32](Home-fa.md) · [اتصال و نخستین افزودن به شبکه](Connection-fa.md)

<div dir="rtl" lang="fa">

از [راهنمای مرجع عیب‌یابی](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md) استفاده کنید. از نخستین لایهٔ ناموفق شروع کنید و هر بار فقط یک عامل را تغییر دهید:

1. **برق و سیم‌کشی:** پایداری تغذیه، زمین مشترک، جهت اتصال‌دهنده و برچسب سیگنال‌ها. پیش از تغییر سیم‌کشی برق را قطع کنید.
2. **شبکه:** میزبان Z-Wave JS باید به ESP32 دسترسی داشته باشد؛ کشف چندپخشی و پاسخ ping تأیید API نیستند.
3. **API رمزگذاری‌شده:** کلید درست، انتقال بومی و کدگذاری URL. نشانی‌های اتصال را در گزارش‌های عمومی مسئله درج نکنید.
4. **UART و رادیو:** کنترل‌کننده باید به‌وسیلهٔ تنها درایور مسئول آن شناسایی شود. از پیکربندی مستند برد استفاده کنید، نه نقشهٔ پایه‌ای که از عکسی نامرتبط استنباط شده است.
5. **حسگر و HA:** افزودن به شبکه، مصاحبهٔ شناسایی و گزارش‌دهی را از مشکلات WS Server و موجودیت‌های HA تفکیک کنید.

![لایه‌های تشخیص](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

پیش از به‌روزرسانی، [روش‌های پشتیبان‌گیری و نگهداری](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md) را دنبال کنید. بازنشانی کارخانه وضعیت شبکه را پاک می‌کند و درمان معمول خطاهای Wi-Fi، کلید یا UART نیست. بازیابی کنترل‌کننده و به‌روزرسانی رادیو از طریق این پراکسی همچنان جزو [موارد سخت‌افزاری تأییدنشده](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) هستند.

هنگام گزارش مشکل، هویت برد، نسخه‌ها، نخستین لایهٔ ناموفق و مشاهدات پاک‌سازی‌شده از داده‌های حساس را ذکر کنید. از [راهنمای امنیت](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md) پیروی کنید: کلیدهای Wi-Fi/API/OTA/Z-Wave،‏ DSK، نشانی‌های خصوصی، پشتیبان خام یا میان‌افزار شخصی کامپایل‌شده را منتشر نکنید.

</div>
