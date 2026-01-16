# 📐 Lineer Cebir ve Robotik: Uzayın Matematiği

> *"Robotun kolu senin elin gibidir; ama beyni matrislerle düşünür. Sen 'sağa git' dersin, o milyonlarca sayıyı çarpar. Bu dili anlamazsan, robotun neden kilitlendiğini (Singularity) asla anlayamazsın."*

Lineer Cebir, genellikle bilgisayar mühendisliğinin veya teorik matematiğin konusu sanılır. Oysa **Robotik** ve **Mekatronik**, hareket eden lineer cebirdir. 6 eksenli bir endüstriyel robotun her hareketi, bir matris çarpımı senfonisidir.

---

## 🏗️ 1. Matrisler ve Dönüşümler (Transformations)

Bir robot kolu, birbirine bağlı eklemlerden (Joints) ve uzuvlardan (Links) oluşur.
*   **Koordinat Sistemleri (Frames):** Robotun tabanı (Base Frame) bir dünyadır. Robotun elindeki tutucu (Tool Frame) başka bir dünyadır.
*   **Görev:** "Robotun elini, masadaki bardağın olduğu konuma götür."
*   **Sorun:** Masadaki bardak, masa koordinatlarına göredir. Robot ise kendi tabanına göre hareket eder.
*   **Çözüm (Homojen Dönüşüm Matrisleri):** Bizim basitçe "uzan ve al" dediğimiz işlem; robot için `T_Base_to_Shoulder * T_Shoulder_to_Elbow * T_Elbow_to_Wrist * T_Wrist_to_Tool` matris çarpımıdır.

### Saha Notu: TCP (Tool Center Point) Ayarı
Sahada en sık yapılan hata, robotun ucuna taktığınız ekipmanı (örneğin kaynak torcu) robota tanıtmamaktır.
*   Robot, fabrika çıkışında kendi bilek noktasını (Flange) bilir.
*   Siz ucuna 30cm uzunluğunda yamuk bir kaynak torcu takarsınız.
*   Robotu "Kendi ekseninde dön" komutuyla çevirdiğinizde, torcun ucu sabit kalmaz, geniş bir daire çizer.
*   **Çözüm:** TCP kalibrasyonu yapmak. Yani robota, yeni "elinin" ucunun nerede olduğunu, bir **Öteleme (Translation) ve Dönme (Rotation) Matrisi** olarak öğretmektir.

---

## ☣️ 2. Singularity (Tekillik): Robotun Kara Deliği

Sahada çalışırken bazen robotun garip sesler çıkardığını, titrediğini, hatta kilitlenip "Joint Speed Limit Error" vererek durduğunu görürsünüz. Hedef nokta robotun erişim alanı içindedir, peki sorun ne?

**Sorun: Singularity (Tekillik).**

### Matematiksel Açıklama
Robotun hızlarını hesaplarken **Jacobian Matrisi** denilen bir matrisin tersini (Inverse) alırız.
*   Lineer cebirde kural: **Hangi matrisin tersi alınamaz? Determinantı 0 olan matrisin!**
*   Eğer robot kolu dümdüz uzanırsa veya bazı eklemler aynı hizaya gelirse, Jacobian matrisinin determinantı sıfıra yaklaşır.
*   Matrisin tersini almaya çalıştığınızda (1/0 durumu), sonuç **SONSUZ** olur.

### Fiziksel Karşılık
Robotun kontrolcüsü, o noktaya gitmek için eklem motorlarına "Sonsuz hızda dön!" komutu gönderir.
*   Motorlar inleyerek maksimum hıza çıkmaya çalışır.
*   Sistem titrer ve güvenlik limitlerine takılarak "Alarm" verip durur.
*   **Çözüm:** Robotu asla tam sınırlarında (tam düz uzanmış veya tam katlanmış) çalıştırma. Yörünge planlarken "Singularity Avoidance" tekniklerini kullan. Eklemlere 1-2 derecelik offset ver.

---

## 🧭 3. Vektörler ve Kuvvet Kontrolü

Sadece konumu (X, Y, Z) değil, kuvveti de kontrol ediyoruz.
*   **Senaryo:** Robot zımpara yapıyor.
*   **Vektör Hesabı:** Yüzeyin "Normal Vektörü"nü (yüzeye dik olan ok) hesaplamalısın. Robot, hareket ederken bu vektöre ters yönde sabit bir kuvvet (örneğin 10N) uygulamalıdır.
*   **Dot Product (İç Çarpım):** Kuvvetin ne kadarının yüzeye dik, ne kadarının teğet olduğunu bulmak işe yarar.

---

> **Ustanın Özeti:**
> *   Robotun "eli" neresidir? Bunu matrisle (TCP) tanımlamazsan, robot kör bir insan gibi eşyaları devirir.
> *   Singularity, robotun matematiksel felcidir. Onu bu duruma sokma.
> *   Lineer cebir bilmeyen robotçu, sadece "Teach Pendant" ile nokta kaydeden operatör olur. Matrisleri bilen ise robotun dans koreografisini yazar.
