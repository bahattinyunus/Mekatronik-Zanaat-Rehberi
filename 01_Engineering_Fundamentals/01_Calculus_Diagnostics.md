# 🩺 Kalkülüs ile Sistem Teşhisi (Calculus Diagnostics)

> *"Diferansiyel denklemler sadece kağıt üzerinde çözülmez; makinenin titremesinde, ısınmasında ve sesinde yaşarlar."*

Bir "Teknoloji Mimarı" ve "Siber Tamirci" için türev ve integral, sadece sınav geçmek için değildir. Bunlar, makinenin sağlığını izleyen en temel göstergelerdir.

## 1. Türev (Derivative): Hata Hızı ve Öngörü

Türev, ani değişimdir. Bir şeyin ne kadar hızlı kötüye gittiğini anlatır.

### Saha Senaryosu: Isınan Motor
Bir motorun sıcaklığını ölçüyorsunuz.
*   **Durum A:** Sıcaklık 40°C, 5 dakika sonra 45°C. Türev (Eğim) düşüktür. Sorun yok.
*   **Durum B:** Sıcaklık 40°C, 1 dakika sonra 60°C. Türev çok yüksektir.
    *   **Teşhis:** Motorun yükü aniden arttı veya soğutma fanı durdu.
    *   **Aksiyon:** Termal koruma (Thermal Shutdown) beklemeden sistemi kapat. Türev based (türev tabanlı) koruma budur.

### Saha Senaryosu: PID Kontrol - D Terimi
Robot kolu hedefe gidiyor.
*   Sadece hataya bakarsan (P), robot hızla hedefe koşar ve duramaz, çarpar (Overshoot).
*   Hatadaki değişime bakarsan (D), robot "çok hızlı yaklaşıyorum, fren yapmalıyım" der.
*   **Kural:** D katsayısı, sistemin "geleceği görme" yeteneğidir.

## 2. İntegral (Integral): Geçmişin Birikimi

İntegral, hafızadır. Küçük sorunların zamanla nasıl büyük bir dağa dönüştüğünü anlatır.

### Saha Senaryosu: Hidrolik Sızıntı
Basınç tankında çok küçük bir kaçak var.
*   Anlık basınç düşüşü (Bar/saniye) neredeyse sıfırdır. Sensör fark etmez.
*   Ama 1 saat boyunca bu kaybı toplarsan (İntegral alırsan), tankın yarısının boşaldığını görürsün.
*   **Teşhis:** "Steady State Error" (Kalıcı Durum Hatası).
*   **Aksiyon:** PID'deki 'I' terimi, "hedefe ulaşamadım, biraz daha güç ver" der. Ancak sızıntı varsa, I terimi sonsuza kadar artar (Integral Windup) ve sistemi patlatabilir. Buna dikkat et.

---
> **Ustanın Notu:** "Makinenin sesindeki değişimi (türev) kulağınla duyarsın. Makinenin altındaki yağ birikintisini (integral) gözünle görürsün. Matematik, sadece bu duyularını sayıya dökmektir."
