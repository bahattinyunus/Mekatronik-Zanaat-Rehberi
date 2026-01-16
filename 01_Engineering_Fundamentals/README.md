# 01. Mühendislik Temelleri: Makinenin Dili, Kainatın Sırları ve Arıza Teşhisi (Diagnosis)

> *"Matematik bize okulda ödev çözmek için verilen sıkıcı bir araç değil; makinenin hayati verilerini okumak, 'can çekişen' bir sistemin çığlığını duymak ve evrenin değişmez kurallarıyla konuşmak için bahşedilmiş kutsal bir dildir."*

---

## 🛡️ Metal Yaka Perspektifi: Neden ve Nasıl Öğreniyoruz?

Mühendislik temelleri (Matematik, Fizik, Kimya), genellikle öğrencilerin "Bunu gerçek hayatta nerede kullanacağız?" diye sorguladığı, ancak mezun olduktan sonra eksikliğini en acı şekilde hissettiği derslerdir. Bir **"Metal Yaka"** (AI Destekli Teknoloji Mimarı) için bu dersler, bir ressamın fırçası, bir cerrahın neşteri veya bir dedektifin büyüteci kadar hayatidir.

Biz bu dersleri; **akademik sınavları geçmek için değil, sanayi sahasında hayatta kalmak için** öğreniyoruz.

*   Diferansiyel denklemi sadece teorik olarak çözemezseniz; sahada deli gibi titreyen, kararsızlığa düşmüş bir PID kontrolcüsünü asla sakinleştiremezsiniz.
*   Statik ve Mukavemet bilmezseniz; tasarladığınız robot kolunun neden yük altında esnediğini, neden beklenen hassasiyette (tekrarlanabilirlik) çalışmadığını asla anlayamazsınız.
*   Termodinamik bilmezseniz; dünyanın en iyi kodunu da yazsanız, o işlemcinin neden sürekli "Thermal Throttling" yaparak sistemi yavaşlattığını çözemezsiniz.

Bu modülde, akademik ispatların steril ve soğuk dünyasından çıkıp; gürültülü, yağlı ve gerçek olan **teşhis (diagnosis)**, **kestirimci bakım (predictive maintenance)** ve **öngörü (prediction)** dünyasına adım atıyoruz.

---

## 🧠 1. Kalkülüs: Değişimin ve Geleceğin Lisanı

Sanayide "duran" bir makine ya kapalıdır ya da bozuktur. Çalışan, değer üreten her makine sürekli bir **değişim** halindedir. Isınır, hızlanır, yavaşlar, basınçlanır, titreşir ve aşınır. Kalkülüs, işte bu değişimi anlama ve yönetme sanatıdır.

### Türev (Derivative): Hatanın Ayak Sesleri
Bizim için türev, grafikteki bir teğetin eğimi değildir. Türev, **geleceğin bilgisidir**.
*   **Hata Hızı (Rate of Error):** Sensör verisindeki anlık değişim hızı, bize hatanın ne kadar hızlı büyüdüğünü söyler.
*   **Öngörü:** PID kontrolcüsündeki 'D' (Derivative) terimi, türev sayesinde geleceği tahmin eder. "Hata şu an küçük ama çok hızlı artıyor, hemen fren yapmalıyım!" diyerek sistemi kaza yapmaktan kurtarır.
*   **Saha Karşılığı:** Motorun sıcaklığı 1 saatte 5 derece arttıysa sorun yok (D düşük). Ama 1 dakikada 5 derece arttıysa (D çok yüksek), fan bozulmuş demektir. Termal koruma devreye girmelidir.

### İntegral (Integral): Geçmişin Yükü ve Hafıza
İntegral, birikimdir. Geçmişte yaşananların bugüne etkisidir.
*   **Birikmiş Hata (Accumulated Error):** PID'deki 'I' (Integral) terimi, geçmişteki küçük ama giderilememiş hataları toplar ve "Yeter artık, hedefe ulaşmak için daha fazla güç uygulamalıyız" der.
*   **Saha Karşılığı:** Hidrolik tankındaki mikro sızıntıyı anlık basınç sensörü fark etmez (Türev sıfıra yakın). Ama sızıntıyı zamana göre integre ederseniz (toplarsanız), tankın yarısının boşaldığını görürsün. İntegral, sinsi hataları yakalar.

---

## ⚛️ 2. Fizik: Mühendisliğin Değişmez Anayasası

Yazılım dünyasında kuralları programcı koyar; gerekirse o kuralları değiştirebilir, esnetebilir ("hack") veya baştan yazabilir. Ancak fiziksel dünyada kurallar evrenindir (Newton, Termodinamik, Maxwell) ve bu kurallar asla tartışılamaz, rüşvet verilemez.

*   **Eylemsizlik (Inertia):** "Duran durmak, giden gitmek ister." 200 kg'lık bir robot kolunu 2 m/s hızla sürerken birden durduramazsınız. Durdurmaya çalışırsanız, o enerji bir yerden çıkar (redüktör dişlisini kırar, kayışı koparır, robotun taban cıvatalarını söker).
*   **Enerjinin Korunumu:** Enerji yok olmaz, sadece şekil değiştirir. Genellikle de istemediğimiz bir şekle: **Isı**. Verimsiz her sistem, faturayı ısı olarak öder.

---

## 📐 3. Lineer Cebir: Robotik Uzayın Haritası

Bir robot kolunun, uç noktasının (Tool Center Point - TCP) uzayda nerede olduğunu bilmesi için sadece geometri yetmez, **Lineer Cebir** gerekir.
*   **Matrisler ve Dönüşüm:** Robotun her bir eklemi bir matris, her hareketi bir matris çarpımıdır.
*   **Singularity (Tekillik):** Robotun kilitlendiği, sonsuz hıza çıkmaya çalıştığı o korkunç an, aslında matematiksel bir **determinantın sıfır olması** durumudur. Matrisin tersinin alınamadığı (inverse kinematics fail) noktadır. Sahada robotu tamir eden tekniker, aslında matristeki o "sıfırı" yok etmeye çalışır.

---

## 📚 Modül İçeriği ve Saha Rehberi

Bu klasörde, teorik ders kitaplarının aksine, "Bu bilgi ile sahada nasıl arıza çözerim?" sorusuna odaklanan notlar bulacaksınız.

| Dosya | Açıklama | Saha Uygulaması |
| :--- | :--- | :--- |
| **[`01_Calculus_Diagnostics.md`](./01_Calculus_Diagnostics.md)** | Kalkülüs ile Sistem Teşhisi | PID ayarı, Isı artış analizi, Sızıntı tespiti. |
| **[`01_Physics_Safety.md`](./01_Physics_Safety.md)** | Fizik Yasaları ve İş Güvenliği | Eylemsizlik momenti, Tork hesabı, Potansiyel enerji tehlikeleri. |
| **[`02_Linear_Algebra_Robotics.md`](./02_Linear_Algebra_Robotics.md)** | Robotik için Matrisler | İleri/Ters Kinematik, Singularity, Koordinat sistemleri. |

---

> **Ustanın Bilgelik Notu:**  
> "Formülleri ezberlemek için hafızanızı yormayın; onların grafiklerini, fiziksel hissini ve sesini hayal edin. Bir sinüs dalgası gördüğünüzde aklınıza trigonometri sınavları gelmesin; aklınıza saniyede 50 kez yön değiştiren şebeke voltajı (AC) veya harmonik hareket yapan, titreyen bir yay sistemi gelsin. Matematik kağıt üzerinde değil, makinenin metal gövdesinde yaşar."
