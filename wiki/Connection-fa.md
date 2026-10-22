# اتصال و نخستین افزودن به شبکه

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

[مستندات ZAC93 + ESP32](Home-fa.md) · [عیب‌یابی و بازیابی](Troubleshooting-fa.md)

<div dir="rtl" lang="fa">

از [راهنمای تفصیلی سخت‌افزار](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md)، شامل عکس‌های مرجع برچسب‌دار، پیروی کنید. WROOM یا S3 را صریحاً انتخاب کنید. پیش از اتصال سیم‌ها برق را قطع کنید، نام سیگنال‌ها و تغذیه و سطح منطقی ۳٫۳ ولت را بررسی کنید و از YAML موجود همان برد استفاده کنید. این صفحه نقشهٔ پایهٔ دیگری معرفی نمی‌کند.

1. [ESPHome را روی ESP32 نصب کنید](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). میان‌افزار ZAC93 را دست‌نخورده نگه دارید و اسرار محلی را خصوصی حفظ کنید.
2. [Z-Wave JS UI را به پراکسی بومی ESPHome و سپس HA را به WS Server آن متصل کنید](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). این‌ها دو اتصال جداگانه‌اند؛ درگاه API در ESP32 درگاه سرور Z-Wave برای HA نیست. دقیقاً یک درایور Z-Wave باید مسئول کنترل‌کننده باشد.
3. [حسگر واقعی را به شبکه اضافه و مشاهده کنید](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). روش افزودن مخصوص همان حسگر را دنبال و فرایند مصاحبهٔ شناسایی آن را کامل کنید. صرف اتصال به API این مرحله را تأیید نمی‌کند.
4. نسخه‌های نرم‌افزار، گزارش‌های واقعی و کاستی‌های باقی‌مانده را در پروندهٔ خصوصی راه‌اندازی ثبت کنید. پیش از مهاجرت یا به‌روزرسانی، NVM و کلیدهای شبکه را حفظ کنید.

راهنمای HA شامل تصاویر مرجع خارجی با ذکر منبع است؛ این تصاویر سند تصویری ساختی نیستند که در اینجا واقعاً راه‌اندازی فیزیکی شده باشد. برای درک تفاوت، [وضعیت اعتبارسنجی](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) را بخوانید.

</div>
