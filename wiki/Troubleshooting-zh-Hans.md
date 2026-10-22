# 故障排查与恢复

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

[ZAC93 + ESP32 文档](Home-zh-Hans.md) · [连接与首次入网](Connection-zh-Hans.md)

使用[权威故障排查指南](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md)。从首个发生故障的层级开始，每次只改变一个因素：

1. **供电与接线：**检查供电稳定性、共地、连接器方向和信号标签。更改接线前先断电。
2. **网络：**Z-Wave JS 主机必须能够访问 ESP32；组播发现和 ping 响应不等于 API 验证。
3. **加密 API：**检查正确的密钥、原生传输方式和 URL 编码。不要将连接 URL 粘贴到公开 issue 中。
4. **UART 与无线电：**控制器必须由其唯一驱动识别。使用文档规定的开发板配置，不要从无关照片推断引脚定义。
5. **传感器与 HA：**区分入网、设备信息访谈和报告问题，以及 WS Server 和 HA 实体问题。

![诊断层级](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

更新前遵循[备份与维护流程](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md)。恢复出厂设置会清除网络状态，并非解决 Wi-Fi、密钥或 UART 错误的常规办法。通过此代理恢复控制器或更新无线电固件，仍属于[尚未验证的硬件事项](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md)。

报告问题时，应提供开发板标识、版本、首个发生故障的层级以及已脱敏的观察结果。遵循[安全指南](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md)：不得提供 Wi-Fi/API/OTA/Z-Wave 密钥、DSK、私有地址、原始备份或编译后的个人固件。
