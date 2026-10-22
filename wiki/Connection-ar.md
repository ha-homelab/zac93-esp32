# التوصيل والإضافة الأولى إلى الشبكة

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

[وثائق ZAC93 + ESP32](Home-ar.md) · [استكشاف الأخطاء والاستعادة](Troubleshooting-ar.md)

<div dir="rtl" lang="ar">

اتبع [دليل العتاد المفصل](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md)، بما فيه الصور المرجعية ذات التسميات. اختر WROOM أو S3 صراحة. افصل الطاقة قبل توصيل الأسلاك، وتحقق من أسماء الإشارات ومن تغذية ومستويات منطق 3.3 فولت، واستخدم ملف YAML الموجود لتلك اللوحة. لا تقدم هذه الصفحة مخطط أطراف آخر.

1. [ثبّت ESPHome على ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). أبقِ البرنامج الثابت لـZAC93 دون تغيير واحتفظ بالأسرار المحلية بشكل خاص.
2. [وصّل Z-Wave JS UI بوكيل ESPHome الأصلي، ثم وصّل HA بخادم WS Server الخاص به](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). هذان اتصالان منفصلان؛ منفذ API في ESP32 ليس منفذ خادم Z-Wave الخاص بـHA. اجعل برنامج تشغيل Z-Wave واحدًا فقط مسؤولًا عن وحدة التحكم.
3. [أضف المستشعر الفعلي وراقبه](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). اتبع إجراء الإضافة الخاص بالمستشعر وأكمل استجواب معلوماته (interview). الاتصال بـAPI وحده لا يؤكد إنجاز هذه الخطوة.
4. سجّل إصدارات البرامج والتقارير الفعلية والنواقص المتبقية في سجل تشغيل تجريبي خاص. احفظ NVM ومفاتيح الشبكة قبل الترحيل أو التحديثات.

يحتوي دليل HA على لقطات شاشة مرجعية خارجية مع ذكر مصادرها؛ وهي ليست سجل لقطات لبناء خضع هنا لتشغيل تجريبي فعلي. اقرأ [حالة التحقق](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) لفهم الفرق.

</div>
