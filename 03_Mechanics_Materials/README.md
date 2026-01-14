# Mekanik & Malzeme: Canavarın Kemikleri

> *"Yazılım esnektir, demir serttir. Yazılımı güncellersin, ama kırılan mili güncelleyemezsin."*

Mekatronik sistemin "bedeni" burasıdır. Dünyanın en iyi yapay zekası bile, dişlisi kırılmış bir redüktörü döndüremez. Bir "Siber Tamirci" olarak, metalin dilinden anlamak zorundasın. Neresinin yağlanacağını, neresinin sıkılacağını ve neresinin "metal yorgunluğu" çektiğini bilmelisin.

## 🛠️ Metal Yaka Perspektifi: Demirle Dans

### 1. Simülasyon vs Gerçeklik
SolidWorks'te veya Fusion 360'ta her parça mükemmeldir. sürtünme sıfırdır, montaj hatası yoktur. Gerçekte ise toz vardır, boşluk (backlash) vardır, titreşim vardır.
*   **Tolerans:** Kağıt üstünde 10mm olan delik, pratikte 9.9mm veya 10.1mm olabilir. Rulman o deliğe girmezse, tasarımın çöp olur. Çekiçle montaj yapılmaz, presle ve ısıyla yapılır.

### 2. Malzeme Bilgisi
Neden her şeyi çelikten yapmıyoruz? Neden bazen alüminyum, bazen plastik (Delrin/Kestamid) kullanıyoruz?
*   **Ağırlık vs Mukavemet:** Robot kolunun ucunu ağır yaparsan, motoru büyütmek zorundasın. Motor büyürse kol ağırlaşır. Bu bir kısır döngüdür.
*   **Yorulma (Fatigue):** Bir parça tek seferde kırılmaz. Milyonlarca kez titreşir, sonra aniden "çıt" diye kopar. Kestirimci bakım (Predictive Maintenance) burada devreye girer.

## 📚 Konu Başlıkları ve Saha Uygulamaları

### Statik ve Dinamik
*   **Tork Hesabı:** Motor seçimi yaparken "bunu kaldırır mı?" sorusunun cevabı. Atalet momenti (Intertia) nedir? Neden duran bir yükü kaldırmak, hareket ettirmekten zordur?
*   **Dişli Kutuları (Redüktörler):** Hızı düşür, gücü (torku) artır. Planet redüktörler, sonsuz vidalar. Boşluk (Backlash) robotun hassasiyetini nasıl öldürür?

### Üretim Yöntemleri: Dijitalden Fiziksele
*   **3D Yazıcılar:** Hızlı prototipleme. Ama katmanlar arası zayıftır. Yük taşıyan parça basılmaz, kalıp veya kapak basılır.
*   **CNC İşleme (Talaşlı İmalat):** Mikron hassasiyeti. Metal Yaka'nın, G-Code ile metale şekil verdiği yer.
*   **Kaynak:** İki metali "atom düzeyinde" birleştirmek.

### Pnömatik ve Hidrolik: Akışkan Gücü
*   Elektrik motorları temizdir ama hidrolik kadar güçlü değildir. İş makineleri, presler neden hala yağ ile çalışır?
*   **Valfler ve Sızıntı:** Pnömatik sistemin en büyük düşmanı hava kaçağıdır. Tıslayan bir hortum, fabrikanın parasını havaya üfler.

---

> **Ustanın Notu:** "Makineyi dinle. Sağlıklı bir makine, ritmik bir ses çıkarır. Tıkırtı, sürtünme, vuruntu... Bunlar makinenin yardım çığlıklarıdır. Kırılmadan önce duyarsan tamir edersin, duymazsan hurdaya atarsın."
