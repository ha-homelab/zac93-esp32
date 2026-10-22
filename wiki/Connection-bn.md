# সংযোগ ও প্রথমবার নেটওয়ার্কে অন্তর্ভুক্তি

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

[ZAC93 + ESP32 নথিপত্র](Home-bn.md) · [সমস্যা সমাধান ও পুনরুদ্ধার](Troubleshooting-bn.md)

লেবেলযুক্ত রেফারেন্স ছবিসহ বিস্তারিত [হার্ডওয়্যার নির্দেশিকা](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md) অনুসরণ করুন। স্পষ্টভাবে WROOM বা S3 নির্বাচন করুন। তার লাগানোর আগে বিদ্যুৎ বিচ্ছিন্ন করুন, সিগন্যালের নাম এবং 3.3 V সরবরাহ ও লজিক স্তর যাচাই করুন, এবং ওই বোর্ডের বিদ্যমান YAML ব্যবহার করুন। এই পৃষ্ঠায় আরেকটি পিন বিন্যাস দেওয়া হচ্ছে না।

1. [ESP32-তে ESPHome ইনস্টল করুন](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md)। ZAC93-এর ফার্মওয়্যার অপরিবর্তিত রাখুন এবং স্থানীয় গোপন তথ্য ব্যক্তিগতভাবে সংরক্ষণ করুন।
2. [Z-Wave JS UI-কে নেটিভ ESPHome প্রক্সির সঙ্গে, তারপর HA-কে সেটির WS Server-এর সঙ্গে যুক্ত করুন](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md)। এগুলো দুটি আলাদা সংযোগ; ESP32-এর API পোর্ট HA-এর Z-Wave সার্ভারের পোর্ট নয়। ঠিক একটি Z-Wave ড্রাইভারকে কন্ট্রোলারের দায়িত্ব দিন।
3. [প্রকৃত সেন্সরটি অন্তর্ভুক্ত করে পর্যবেক্ষণ করুন](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md)। সেন্সরের নিজস্ব অন্তর্ভুক্তির পদ্ধতি মেনে তার interview সম্পন্ন করুন। শুধু API সংযোগ এই ধাপ সম্পন্ন হওয়ার প্রমাণ নয়।
4. ব্যক্তিগত কমিশনিং রেকর্ডে সফ্টওয়্যারের সংস্করণ, প্রকৃত রিপোর্ট এবং বাকি ঘাটতি লিখে রাখুন। মাইগ্রেশন বা আপডেটের আগে NVM ও নেটওয়ার্কের কী সংরক্ষণ করুন।

HA নির্দেশিকায় উৎস উল্লেখ করা বাইরের রেফারেন্স স্ক্রিনশট রয়েছে; এগুলো এখানে বাস্তবে চালু ও পরীক্ষা করা কোনো নির্মাণের স্ক্রিনশট রেকর্ড নয়। পার্থক্যটি জানতে [যাচাইকরণের অবস্থা](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) পড়ুন।
