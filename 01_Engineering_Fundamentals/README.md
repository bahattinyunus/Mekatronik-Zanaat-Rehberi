# Mühendislik Temelleri: Makinenin Dili

> *"Matematik bize ödev çözmek için değil, makinenin hayati verilerini okumak için verildi."*

Mühendislik temelleri, genellikle öğrencilerin "bunu nerede kullanacağız?" diye sorduğu sıkıcı dersler yığını olarak görülür. Bir "Metal Yaka" için ise bu dersler, bir makinenin röntgenini çekmek gibidir. Diferansiyel denklemi çözemezsen, PID kontrolcünün neden sarsıntılı çalıştığını (overshoot) anlayamazsın. Statik bilmezsen, robot kolunun neden yük altında titrediğini göremezsin.

Biz burada akademik ispat yapmıyoruz; **teşhis (diagnosis)** koyuyoruz.

## 🛠️ Metal Yaka Perspektifi: Neden Öğreniyoruz?

### 1. Kalkülüs = Değişimin Dili
Bir makine duruyorsa tamirdedir, çalışıyorsa "değişim" halindedir. Hızlanır, ısınır, basınçlanır.
*   **Türev (Derivative):** Bizim için sadece "eğim" değildir. Hatanın ne kadar hızlı büyüdüğünü (Error Rate) anlatır. PID'deki 'D', geleceği tahmin eder.
*   **İntegral (Integral):** Geçmişte yapılan hataların toplamıdır. PID'deki 'I', geçmiş hataları temizler.

### 2. Fizik = Kurallar Kitabı
Yazılımda kuralları sen koyarsın, fizikte kurallar evrenindir. Onları değiştiremezsin, sadece yönetebilirsin.
*   **Termodinamik:** Yanmış bir işlemci, termodinamiğin "enerji yok olmaz, ısıya dönüşür" kuralının bir sonucudur. Soğutucu bloğunu hesaplamazsan, kodun ne kadar iyi olursa olsun sistem ölür.
*   **Elektromanyetizma:** Kablo, sadece bakır değildir; aynı zamanda bir anten ve bir dirençtir. Yüksek frekansta o kablonun nasıl davrandığını bilmezsen, parazit (noise) seni yener.

## 📚 Konu Başlıkları ve Saha Uygulamaları

### Matematik: Saha Notları
*   **Lineer Cebir:** Robot kinematiği (Robotun uzaydaki konumu). Matris çarpımı yapmadan 6 eksenli bir robotu kontrol edemezsin. AI yapar, ama sen doğrulamazsan robot duvara çarpar.
*   **İstatistik:** Sensör verisi asla temiz gelmez. Gürültülü veriden gerçeği ayıklamak (Kalman Filtresi temelleri) için istatistik bilmelisin.

### Fizik: Arıza Tespit Rehberi
*   **Newton Kanunları:** Robot motoru neden yandı? "Tork = Kuvvet x Yol". Kolu uzatırsan (yol artar), tork artar. Motor yetmez, yanar. Suçlu kod değil, fiziktir.

### Teknik Resim: Mavi Baskıyı Okumak
*   Bir, makinenin planıdır. AI sana 3D model çizebilir ama o parçanın CNC'de nasıl işleneceğini (Toleranslar, Yüzey İşleme) teknik resim anlatır.

---

> **Ustanın Notu:** "Formülü ezberleme, grafiğini gözünde canlandır. Bir sinüs dalgası gördüğünde aklına trigonometri dersi gelmesin; aklına salınım yapan bir yay veya şebeke voltajı gelsin."
