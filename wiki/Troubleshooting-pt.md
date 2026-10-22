# Diagnóstico e recuperação

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

[Documentação ZAC93 + ESP32](Home-pt.md) · [Ligação e primeira inclusão](Connection-pt.md)

Utilize o [guia de referência para diagnóstico](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md). Comece pela primeira camada com falha e altere apenas um fator de cada vez:

1. **Alimentação e cablagem:** estabilidade da alimentação, massa comum, orientação dos conectores e identificação dos sinais. Desligue a alimentação antes de alterar a cablagem.
2. **Rede:** o host do Z-Wave JS tem de alcançar o ESP32; a descoberta multicast e uma resposta ao ping não verificam a API.
3. **API encriptada:** chave correta, transporte nativo e codificação de URL. Não cole URLs de ligação em issues públicas.
4. **UART e rádio:** o controlador físico deve ser identificado pelo seu único driver. Use a configuração documentada da placa, não um mapa de pinos deduzido de uma fotografia sem relação.
5. **Sensor e HA:** distinga inclusão, entrevista e comunicação de relatórios de problemas do WS Server e das entidades HA.

![Camadas de diagnóstico](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

Siga os [procedimentos de cópia de segurança e manutenção](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md) antes de atualizar. A reposição de fábrica apaga o estado da rede e não é uma solução normal para erros de Wi-Fi, chaves ou UART. A recuperação do controlador e as atualizações de rádio através deste proxy continuam entre os [itens de hardware não verificados](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).

Ao comunicar um problema, inclua a identidade da placa, as versões, a primeira camada com falha e observações sem dados sensíveis. Siga as [orientações de segurança](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md): não inclua chaves Wi-Fi/API/OTA/Z-Wave, DSK, endereços privados, cópias de segurança em bruto ou firmware pessoal compilado.
