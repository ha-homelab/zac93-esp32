# استكشاف الأخطاء والاستعادة

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

[وثائق ZAC93 + ESP32](Home-ar.md) · [التوصيل والإضافة الأولى إلى الشبكة](Connection-ar.md)

<div dir="rtl" lang="ar">

استخدم [دليل استكشاف الأخطاء المعتمد](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md). ابدأ بأول طبقة تفشل، وغيّر عاملًا واحدًا في كل مرة:

1. **الطاقة والأسلاك:** استقرار التغذية والأرضي المشترك واتجاه الموصل وتسميات الإشارات. افصل الطاقة قبل تعديل الأسلاك.
2. **الشبكة:** يجب أن يتمكن مضيف Z-Wave JS من الوصول إلى ESP32؛ الاكتشاف متعدد البث والرد على ping ليسا تحققًا من API.
3. **API المشفر:** المفتاح الصحيح والنقل الأصلي وترميز URL. لا تلصق عناوين URL للاتصال في البلاغات العامة.
4. **UART والراديو:** يجب أن يتعرف برنامج التشغيل الوحيد المسؤول على وحدة التحكم. استخدم إعداد اللوحة الموثق، لا مخطط أطراف مستنتجًا من صورة غير مرتبطة.
5. **المستشعر وHA:** ميّز الإضافة واستجواب المعلومات والتقارير عن مشكلات WS Server وكيانات HA.

![طبقات التشخيص](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

اتبع [إجراءات النسخ الاحتياطي والصيانة](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md) قبل التحديثات. إعادة ضبط المصنع تمحو حالة الشبكة وليست علاجًا اعتياديًا لأخطاء Wi-Fi أو المفاتيح أو UART. لا تزال استعادة وحدة التحكم وتحديثات الراديو عبر هذا الوكيل ضمن [بنود العتاد غير المتحقق منها](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).

عند الإبلاغ عن مشكلة، أدرج هوية اللوحة والإصدارات وأول طبقة تفشل وملاحظات أزيلت منها البيانات الحساسة. اتبع [إرشادات الأمان](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md): لا تنشر مفاتيح Wi-Fi/API/OTA/Z-Wave أو DSK أو العناوين الخاصة أو النسخ الاحتياطية الخام أو البرامج الثابتة الشخصية المترجمة.

</div>
