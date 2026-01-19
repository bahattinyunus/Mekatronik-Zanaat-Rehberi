# 🔌 Topraklama, EMI ve Gürültü: Görünmez Savaş

> *"İyi bir topraklama (Grounding), elektronik devrenin atık su gideridir. Tıkanırsa, tüm pislik (gürültü) eve (işlemciye) geri basar."*

Sahada karşılaşılan en garip, en anlamsız ve "hayalet" arızaların %90'ı topraklama ve gürültü kaynaklıdır.
*   "Robot durduk yere zıplıyor."
*   "Ekran bazen donuyor."
*   "Sensör verisi çok titriyor."

Cevap genellikle kodda değil, topraklamadadır.

---

## 🌪️ 1. Gürültü (Noise) Nedir?

Elektronikte gürültü, istemediğimiz sinyallerdir.
*   **Kaynaklar:** Motor sürücüleri (VFD/Inverter), Kontaktörler, Floresan lambalar, Kaynak makineleri.
*   **Kurbanlar:** Mikrodenetleyiciler (3.3V), Sensörler (Analog sinyaller), Haberleşme hatları.

Nasıl bulaşır?
1.  **İletim (Conducted):** Kablolar üzerinden gelir.
2.  **Işıma (Radiated):** Havadan radyo dalgası gibi gelir (EMI).

---

## ⚡ 2. Ground Loop (Şase Döngüsü) Belası

Toprak (GND) her yerde 0 Volt mudur? **HAYIR.**

Kablo bir dirençtir. Eğer topraklama kablosundan akım geçiyorsa, $V = I \times R$ yasası gereği kablonun başında ve sonunda voltaj farkı oluşur.

### Senaryo:
*   Sensör makinenin A noktasında şaseye bağlı.
*   İşlemci makinenin B noktasında şaseye bağlı.
*   A ve B arasında güçlü bir motorun topraklama akımı akıyor.
*   Sonuç: Sensörün "0 Voltu" ile İşlemcinin "0 Voltu" birbirinden farklı!
*   **Etki:** İşlemci, sensörden gelen veriye bu voltaj farkını (gürültüyü) ekler. Veri bozulur.
*   **Çözüm:** **Tek Nokta Topraklama (Star Grounding).** Tüm cihazların toprak hatları, tek bir cıvatada birleşmelidir. Papatya zinciri (Daisy Chain) yapmayın.

---

## 🛡️ 3. Ekranlama (Shielding) Sanatı

Hassas sinyal taşıyan (Encoder, Analog Sensör) kabloların dışı metal örgüyle kaplıdır (Shield). Bu örgü, dışarıdaki paraziti toplar ve toprağa atar.

**Kritik Kural:** Ekranın örgüsünü **SADECE BİR TARAFTAN** toprağa bağla!
*   Genellikle pano tarafında toprağa bağlanır, sensör tarafında boş bırakılır.
*   **Neden?** Eğer iki tarafı da toprağa bağlarsan, ve iki toprak noktası arasında voltaj farkı varsa (Ground Loop), o ekranın üzerinden akım akar. Akım akan ekran, koruma yapmaz; aksine parazit kaynağına dönüşür!

---

## 🧲 4. Donanımsal Filtreler

Yazılımla "Average filter" (Ortalama filtresi) atmak en son çaredir. Sorunu kaynağında çözmelisin.
1.  **Ferrit Boncuk (Ferrite Bead):** Kabloya takılan o siyah silindir mıknatıs. Yüksek frekanslı gürültüyü ısıya çevirip yutar.
2.  **Kondansatör (Decoupling):** Her çipin dibine 100nF seramik kondansatör koyulmasının sebebi süs değildir. Çipin anlık enerji ihtiyacını karşılar ve besleme hattındaki gürültüyü emer.
3.  **Optokuplör (Opto-Isolator):** Kirli dünya (24V Röleler, Motorlar) ile Temiz dünya (3.3V İşlemci) arasında ışıkla haberleşme sağlar. Elektriksel bağlantıyı tamamen keser. En güvenli yöntemdir.

---

---

## 🏗️ 5. Yıldız Topraklama (Star Grounding) vs Papatya Zinciri (Daisy Chain)

Kablolamada şekil her şeydir.

*   **Papatya Zinciri (HATA):** Cihaz 1 -> Cihaz 2 -> Cihaz 3 -> Toprak.
    *   *Sorun:* Cihaz 1'in çektiği akım, hem Cihaz 2'nin hem Cihaz 3'ün üzerinden geçer. Cihaz 3'ün toprağı kirlenir.
*   **Yıldız Bağlantı (DOĞRU):**
    *   Cihaz 1 -> Merkez Toprak
    *   Cihaz 2 -> Merkez Toprak
    *   Cihaz 3 -> Merkez Toprak
    *   *Sonuç:* Herkesin toprağı "Bakir" ve temizdir. Kimse kimseyi kirletmez.

### Faraday Kafesi: Metal Kale
Pano neden plastik değil de metaldir? Çünkü metal, dışarıdan gelen radyo dalgalarını (telefon sinyali, telsiz vb.) yutar ve içindeki işlemciyi korur.
*   **Metal Yaka Kuralı:** Panonun kapağı açıksa koruma yoktur. Pano kapağı ile gövdesi arasında "Topraklama Şeridi" (Örgülü kablo) kopuksa, o kapak bir antendir, kalkan değil.

---

> **Ustanın Özeti:** "Kablolama, devrenin şeması kadar önemlidir. Kabloları spagetti gibi atarsan, o makine asla stabil çalışmaz. Güç kabloları ile sinyal kablolarını **asla** yan yana, paralel döşeme. Aralarından en az 10cm boşluk bırak veya birbirlerini 90 derece ile kessinler."
