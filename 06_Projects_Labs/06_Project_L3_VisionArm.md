# 🦾 Seviye 3 Proje: Görüntü İşlemeli Robot Kol (Pick & Place)

> *"Göz ve El Koordinasyonu. Bir insanın kahve fincanını alması basittir, ama bunu bir makineye öğretmek için Lineer Cebir, Görüntü İşleme, Ters Kinematik ve Gerçek Zamanlı Kontrolü birleştirmeniz gerekir. Bu proje, Mekatronik Mühendisliğinin zirvesidir."*

---

## 🎯 Hedef
Masa üzerine rastgele bırakılan renkli blokları (Kırmızı, Mavi, Yeşil) kamera ile tespit etmek, robot kol ile almak ve renklerine göre ayrılmış kutulara dizmek.

---

## 🧠 Öğrenilecek Metal Yaka Becerileri
1.  **Bilgisayarlı Görü (Computer Vision):** OpenCV kullanarak renk uzayları (HSV vs RGB), gürültü temizleme (Erosion/Dilation) ve nesne merkezi (Centroid) bulma.
2.  **Koordinat Dönüşümü:** Kameranın gördüğü piksel (Px, Py) ile robotun dünyasındaki milimetre (Rx, Ry) arasındaki ilişkiyi kurmak (Kamera Kalibrasyonu).
3.  **Ters Kinematik (Inverse Kinematics - IK):** Robotun ucunu (X,Y,Z) noktasına götürmek için her bir eklemin (Theta1, Theta2, Theta3) kaç derece dönmesi gerektiğini hesaplamak.
4.  **Seri Haberleşme:** PC (Python) ile Mikrodenetleyici (Arduino/STM32) arasında güvenilir veri paketi protokolü kurmak.

---

## 🛠️ Donanım Listesi
*   **Robot Kol:** 3 veya 4 Eksenli (DOF) Robot Kolu (Servo motorlu veya Step motorlu).
*   **Kamera:** USB Webcam veya Raspberry Pi Kamera. (Sabit, masaya tepeden bakan kuş bakışı montaj).
*   **PC/SBC:** Görüntü işleme için Laptop veya Raspberry Pi 4.
*   **Kontrolcü:** Servo motorları sürmek için Arduino veya PCA9685 Sürücü.

---

## ⚙️ Sistem Mimarisi

### 1. Göz: Görüntü İşleme (Python + OpenCV)
*   **Renk Tespiti:** RGB uzayı ışık değişiminden çok etkilenir. HSV (Hue, Saturation, Value) uzayına geç. "Sadece Kırmızıyı Gör" maskesi uygula.
*   **Kontur Bulma:** `cv2.findContours` ile şeklin sınırlarını bul, `cv2.moments` ile ağırlık merkezini (Cx, Cy) hesapla.
*   **Kalibrasyon Matrisi:** Kameradaki 100 piksel gerçekte kaç cm? Masanın üzerine cetvel koy ve "Piksel/mm" oranını bul.

### 2. Beyin: Koordinat Dönüşümü ve IK
*   Kamera (0,0) noktası sol üst köşedir. Robotun (0,0) noktası ise tabanının merkezidir.
*   **Koordinat Ofseti:** `Robot_X = (Kamera_X * Skala) - Ofset_X`
*   **Ters Kinematik:** Geometrik yöntem veya trigonometri kullanarak, o konuma gitmek için gereken açıları hesapla. (Lise geometrisindeki Kosinüs Teoremi burada hayat kurtarır).

### 3. El: Motor Kontrolü ve Haberleşme
*   Python, hesapladığı açıları (Örn: `A:90,B:45,C:120,Gripper:1`) USB portundan gönderir.
*   Arduino bu paketi alır, dizeyi ayrıştırır (Parsing) ve servoları o açılara yavaşça (rampalı) sürer.

---

## 🚧 Saha Zorlukları (Field Challenges)

1.  **Işık Değişimi:** Odaya güneş girince kırmızı rengi turuncu görebilir.
    *   *Çözüm:* Işıktan etkilenmeyen nesneler kullan veya yapay aydınlatma (LED halka ışık) ile ortamı sabitle.
2.  **Mekanik Boşluk (Backlash):** Ucuz servoların dişlilerinde boşluk vardır. Hesaplanan yere gitse bile 1-2 cm sapabilir.
    *   *Çözüm:* Kaliteli servo kullan veya yazılımsal sapma payı (Offset) ekle.
3.  **Zaman Gecikmesi (Latency):** Görüntü işleme yavaştır. Robot hareket ederken görüntü alırsan, robotun eski konumunu görürsün.
    *   *Çözüm:* "Dur, Bak, Hesapla, Hareket Et" döngüsü kur.

---

> **Ustanın Tavsiyesi:** "Önce kör bir robot yap. Koordinat verince hatasız gidiyor mu? Sonra kamerayı ekle. İki bilinmeyenli denklem çözmeye çalışma. Önce mekaniğe güven, sonra göze güven."
