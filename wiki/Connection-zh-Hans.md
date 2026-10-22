# 连接与首次入网

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

[ZAC93 + ESP32 文档](Home-zh-Hans.md) · [故障排查与恢复](Troubleshooting-zh-Hans.md)

请遵循详细的[硬件指南](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md)，包括带标注的参考照片。明确选择 WROOM 或 S3。接线前先断电，核对信号名称以及 3.3 V 供电和逻辑电平，并使用对应开发板已有的 YAML。本页不提供另一套引脚定义。

1. [在 ESP32 上安装 ESPHome](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md)。保留 ZAC93 原有固件，并妥善保密本地密钥等敏感信息。
2. [将 Z-Wave JS UI 连接到原生 ESPHome 代理，再将 HA 连接到其 WS Server](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md)。这是两个独立连接；ESP32 的 API 端口并不是 HA 所用的 Z-Wave 服务器端口。必须仅由一个 Z-Wave 驱动负责控制器。
3. [将实际传感器加入网络并观察其表现](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md)。遵循传感器自己的入网流程，并完成设备信息访谈（interview）。仅有 API 连通性不能确认此步骤已完成。
4. 在私有调试验收记录中记下软件版本、实际报告和剩余缺项。迁移或更新前保存 NVM 和网络密钥。

HA 指南中的外部参考截图均标注了来源；它们并非此处某个已完成实物调试验收的装置的截图记录。请阅读[验证状态](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md)，了解两者区别。
