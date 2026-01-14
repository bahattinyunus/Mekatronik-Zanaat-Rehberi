# Kontrol Sistemleri & Robotik: Robot Doktorluğu

> *"Otonom sistemler (AI) dünyayı yönetecek, peki o sistemler hastalandığında kim bakacak?"*

Bizler, **Robot Doktorlarıyız**. Fabrikadaki robot kolu durduğunda, sorun her zaman kodda değildir. Belki dişli sıyırmıştır, belki kayış gevşemiştir, belki de enkoder tozlanmıştır. AI yazılımında bir bug (hata) olduğunda onu yeniden başlatabilirsin, ama robot kolu bir yere çarptığında onu "tamir" etmelisin.

## 🛠️ Metal Yaka Perspektifi: Yoğun Bakım Ünitesi (Robot ER)

### 1. Diagnosis (Teşhis)
Robot hata kodu verdi: "Eksen 4 Aşırı Akım".
*   **Beyaz Yaka:** Kodu inceler, limitleri değiştirir.
*   **Metal Yaka:** Robotun yanına gider. Eksen 4'e elle dokunur. "Isınmış mı?", "Sıkışma var mı?". Belki de 4. eksendeki fren balatası yapışmıştır. Yazılımla çözülemeyen donanımsal bir kilitlenme.

### 2. Kalibrasyon: Sıfır Noktası
Robotun dünyanın neresinde olduğunu bilmesi gerekir. Bir çarpışma sonrası bu "sıfır noktası" kayar. Robotu (Mastering) yeniden kalibre etmek, bir müzik aletini akort etmek gibidir. Hassas, sabır isteyen ve kulak (tecrübe) gerektiren bir iştir.

## 📚 Konu Başlıkları ve Saha Uygulamaları

### Kontrol Teorisi: Denge Sanatı
*   **PID Kontrol:** Sadece formül değil. P (Şimdiki Hata), I (Geçmiş Hatalar), D (Gelecek Tahmini).
    *   **Tuning (Ayar):** Robot titriyor mu? D kazancını azalt. Hedefe varamıyor mu? I kazancını artır. Bu hissetme işidir.

### Robot Kinematiği
*   **İleri Kinematik:** "Açıları veriyorum, uç nerede?"
*   **Ters Kinematik:** "Ucun buraya gitmesini istiyorum, açıları (motorları) sen hesapla."
*   **Tekillik (Singularity):** Robotun matematiksel olarak kilitlendiği, sonsuz hıza çıkmaya çalıştığı kör noktalar. Robotu bu noktalardan uzak tutmak, operatörün hayatını kurtarır.

### Endüstriyel Otomasyon
*   **PLC (Programlanabilir Mantık Denetleyicisi):** Fabrikanın beyni. Mavi ekran vermez, virüs bulaşmaz, 7/24 çalışır.
*   **SCADA:** Fabrikanın kokpiti. Tüm bu sistemi tek ekrandan izlemek ve yönetmek.

---

> **Ustanın Notu:** "Robotun gücüne güvenme, acil stop butonuna (Emergency Stop) güven. Robotun gözü yoktur (kamera takmadıysan), hissi yoktur (tork sensörü yoksa). Önüne geçersen seni ezer ve hatanın senin olduğunu bile anlamaz."
