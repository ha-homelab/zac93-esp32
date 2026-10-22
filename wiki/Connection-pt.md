# Ligação e primeira inclusão

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

[Documentação ZAC93 + ESP32](Home-pt.md) · [Diagnóstico e recuperação](Troubleshooting-pt.md)

Siga o [guia detalhado de hardware](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md), incluindo as fotografias de referência identificadas. Selecione explicitamente WROOM ou S3. Desligue a alimentação antes de ligar fios, verifique os nomes dos sinais e a alimentação e lógica de 3,3 V, e utilize o YAML existente dessa placa. Esta página não introduz outro mapa de pinos.

1. [Instale o ESPHome no ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). Mantenha intacto o firmware do ZAC93 e preserve a privacidade dos segredos locais.
2. [Ligue o Z-Wave JS UI ao proxy nativo do ESPHome e depois o HA ao respetivo WS Server](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). São duas ligações distintas; a porta API do ESP32 não é a porta do servidor Z-Wave do HA. Mantenha exatamente um controlador de software Z-Wave responsável pelo controlador físico.
3. [Inclua e observe o sensor real](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Siga o procedimento de inclusão do próprio sensor e conclua a sua entrevista. A conectividade API, por si só, não confirma este passo.
4. Registe versões do software, relatórios reais e lacunas restantes num registo privado de colocação em serviço. Preserve a NVM e as chaves de rede antes de migrações ou atualizações.

O guia do HA contém capturas de referência externas com atribuição; não documentam uma instalação fisicamente colocada em serviço aqui. Leia o [estado da validação](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) para compreender a distinção.
