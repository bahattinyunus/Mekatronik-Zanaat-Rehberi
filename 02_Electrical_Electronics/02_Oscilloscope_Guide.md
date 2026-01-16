# 👁️ Osiloskop Rehberi: Görünmezi Görmek (Time's Microscope)

> *"Multimetre sana yalan söyler, osiloskop gerçeği çıplaklığıyla haykırır. Biri ortalamayı, diğeri anlık gerçeği gösterir."*

Elektronik tamirinde ve tasarımında en büyük sorun, elektriğin görünmez olmasıdır. Kabloya baktığında içinden 5 Volt mu geçiyor, yoksa 50 Volt mu geçiyor göremezsin. Osiloskop, elektriği **zamana karşı çizen** bir makinedir. O olmadan "körsünüz" demektir.

---

## 🛑 1. Önce Güvenlik: Osiloskobu Patlatma Rehberi (!)

Osiloskop kullanırken en sık yapılan ve en pahalı hata: **Ground Clip Faciası.**

*   **Kural:** Osiloskop probunun o küçük siyah timsah ağzı (Ground Clip), osiloskop cihazının üzerinden **TOPRAK (Earth)** hattına doğrudan bağlıdır.
*   **Senaryo:** Şebeke (220V) veya izole olmayan bir devre üzerinde çalışıyorsun.
*   **Hata:** Sinyali ölçmek için probun ucunu bir yere, siyah timsahı da devrenin "Fazına" veya yüksek voltajlı bir noktasına değdirdin.
*   **Sonuç:** **BÜYÜK PATLAMA.** Devredeki yüksek akım, timsah ağzından girer, osiloskobun içinden geçer ve prizdeki toprak hattına akar. Osiloskop yanar, prob kablosu erir, sigortalar atar.
*   **Metal Yaka Çözümü:**
    *   Timsah ağzını **SADECE** devrenin GND (Şase) noktasına bağla.
    *   İzole olmayan devrelerde (Power Supply tamiri vb.) çalışırken **İzolasyon Trafosu** kullan veya **Diferansiyel Prob** kullan.

---

## 📉 2. Multimetre Neden Yetmez?

*   **PWM Sinyali:** Multimetreye %50 Duty Cycle olan 5V bir PWM sinyalini ölçtürürseniz size "2.5V DC" der. Bu koca bir yalandır. Orada sabit bir 2.5V yoktur; saniyede binlerce kez 5V ve 0V arasında gidip gelen bir kare dalga vardır.
*   **Ripple ve Gürültü:** Mikrodenetleyiciniz (STM32/Arduino) rastgele reset mi atıyor? Multimetre ile besleme voltajına bakarsınız: "3.32V" (Mükemmel). Osiloskopla bakarsınız: Voltaj 2.8V ile 3.8V arasında çılgınca salınan bir testere dişidir. İşlemci bu anlık düşüşlerde (Brown-out) reset atar. Multimetre bunu göremez çünkü o çok yavaştır.

---

## 🎯 3. Temel Ayarlar: Tetiği Çekmek (Triggering)

Ekranda sürekli kayan, durmayan anlamsız çizgiler görüyorsanız, **Trigger (Tetik)** ayarınız yanlıştır. Osiloskop sürekli fotoğraf çeken bir kameradır; Trigger ise "Fotoğrafı tam ne zaman çekeyim?" ayarıdır.

*   **Trigger Level:** "Voltaj 2.5V çizgisini geçtiği anda ekranı dondur" emridir. Bu seviyeyi sinyalin içine getirmelisiniz.
*   **Mode (Auto vs Normal vs Single):**
    *   **Auto:** Sinyal olsa da olmasa da ekrana sürekli bir şeyler çizer. Genel bakış için iyidir.
    *   **Normal:** Sadece sinyal Trigger seviyesini geçerse ekranı günceller.
    *   **Single (Tek Atış - The Trap):** En büyük silahımızdır.
        *   Devreye enerji verdiğin anda oluşan o milisaniyelik voltaj dikenini (Inrush Current / Voltage Spike) yakalamak istiyorsun.
        *   Tetiği kur, "Single" moduna al. Osiloskop "Ready" (Hazır) durumuna geçer ve avını bekleyen bir keskin nişancı gibi bekler.
        *   Şalteri kaldır. Sinyal geldiği anda osiloskop o anı yakalar, ekrana çizer ve **STOP** eder. O anı artık inceleyebilirsin.

---

## 🕵️ 4. Saha Dedektifliği: Sinyal Okuma Kılavuzu

### A. İletişim Hatları (UART, I2C, SPI)
*   **İdeal:** Keskin köşeli, dik kenarlı kare dalgalar.
*   **Sorunlu (Kapasitif Yük):** Kareler "Köpekbalığı Yüzgecine" benziyorsa. Kenarlar yayvanlaşmışsa.
    *   **Teşhis:** Kablo çok uzun (Kapasitans yüksek) veya I2C Pull-up direnci çok yüksek değerde. Veri 1'e çıkamadan 0'a düşüyor.
*   **Sorunlu (Ringing/Çınlama):** Karenin köşelerinde sönümlenen dalgalanmalar varsa.
    *   **Teşhis:** Kablo empedansı uyumsuz veya hat çok hızlı sürülüyor.

### B. Motor Sürücü Çıkışları (Inductive Kickback)
*   MOSFET motoru kapattığı anda voltaj aniden eksiye (-) veya çok yüksek artıya fırlıyor mu?
*   **Teşhis:** Koruma diyotlarınız (Flyback Diodes) çalışmıyor veya yok. Bu yüksek voltaj dikenleri sürücünüzü delecek.

### C. Sensör Gürültüsü
*   Sensörden düz bir çizgi (DC) gelmesi gerekirken, üzerinde "kılçık" gibi dikenler mi var?
*   **Teşhis:** Yanından geçen güçlü bir motor kablosundan parazit kapıyor. Kabloyu ayır, bükümlü (Twisted Pair) yap veya ekranla.

---

> **Ustanın Notu:** "Osiloskop sadece bir ölçü aleti değil, bir zaman makinesidir. Size mikrosaniyeler içinde gerçekleşen ve gözün asla göremeyeceği olayları gösterir. Ona güvenin ama **Toprak (Ground)** klipsine asla arkanızı dönmeyin."
