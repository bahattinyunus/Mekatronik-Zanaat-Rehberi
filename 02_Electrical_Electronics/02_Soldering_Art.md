# 🔥 Lehim Sanatı: Elektronik Bağlantının Kimyası

> *"İyi lehim parlar, kötü lehim sistemi karartır. Lehim, iki metali birbirine yapıştırmak değil, onları atomik düzeyde kaynaştırmaktır."*

Yeni başlayanların en büyük yanılgısı, lehimi bir "yapıştırıcı" gibi görmeleridir. Hayır. Lehimleme (Soldering), bir **metalürjik alaşım oluşturma** sürecidir. Bakır ped, komponent bacağı ve kalay birleşerek, elektronların engelsizce akabileceği tek bir metal yapı oluşturmalıdır.

---

## 🧪 1. Malzemeler: Silahlarını Tanı

### A. Havya (The Iron)
*   **Isı Ayarı:** Hayati önem taşır.
    *   **320-350°C:** Kurşunlu lehim (80/20) için ideal.
    *   **370-400°C:** Kurşunsuz (RoHS) lehim için gerekli.
*   **Güç:** 15W'lık kalem havyalar sadece oyuncaktır. İyi bir istasyon havya (60W+), ısıyı kaybettiği anda tekrar yükseltebilmelidir (Isı Regülasyonu).
*   **Uç (Tip) Seçimi:**
    *   **İğne Uç (Conical):** Çok ince SMD işler için. Dikkat: Isıyı uca iletmekte zorlanır. Kalın kablo lehimlenemez.
    *   **Balta/Keski Uç (Chisel):** En kullanışlı uçtur. Geniş yüzeyi sayesinde ısıyı pede mükemmel aktarır.

### B. Flux (Pasta/Reçine): Lehimin Ruhu
*   Lehimin içindeki o "duman" Flux'tır.
*   **Görevi:** Isı uygulandığında metal yüzeyler anında oksitlenir (paslanır). Lehim pasa yapışmaz. Flux, bu oksit tabakasını asidik etkisiyle temizler ve lehimin sabunlu su gibi yayılmasını (Wetting) sağlar.
*   **Kural:** Lehim topaklanıyorsa, yapışmıyorsa; daha fazla ısıtma, **daha fazla Flux sür!**

---

## 👨‍🎨 2. Mükemmel Lehimin Anatomisi

İyi bir lehim bağlantısı nasıl olmalıdır?
1.  **Konik Şekil (Volcano):** Lehim, pedin tamamına yayılmalı ve bacağa doğru tırmanarak bir yanardağ konisi oluşturmalıdır.
2.  **Parlak Yüzey:** Yüzey pürüzsüz ve ayna gibi parlak olmalıdır (Kurşunsuz lehimlerde biraz daha mat olabilir).
3.  **İçbükey Yapı:** Lehim top gibi şişkin (dışbükey) değil, içe doğru kavisli olmalıdır.

### Adım Adım Teknik
1.  **Hazırlık:** Havya ucunu temizle ve azıcık lehimle kapla (Tinned).
2.  **Isıtma (Kritik An):** Havya ucunu, **hem pede hem de komponent bacağına** aynı anda değdir. Metali ısıtmazsan lehim tutmaz. 2-3 saniye bekle.
3.  **Besleme:** Lehimi havya ucuna değil, **ısıttığın parçanın (padin) üzerine** değdir. Lehim eriyip akmaya başlamalıdır.
4.  **Çekiş:** Yeterince lehim eriyince (boğmadan), önce lehim telini çek. Havya hala orada kalsın. Lehimin yayıldığını gör.
5.  **Bitiş:** Havyayı çek ve **asla üfleme, oynatma.** Doğal soğumaya bırak.

---

## 💀 3. Ölümcül Hatalar ve Tedavileri

### A. Soğuk Lehim (Cold Joint) - Sinsi Katil
*   **Görüntü:** Gri, mat, pütürlü ve topaklanmış.
*   **Sebep:** Yeterince ısıtılmadı veya donarken hareket ettirildi.
*   **Sonuç:** Elektrik bazen geçer, bazen geçmez. Oda sıcaklığı değişince temassızlık yapar. Cihazı tokatlayınca çalışır.
*   **Çözüm:** Bol Flux sür ve tekrar ısıtıp lehimin akmasını (reflow) sağla.

### B. Lehim Köprüsü (Solder Bridge)
*   **Görüntü:** İki bacak birbirine lehimle kaynamış.
*   **Sonuç:** Kısa devre. Entegre yanar.
*   **Çözüm:**
    *   **Flux Sür:** Bazen sadece flux sürüp ısıtmak, yüzey gerilimi sayesinde lehimi birbirinden ayırır.
    *   **Lehim Emme Teli (Solder Wick):** Bakır örgüyü üzerine koy, havyayı bas ve fazlalığı sünger gibi emdir.

---

    *   **Lehim Emme Teli (Solder Wick):** Bakır örgüyü üzerine koy, havyayı bas ve fazlalığı sünger gibi emdir.

### C. PCB Cerrahlığı: Jumper Atma (Trace Repair)
Bazen yollar kopar veya yanar. O kart çöp mü? Asla.
1.  **Malzeme:** "Kynar Wire" (Bobin teli gibi kaplamalı ince tel) veya 0.1mm emaye bobin teli.
2.  **Teknik:**
    *   Kopan yolun başını ve sonunu kazı, bakırı çıkar.
    *   Teli lehimle.
    *   **Sabitleme:** Teli havada bırakma, titreşimden kopar. Üzerine **UV Solder Mask** (Yeşil boya) damlat ve UV feneriyle dondur.
    *   Bu işleme "Bypass Ameliyatı" denir.

---

## 🔬 4. İleri Teknikler: SMD ve Sıcak Hava

Artık devreler küçüldü. Through-hole (Delikten geçme) bitti, SMD (Yüzey Montaj) çağı başladı.
*   **Sıcak Hava Tabancası (Hot Air):** Havyanın ucu entegrenin 64 bacağına aynı anda değemez. Sıcak hava ise değebilir.
    *   **Teknik:** 350°C, düşük üfleme hızı.
    *   **Reflow:** Pedlere lehim pastası (Solder Paste) sür, malzemeyi cımbızla koy, sıcak havayı tut. Lehim eriyince (sıvılaşınca) yüzey gerilimi sayesinde çip "tık" diye yerine oturur. Büyü gibidir.

### Flux Seçim Rehberi

| Flux Türü | Özellik | Kullanım Alanı | Temizlik |
| :--- | :--- | :--- | :--- |
| **Rosin (R/RMA)** | Klasik, reçine bazlı. | Genel lehimleme. | Gerekmez (Ama yapışkan kalır). |
| **No-Clean (NC)** | Düşük artık bırakır. | Seri üretim, SMD. | Temizlemeye gerek yok. |
| **Water Soluble (WS)** | Çok agresif, çok iyi temizler. | Zor, oksitli yüzeyler. | **ZORUNLU!** Su ile hemen yıkanmalı yoksa kartı yer. |

---

> **Ustanın Notu:** "Flux dumanı zehirlidir (kolofan içerir). Bunu akciğerlerine çekme, fan kullan. Ve havya ucunu asla zımpara veya bıçakla kazıma! Uçtaki koruyucu kaplamayı yok edersen, bakır uç saniyeler içinde oksitlenir ve çöp olur. Sadece ıslak sünger veya pirinç tel yumak kullan."
