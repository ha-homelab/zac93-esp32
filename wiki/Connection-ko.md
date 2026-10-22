# 연결 및 최초 네트워크 포함

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

[ZAC93 + ESP32 문서](Home-ko.md) · [문제 해결 및 복구](Troubleshooting-ko.md)

라벨이 표시된 참고 사진을 포함한 자세한 [하드웨어 가이드](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md)를 따르세요. WROOM 또는 S3를 명시적으로 선택하세요. 배선을 연결하기 전에 전원을 분리하고 신호 이름과 3.3 V 전원 및 논리 레벨을 확인한 뒤 해당 보드의 기존 YAML을 사용하세요. 이 페이지는 별도의 핀 배치를 제시하지 않습니다.

1. [ESP32에 ESPHome을 설치하세요](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). ZAC93 펌웨어는 그대로 유지하고 로컬 비밀 정보는 비공개로 보관하세요.
2. [Z-Wave JS UI를 네이티브 ESPHome 프록시에 연결한 다음 HA를 해당 WS Server에 연결하세요](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). 두 연결은 별개입니다. ESP32의 API 포트는 HA에서 사용하는 Z-Wave 서버 포트가 아닙니다. 정확히 하나의 Z-Wave 드라이버만 컨트롤러를 담당하도록 하세요.
3. [실제 센서를 네트워크에 포함하고 관찰하세요](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). 센서 자체의 포함 절차에 따라 인터뷰를 완료하세요. API 연결만으로는 이 단계가 완료되었다고 확인할 수 없습니다.
4. 소프트웨어 버전, 실제 보고 데이터, 남은 미비점을 비공개 시운전 기록에 남기세요. 마이그레이션이나 업데이트 전에 NVM과 네트워크 키를 보존하세요.

HA 가이드에는 출처를 밝힌 외부 참고 스크린샷이 포함되어 있습니다. 이곳에서 실제 하드웨어 시운전을 마친 구성의 스크린샷 기록은 아닙니다. 차이점은 [검증 상태](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md)를 읽어 보세요.
