# 🏎️ Seviye 1 Proje: Profesyonel Çizgi İzleyen Robot

> *"Çizgi izleyen robot bir oyuncak değildir. Otonom sürüşün, PID kontrolün ve yüksek hız dinamiğinin 'Hello World'üdür. 3 m/s hızla giden bir robota viraj aldırmak, Formula 1 aracı tasarlamakla aynı fizik kurallarına tabidir."*

---

## 🎯 Hedef
Siyah zemin üzerindeki beyaz çizgiyi (veya tam tersi) en yüksek hızda, yoldan çıkmadan takip eden bir robot yapmak.

## 🧠 Öğrenilecek Metal Yaka Becerileri
1.  **PID Kontrol:** Oransal (P) hatayı, İntegral (I) birikimi ve Türev (D) öngörüsünü kodda değil, pistte hissetmek.
2.  **Sensör Kalibrasyonu:** Ortam ışığından etkilenmeyen, normalize edilmiş (0-100 arası) sensör verisi okumak.
3.  **Motor Sürücü (H-Köprüsü):** PWM frekansının motor torkuna ve sesine etkisi.
4.  **Güç Yönetimi:** LiPo bataryayı güvenli kullanmak ve voltaj düşümünü (Voltage Drop) yönetmek.

---

## 🛠️ Donanım Listesi
*   **İşlemci:** Arduino Nano / STM32 / ESP32 (Tercihen STM32 - Hız için).
*   **Sensör:** QTR-8A veya QTR-8RC (Kızılötesi Sensör Dizisi). Tek sensör yetmez, en az 5-8 sensörlü dizi gerekir.
*   **Motor:** 6V-12V Redüktörlü DC Motor (Yüksek devir, örn: 1000-3000 RPM).
*   **Sürücü:** TB6612FNG veya L298N (L298N çok voltaj düşürür, TB6612 önerilir).
*   **Tekerlek:** Sürtünmesi yüksek silikon tekerlek (Pati yapmaması için).

---

## ⚙️ Algoritma Mimarisi (Gömülü Yazılım)

### 1. Sensör Okuma ve Ağırlıklı Ortalama
Sadece "Çizgi var/yok" (0/1) demek yetmez. Çizginin sensör dizisinin **tam olarak neresinde** olduğunu bulmalısın.
*   `Pozisyon = (0*S1 + 1000*S2 + 2000*S3 + ... ) / (S1+S2+S3...)`
*   Bu formül size 0 ile 7000 arasında hassas bir konum verir (Örn: 3500 tam merkez).

### 2. PID Hesaplama
```c
Hata = Hedef_Pozisyon (3500) - Anlık_Pozisyon; // P
Türev = Hata - Eski_Hata;                       // D (Geleceği tahmin)
Integral = Integral + Hata;                     // I (Geçmiş hatalar)

Düzeltme_Hızı = (Kp * Hata) + (Kd * Türev) + (Ki * Integral);

Sol_Motor_Hızı = Baz_Hız + Düzeltme_Hızı;
Sag_Motor_Hızı = Baz_Hız - Düzeltme_Hızı;
```

### 3. Motor Kontrolü
Hesaplanan `Sol_Motor_Hızı` değerini 0-255 (veya 0-1000) arasına sınırla (Constrain). Eksi değer çıkarsa motoru geri döndür (Aktif Frenleme).

---

## 🚧 Saha Zorlukları (Field Challenges)

1.  **Güneş Işığı:** Robotu pencere kenarında çalıştırırsan sapıtır. IR sensörler güneş ışığından etkilenir.
    *   *Çözüm:* Sensörlerin etrafına "Etek" (siperlik) yap veya modülasyonlu sensör kullan.
2.  **Kör Nokta:** Keskin virajda çizgi sensörün dışına çıkarsa robot son gördüğü yöne mi dönmeli, durmalı mı?
    *   *Çözüm:* "Last Known Position" (Son bilinen konum) hafızası ekle.
3.  **Batarya Zayıflaması:** Pil 12V iken PID ayarı mükemmeldir. Pil 11V'a düşünce motorlar yavaşlar, PID ayarı "hantal" kalır.
    *   *Çözüm:* Voltajı ölç ve PWM değerini voltaja göre otomatik ölçekle (Voltage Compensation).

---

> **Ustanın Tavsiyesi:** "Önce yavaş ama pürüzsüz (titreşimsiz) gitmesini sağla. Hız, kararlılıktan sonra gelir. Titreyen robot enerji kaybeder."
