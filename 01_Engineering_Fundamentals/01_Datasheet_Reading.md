# 01. Datasheet Okuma Sanatı: Mühnedisin Kutsal Kitabı

> *"Datasheet okumayan mühendis, pusulasız okyanusa açılan kaptan gibidir. Er ya da geç bir kayaya (yanlış voltaja) çarpar ve batar. Datasheet, üreticinin size yazdığı aşk mektubu değil, yasal uyarı metnidir."*

---

## 📄 1. "Features" (Özellikler): Pazarlama Tuzakları

İlk sayfa her zaman "bizim ürünümüz harika" der. Buna heveslenmeyin.
*   **Yazan:** "Up to 1A Current" (1 Ampere kadar akım).
*   **Gerçek:** Evet ama sadece laboratuvar ortamında, üzerine devasa bir soğutucu takarsan ve sıcaklık 25°C ise. Gerçek sahada o çip 0.5A'de yanabilir. İlk sayfaya asla güvenme.

---

## ⚡ 2. Absolute Maximum Ratings: Ölüm Sınırı

Burası **"Patlama Noktası"**dır.
*   Tablo der ki: `Vcc Max: 6.0V`.
*   Soru: "Hocam 6.1V versem çalışır mı?"
*   Cevap: **HAYIR.** 6.01V verdiğin an o çibin içindeki silikon transistörler delinir (Breakdown). Geri dönüşü yoktur.
*   **Metal Yaka Kuralı:** Asla sınırlarda dolaşma. Max 30V diyorsa, sen 24V sınırını geçme. %20 güvenlik payı bırak.

---

## 📊 3. Electrical Characteristics: Gerçek Hayat

Burası bizim oyun alanımızdır. Burada 3 sütun görürsün: **Min, Typ, Max**.
*   **Min (Minimum):** En kötü ihtimal (Düşük).
*   **Typ (Typical):** Ortalama dünyada olması gereken.
*   **Max (Maximum):** En kötü ihtimal (Yüksek).

**Ders:** Bir LED'in parlaklığını hesaplarken "Typ" değerini alabilirsin. Ama bir güç kaynağı tasarlarken her zaman **"Max"** değerine (En kötü senaryoya) göre tasarım yapmalısın. "Typical" değere güvenen mühendis, seri üretimde batar. Çünkü fabrikadan çıkan 1000 çipten 500'ü "Max" akımı çekebilir.

---

## 📍 4. Pin Configuration (Pinout)

Çipi ters takarsan yanar. Nokta (Dot) nerede? Çentik (Notch) nerede?
*   Pin 1 her zaman "Nokta"nın olduğu yerdedir.
*   Saymaya saat yönünün tersine (Counter-Clockwise) devam edilir.

---

## 🌡️ 5. Thermal Characteristics: Isı Yönetimi

*   **RθJA (Junction-to-Ambient):** Çip soğutucusuz havada dururken ne kadar ısınır?
*   Formül: `Isınma = Harcanan Güç (W) x RθJA`.
*   Bu değeri kontrol etmeden PCB tasarlama. Çip elini yakıyorsa, bu bölüme bakmadın demektir.

---

> **Ustanın Tavsiyesi:**
> "Yeni bir sensör veya çip kullanacaksan, kod yazmaya başlamadan önce Datasheet'in 'Electrical Characteristics' tablosunu A4 kağıda bas ve masana yapıştır. O tablo senin haritandır."
