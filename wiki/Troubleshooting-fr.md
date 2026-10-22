# Dépannage et récupération

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

[Documentation ZAC93 + ESP32](Home-fr.md) · [Connexion et première inclusion](Connection-fr.md)

Utilisez le [guide de dépannage de référence](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md). Partez de la première couche défaillante et ne modifiez qu’un facteur à la fois :

1. **Alimentation et câblage :** stabilité de l’alimentation, masse commune, orientation des connecteurs et étiquettes des signaux. Coupez l’alimentation avant toute modification du câblage.
2. **Réseau :** l’hôte Z-Wave JS doit joindre l’ESP32 ; la découverte multicast et une réponse au ping ne vérifient pas l’API.
3. **API chiffrée :** clé correcte, transport natif et encodage des URL. Ne collez pas les URL de connexion dans des tickets publics.
4. **UART et radio :** le contrôleur doit être identifié par son unique pilote. Utilisez la configuration documentée de la carte, pas un brochage déduit d’une photographie sans rapport.
5. **Capteur et HA :** distinguez inclusion, entretien d’identification et remontée des rapports des problèmes de WS Server et d’entités HA.

![Couches de diagnostic](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

Suivez les [procédures de sauvegarde et de maintenance](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md) avant les mises à jour. Une réinitialisation d’usine efface l’état du réseau et n’est pas un remède normal aux erreurs Wi-Fi, de clé ou d’UART. La restauration du contrôleur et les mises à jour radio via ce proxy figurent toujours parmi les [points matériels non vérifiés](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md).

Pour signaler un problème, indiquez l’identité de la carte, les versions, la première couche défaillante et des observations expurgées. Respectez les [consignes de sécurité](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md) : aucune clé Wi-Fi/API/OTA/Z-Wave, aucun DSK, aucune adresse privée, sauvegarde brute ou image compilée de firmware personnel.
