# חיבור וצירוף ראשון לרשת

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

[תיעוד ZAC93 + ESP32](Home-he.md) · [פתרון בעיות ושחזור](Troubleshooting-he.md)

<div dir="rtl" lang="he">

פעלו לפי [מדריך החומרה המפורט](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md), כולל תצלומי הייחוס המסומנים. בחרו במפורש WROOM או S3. נתקו את החשמל לפני חיבור חוטים, בדקו את שמות האותות ואת מתח האספקה והרמות הלוגיות של 3.3 V, והשתמשו ב־YAML הקיים של אותה לוחית. עמוד זה אינו מציג מפת פינים נוספת.

1. [התקינו ESPHome על ה־ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). השאירו את קושחת ZAC93 ללא שינוי ושמרו סודות מקומיים באופן פרטי.
2. [חברו Z-Wave JS UI לפרוקסי המקורי של ESPHome, ולאחר מכן חברו את HA ל־WS Server שלו](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). אלו שני חיבורים נפרדים; פורט ה־API של ESP32 אינו פורט שרת ה־Z-Wave של HA. ודאו שבדיוק מנהל התקן אחד של Z-Wave אחראי לבקר.
3. [צרפו את החיישן האמיתי לרשת וצפו בפעולתו](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). פעלו לפי נוהל הצירוף של החיישן עצמו והשלימו את תהליך התשאול שלו. חיבור API לבדו אינו מאשר שלב זה.
4. תעדו גרסאות תוכנה, דיווחים אמיתיים ופערים שנותרו ברישום הפעלה ראשונית פרטי. שמרו את ה־NVM ואת מפתחות הרשת לפני מעבר או עדכון.

מדריך HA כולל צילומי מסך חיצוניים לעיון עם ייחוס למקור; הם אינם תיעוד בצילומי מסך של מערכת שהופעלה ונבדקה פיזית כאן. קראו את [מצב האימות](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) כדי להבין את ההבחנה.

</div>
