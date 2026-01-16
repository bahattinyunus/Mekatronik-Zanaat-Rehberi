# 🏭 Seviye 2 Proje: Masaüstü CNC (Mini Fabrika)

> *"Bir makine yapan makine yapmak... Mühendisliğin en büyük hazzı budur. CNC (Computer Numerical Control), bir matkabı bir heykeltraşın eline dönüştüren teknolojidir. Bu projede milimetrenin yüzde biriyle (0.01mm) kavga edeceksiniz."*

---

## 🎯 Hedef
G-Code (NC dosyası) okuyabilen, 3 eksenli (X, Y, Z), kalemle kağıda çizim yapabilen (Plotter) veya yumuşak malzemeyi kazıyabilen (Engraver) mini bir CNC router yapmak.

---

## 🧠 Öğrenilecek Metal Yaka Becerileri
1.  **Step Motor Kontrolü:** Adım adım (Step/Dir) hareket. Microstepping kavramı ve tork/hız ilişkisi.
2.  **Mekanik Rijitlik:** Esneyen bir şasennin, yuvarlak yerine oval çizdiğini tecrübe etmek.
3.  **Güç Elektroniği:** Yüksek akımlı motorları sürmek, ısınma sorunları ve akım ayarı (Current Limiting).
4.  **G-Code Yorumlama:** `G01 X10 Y20` komutunun nasıl bir elektrik sinyaline dönüştüğü.

---

## 🛠️ Donanım Listesi
*   **İşlemci:** Arduino Uno + CNC Shield V3 (Endüstri standardı başlangıç kiti).
*   **Sürücüler:** A4988 veya DRV8825 Step Sürücüler.
*   **Motorlar:** NEMA 17 Step Motorlar (3 Adet).
*   **Mekanik:** Sigma profiller, V-Tekerlekler veya Lineer Rulmanlar (LM8UU), Vidalı Mil (Lead Screw) veya Kayış-Kasnak (GT2).
*   **Güç Kaynağı:** 12V veya 24V Endüstriyel Switch Mode Adaptör (En az 10A).

---

## ⚙️ GRBL: CNC'nin Kalbi
Bu projede tekerleği yeniden icat edip G-Code yorumlayıcı (Parser) yazmayacağız. Dünyanın en iyi açık kaynak CNC yazılımı olan **GRBL**'i kullanacağız.
*   **Firmware:** GRBL kütüphanesini Arduino'ya yükle.
*   **Config ($$ Ayarları):**
    *   `$100=80.0` (X ekseni adım/mm ayarı). Bu değer yanlışsa 10cm çiz dediğinde 12cm çizer.
    *   `$110=1000` (Max Hız mm/dk). Çok hızlı yaparsan motor adım kaçırır (Stall).
    *   `$120=50` (İvmelenme). Çok ani kalkış yaparsan makine sarsılır.

---

## 📐 Adım/mm Hesabı (Sanayi Matematiği)
Motorun 1 turu (360 derece) kaç adımdır? -> Genelde 200 adım (1.8 derece).
Sürücü ayarı nedir? -> 1/16 Microstepping (Yani 1 tur = 3200 adım).
Vidalı milin adımı (Pitch) nedir? -> 1 turda 8mm ilerliyor.

**Soru:** 1mm gitmek için işlemci kaç sinyal (pulse) göndermeli?
**Cevap:** `(200 * 16) / 8 = 400 Adım/mm`.
Bu değeri GRBL `$100` parametresine girmezsen, makinen yanlış ölçüde keser. İşte kalibrasyon budur.

---

## 🚧 Saha Zorlukları (Field Challenges)

1.  **Eksen Kaçıklığı (Squareness):** X ve Y ekseni birbirine tam 90 derece dik değilse, kare çizdirdiğinde "eşkenar dörtgen" çıkar.
    *   *Çözüm:* Gönyeyle montaj yap ve yazılımsal köşe düzeltme (skew compensation) yerine mekaniği düzelt.
2.  **Adım Kaçırma (Losing Steps):** Makine çalışırken "tak" diye bir ses gelir ve çizim kayar.
    *   *Sebep:* Motor gücü yetmedi, mekanik sıkıştı veya hızlanma (Acceleration) çok yüksek.
    *   *Çözüm:* Mekaniği yağla, voltajı artır veya ivmeyi düşür.
3.  **Elektriksel Gürültü:** Spindle (kesici motor) çalıştığında USB bağlantısı kopuyor.
    *   *Çözüm:* USB kablosuna ferrit tak, motor kablolarını blendajla ve topraklamayı düzgün yap.

---

> **Ustanın Tavsiyesi:** "Bir CNC'nin kalitesi motorundan değil, gövdesinden belli olur. Gövde esnerse (Rijitlik yoksa), 1 mikronluk hassas motorun hiçbir anlamı yoktur. Önce sağlam bir iskelet kur."
