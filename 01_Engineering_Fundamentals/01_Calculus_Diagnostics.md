# 🩺 Kalkülüs ile Sistem Teşhisi ve Arıza Analizi (Calculus for Diagnostics)

> *"Diferansiyel denklemler sadece mürekkeple kağıt üzerine yazılmaz; motorun titremesinde, sürücünün ısınmasında, fanın uğultusunda ve sensörün gürültüsünde canlı kanlı yaşarlar."*

Bir **"Metal Yaka"** (AI Destekli Teknoloji Mimarı) ve **"Siber Tamirci"** için türev ve integral, lise sıralarında çözülen x'li y'li bulmacalar değildir. Bunlar, makinenin sağlığını izleyen, arızayı daha oluşmadan haber veren (kestirimci bakım) ve sistemin geleceğini gören en temel biyometrik göstergelerdir.

Hekim için **Stetoskop** ve **EKG** neyse; bizim için **Türev** ve **İntegral** odur.

---

## 📉 1. Türev (Derivative): Hata Hızı, Öngörü ve Frenleme

**Akademik Tanım:** Bir fonksiyonun bir noktadaki değişim oranı veya teğetinin eğimi.
**Metal Yaka Tanımı:** Hatanın veya durumun **"kötüye gitme katsayısı"**. Geleceğin fragmanı.

Bize türev ne söyler? "Şu an durum iyi olabilir ama **uçuruma doğru çok hızlı gidiyoruz!**"

### 🛠️ Saha Senaryosu 1: Isınan Motor ve Termal Kaçak (Thermal Runaway)
Bir servo motorun sıcaklığını izliyorsunuz.
*   **Ölçüm:** $T(t)$ (Zamana bağlı sıcaklık)
*   **Durum A:** Sıcaklık 40°C. 10 dakika sonra 42°C.
    *   $\frac{dT}{dt} \approx 0.2^\circ C/dk$ (Düşük Türev) -> **PANİK YOK.** Sistem dengeye (Steady State) yakın.
*   **Durum B:** Sıcaklık 40°C. 1 dakika sonra 55°C.
    *   $\frac{dT}{dt} = 15^\circ C/dk$ (Çok Yüksek Türev!) -> **ACİL DURDURMA!**
    *   **Teşhis:** Motor mili sıkışmış (Locked Rotor) veya soğutma fanı parçalanmış. Sıcaklığın "Limit Değere" (örneğin 90°C) ulaşmasını beklerseniz motor yanar. Türeve bakarak **henüz 55 derecedeyken** sistemi kapatırsanız, motoru kurtarırsınız.

**Python Simülasyonu (Türevsel Koruma):**
```python
def check_motor_temp(current_temp, prev_temp, dt):
    limit_temp = 90.0
    derivative_limit = 10.0 # Derece/Saniye (Çok hızlı artış limiti)
    
    # 1. Klasik Koruma (Geç Kalabilir)
    if current_temp > limit_temp:
        return "ALARM: Aşırı Sıcaklık! (Geç Kaldın, sargılar yandı bile)"
        
    # 2. Türevsel (Öngörülü) Koruma (Metal Yaka Yaklaşımı)
    rate_of_change = (current_temp - prev_temp) / dt
    if rate_of_change > derivative_limit:
        return f"UYARI: Sıcaklık çok hızlı artıyor! ({rate_of_change} C/s). Soğutma arızası muhtemel. Sistemi KAPAT."
        
    return "Sistem Normal"
```

### 🛠️ Saha Senaryosu 2: PID Kontrolde 'D' Terimi (Fren Etkisi)
Robot kolu bir noktadan diğerine gidiyor.
*   **Sorun:** Sadece hedefe olan mesafeye (Hata = P) bakarsan, hedef noktasına tam hızla gelir ve duramazsın (Overshoot - Aşma).
*   **Çözüm (D - Türev):** Robot kontrolcüsü, hatanın türevine (azalma hızına) bakar.
    *   "Hatayı çok hızlı kapatıyorum, bu hızla gidersem hedefi geçerim." der.
    *   Hedefe varmadan **karşı tork** (Counter-Torque) uygulayarak fren yapar.
*   **Arıza Teşhisi:** Robot hedefte duramıyor ve titriyorsa (Oscillation), D katsayısı yanlıştır veya türev sinyali "gürültülüdür" (Noise).

---

## 📈 2. İntegral (Integral): Hafıza, Birikim ve Sabır

**Akademik Tanım:** Bir eğrinin altındaki alan. Toplam değişim.
**Metal Yaka Tanımı:** **Geçmişin günahları ve sevapları.** Unutmayan hafıza. Küçük ama sürekli sorunların birikmesi.

### 🛠️ Saha Senaryosu 1: Hidrolik Sızıntı ve "Steady State Error"
Büyük bir hidrolik presin basınç altında 100 Bar'da durması gerekiyor.
*   **Mikro Sızıntı:** Valfte çok küçük bir çizik var. Saniyede 0.01 Bar kaçırıyor.
    *   Anlık ölçümde veya Türev'de bu neredeyse sıfırdır. Sensör gürültüsü sanılır.
*   **İntegral Etkisi:** 1 saat boyunca bu kaybı toplarsan (İntegral alırsan);
    *   $\int_{0}^{3600} 0.01 dt = 36 \text{ Bar}$ kayıp!
*   **Kontrolcü Tepkisi (I Terimi):** PID kontrolcüdeki 'I' terimi, "Sürekli hedeflediğim basıncın altındayım, o zaman vanayı biraz daha açmalıyım" der.
*   **Tehlike (Integral Windup):** Sızıntı çok büyükse, I terimi hatayı kapatmak için vanayı %100 açar ama basınç yükselmez. Sistem "doyuma" (saturation) ulaşır. Sonra sızıntı aniden kesilirse (veya vana düzelirse), sistemde muazzam bir enerji biriktiği için basınç 200 Bar'a fırlar ve patlar. Buna **Integral Windup** denir.

### 🛠️ Saha Senaryosu 2: Enerji Tüketimi ve Verimlilik
Bir makinenin çektiği **Güç (Watt)** anlık veridir. Faturayı ödediğiniz şey ise **Enerji (Watt-Saat)** yani Gücün zamana göre integralidir.
*   **Teşhis:** Makinenin anlık güç çekimi normal görünebilir (Pick yapmıyordur). Ancak gün sonu toplam enerji tüketimi (İntegral) geçen aya göre %20 arttıysa;
    *   Rulmanlar yağsız kalmış ve sürtünme artmıştır.
    *   Filtreler tıkanmış, pompa daha çok zorlanıyordur.
    *   Öngörücü bakım: Fatura artışı, mekanik arızanın ilk habercisidir.

---

## 🧮 3. İkinci Türev (Acceleration / Jerk): Konfor ve Mekanik Ömür

Hızın türevi İvme ($a$), İvmenin türevi ise Sarsım ($Jerk$, $j$) dır.
*   **Mühendislik:** Robotun $X$ noktasından $Y$ noktasına gitmesini istiyorsun.
*   **Konfor ve Ömür:** Sadece hızı değil, ivmeyi de, hatta ivmenin değişimini (Jerk) de sınırlamalısın.
*   **S-Curve (S-Eğrisi) Hız Profili:** Hız grafiği "S" harfi şeklinde olmalıdır. Robot kalkarken yavaşça ivmelenmeli, dururken yavaşça ivmesini azaltmalıdır (Jerk Control).
*   **Arıza Nedeni:** Eğer hız profilin "Trapez" (Köşeli) ise, köşelerde ivme sonsuza gider (teorik olarak). Bu, robotun dişlilerine **çekiçle vurmak** demektir. "Tık-Tık" sesleri geliyorsa, yazılımda "Jerk Limiti" koymamışsındır.

---

---

## 🎼 4. Frekans Alanı (Frequency Domain): Makinenin Müziği

Zaman alanında (Time Domain) gördüğün karmaşık bir sinyal, aslında basit dalgaların toplamıdır. Jean-Baptiste Fourier bunu 200 yıl önce buldu.

*   **Zaman Grafiği:** Karmaşık, gürültülü bir çizgi. Hiçbir şey anlaşılmıyor.
*   **FFT (Hızlı Fourier Dönüşümü):** Sinyali frekanslarına ayırır.
    *   **50 Hz'de bir tepe (Peak):** Şebeke gürültüsü (Elektriksel).
    *   **100 Hz'de bir tepe:** Motor balanssızlığı (Mekanik, devirle orantılı).
    *   **3500 Hz'de bir tepe:** Rulman bilya hatası (Yüksek frekanslı sürtünme).

**Metal Yaka Ders:** Bir makinenin sadece sesini kaydedip FFT alarak, hangi rulmanın (iç bilezik mi, dış bilezik mi) bozulduğunu **makineyi açmadan** söyleyebilirsin. Bu, diferansiyel denklemlerin sanayideki en büyük sihridir.

---

> **Ustanın Özeti:**
> *   **Türev** alıyorsan **Gürültüye (Noise)** dikkat et. Gürültülü sinyalin türevi felakettir. (Low Pass Filter kullanmadan türev alma).
> *   **İntegral** alıyorsan **Doyuma (Saturation)** dikkat et. Sonsuza kadar biriktirme, bir yerde sıfırla (Anti-Windup).
> *   **Matematik**, makinenin hisleridir. Onu dinle.
