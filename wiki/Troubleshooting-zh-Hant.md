# 疑難排解與復原

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

[ZAC93 + ESP32 文件](Home-zh-Hant.md) · [連線與首次加入網路](Connection-zh-Hant.md)

使用[權威疑難排解指南](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md)。從第一個發生故障的層級開始，每次只改變一個因素：

1. **供電與接線：**檢查供電穩定性、共地、連接器方向與訊號標籤。變更接線前先斷電。
2. **網路：**Z-Wave JS 主機必須能夠存取 ESP32；多播探索和 ping 回應並不等於 API 驗證。
3. **加密 API：**檢查正確的金鑰、原生傳輸方式和 URL 編碼。不要將連線 URL 貼到公開 issue 中。
4. **UART 與無線電：**控制器必須由其唯一驅動程式識別。使用文件所述的開發板設定，不要從無關照片推斷接腳定義。
5. **感測器與 HA：**區分加入網路、裝置資訊訪談與回報問題，以及 WS Server 和 HA 實體問題。

![診斷層級](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

更新前遵循[備份與維護流程](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md)。恢復原廠設定會清除網路狀態，並非解決 Wi-Fi、金鑰或 UART 錯誤的常規方法。透過此代理復原控制器或更新無線電韌體，仍屬於[尚未驗證的硬體事項](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md)。

回報問題時，應提供開發板識別資訊、版本、第一個發生故障的層級，以及已移除敏感資訊的觀察結果。遵循[安全性指南](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md)：不得提供 Wi-Fi/API/OTA/Z-Wave 金鑰、DSK、私人位址、原始備份或編譯後的個人韌體。
