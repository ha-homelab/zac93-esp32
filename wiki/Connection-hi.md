# कनेक्शन और पहली बार नेटवर्क में शामिल करना

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

[ZAC93 + ESP32 दस्तावेज़](Home-hi.md) · [समस्या निवारण और पुनर्प्राप्ति](Troubleshooting-hi.md)

लेबल वाली संदर्भ तस्वीरों सहित विस्तृत [हार्डवेयर गाइड](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md) का पालन करें। WROOM या S3 स्पष्ट रूप से चुनें। तार जोड़ने से पहले बिजली बंद करें, सिग्नल के नाम तथा 3.3 V सप्लाई और लॉजिक स्तर जाँचें, और उसी बोर्ड का मौजूदा YAML इस्तेमाल करें। यह पृष्ठ कोई दूसरा पिन मैप प्रस्तुत नहीं करता।

1. [ESP32 पर ESPHome इंस्टॉल करें](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md)। ZAC93 का फ़र्मवेयर अपरिवर्तित रखें और स्थानीय गोपनीय जानकारी निजी रखें।
2. [Z-Wave JS UI को नेटिव ESPHome प्रॉक्सी से, फिर HA को उसके WS Server से जोड़ें](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md)। ये दो अलग कनेक्शन हैं; ESP32 का API पोर्ट HA के Z-Wave सर्वर का पोर्ट नहीं है। कंट्रोलर की जिम्मेदारी ठीक एक Z-Wave ड्राइवर के पास होनी चाहिए।
3. [वास्तविक सेंसर को शामिल करें और उसका व्यवहार देखें](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md)। सेंसर की अपनी नेटवर्क में शामिल करने की प्रक्रिया का पालन करें और उसका इंटरव्यू पूरा करें। केवल API कनेक्टिविटी इस चरण की पुष्टि नहीं करती।
4. निजी कमीशनिंग रिकॉर्ड में सॉफ़्टवेयर संस्करण, वास्तविक रिपोर्ट और बाकी कमियाँ दर्ज करें। माइग्रेशन या अपडेट से पहले NVM और नेटवर्क कुंजियाँ सुरक्षित रखें।

HA गाइड में स्रोत का उल्लेख करते हुए बाहरी संदर्भ स्क्रीनशॉट दिए गए हैं; ये यहाँ भौतिक रूप से चालू और परीक्षित किसी निर्माण के स्क्रीनशॉट का रिकॉर्ड नहीं हैं। अंतर समझने के लिए [सत्यापन स्थिति](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) पढ़ें।
