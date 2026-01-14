# 🎛️ PID Ayar Rehberi (Tuning Guide): Makineyle Dans

> *"Otomatik Tuning (Auto-tune) iyidir ama mükemmel değildir. Robotun ruhunu sadece elinizle yaptığınız hassas ayar (Fine Tuning) ile yakalayabilirsiniz."*

PID (Oransal-İntegral-Türev), endüstriyel kontrolün %95'idir. Formülü bilmek yetmez, parametrelerin (Kp, Ki, Kd) ne hissettirdiğini bilmelisiniz.

## Adım 1: Hazırlık
*   Tüm parametreleri sıfırla (Ki=0, Kd=0).
*   Sadece Kp (Oransal) ile başla.
*   Güvenlik limitlerini (Max tork/hız) ayarla. Robot çıldırırsa kimseyi öldürmesin.

## Adım 2: P - Güç (Proportional)
Hedefe gitme isteği.
*   Kp'yi yavaşça artır. Robot hedefe gitmeye başlar.
*   Daha da artır. Robot hedefe hızlı gider ama duramaz, hedefi geçer (Overshoot) ve geri döner.
*   **Salınım Noktası:** Robot hedef etrafında sürekli titremeye (Osilosyon) başladığı an, Kp'yi orada bırak ve biraz (%30) geri al.

## Adım 3: D - Fren (Derivative)
Titreşimi öldürmek.
*   Kp sabitken, Kd'yi artırmaya başla.
*   Robotun hedefe yaklaşırken yavaşladığını ve o çılgın titreşimin azaldığını göreceksin. D terimi "sanal sürtünme" gibidir.
*   Çok artırırsan robot "uyuşuk" olur, titrer (yüksek frekanslı zırıltı).

## Adım 4: I - Hafıza (Integral)
Son milimi tamamlamak.
*   Robot durdu ama hedefe 1mm kala kaldı. Gitmiyor. Çünkü hata az olduğu için P gücü motoru yenmeye yetmiyor.
*   Ki'yi çok az (0.01 gibi) artır.
*   Mantar gibi yavaşça hedefe oturduğunu göreceksin.
*   Çok artırırsan robot hedefte duramaz, sürekli ileri-geri yüzer (Instability).

## Saha Özeti
*   **Robot Tembelse:** P düşük.
*   **Robot Çok Titriyorsa (Düşük Frekans):** P yüksek.
*   **Robot Hedefe Varamıyorsa:** I düşük.
*   **Robot "Zırıldıyorsa" (Yüksek Frekans):** D yüksek veya Gürültü var.

---
> **Ustanın Notu:** "PID ayarı sabır işidir. Bazen en iyi ayar, matematiksel olarak 'en hızlı' olan değil, mekaniği en az yoran 'en yumuşak' olandır. Makineye nazik davranın."
