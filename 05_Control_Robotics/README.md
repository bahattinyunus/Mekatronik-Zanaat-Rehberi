# 05. Kontrol Sistemleri & Robotik: Robot Doktorluğu ve Sistem Cerrahlığı

> *"Otonom sistemler (AI) dünyayı yönetecek olabilir; peki o sistemler hastalandığında, delirdiğinde veya travma geçirdiğinde (Kaza) onlara kim bakacak? Bizler, Robot Doktorlarıyız."*

---

## ⚕️ Metal Yaka Perspektifi: Robot Yoğun Bakım Ünitesi (Robot ER)

Otonom bir fabrikadaki robot kolu aniden durduğunda, sorun her zaman "buglı kod" değildir. Belki bir dişli sıyırmıştır, belki triger kayışı gevşemiştir, belki de enkoderin optik okuyucusu tozlanmıştır.
Bir AI yazılımında hata (bug) olduğunda sunucuyu yeniden başlatabilirsiniz; ama bir robot kolu 200kg yükle kontrolsüzce bir yere çarptığında onu "tamir" etmelisiniz. **Bu, dijital değil fiziksel ve cerrahi bir müdahaledir.**

### 1. Diagnosis (Teşhis Koyma Sanatı)
Robotun ekranında beliren hata kodu: **"Eksen 4 - Aşırı Akım Hatası (Overcurrent Error)"**.

*   **Beyaz Yaka (Teorist) Yaklaşımı:** Kodu inceler, PID parametrelerini değiştirir, akım limitlerini yazılımla artırır.
    *   *Sonuç:* Motor yanar veya sürücü kartı patlar.
*   **Metal Yaka (Cerrah) Yaklaşımı:** Robotun yanına gider.
    *   Eksen 4'ün motoruna elini koyar. "Çok mu ısınmış?" (Ateşine bakar).
    *   Freni manuel olarak açıp ekseni eliyle hareket ettirmeye çalışır. "Mekanik sıkışma var mı?".
    *   Belki de 4. eksendeki elektromanyetik fren balatası yapışmıştır ve motor freni yenmeye çalışırken aşırı akım çekiyordur.
    *   **Çözüm:** Yazılım değil, balata temizliğidir. İşte bu, veriyle değil, **hisle ve fizik yasalarıyla** yapılan bir teşhistir.

### 2. Kalibrasyon: Robotun Sıfır Noktası
Robotun uzayda nerede olduğunu bilmesi gerekir. Her robotun bir "Home" veya "Zero" pozisyonu vardır. Bir çarpışma (Collision) sonrası veya kayış değişiminden sonra bu "sıfır noktası" kayar.
*   Robotu (Mastering/Zeroing) yeniden kalibre etmek, bir virtüözün enstrümanını akort etmesi gibidir. Çok hassas, büyük sabır isteyen ve mükemmel bir "kulak" (tecrübe) gerektiren bir sanattır.

---

## 🏗️ Konu Başlıkları ve Derinlemesine Saha Uygulamaları

### Kontrol Teorisi: Denge ve Kararlılık
*   **PID Kontrol:** Bu sadece bir formül değildir (Oransal, İntegral, Türev). Sistemin karakteridir, mizacıdır.
    *   **P (Agresiflik):** Şimdiki hataya tepki verir. Çok yüksekse sistem sinirlidir, titrer.
    *   **I (Takıntı/Hafıza):** Geçmiş hataları asla unutmaz, hedefe tam oturana kadar zorlar.
    *   **D (Öngörü/Refleks):** Geleceği tahmin eder, frene basar. Titreşimi öldürür.
    *   **Tuning (Terbiye Etmek):** Hırçın bir atı (robotu) evcilleştirmek gibidir. Matematiksel formüller (Ziegler-Nichols) sahada her zaman çalışmaz; motorun sesini dinleyerek ayar yapmalısınız.

### Robot Kinematiği: Hareketin Geometrisi
*   **İleri Kinematik:** "Motorlara açı verdim, elim nereye gitti?"
*   **Ters Kinematik (IK):** "Elimin şuraya gitmesini istiyorum, motorlar kaç derece dönmeli?"
*   **Tekillik (Singularity):** Robotun matematiksel karadelikleri.
    *   Robotun eklemlerinin aynı hizaya geldiği ve matematiksel çözümün kaybolduğu (Sonsuz hız gerektiren) pozisyonlar.
    *   Bir Metal Yaka, robotu programlarken bu "ölüm bölgelerinden" (Singularity Zones) uzak tutar. Çünkü robot burada kontrolsüzce savrulur.

### Endüstriyel Otomasyon: Fabrikanın Beyni
*   **PLC (Programlanabilir Mantık Denetleyicisi):** Endüstrinin kalbi. Mavi ekran vermez, virüs bulaşmaz, tozdan etkilenmez.
*   **SCADA:** Fabrikanın kokpiti. Binlerce sensörü izlemek. Kırmızı ışık yandığında, arızanın hangi sensörde olduğunu **sahaya gitmeden** bulabilmek.

---

## 📚 Modül İçeriği ve Saha Rehberi

| Dosya | Açıklama | Saha Uygulaması |
| :--- | :--- | :--- |
| **[`05_PID_Tuning_Guide.md`](./05_PID_Tuning_Guide.md)** | PID Ayar Sanatı | Ziegler-Nichols değil, elle ve kulakla (Heuristic) ayar yapma. |
| **[`05_Robot_Safety.md`](./05_Robot_Safety.md)** | Robot Güvenliği (LOTO) | Kill Zone, Deadman Switch ve Enerji İzolasyonu. |
| **[`05_Sensors_Feedback.md`](./05_Sensors_Feedback.md)** | Sensörler ve Gürültü | Encoder, Resolver ve Gürültü filtreleme. |
| **[`05_PLC_Ladder_Logic.md`](./05_PLC_Ladder_Logic.md)** | PLC & Ladder Mantığı | Fail-Safe (NC/NO) güvenliği, Tarama döngüsü ve Reliability. |

---

> **Ustanın Bilgelik Notu:**  
> "Robotun gücüne asla güvenme, sadece Acil Durdurma (Emergency Stop) butonuna güven. Robotun gözü yoktur (kamera takmadıysan), hissi yoktur (tork sensörü yoksa) ve vicdanı yoktur. Yörüngesinin önüne geçersen seni ezer geçer ve bir hata oluştuğunu bile anlamadan işine devam eder. Robotla şakalaşma."
