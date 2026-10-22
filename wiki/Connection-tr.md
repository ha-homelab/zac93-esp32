# Bağlantı ve ilk ağa dahil etme

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

[ZAC93 + ESP32 belgeleri](Home-tr.md) · [Sorun giderme ve kurtarma](Troubleshooting-tr.md)

Etiketli referans fotoğrafları da içeren ayrıntılı [donanım kılavuzunu](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/hardware.md) izleyin. WROOM veya S3 seçimini açıkça yapın. Kabloları bağlamadan önce gücü kesin, sinyal adlarını ve 3,3 V besleme/mantık seviyelerini doğrulayın ve o kartın mevcut YAML dosyasını kullanın. Bu sayfa başka bir pin düzeni tanımlamaz.

1. [ESP32 üzerine ESPHome kurun](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/firmware.md). ZAC93 ürün yazılımını değiştirmeyin ve yerel gizli bilgileri özel tutun.
2. [Z-Wave JS UI'ı yerel ESPHome proxy'sine, ardından HA'yı onun WS Server'ına bağlayın](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/home-assistant.md). Bunlar iki ayrı bağlantıdır; ESP32'nin API portu, HA'nın Z-Wave sunucu portu değildir. Denetleyiciden tam olarak bir Z-Wave sürücüsü sorumlu olsun.
3. [Gerçek sensörü ağa dahil edin ve gözlemleyin](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md). Sensörün kendi dahil etme prosedürünü izleyin ve görüşmesini (interview) tamamlayın. Yalnızca API bağlantısı bu adımı doğrulamaz.
4. Yazılım sürümlerini, gerçek raporları ve kalan eksikleri özel bir devreye alma kaydına yazın. Geçiş veya güncellemelerden önce NVM'yi ve ağ anahtarlarını koruyun.

HA kılavuzunda kaynakları belirtilmiş harici referans ekran görüntüleri bulunur; bunlar burada fiziksel olarak devreye alınmış bir yapının ekran görüntüsü kaydı değildir. Aradaki fark için [doğrulama durumunu](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) okuyun.
