# 03. Mekanik & Malzeme: Canavarın Kemikleri ve Metalin Ruhu

> *"Yazılım esnektir, güncellenebilir ve sanaldır; hatası kolayca düzeltilir. Demir ise serttir, ağırdır ve affetmez. Yazılımı güncellersin, ama kırılan bir mili 'update' edemezsin, ancak değiştirebilirsin."*

---

## 🏗️ Metal Yaka Perspektifi: Mekanik Empati

Mekatronik sistemin "bedeni", iskeleti ve kasları burasıdır. Dünyanın en gelişmiş yapay zekasına (AI) ve en temiz koduna sahip bir otonom araç bile olsa, tekerlek mili kırılırsa veya diferansiyel dişlisi sıyırırsa olduğu yerde kalır.

Bir **"Siber Tamirci"** ve **"Teknoloji Mimarı"** olarak, metalin dilinden anlamak, malzeme bilimine hakim olmak zorundasınız. Makinenin neresinin yağlanacağını, neresinin ne kadar sıkılacağını (Tork anahtarı!), neresinin "metal yorgunluğu" çekmeye başladığını ve dişlilerin arasındaki o mikro boşluğu (backlash) parmak uçlarınızda hissetmelisiniz.

Biz buna **"Mekanik Empati"** diyoruz. Makine konuşamaz, ama titreşimiyle ve sesiyle size acı çektiğini anlatır.

---

## ⚔️ 1. Simülasyonun Mükemmelliği vs Gerçekliğin Kusurları

Bilgisayar ekranında (SolidWorks, Fusion 360, ANSYS) çizdiğiniz her parça mükemmeldir. Yüzeyler sonsuz pürüzsüzdür, sürtünme katsayısı sabittir, montaj hatası yoktur, cıvatalar asla gevşemez.
**Gerçek dünyada ise toz vardır, pas vardır, kir vardır, boşluk (backlash) vardır ve en önemlisi titreşim vardır.**

*   **Tolerans ve Geçmeler:** CAD programında 10.00mm çapında bir deliğe, 10.00mm çapında bir mili sokabilirsiniz. Gerçek hayatta o mil o deliğe **GİRMEZ**.
    *   **Sıkı Geçme (Interference Fit):** Mili sıvı azotla dondurup, deliği pürmüzle ısıtıp çakmak gerekir.
    *   **Boşluklu Geçme (Clearance Fit):** Mil rahat dönsün diye delik 10.02mm, mil 9.98mm yapılır. (H7/g6 toleransı).
    *   **Saha Hatası:** "Çekiçle montaj, mühendislik hatasıdır." Rulmanı çekiçle çakarsan, bilyaları zedelersin ve ömrünü o an bitirirsin.

---

## 🧱 2. Malzeme Bilgisi: Neyi Nereden Yapmalı?

Neden her şeyi en sağlam malzeme olan çelikten yapmıyoruz? Neden bazen uçak alüminyumu (7075), bazen mühendislik plastiği (Delrin/Kestamid/PEEK) kullanıyoruz?

### Ağırlık vs Mukavemet Kısırdöngüsü
Robot kolunun ucundaki tutucuyu (gripper) gereksiz yere ağır yaparsanız (çelikten), onu kaldıracak motoru büyütmek zorunda kalırsınız. Motor büyürse kol ağırlaşır, kol ağırlaşırsa gövde motoru büyür.
*   **Çözüm:** Stratejik malzeme kullanımı. Yük taşıyan yerlere Çelik, gövdeye Alüminyum, sürtünme yüzeylerine Kestamid/Delrin.

### Yorulma (Fatigue): Sessiz Katil
Bir metal parça genellikle "tek seferde" yükü kaldıramadığı için kırılmaz. Milyonlarca kez titreşir, esner, geri gelir. Yüzeyde mikroskobik çatlaklar oluşur ve sonra aniden, beklenmedik bir anda "çıt" diye kopar.
*   **Kestirimci Bakım:** Titreşim analizi (Vibration Analysis) ile bu çatlağın sesini, daha parça kırılmadan duymaktır.

---

## ⚙️ 3. Hareket İletimi: Gücün Yolculuğu

### Dişli Kutuları ve Boşluk (Backlash)
Motor çok hızlı döner (3000 RPM) ama torku düşüktür. Robot kolu ise yavaş dönmeli ama güçlü olmalıdır. Araya **Redüktör** koyarız.
*   **Backlash (Dişli Boşluğu):** Dişlilerin arasına girmesi için gereken o mikro boşluk.
*   **Sorun:** Robot kolunu durdurduğunuzda ucu "sallanıyorsa", redüktör boşluğu fazladır.
*   **Çözüm:** **Harmonic Drive** veya **Sikloid (Cycloid)** redüktörler. Bunlarda boşluk neredeyse sıfırdır ama çok pahalıdırlar. Nerede kullanacağını bilmelisin.

### Vidalar ve Gevşeme
Titreşim altındaki her vida gevşemek ister.
*   **Saha Çözümü:** Loctite (Anaerobik yapıştırıcı), Fiberli Somun, Rondela veya en garantisi: Tel ile emniyetleme.

---

## 📚 Modül İçeriği ve Saha Rehberi

| Dosya | Açıklama | Saha Uygulaması |
| :--- | :--- | :--- |
| **[`03_Material_Fatigue.md`](./03_Material_Fatigue.md)** | Metal Yorgunluğu ve Kırılma | Kırık yüzey analizi (Fraktografi), Yorulma önleme. |
| **[`03_Backlash_Vibration.md`](./03_Backlash_Vibration.md)** | Boşluk ve Titreşim | Redüktör boşluğu ayarı, Rezonans tespiti. |
| **[`03_Production_Methods.md`](./03_Production_Methods.md)** | Üretim Yöntemleri (CNC/3D) | Hangi parça nasıl üretilir? 3D baskı nerede kullanılır? |
| **[`03_Hydraulics_Pneumatics.md`](./03_Hydraulics_Pneumatics.md)** | Hidrolik & Pnömatik | Kavitasyon tespiti, Sızıntı yönetimi ve Valf mantığı. |

---

> **Ustanın Bilgelik Notu:**  
> "Makineyi her zaman dinle. Sağlıklı bir makine, ritmik ve tutarlı bir ses (humming) çıkarır. Düzensiz tıkırtı, sürtünme sesi, tiz bir ciyaklama veya vuruntu... Bunlar makinenin yardım çığlıklarıdır. Eğer bu sesi kırılma gerçekleşmeden önce duyarsan sistemi tamir edersin; duymazsan veya görmezden gelirsen, o makineyi ancak hurdaya atarsın."
