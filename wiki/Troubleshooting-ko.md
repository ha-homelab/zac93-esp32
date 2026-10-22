# 문제 해결 및 복구

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

[ZAC93 + ESP32 문서](Home-ko.md) · [연결 및 최초 네트워크 포함](Connection-ko.md)

[기준 문제 해결 가이드](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md)를 사용하세요. 처음 실패하는 계층부터 확인하고 한 번에 하나의 요인만 바꾸세요.

1. **전원과 배선:** 전원 안정성, 공통 접지, 커넥터 방향, 신호 라벨을 확인하세요. 배선을 변경하기 전에 전원을 분리하세요.
2. **네트워크:** Z-Wave JS 호스트에서 ESP32에 접근할 수 있어야 합니다. 멀티캐스트 검색과 ping 응답은 API 검증이 아닙니다.
3. **암호화된 API:** 올바른 키, 네이티브 전송 방식, URL 인코딩을 확인하세요. 공개 이슈에 연결 URL을 붙여 넣지 마세요.
4. **UART 및 무선:** 컨트롤러는 이를 담당하는 단 하나의 드라이버가 식별해야 합니다. 관계없는 사진에서 추측한 핀 배치 대신 문서화된 보드 설정을 사용하세요.
5. **센서와 HA:** 포함, 인터뷰, 보고 문제와 WS Server 및 HA 엔티티 문제를 구분하세요.

![진단 계층](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

업데이트 전에 [백업 및 유지보수 절차](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md)를 따르세요. 공장 초기화는 네트워크 상태를 지우므로 Wi-Fi, 키, UART 오류를 해결하는 일반적인 방법이 아닙니다. 이 프록시를 통한 컨트롤러 복원 및 무선 업데이트는 여전히 [검증되지 않은 하드웨어 항목](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md)에 속합니다.

이슈를 보고할 때는 보드 식별 정보, 버전, 처음 실패하는 계층, 민감 정보를 제거한 관찰 결과를 포함하세요. [보안 지침](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md)을 따르세요. Wi-Fi/API/OTA/Z-Wave 키, DSK, 비공개 주소, 원본 백업, 컴파일된 개인용 펌웨어를 공개해서는 안 됩니다.
