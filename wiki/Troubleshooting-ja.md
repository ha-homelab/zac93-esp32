# トラブルシューティングと復旧

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

[ZAC93 + ESP32 ドキュメント](Home-ja.md) · [接続と初回のネットワーク登録](Connection-ja.md)

[正規のトラブルシューティングガイド](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md)を使用してください。最初に失敗する層から調べ、要因は一度に 1 つだけ変更します。

1. **電源と配線：**電源の安定性、共通グラウンド、コネクターの向き、信号ラベルを確認します。配線を変更する前に電源を切ってください。
2. **ネットワーク：**Z-Wave JS ホストから ESP32 に到達できる必要があります。マルチキャストによる検出や ping の応答は API の検証ではありません。
3. **暗号化 API：**正しいキー、ネイティブな通信方式、URL エンコードを確認します。接続 URL を公開 issue に貼り付けないでください。
4. **UART と無線：**コントローラーは、それを担当する唯一のドライバーによって識別される必要があります。無関係な写真から推測したピン配置ではなく、文書化された基板設定を使用してください。
5. **センサーと HA：**ネットワーク登録・インタビュー・レポートの問題を、WS Server や HA エンティティの問題と区別します。

![診断の層](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

更新前に[バックアップと保守の手順](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md)に従ってください。工場出荷時へのリセットはネットワーク状態を消去するため、Wi-Fi、キー、UART のエラーに対する通常の対処法ではありません。このプロキシ経由でのコントローラー復元や無線の更新は、引き続き[未検証のハードウェア項目](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md)です。

問題の報告には、基板の識別情報、バージョン、最初に失敗する層、機密情報を取り除いた観察結果を含めてください。[セキュリティ指針](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md)に従い、Wi-Fi/API/OTA/Z-Wave キー、DSK、非公開アドレス、生のバックアップ、コンパイル済みの個人用ファームウェアを公開しないでください。
