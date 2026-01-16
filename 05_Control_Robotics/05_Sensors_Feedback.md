# 📡 Sensörler ve Geri Besleme (Feedback): Robotun Duyu Organları

> *"Gözleri olmayan (kör) bir robot sadece ezberlediği yere gider. Gözleri olan (sensörlü) bir robot ise hedefini bulur. Kontrol teorisinin temeli 'Geri Besleme'dir (Feedback); yani yaptığın hatayı ölçüp düzeltmektir."*

Bir Metal Yaka için sensör, datasheet'teki bir parça kodu değil, fiziksel bir ölçüm cihazıdır. Sensör yalan söylemez ama bazen "halüsinasyon" (Gürültü) görür.

---

## 1. Enkoderler: Konumun Bekçileri (Position Feedback)

Motor milinin kaç derece döndüğünü ölçer.
*   **Artımsal (Incremental) Enkoder:** Sadece değişimi (hızı) ölçer. Elektrik kesilirse konumunu unutur. Her açılışta robotun "Home" yapması gerekir.
    *   *Saha Notu:* Kabloda kopukluk varsa, motor bir anda kontrolsüzce son hıza çıkar (Runaway).
*   **Mutlak (Absolute) Enkoder:** Her pozisyonun benzersiz bir kodu vardır. Elektrik kesilse bile nerede olduğunu unutmaz. Modern robot kollarında bu kullanılır. Pil ile beslenirler; pil biterse robot hafızasını (kalibrasyonu) kaybeder.

## 2. Resolver: Kirli İşlerin Adamı

Enkoder cam ve optikten yapılır, kırılgandır. **Resolver** ise sadece bakır sargı ve demirden oluşur.
*   **Avantajı:** Titreşime, yağa, toza ve yüksek sıcaklığa dayanıklıdır. Tanklarda, ağır sanayide, CNC tezgahlarında kullanılır.
*   **Dezavantajı:** Enkoder kadar hassas değildir. Analog çalışır.

---

## 3. Gürültü (Noise) ve Topraklama

Mükemmel bir sensörünüz olabilir ama kablosu bir motor sürücünün (VFD) yanından geçiyorsa, geçmiş olsun.
*   **Belirti:** Sensör dururken bile değerler zıplıyorsa (Örn: Sıcaklık 25°C -> 85°C -> 25°C), bu elektromanyetik gürültüdür (EMI).
*   **Yazılımsal Filtre (Low Pass Filter):**
    *   Ham veriyi doğrudan kullanma. Ortalamasını al.
    *   `Filtreli_Veri = (Eski_Veri * 0.9) + (Yeni_Veri * 0.1);` -> Bu basit formül, ani zıplamaları öldürür.
*   **Donanımsal Çözüm:** blendajlı (Shielded) kablo kullan ve blendajı **sadece bir ucundan** (panodan) toprakla.

---

## 4. Limit Switch ve Proximity (Yaklaşım) Sensörleri

*   **Mekanik Switch:** Basittir, ucuzdur ama bozulur (Mekanik ömür). Tozdan etkilenmez.
*   **Endüktif Sensör:** Sadece metali algılar. Temassızdır, ömrü uzundur.
*   **Kapasitif Sensör:** Her şeyi algılar (El, plastik, sıvı). Yanlış tetiklemeye (False Positive) çok müsaittir.

> **Ustanın İpucu:** "Bir sensörün çalışıp çalışmadığını anlamak için LED'ine bakma. LED yanabilir ama kablo kopuk olabilir. PLC girişindeki ışığa bak veya multimetre ile çıkış voltajını ölç."
