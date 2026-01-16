# 🤖 İstemi Mühendisliği (Prompt Engineering): AI ile Donanım Kodlama

> *"AI senin stajyerindir; ne kadar iyi tarif edersen (Prompt), o kadar kaliteli iş çıkarır. 'Bana kod yaz' dersen çöp verir. 'Bu register'ı şu bit maskesiyle set et' dersen, sana mühendislik harikası verir."*

Bir Metal Yaka için kodlama, artık satır satır yazmak değil, AI'ya **ne yazacağını dikte etme** sanatıdır.

---

## 1. Altın Şablon (The Golden Template)

AI'dan (ChatGPT, Claude, Copilot) kod isterken şu şablonu "Kopyala-Yapıştır" yapın ve boşlukları doldurun:

*   **ROL:** "Sen kıdemli bir Gömülü Sistem Mühendisisin (Senior Embedded Engineer) ve güvenlik kritik sistemler (Safety-Critical Systems) konusunda uzmansın."
*   **DONANIM:** "Hedef işlemci: **STM32F407VG**. Saat hızı: **168MHz**. Derleyici: **GCC (ARM-NONE-EABI)**."
*   **KÜTÜPHANE:** "**STM32 HAL Library** kullan. (Veya Register-level kod yaz)."
*   **GÖREV:** "UART1 üzerinden, DMA (Doğrudan Bellek Erişimi) kullanarak, `0x0A` (Newline) karakteri gelene kadar veri okuyan ve bunu bir Ring Buffer'a (Dairesel Tampon) yazan bir C modülü oluştur."
*   **KISITLAR (CONSTRAINT):**
    *   "Asla `HAL_Delay` veya blocking (kilitleyici) fonksiyon kullanma."
    *   "Kesme (Interrupt) fonksiyonları mümkün olduğunca kısa olsun."
    *   "Olası hataları (Parity Error, Noise Error) yönet."
    *   "State Machine (Durum Makinesi) mimarisi kullan."

---

## 2. Hata Ayıklama (Debugging) İstemleri

AI sadece kod yazmaz, sizin yazdığınız (veya başkasının yazdığı) koddaki sinsi hataları bulur.

### Race Condition Avcısı
> **Prompt:** "Aşağıdaki C kodunda, ana döngü (Main Loop) ve Kesme (ISR) aynı global değişkene erişiyor. Burada bir **Race Condition** veya **Data Corruption** riski var mı? Varsa `volatile` değişken veya kritik bölüm (Critical Section) kullanarak düzelt."

### Stack Overflow Analizi
> **Prompt:** "Bu fonksiyonun iç içe (recursive) çağrıldığında stack taşması (Stack Overflow) yaratma riski nedir? Bu kodu nasıl daha güvenli, yinelemeli (iterative) hale getirebiliriz?"

---

## 3. Optimizasyon

> **Prompt:** "Bu fonksiyon `sin()` ve `cos()` gibi ağır matematik işlemleri kullanıyor ve çok yavaş. Bunu hızlandırmak için **Lookup Table (LUT)** veya **Fixed-Point Arithmetic** (Sabit Noktalı Aritmetik) kullanarak tekrar yaz."

---

> **Ustanın Uyarısı (AI Halüsinasyonu):**
> AI, bazen olmayan donanım uydurur. Size "Timer 14'ü kullan" der, ama kullandığınız çipte Timer 14 yoktur. AI'ın verdiği her register adını ve pin numarasını **Datasheet** ile karşılaştırın. Güven ama doğrula.
