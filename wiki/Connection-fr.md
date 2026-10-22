# Connexion et première inclusion

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

[Documentation ZAC93 + ESP32](Home-fr.md) · [Dépannage et récupération](Troubleshooting-fr.md)

Suivez le [guide matériel détaillé](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md), notamment les photographies de référence légendées. Choisissez explicitement WROOM ou S3. Coupez l’alimentation avant de connecter les fils, vérifiez les noms des signaux ainsi que l’alimentation et les niveaux logiques de 3,3 V, puis utilisez le YAML existant de cette carte. Cette page n’introduit pas un nouveau brochage.

1. [Installez ESPHome sur l’ESP32](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). Conservez le firmware du ZAC93 intact et gardez les secrets locaux privés.
2. [Connectez Z-Wave JS UI au proxy natif ESPHome, puis HA à son WS Server](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). Il s’agit de deux connexions distinctes ; le port API de l’ESP32 n’est pas le port du serveur Z-Wave de HA. Un seul pilote Z-Wave doit être responsable du contrôleur.
3. [Incluez le capteur réel et observez-le](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Suivez sa propre procédure d’inclusion et terminez son entretien d’identification. La seule connectivité API ne confirme pas cette étape.
4. Consignez les versions logicielles, les rapports réels et les lacunes restantes dans un dossier privé de mise en service. Sauvegardez la NVM et les clés réseau avant toute migration ou mise à jour.

Le guide HA contient des captures de référence externes avec attribution ; elles ne constituent pas la trace d’une installation physiquement mise en service ici. Consultez l’[état de validation](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) pour comprendre cette distinction.
