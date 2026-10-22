# সমস্যা সমাধান ও পুনরুদ্ধার

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

[ZAC93 + ESP32 নথিপত্র](Home-bn.md) · [সংযোগ ও প্রথমবার নেটওয়ার্কে অন্তর্ভুক্তি](Connection-bn.md)

[প্রামাণ্য সমস্যা সমাধানের নির্দেশিকা](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md) ব্যবহার করুন। প্রথম যে স্তরটি ব্যর্থ হচ্ছে সেখান থেকে শুরু করুন, প্রতিবার কেবল একটি বিষয় বদলান:

1. **বিদ্যুৎ ও তার সংযোগ:** সরবরাহের স্থিতিশীলতা, অভিন্ন গ্রাউন্ড, সংযোজকের অভিমুখ ও সিগন্যাল লেবেল। তার সংযোগ বদলানোর আগে বিদ্যুৎ বিচ্ছিন্ন করুন।
2. **নেটওয়ার্ক:** Z-Wave JS হোস্ট থেকে ESP32-তে পৌঁছানো সম্ভব হতে হবে; মাল্টিকাস্ট আবিষ্কার এবং ping-এর উত্তর API যাচাইকরণ নয়।
3. **এনক্রিপ্টেড API:** সঠিক কী, নেটিভ ট্রান্সপোর্ট ও URL এনকোডিং। সংযোগের URL প্রকাশ্য ইস্যুতে পেস্ট করবেন না।
4. **UART ও রেডিও:** কন্ট্রোলারকে তার একমাত্র দায়িত্বপ্রাপ্ত ড্রাইভার দিয়ে শনাক্ত হতে হবে। অসংশ্লিষ্ট ছবি থেকে অনুমান করা পিন বিন্যাস নয়, নথিভুক্ত বোর্ড কনফিগারেশন ব্যবহার করুন।
5. **সেন্সর ও HA:** অন্তর্ভুক্তি, interview ও রিপোর্টিংয়ের সমস্যাকে WS Server এবং HA এন্টিটির সমস্যা থেকে আলাদা করুন।

![রোগনির্ণয়ের স্তর](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

আপডেটের আগে [ব্যাকআপ ও রক্ষণাবেক্ষণের পদ্ধতি](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md) অনুসরণ করুন। ফ্যাক্টরি রিসেট নেটওয়ার্কের অবস্থা মুছে দেয় এবং Wi-Fi, কী বা UART ত্রুটির স্বাভাবিক সমাধান নয়। এই প্রক্সির মাধ্যমে কন্ট্রোলার পুনরুদ্ধার ও রেডিও আপডেট এখনও [যাচাই না হওয়া হার্ডওয়্যার বিষয়গুলোর](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) মধ্যে রয়েছে।

সমস্যা জানানোর সময় বোর্ডের পরিচয়, সংস্করণ, প্রথম ব্যর্থ স্তর এবং সংবেদনশীল তথ্য বাদ দেওয়া পর্যবেক্ষণ দিন। [নিরাপত্তা নির্দেশনা](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md) অনুসরণ করুন: Wi-Fi/API/OTA/Z-Wave কী, DSK, ব্যক্তিগত ঠিকানা, অপরিবর্তিত ব্যাকআপ বা কম্পাইল করা ব্যক্তিগত ফার্মওয়্যার প্রকাশ করবেন না।
