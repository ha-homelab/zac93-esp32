# 連線與首次加入網路

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

[ZAC93 + ESP32 文件](Home-zh-Hant.md) · [疑難排解與復原](Troubleshooting-zh-Hant.md)

請遵循詳細的[硬體指南](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md)，包括附有標註的參考照片。明確選擇 WROOM 或 S3。接線前先斷電，核對訊號名稱以及 3.3 V 供電與邏輯準位，並使用對應開發板既有的 YAML。本頁不提供另一套接腳定義。

1. [在 ESP32 上安裝 ESPHome](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md)。保留 ZAC93 原有韌體，並妥善保密本機金鑰等敏感資訊。
2. [將 Z-Wave JS UI 連線至原生 ESPHome 代理，再將 HA 連線至其 WS Server](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md)。這是兩個獨立連線；ESP32 的 API 連接埠並不是 HA 所用的 Z-Wave 伺服器連接埠。必須僅由一個 Z-Wave 驅動程式負責控制器。
3. [將實際感測器加入網路並觀察其運作](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md)。遵循感測器本身的加入網路流程，並完成裝置資訊訪談（interview）。只有 API 連通性不能確認此步驟已完成。
4. 在私人試運轉驗收紀錄中記下軟體版本、實際回報與剩餘缺項。遷移或更新前保存 NVM 和網路金鑰。

HA 指南中的外部參考螢幕擷取畫面均標註來源；它們並非此處某個已完成實體試運轉驗收之裝置的畫面紀錄。請閱讀[驗證狀態](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md)，了解兩者區別。
