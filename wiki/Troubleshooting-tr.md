# Sorun giderme ve kurtarma

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

[ZAC93 + ESP32 belgeleri](Home-tr.md) · [Bağlantı ve ilk ağa dahil etme](Connection-tr.md)

[Esas sorun giderme kılavuzunu](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/troubleshooting.md) kullanın. İlk başarısız katmandan başlayın ve her seferinde tek bir etkeni değiştirin:

1. **Güç ve kablolama:** besleme kararlılığı, ortak toprak, konektör yönü ve sinyal etiketleri. Kablolamayı değiştirmeden önce gücü kesin.
2. **Ağ:** Z-Wave JS ana makinesi ESP32'ye erişebilmelidir; multicast keşfi ve ping yanıtı API doğrulaması değildir.
3. **Şifreli API:** doğru anahtar, yerel aktarım ve URL kodlaması. Bağlantı URL'lerini herkese açık sorun kayıtlarına yapıştırmayın.
4. **UART ve radyo:** denetleyici, kendisinden sorumlu tek sürücü tarafından tanınmalıdır. İlgisiz bir fotoğraftan çıkarılan pin düzeni yerine belgelenmiş kart yapılandırmasını kullanın.
5. **Sensör ve HA:** ağa dahil etme, interview ve raporlamayı WS Server ve HA varlığı sorunlarından ayırın.

![Tanılama katmanları](https://raw.githubusercontent.com/ha-homelab/zac93-esp32/main/assets/diagrams/diagnostic-ladder.svg)

Güncellemelerden önce [yedekleme ve bakım prosedürlerini](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/commissioning.md) izleyin. Fabrika ayarlarına sıfırlama ağ durumunu siler; Wi-Fi, anahtar veya UART hatalarının olağan çözümü değildir. Bu proxy üzerinden denetleyici geri yükleme ve radyo güncellemeleri hâlâ [doğrulanmamış donanım maddeleri](https://github.com/ha-homelab/zac93-esp32/blob/main/docs/validation.md) arasındadır.

Sorun bildirirken kart kimliğini, sürümleri, ilk başarısız katmanı ve hassas bilgilerden arındırılmış gözlemleri ekleyin. [Güvenlik yönergelerine](https://github.com/ha-homelab/zac93-esp32/blob/main/SECURITY.md) uyun: Wi-Fi/API/OTA/Z-Wave anahtarı, DSK, özel adres, ham yedek veya derlenmiş kişisel ürün yazılımı paylaşmayın.
