<p align="center">
  <a href="../README.md">🏠 Home</a>| 
  <a href="../01_Engineering_Fundamentals/README.md">📚 Fundamentals</a> | 
  <a href="../02_Electrical_Electronics/README.md">⚡ Electronics</a> | 
  <a href="../03_Mechanics_Materials/README.md">⚙️ Mechanics</a> | 
  <a href="../04_Programming_Embedded/README.md">💾 Embedded</a> | 
  <b>[ 🦾 Robotics ]</b> | 
  <a href="../06_Projects_Labs/README.md">🧪 Laboratory</a>
</p>

---

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

---

## 📚 Modül İçeriği ve Saha Rehberi

| Dosya | Açıklama | Saha Uygulaması |
| :--- | :--- | :--- |
| **[`05_PID_Tuning_Guide.md`](./05_PID_Tuning_Guide.md)** | PID Ayar Rehberi | Motor kararlılığı, salınım engelleme. |
| **[`05_Sensors_Feedback.md`](./05_Sensors_Feedback.md)** | Sensörler ve Geri Besleme | Enkoder hataları, limit switch tamiri. |
| **[`05_PLC_Ladder_Logic.md`](./05_PLC_Ladder_Logic.md)** | PLC Başlangıç Rehberi | Endüstriyel otomasyon mantığı. |

---

> **Ustanın Bilgelik Notu:**  
> "Robotun gücüne asla güvenme, onunla asla şakalaşma. Bir robotun freni açıldığında yerçekimi onun tek yöneticisidir. Her zaman acil durdurma (E-Stop) butonuna yakın dur."
