# Projeler & Laboratuvarlar: İspat Meydanı (The Proving Ground)

> *"Teoride, teori ile pratik aynıdır. Pratikte ise farklıdır."*

Burası sınıf değil, **hurdalıktır**. Burası, mükemmel çalışan kodların donanımla buluşunca patladığı, kusursuz tasarımların montajda birbirine uymadığı yerdir. Ve gerçek öğrenme tam olarak burada, işler ters gittiğinde başlar.

Bir "Metal Yaka" portföyü, "çalışan projeler" listesi değil, "karşılaşılan sorunlar ve çözümler" kataloğudur.

## 🛠️ Metal Yaka Perspektifi: Proje Kültürü

### 1. Başarısızlık Günlüğü (Builder's Log)
Çalışan bir robotun videosunu herkes çeker. Bizim için değerli olan, o robot çalışana kadar kaç motor yaktığın, kaç kere kodun çöktüğü ve bu sorunları **nasıl aştığındır**.
*   **Hata:** "Motor dönmüyor."
*   **Çözüm:** "Multimetre ile ölçtüm, sürücü bacağına sinyal gelmiyor. Kodu kontrol ettim, GPIO'yu output olarak tanımlamayı unutmuşum." -> İşte bu, altın değerinde bir nottur.

### 2. "Hello World" Değil, "Blink LED" Hiç Değil
Ekrana yazı yazdırmak yazılımcının işidir. Bizim "Hello World"ümüz, fiziksel bir LED'i yakıp söndürmektir. Ama o da yetmez. Bizim gerçek projemiz, bir motoru yük altında, ısınmadan, istenilen pozisyona, istenilen hızda götürmektir.

## 📚 Proje Kategorileri & Örnekler

### Seviye 1: Çırak (Bileşenleri Tanıma)
*   **Çizgi İzleyen Robot:** Basit görünüyor değil mi? Ama PID kontrolü öğrenmek için dünyadaki en iyi okuldur. Sensör gürültüsüyle ve motor tepki süresiyle tanışma.
*   **Akıllı Sera:** Sensör okuma (sıcaklık/nem) ve röle kontrolü (su motoru). IoT dünyasına giriş.

### Seviye 2: Kalfa (Sistemi Kurma)
*   **Kendini Dengeleyen Robot:** Ters sarkaç. Gerçek zamanlı kontrol (RTOS) ve IMU (Jiroskop) sensör füzyonu (Kalman Filtreleri) olmadan ayakta duramaz.
*   **3D Yazıcı / CNC Yapımı:** Kendi takım tezgahını yapmak. Step motor kontrolü, şase rijitliği ve güç kaynağı hesabı.

### Seviye 3: Usta / Baş Teknisyen (Entegrasyon)
*   **Görüntü İşlemeli Robot Kol (Pick & Place):** Kamera (OpenCV) nesneyi görür, koordinatı çıkarır, ters kinematik ile robot kolu oraya gider, parçayı alır. Yazılım, Elektronik ve Mekaniğin senfonisi.
*   **Otonom Mobil Robot (AMR):** SLAM (Eş Zamanlı Konumlandırma ve Haritalama). Robotun bilmediği bir odada harita çıkarıp yolunu bulması. ROS (Robot Operating System) ustalığı.

---

> **Ustanın Notu:** "Çalışmayan projenizi çöpe atmayın. O bir başarısızlık değil, henüz çözülmemiş bir bulmacadır. En iyi mühendisler, en çok parça bozanlardır; çünkü her bozdukları parçada o parçanın limitlerini öğrenmişlerdir."
