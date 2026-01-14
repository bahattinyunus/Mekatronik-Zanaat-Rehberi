# Programlama & Gömülü Sistemler: Beyin Cerrahlığı

> *"Kod, silikonun ruhudur. Ama kötü yazılmış kod, silikonu ısıtır, yorar ve sonunda öldürür."*

AI çağında "Sıfırdan Sürücü (Driver) Yazmak" artık bir meziyet değildir; bunu AI saniyeler içinde yapar. Meziyet, o kodu alıp STM32'nin 128KB'lık hafızasına sığdırmak (Optimization), sonsuz döngüye girip sistemi kilitlemesini engellemek (Watchdog) ve milisaniyelik gecikmelere tahammülü olmayan donanımla konuşturmaktır.

Biz "kod yazıcı" (Coder) değiliz; biz **"Gömülü Sistem Entegratörü"**yüz.

## 🛠️ Metal Yaka Perspektifi: Kod Enjeksiyonu

### 1. İstemi Mühendisliği (Prompt Engineering)
C++ sözdizimini (syntax) ezberlemek hamallıktır. Önemli olan "ne istediğini" bilmektir.
*   **Yanlış:** "Bana I2C kodu yaz."
*   **Doğru:** "STM32F4 serisi için, HAL kütüphanesini kullanarak, DMA modunda çalışan, hataya dayanıklı (fault-tolerant) ve timeout mekanizması olan bir I2C sensör okuma fonksiyonu yaz."

### 2. Gerçek Zamanlı (Real-Time) Kısıtlar
Web sitesi 1 saniye geç açılırsa kullanıcı "yavaş" der. Robotun fren sistemi 1 milisaniye geç çalışırsa, birisi ölebilir.
*   **RTOS (Gerçek Zamanlı İşletim Sistemi):** Windows gibi değildir. Mavi ekran verme lüksü yoktur. İşleri sıraya koyan, önceliklendiren trafik polisidir.

## 📚 Konu Başlıkları ve Saha Uygulamaları

### C/C++: Donanımın Ana Dili
*   **Pointer'lar:** Bellek adreslerine doğrudan erişim. Yanlış yere yazarsan (Buffer Overflow), sistemi çökertirsin. Elektronikteki "kısa devre" neyse, yazılımdaki "Segmentation Fault" odur.
*   **Bit Manipülasyonu:** 32-bitlik bir register'ın sadece 3. bitini '1' yapmak. Çünkü o bit, motoru açan anahtardır.

### Mikrodenetleyiciler: Beyni Yönetmek
*   **Kesmeler (Interrupts):** Kapı zili gibidir. İşlemci ne yaparsa yapsın, zil çalınca (sensör tetiklenince) her şeyi bırakıp kapıya bakmalıdır. Doğru kurgulanmazsa sistem kilitlenir.
*   **DMA (Direct Memory Access):** İşlemciyi yormadan veriyi taşıyan "hamal". Sensörden hafızaya veri akarken CPU başka iş yapar.

### Haberleşme Protokolleri: Makine Dili Konuşmak
*   **I2C ve SPI:** Kart içi fısıldaşmalar.
*   **UART:** Bilgisayarla konuşmak.
*   **CAN-Bus:** Otomobilin ve fabrikanın sinir ağı. Gürültüye karşı bağışıktır. Bir Tesla'nın da, bir tankın da kalbidir.

---

> **Ustanın Notu:** "`delay(1000)` yazmak bir suçtur. İşlemciyi 1 saniye boyunca uyutamazsın; o sırada dünya dönmeye devam ediyor, sensörler veri gönderiyor. `millis()` kullan, Timer kullan, RTOS kullan. İşlemciyi asla boşa bekletme."
