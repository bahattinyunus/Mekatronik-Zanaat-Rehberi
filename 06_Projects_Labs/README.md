<p align="center">
  <a href="../README.md">🏠 Home</a> | 
  <a href="../01_Engineering_Fundamentals/README.md">📚 Fundamentals</a> | 
  <a href="../02_Electrical_Electronics/README.md">⚡ Electronics</a> | 
  <a href="../03_Mechanics_Materials/README.md">⚙️ Mechanics</a> | 
  <a href="../04_Programming_Embedded/README.md">💾 Embedded</a> | 
  <a href="../05_Control_Robotics/README.md">🦾 Robotics</a> | 
  <b>[ 🧪 Laboratory ]</b>
</p>

---

# 06. Projeler & Laboratuvar: İspat Meydanı ve Hurdalık

![Challenge](https://img.shields.io/badge/Challenge-ACCEPTED-success?style=for-the-badge&logo=target)
![Mode](https://img.shields.io/badge/Mode-Survival-critical?style=for-the-badge)

> *"Teoride, teori ile pratik aynıdır. Pratikte ise, dağlar kadar farklıdır."*

Burası steril bir sınıf veya sessiz bir kütüphane değil; burası bir **hurdalıktır**. Burası, bilgisayar ekranında mükemmel çalışan algoritmaların donanımla buluşunca patladığı, simülasyonda kusursuz oturan tasarımların montajda deliklerinin birbirini karşılamadığı, kabloların koptuğu, dumanların çıktığı ve gerçek öğrenmenin başladığı yerdir.

Bir "Metal Yaka" teknisyeninin CV'si (Özgeçmişi), "başarıyla tamamlanmış temiz projeler" listesi değil; **"karşılaşılan felaketler, patlayan parçalar ve bunlara bulunan dahiyane sahra çözümleri"** kataloğudur.

---

## 🛠️ Metal Yaka Kültürü: Hata Yap, Kaydet, Öğren

### 1. Başarısızlık Günlüğü (Failure Log)
Çalışan ve ışıldayan bir robotun videosunu herkes çeker ve LinkedIn'e koyar. Bu **pazarlamadır**.
Bizim için değerli olan o son video değil; o robotu çalıştırana kadar kaç tane sürücü yaktığın, kaç gece uykusuz kaldığın ve sorunu nasıl çözdüğündür. Bu **mühendisliktir**.

*   **Çöp Veri:** "3 Eksen CNC yaptım, çalıştı." (Kimseye faydası yok).
*   **Altın Veri:** "Step motorlar eksen kaçırıyordu. Osiloskopla baktım, kablolar birbirine paralel gittiği için EMI (Gürültü) biniyordu. Kabloları örgü (twisted pair) yaptım ve blendajladım. Sorun çözüldü." (İşte bu, sektörel tecrübedir).

### 2. "Hello World" Değil, "Smoke Test"
Bir yazılımcı için "Hello World", ekrana yazı yazdırmaktır, risksizdir.
Bir donanımcı için ilk adım **"Smoke Test" (Duman Testi)** dir. Sisteme ilk kez enerji verdiğin o korku dolu andır. Patlama yoksa, duman yoksa başarılısındır. Sonra LED yakarsın (Blink), sonra motor döndürürsün.

---

## 🥋 Proje Ağacı ve Seviye Sistemi

Bu modülde, bir Çırak'tan bir Usta'ya dönüşüm yolculuğunuzu simüle eden projeler bulunur.

### 🟡 Seviye 1: Çırak (The Apprentice)
*Hedef: Bileşenleri tanıma, lehim yapma, basit kontrol döngüsü.*

*   **P1.1 - Analog Hat İzleyen (Çizgisiz):** İşlemci yok. Sadece OpAmp (Karşılaştırıcı), transistörler ve sensörler. Elektroniğin temel mantığını (Logic) donanımla kurmak.
*   **P1.2 - Akıllı Sera (Histerezis):** Sıcaklık/Nem sensörü ve Röle. Amaç: Motorun "zırt-pırt" açılıp kapanmasını (Chattering) engellemek için yazılımsal histerezis (Hysteresis) uygulamak.

### 🟠 Seviye 2: Kalfa (The Journeyman)
*Hedef: Sistem entegrasyonu, mekanik tasarım, güç elektroniği.*

*   **P2.1 - Masaüstü CNC / Plotter:** Step motor kontrolü, G-Code işleme, şase rijitliği. X-Y-Z eksenlerinin dikliğini (Squareness) ayarlamak.
*   **P2.2 - Dengede Duruş (Self-Balancing Robot):** Ters sarkaç. PID kontrolün ve Sensör Füzyonunun (Jiroskop + İvmeölçer = Kalman Filtresi) zorunlu olduğu proje. Ayakta duramayan robot düşer ve kırılır; yazılımın fiziksel cezası vardır.

### 🔴 Seviye 3: Usta (The Master)
*Hedef: Yapay Zeka, Görüntü İşleme, Endüstriyel Haberleşme.*

*   **P3.1 - Görüntü İşlemeli Ayıklama Kolu (Vision Pick & Place):** Kamera (OpenCV) nesneyi tanır, rengini ve koordinatını bulur. 3 Eksenli robot koluna "Ters Kinematik" ile emir gider. Robot parçayı alır ve doğru kutuya atar.
*   **P3.2 - Fabrika İçi Otonom Taşıyıcı (AMR):** Lidar ile haritalama (SLAM). A noktasından B noktasına insana çarpmadan giden lojistik robotu.

---

## 📚 Modül İçeriği ve Şablonlar

| Dosya | Açıklama | Kullanım Amacı |
| :--- | :--- | :--- |
| **[`06_Failure_Log_Template.md`](./06_Failure_Log_Template.md)** | Arıza Kayıt Şablonu | Her patlayan parça, her bug buraya yazılacak. |
| **[`06_Project_L1_LineFollower.md`](./06_Project_L1_LineFollower.md)** | Seviye 1: Hat İzleyen | PID'yi görerek öğrenmek. |
| **[`06_Project_L2_CNC_Build.md`](./06_Project_L2_CNC_Build.md)** | Seviye 2: CNC Yapımı | Mekanik hassasiyet ve eksen kontrolü. |
| **[`06_Project_L3_VisionArm.md`](./06_Project_L3_VisionArm.md)** | Seviye 3: Robot Kol & AI | Kinematik ve OpenCV entegrasyonu. |

---

> **Ustanın Bilgelik Notu:**  
> "Çalışmayan projenizi asla çöpe atmayın. O bir başarısızlık değil, henüz çözülmemiş bir bulmacadır. Dünyanın en iyi mühendisleri, en çok parça bozanlardır; çünkü her bozdukları parçada o malzemenin limitlerini, o kodun açığını ve fiziğin kurallarını yaşayarak öğrenmişlerdir. **Boza boza yapmayı öğreneceksiniz.**"
