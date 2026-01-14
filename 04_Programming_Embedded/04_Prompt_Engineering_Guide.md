# 🤖 İstemi Mühendisliği (Prompt Engineering): AI ile Kodlama

> *"AI bir stajyerdir; ne kadar iyi tarif ederseniz o kadar iyi iş çıkarır. 'Bunu yap' derseniz saçmalar, 'Bunu şu standartta, şu kısıtlarla yap' derseniz harikalar yaratır."*

Gömülü sistemler için AI kullanırken, genel geçer kod değil, donanıma özel (hardware-aware) kod istemelisiniz.

## 1. Altın Şablon (The Golden Template)

AI'dan (ChatGPT, Claude, Copilot) kod isterken şu şablonu kullanın:

*   **Rol:** "Sen kıdemli bir Gömülü Sistem Mühendisisin (Senior Embedded Engineer)."
*   **Donanım:** "Hedef işlemci: STM32F407VG. Saat hızı: 168MHz."
*   **Kütüphane:** "STM32 HAL Kütüphanesini kullan. (Veya Register-level)"
*   **Görev:** "UART üzerinden DMA ile veri alan ve veriyi Ring Buffer'a yazan bir sürücü yaz."
*   **Kısıtlar (Çok Önemli):**
    *   "Asla `HAL_Delay` veya blocking fonksiyon kullanma."
    *   "Kesme (Interrupt) içinde minimum işlem yap."
    *   "Hata durumlarını (Timeout, Overrun) yönet."
    *   "Kodu C99 standardında yaz ve bol yorum satırı ekle."

## 2. Hata Ayıklama İstemleri

AI sadece kod yazmaz, hata da bulur.
*   **İstemi:** "Aşağıdaki ISR (Kesme Servis Rutini) kodunda bir 'Race Condition' veya 'Priority Inversion' riski var mı? Varsa nasıl düzeltirim?"
*   **İstemi:** "Bu `while` döngüsünün sonsuz döngüye girip sistemi kilitleme (Deadlock) ihtimali var mı? Bir watchdog veya timeout mekanizması ekle."

## 3. Kod Optimizasyonu
*   **İstemi:** "Bu fonksiyonu hızlandırmam lazım. Gereksiz değişken kopyalamalarını kaldır, pointer kullanarak `pass-by-reference` yap ve `inline` kullanmayı değerlendir."

---
> **Ustanın Notu:** "AI'ın yazdığı kodu asla körü körüne kopyalama. O kodun işlemcinin hangi bacağını (GPIO) açtığını, hangi saati (RCC Clock) aktif ettiğini datasheet'ten doğrula. AI halüsinasyon görüp olmayan bir pini tanımlayabilir. Son sorumluluk her zaman senindir."
