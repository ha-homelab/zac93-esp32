# समस्या निवारण और पुनर्प्राप्ति

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

[ZAC93 + ESP32 दस्तावेज़](Home-hi.md) · [कनेक्शन और पहली बार नेटवर्क में शामिल करना](Connection-hi.md)

[प्रामाणिक समस्या निवारण गाइड](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md) इस्तेमाल करें। पहली विफल परत से शुरू करें और एक समय में केवल एक कारक बदलें:

1. **बिजली और वायरिंग:** सप्लाई की स्थिरता, साझा ग्राउंड, कनेक्टर की दिशा और सिग्नल लेबल। वायरिंग बदलने से पहले बिजली बंद करें।
2. **नेटवर्क:** Z-Wave JS होस्ट की पहुँच ESP32 तक होनी चाहिए; मल्टीकास्ट खोज और ping का उत्तर API का सत्यापन नहीं हैं।
3. **एन्क्रिप्टेड API:** सही कुंजी, नेटिव ट्रांसपोर्ट और URL एन्कोडिंग। कनेक्शन URL सार्वजनिक इश्यू में पेस्ट न करें।
4. **UART और रेडियो:** कंट्रोलर की पहचान उसके एकमात्र ड्राइवर द्वारा होनी चाहिए। असंबंधित तस्वीर से अनुमानित पिन मैप के बजाय दस्तावेज़ में दिया गया बोर्ड कॉन्फ़िगरेशन इस्तेमाल करें।
5. **सेंसर और HA:** नेटवर्क में शामिल करने, इंटरव्यू और रिपोर्टिंग की समस्याओं को WS Server और HA एंटिटी की समस्याओं से अलग समझें।

![निदान की परतें](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

अपडेट से पहले [बैकअप और रखरखाव प्रक्रियाओं](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md) का पालन करें। फ़ैक्टरी रीसेट नेटवर्क की स्थिति मिटा देता है और Wi-Fi, कुंजी या UART त्रुटियों का सामान्य उपाय नहीं है। इस प्रॉक्सी के जरिए कंट्रोलर बहाल करना और रेडियो अपडेट करना अभी भी [असत्यापित हार्डवेयर मदों](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) में शामिल हैं।

समस्या की रिपोर्ट करते समय बोर्ड की पहचान, संस्करण, पहली विफल परत और संवेदनशील जानकारी हटाकर तैयार किए गए अवलोकन शामिल करें। [सुरक्षा मार्गदर्शन](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md) का पालन करें: Wi-Fi/API/OTA/Z-Wave कुंजियाँ, DSK, निजी पते, कच्चे बैकअप या कम्पाइल किया हुआ निजी फ़र्मवेयर साझा न करें।
