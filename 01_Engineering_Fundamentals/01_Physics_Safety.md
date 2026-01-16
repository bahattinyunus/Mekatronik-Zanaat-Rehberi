# ⚠️ Fiziğin Kanunları, Arıza Analizi ve İş Güvenliği (Physics of Failure)

> *"Fizik kurallarına itiraz edemezsiniz, rüşvet veremezsiniz ve onları kandıramazsınız. İhmal ederseniz, bedelini canınızla ödersiniz. Atölyede en büyük amir Ustabaşı değil, Isaac Newton'dur."*

Bir Metal Yaka profesyoneli için fizik, test kitabındaki formüller değil; **kırılan dişlinin, yanan motorun ve kopan kayışın** arkasındaki cinayet sebebidir. Bir kaza veya arıza olduğunda, suçlu her zaman bir fizik yasasının ihlalidir.

---

## 🧱 1. Eylemsizlik (Inertia): "Duran Durmak, Giden Gitmek İster"

Newton'un 1. Yasası. En çok görmezden gelinen ve en çok dişli kıran yasa.

### 🚨 Saha Senaryosu: Acil Stop (E-Stop) Felaketi
Büyük bir döner tablada 1 tonluk bir kalıp dönüyor. Operatör aniden "Acil Stop" butonuna bastı.
*   **Yazılımcı Mantığı:** `Motor.Stop()` komutu gönderdim, o halde durmalı.
*   **Fiziksel Gerçek:** Motorun elektriği kesilir ve freni kilitlenir. Ancak 1 tonluk kütle **dönmeye devam etmek ister** ($I \cdot \alpha$).
*   **Sonuç:** Oluşan muazzam eylemsizlik torku, motorun milini burar, redüktör dişlilerini un ufak eder veya sistemi zeminden söker atar.
*   **Metal Yaka Çözümü:**
    *   **Frenleme Direnci (Braking Resistor):** Motorun ürettiği o muazzam rejeneratif enerjiyi ısıya çevirerek "kontrollü" bir şekilde hızlı durdurmak.
    *   **Rampa (Deceleration Ramp):** Acil stop olsa bile, fiziksel limitler dahilinde en sert rampayı kullanmak (Sıfır zamanda duruş imkansızdır).

---

## 💪 2. Moment ve Kaldıraç: "Beni Yerimden Oynatın"

> *"Bana yeterince uzun bir robot kolu verin, en güçlü servo motoru bile yakayım."* — Arşimet (Modernize Edilmiş)

### 🚨 Saha Senaryosu: Robot Bilek Arızası
Bir robot kolunun ucuna (bilek noktasına) 10kg yük takacaksınız.
*   **Durum A:** Yük, bilek merkezinden 5cm uzakta. Tork = $10kg \cdot 9.81 \cdot 0.05m = 4.9 Nm$. (Güvenli)
*   **Durum B:** Yük, uzun bir çubuğun ucunda, merkezden 50cm uzakta. Tork = $10kg \cdot 9.81 \cdot 0.5m = 49 Nm$. (TEHLİKE!)
*   **Sonuç:** Aynı ağırlık (10kg) olmasına rağmen, moment kolu uzadığı için motor 10 kat daha fazla zorlanır. Motor aşırı akımdan ısınır, redüktör "haşlanır".
*   **Ders:** Robot seçerken sadece "Taşıma Kapasitesine" (Payload) bakma; **Ağırlık Merkezi Mesafesine** (Center of Gravity - CoG) bak. Fizik kandırılamaz.

---

## ⚡ 3. Potansiyel Enerji: "Uyuyan Dev"

Makinenin elektriğini kesmek, onun enerjisini sıfırlamak demek değildir. Fiziksel enerji hala pusuda bekliyor olabilir.

### 🚨 Saha Senaryosu: Hidrolik Pres ve Özgür Düşüş
Bir hidrolik pres bakım için durduruldu. Elektrik şalteri indirildi (LOTO - Lock Out Tag Out yapıldı). Teknisyen presin altına girdi.
*   **Tehlike:** Presin üst kütlesi havada duruyor. Onu tutan şey silindirin içindeki yağ basıncı veya mekanik bir valf.
*   **Olay:** Bir hidrolik hortum patladı veya valf sızdırdı. Yerçekimi ivmesi ($g = 9.81 m/s^2$) devreye girer. Tonlarca ağırlık serbest düşüşe geçer.
*   **Kural:** Havada asılı hiçbir yükün altına, altına **Mekanik Takoz** (Pinning) koymadan girilmez. Yazılıma güvenme, elektriğe güvenme, fiziğe (mekanik takoza) güven.

---

## 🌊 4. Rezonans: Yıkıcı Titreşim

Her nesnenin bir "doğal frekansı" vardır. Eğer makinenin titreşimi bu frekansla çakışırsa, kıyamet kopar.

### 🚨 Saha Senaryosu: Titreyen Pano
Bir motor 3000 RPM (50 Hz) ile dönüyor. Makine şasesinin doğal frekansı da tesadüfen 50 Hz.
*   **Olay:** Küçük bir balanssızlık, rezonans etkisiyle devasa sarsıntılara dönüşür. Cıvatalar kendiliğinden gevşer, kaynaklar çatlar.
*   **Teşhis:** Motor devrini 2900 RPM'e veya 3100 RPM'e değiştirdiğinde titreşim bıçak gibi kesiliyorsa, sorun **Rezonanstır**.
*   **Çözüm:** Şaseyi ağırlaştır (kütle ekle) veya rijitliğini değiştirerek doğal frekansı kaydır.

---

## 🔥 5. Termodinamik: Isı Asla Yok Olmaz

Elektronik sistemlerin bir numaralı katili ısıdır.
*   **Verim Yasası:** %90 verimli bir 10kW motor sürücüsü kullanıyorsan, %10'luk kısım (1kW) ısıya dönüşür.
*   **Görselleştirme:** 1kW ısı, odanın ortasında çalışan küçük bir elektrikli soba demektir. O sürücü panosunun içinde bir soba yanıyor!
*   **Ders:** O panoya fan koymazsan, o ısı dışarı çıkamaz. Isı birikimi (Heat Buildup) yarı iletkenleri "pişirir". Pano klimaları lüks değil, termodinamik bir zorunluluktur.

---

> **Ustanın Notu:** "Yerçekimi asla uyumaz, asla mola vermez ve asla hata yapmaz. Siz de yapmayın. İş güvenliği, fiziğe duyulan saygıdır."
