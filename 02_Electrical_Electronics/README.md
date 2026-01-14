# Elektrik & Elektronik: Devre Cerrahlığı

> *"Duman çıktıysa, ruhu bedeni terk etmiştir."*

Elektronik, mekatroniğin sinir sistemidir. Yazılım (beyin) emir verir, mekanik (kas) hareket eder; ama bu emri taşıyan ve gücü sağlayan elektroniktir. Bir yazılımcı hata yaptığında "bip" sesi duyar, bir elektronikçi hata yaptığında **patlama** sesi duyar ve yanık kokusu alır.

Bu modül, şematik çizmekten ziyade, "çalışmayan" bir devreyi hayata döndürme sanatına, yani **Fiziksel Hata Ayıklamaya (Physical Debugging)** odaklanır.

## 🛠️ Metal Yaka Perspektifi: Devre Cerrahlığı

### 1. Dumanı Geri Koyamazsın
Elektronikte "Undo" (Geri Al) tuşu yoktur. Bir MOSFET'i yaktıysan, yanmıştır. Bu yüzden "önce ölç, sonra enerji ver" kuralı kanunumuzdur.
*   **Cerrahın Neşteri:** Havya. İyi lehim, sanat eseridir. Soğuk lehim ise sistemin kanseridir; bazen çalışır, bazen çalışmaz. En zor bulunan arıza budur.

### 2. Görünmez Düşman: Gürültü (Noise)
Dijital dünyada 1 ve 0 vardır. Fiziksel dünyada ise 0.9V, 3.3V, parazitler, dalgalanmalar vardır.
*   **Osiloskop:** Elektronikçinin gözüdür. Multimetre sana ortalamayı gösterir (yalan söyler), osiloskop sana gerçeği (sinyaldeki anlık bozulmayı) gösterir.

## 📚 Konu Başlıkları ve Saha Uygulamaları

### Temel Analiz ve Hata Avı
*   **Ohm ve Kirchhoff:** Bunlar sınav sorusu değil, arıza bulma yöntemidir. Bir yerde voltaj düşüyorsa, orada direnç vardır. Kablo gevşemiştir, klemens paslanmıştır.
*   **Kısa Devre Takibi:** Kartın beslemesi kısa devre mi? Isınan parçayı bulmak için termal kamera veya "parmak testi" (dikkatli ol!) kullanmak.

### Analog Elektronik
*   **Op-Amp'lar:** Sensör sinyalini güçlendirmek. AI'a giden veri buradan geçer. Burası bozuksa, AI çöp veriyle çalışır.
*   **Filtreler:** Fabrika ortamı elektriksel olarak "kirlidir". Motor sürücüler parazit yayar. Kondansatörler ve bobinlerle sinyali temizlemek (Bypass, Decoupling) hayati önem taşır.

### Güç Elektroniği: Sistemin Kasları
*   **MOSFET ve IGBT:** Bunlar anahtardır. Ama evdeki ışık anahtarı gibi değil; saniyede 20.000 kere açılıp kapanırlar. Yanlış sürersen ısınıp patlarlar.
*   **H-Köprüsü:** Motoru ileri-geri süren devre. İki tarafı aynı anda açarsan (Shoot-through), köprüyü havaya uçurursun. Donanımsal "dead-time" neden önemlidir?

### Sensörler: Duyu Organları
*   Sıcaklık (NTC/PTC), Mesafe (Ultrasonik/Lidar), Konum (Encoder).
*   **Arıza Senaryosu:** Encoder kablosu koptuğunda robot kolu neden son hızla duvara çarpar? Bunu yazılımla mı donanımla mı engellersin?

---

> **Ustanın Notu:** "Multimetren senin kılıcın, osiloskobun kalkanındır. Yanında bunlar olmadan savaşa (sahaya) çıkma. Ve asla unutma: En iyi sensör, senin burnundur; yanık kokusu yalan söylemez."
