# 接続と初回のネットワーク登録

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

[ZAC93 + ESP32 ドキュメント](Home-ja.md) · [トラブルシューティングと復旧](Troubleshooting-ja.md)

ラベル付きの参考写真を含む詳細な[ハードウェアガイド](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md)に従ってください。WROOM または S3 を明示的に選びます。配線前に電源を切り、信号名と 3.3 V の電源・ロジックレベルを確認し、その基板用の既存の YAML を使用してください。このページは別のピン配置を定義しません。

1. [ESP32 に ESPHome をインストールします](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md)。ZAC93 のファームウェアは変更せず、ローカルの機密情報は非公開で保管してください。
2. [Z-Wave JS UI をネイティブ ESPHome プロキシに接続し、次に HA をその WS Server に接続します](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md)。これは独立した 2 つの接続です。ESP32 の API ポートは HA 用 Z-Wave サーバーのポートではありません。コントローラーを管理する Z-Wave ドライバーは必ず 1 つだけにしてください。
3. [実際のセンサーをネットワークに登録して動作を観察します](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md)。センサー固有の登録手順に従い、インタビューを完了してください。API がつながるだけでは、この手順の完了は確認できません。
4. ソフトウェアのバージョン、実際のレポート、残る不足事項を非公開の試運転記録に残してください。移行や更新の前に NVM とネットワークキーを保全します。

HA ガイドには出典を示した外部の参考スクリーンショットが含まれますが、ここで実機の試運転を完了した構成の画面記録ではありません。その違いは[検証状況](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md)を確認してください。
