# 🎛️ PID Ayar Sanatı (Tuning): Makineyle Dans

> *"Otomatik Tuning (Auto-tune) iyidir ama mükemmel değildir. Robotun ruhunu sadece elinizle yaptığınız hassas ayar (Fine-Tuning) ile yakalayabilirsiniz. PID, matematiktir; Tuning ise sanattır."*

PID (Oransal-İntegral-Türev), endüstriyel kontrolün %95'idir. Formülü bilmek yetmez, parametrelerin (Kp, Ki, Kd) ne hissettirdiğini ve makineye ne yaptırdığını **duymanız** gerekir.

---

## 🛠️ Manuel Tuning Algoritması (El Yordamı)

Mühendisler Matlab kullanır, teknisyenler kulaklarını. İşte sahadaki adım adım reçete:

### 1. Hazırlık (Sıfır Noktası)
*   **Güvenlik:** Robotun hareket alanını boşalt. Acil Stop butonu elinin altında olsun.
*   **Sıfırla:** Ki = 0, Kd = 0 yap. Sadece Kp (Oransal) ile başlayacağız.

### 2. Adım P: Güç ve Tepki (Proportional)
Hedefe gitme isteğidir. Gaz pedalıdır.
*   Kp'yi yavaşça artır. Robot hedefe gitmeye çalışacaktır.
*   Kp arttıkça hızlanır, ama duramaz ve hedefi geçer (Overshoot).
*   **Salınım Noktası (Oscillation):** Kp'yi öyle bir noktaya getir ki, robot hedef etrafında sürekli, sönmeyen bir şekilde titresin (Zırıldasın).
*   **Ayar:** Bu noktaya geldiğinde Kp'yi %40-50 oranında düşür. Artık kaba ayarı yaptın.

### 3. Adım D: Fren ve Sönümleme (Derivative)
Titreşimi öldüren "Sanal Sürtünme"dir. Geleceği görür ve frene basar.
*   Sistemde overshoot (aşım) veya salınım varsa Kd'yi gıdım gıdım artır.
*   Robotun hedefe yaklaşırken yumuşadığını ve "zınk" diye durduğunu göreceksin.
*   **UYARI:** D kazancı gürültüyü çok sever. Eğer çok artırırsan, motor "yüksek frekanslı, tiz bir ses" (White Noise) çıkarmaya başlar ve ısınır. Bu sesi duyarsan Kd'yi hemen kıs.

### 4. Adım I: Hatayı Sıfırlama (Integral)
Geçmişin muhasebesidir.
*   P ve D ayarlandı ama robot hedefe 1mm kala durdu, gitmiyor. (Steady-State Error). P gücü yetmiyor.
*   Ki değerini çok çok küçük adımlarla (0.001 gibi) aç.
*   Sistemin mantar gibi yavaşça hedefe sürüklendiğini ve tam oturduğunu göreceksin.
*   **Tehlike:** I kazancı sabırsızdır. Çok artırırsan "Integral Windup" olur; robot hedefi geçer, geri döner, tekrar geçer; denizde sallanan tekne gibi (Instability) olur.

---

## 👂 Saha Sentezi: Motorun Sesi Ne Diyor?

*   **Tembel Ses (Düşük Frekanslı Uğultu):** P kazancı çok düşük. Motor "gitmek istiyorum ama gücüm yok" diyor.
*   **Agresif Titreşim (Tak-Tak Vuruntu):** P kazancı çok yüksek. Sistem kararsız.
*   **Tiz Zırıltı (Arı Vızıltısı):** D kazancı çok yüksek veya sinyalde gürültü var. Motor ısınıyor!
*   **Yüzme (Yavaş Salınım):** I kazancı çok yüksek. Hafıza dolu, sistem kararsız.

---

## ⚠️ Integral Windup (Hafıza Taşması) Felaketi
Robot bir engele takıldı, hedefe gidemiyor. Ama I (İntegral) sürekli hatayı topluyor: "Hata var, güç ver! Hata var, güç ver!".
I değeri devasa boyutlara ulaşır.
Engel kalktığı anda, o birikmiş devasa enerjiyle robot mermi gibi fırlar.
*   **Çözüm:** **Anti-Windup** veya **Clamping** (Doyum). I teriminin çıkabileceği maksimum değeri sınırla.

---

---

## 🚀 5. Feedforward (İleri Besleme): Kahin Kontrolü

PID "Hata olunca düzeltirim" der (Reaktif). Feedforward "Hata olacağını biliyorum, önlemini alıyorum" der (Proaktif).

*   **Örnek:** Robot koluna 5kg yük aldın.
    *   **Sadece PID:** Kol aşağı sarkmaya başlar (Hata oluşur). I terimi "Aaa hata var" der ve güç verir. (Geç kaldı).
    *   **Feedforward:** "Elimde 5kg yük var, yerçekimi bunu aşağı çekecek. Daha hareket etmeden motorlara +%20 güç veriyorum."
*   **Formül:** `Çıkış = PID + (Yük * Yerçekimi_Katsayısı)`
*   **Sonuç:** Hata hiç oluşmadan engellenir. Mükemmel takip.

### Step Response (Basamak Cevabı) Referans Tablosu

```text
Grafik: Hedef Çizgisine Ulaşma Şekli

     Hedef -----------------------------------
            /   \      (Overshoot - Aşma)
           /     \________ (Settling - Oturma)
          /
Giriş ___/

1. Overdamped (Aşırı Sönümlü): Hedefe çok yavaş gider, hiç aşmaz. Güvenlidir ama hantaldır.
2. Underdamped (Az Sönümlü): Hızlı gider, hedefi geçer, titrer.
3. Critically Damped (Kritik): En kısa sürede hedefe gider ve durur. (Metal Yaka Hedefi).
```

---

> **Ustanın Notu:** "Mükemmel ayar yoktur, 'yeterince iyi' ayar vardır. Robot ısınıyorsa ayar kötüdür, ses çıkarıyorsa kötüdür. Sessiz ve soğuk çalışan robot, mutlu robottur."
