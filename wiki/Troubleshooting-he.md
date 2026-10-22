# פתרון בעיות ושחזור

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

[תיעוד ZAC93 + ESP32](Home-he.md) · [חיבור וצירוף ראשון לרשת](Connection-he.md)

<div dir="rtl" lang="he">

השתמשו ב[מדריך הקובע לפתרון בעיות](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md). התחילו בשכבה הראשונה שנכשלת ושנו גורם אחד בכל פעם:

1. **חשמל וחיווט:** יציבות האספקה, הארקה משותפת, כיוון המחבר ותוויות האותות. נתקו את החשמל לפני שינוי החיווט.
2. **רשת:** מארח Z-Wave JS חייב להגיע ל־ESP32; גילוי multicast ותשובת ping אינם אימות של ה־API.
3. **API מוצפן:** מפתח נכון, תעבורה מקורית וקידוד URL. אל תדביקו כתובות חיבור בדיווחי תקלה פומביים.
4. **UART ורדיו:** הבקר חייב להיות מזוהה על ידי מנהל ההתקן היחיד שלו. השתמשו בתצורת הלוחית המתועדת, ולא במפת פינים שהוסקה מתמונה לא קשורה.
5. **חיישן ו־HA:** הבדילו בין צירוף, תשאול ודיווח לבין בעיות של WS Server וישויות HA.

![שכבות אבחון](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

פעלו לפי [נוהלי הגיבוי והתחזוקה](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md) לפני עדכונים. איפוס להגדרות יצרן מוחק את מצב הרשת ואינו פתרון רגיל לשגיאות Wi-Fi, מפתחות או UART. שחזור הבקר ועדכוני הרדיו דרך פרוקסי זה עדיין נכללים ב[פריטי החומרה שלא אומתו](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).

בדיווח תקלה כללו את זיהוי הלוחית, הגרסאות, השכבה הראשונה שנכשלת ותצפיות שמהן הוסרו נתונים רגישים. פעלו לפי [הנחיות האבטחה](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md): אין לפרסם מפתחות Wi-Fi/API/OTA/Z-Wave,‏ DSK, כתובות פרטיות, גיבויים גולמיים או קושחה אישית מהודרת.

</div>
