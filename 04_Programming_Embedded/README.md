# 04. Programlama & Gömülü Sistemler: Silikon Beyin Cerrahlığı ve Dijital Entegrasyon

> *"Kod, silikonun ruhudur. Ancak kötü yazılmış bir kod, silikonu ısıtır, yorar, kafasını karıştırır ve sonunda sistemi öldürür. Bizler kod yazıcı değil, silikon cerrahlarıyız."*

---

## 💾 Metal Yaka Perspektifi: Kod Enjeksiyonu ve Optimizasyon

Yapay Zeka (AI) çağında, "Sıfırdan I2C Sürücüsü Yazmak" artık insan için bir övünç kaynağı değildir; bunu bir LLM modeli saniyeler içinde hatasız yapabilir.
Yeni çağın meziyeti; o kodu alıp STM32'nin 128KB'lık kısıtlı hafızasına sığdırmak (Optimization), sonsuz döngüye girip sistemi kilitlemesini engellemek (Watchdog), donanımın fiziksel limitlerine (Timing) uydurmak ve milisaniyelik gecikmelere bile tahammülü olmayan makineyle "kekelemeden" konuşturmaktır.

Biz artık "Coder" (Kodlayıcı) değiliz; biz **"Gömülü Sistem Entegratörü"** ve **"Donanım Fısıldayıcısı"**yız.

---

## 🤖 1. İstemi Mühendisliği (Prompt Engineering)

C++ sözdizimini (syntax) ezberlemek hamallıktır. Önemli olan "ne istediğini" teknik bir dille ifade edebilmektir.
*   **Amatör:** "Bana motor sürme kodu yaz."
    *   *Sonuç:* `delay(1000)` kullanan, işlemciyi kilitleyen, endüstriyel standartlardan uzak çöp kod.
*   **Metal Yaka:** "STM32G4 serisi için, HAL kütüphanesi ve DMA kullanarak, Timer 1'in 4 kanalını PWM modunda süren, %0-%100 duty cycle arasında 'Soft-Start' (Rampa) özelliği olan ve TIM_Update kesmesi ile motor akımını ADC üzerinden okuyan, Non-Blocking (Bloke etmeyen) bir C fonksiyonu oluştur."
    *   *Sonuç:* Üretime hazır, optimize edilmiş, profesyonel kod.

---

## ⏱️ 2. Gerçek Zamanlı (Real-Time) Kısıtlar

Bir web sitesi 1 saniye geç açılırsa kullanıcı sadece oflar. 100km/s hızla giden otonom bir aracın fren sistemi 10 milisaniye geç tepki verirse, kaza olur.
*   **Determinizm:** "Hızlı olmak" değil, "Her seferinde tam zamanında olmak" demektir.
*   **RTOS (Gerçek Zamanlı İşletim Sistemi):** İşlemcinin zamanını mikrosaniyeler mertebesinde dilimleyen, görevleri (Task) önem sırasına göre dizen trafik polisidir. Mavi ekran verme lüksü yoktur.

---

## 🧠 3. C/C++: Donanımın Ana Dili ve Tuzakları

### Pointer'lar ve Bellek Yönetimi
Bellek adreslerine doğrudan erişim (0x20000000).
*   **Tehlike:** Eğer dikkatsizce yanlış bir adrese veri yazarsanız (Buffer Overflow), sistemi anında çökertirsiniz. Bu, elektronikteki "kısa devre"nin yazılım dünyasındaki karşılığıdır: **Hard Fault**.
*   **Metal Yaka Kuralı:** Dinamik bellek (`malloc`, `free`) kullanma! Sürekli hafıza alıp geri vermek (Heap Fragmentation), 3 ay sonra sistemin sebepsizce donmasına yol açar. Her şeyi statik ayır.

### Bit Manipülasyonu
32-bitlik bir register'ın tamamını değiştirmek yerine, sadece 3. bitini '1' yapmak (`Register |= (1<<3)`).
*   Çünkü o 3. bit, lazeri ateşleyen tetiktir. Yanlışlıkla 4. biti değiştirirsen, soğutma sistemini kapatırsın.

---

## 📡 4. Haberleşme Protokolleri: Makine Dili

*   **I2C / SPI:** Kart içi fısıldaşmalar. SPI hızlıdır (Ekran, SD Kart), I2C pratiktir (Sensörler).
*   **UART:** İnsanla veya GPS/Bluetooth ile konuşmak.
*   **CAN-Bus (Controller Area Network):** Endüstriyel şebeke. Otomobillerin ve fabrikaların sinir sistemidir. Diferansiyel sinyal kullandığı için gürültüden etkilenmez. Kabloyu kessen bile kalan hattan veri gitmeye çalışır.

---

## 📚 Modül İçeriği ve Saha Rehberi

| Dosya | Açıklama | Saha Uygulaması |
| :--- | :--- | :--- |
| **[`04_Prompt_Engineering_Guide.md`](./04_Prompt_Engineering_Guide.md)** | AI ile Kodlama Sanatı | Doğru teknik terimlerle kod yazdırma şablonları. |
| **[`04_RTOS_Basics.md`](./04_RTOS_Basics.md)** | RTOS ve Çoklu Görev | Task, Mutex, Semaphore ve Deadlock kavramları. |
| **[`04_Embedded_C_Traps.md`](./04_Embedded_C_Traps.md)** | C Dilinin Tuzakları | Pointer hataları, Volatile kullanımı, Bitwise işlemler. |

---

> **Ustanın Bilgelik Notu:**  
> "`delay(1000)` komutunu kodunda kullanmak, bir gömülü sistem mühendisi için suçtur. İşlemciyi 1 tam saniye boyunca (ki bu işlemci için 1 asır gibidir) uyutamazsınız; o sırada dünya dönmeye devam ediyor, sensörler veri gönderiyor. `millis()` kullanın, Timer kullanın, RTOS kullanın ama işlemciyi asla boşa bekletmeyin (Non-blocking code)."
