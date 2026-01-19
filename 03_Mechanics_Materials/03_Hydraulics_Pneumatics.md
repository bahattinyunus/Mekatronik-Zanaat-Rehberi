# 03. Hidrolik & Pnömatik: Gücün Akışkan Hali

> *"Elektrik ışık hızındadır ama torksuzdur. Hidrolik yavaştır ama bir dağı yerinden oynatır. Pnömatik ise hızlıdır, çeviktir ama 'sünger' gibidir. Hangi gücü nerede kullanacağını bilmek, mühendislik bilgeliğidir."*

---

## 🌊 Metal Yaka Perspektifi: Sızıntı ve Basınç

Bir yazılım "memory leak" (bellek sızıntısı) yaptığında bilgisayar yavaşlar. Bir hidrolik sistem sızıntı yaptığında ise fabrika zemini yağ gölüne döner, basınç düşer ve tonlarca yük operatörün üzerine düşebilir. Bizim dünyamızda "leak" (sızıntı) sanal değil, ölümcül derecede gerçektir.

Bizler **"Akışkan Gücü Yöneticileriyiz"**. Boruların içindeki görünmez gücü (basıncı) yönetir, valflerin senfonisini (tıslamalar ve klik sesleri) dinleriz.

---

## 🛢️ 1. Hidrolik: Sıvı Kas Kuvveti (Hydraulics)

Hidrolik sıkıştırılamaz. Bu yüzden "Kesinlik" ve "Güç" demektir. Bir kepçenin kolunu kaldırmak veya 10 tonluk press makinesini indirmek için kullanılır.

### Sahada Karşılaşılan Sorunlar (Troubleshooting)
*   **Kavitasyon (Cavitation):** Pompa "çakıl taşı kırıyor" gibi ses çıkarıyorsa, yağın içinde hava kabarcıkları patlıyordur.
    *   **Tehlike:** Bu mikro patlamalar metal yüzeyleri oyuk oyuk eder (Pitting) ve pompayı içeriden yer bitirir.
    *   **Çözüm:** Emiş hattını kontrol et, filtre tıkalı mı bak, yağ seviyesini tamamla.
*   **Isınma:** Yağ 60-70°C'yi geçerse viskozitesi düşer (su gibi olur). Conta ve O-ringler pişer, sertleşir ve sızdırmaya başlar.
    *   **Metal Yaka Kuralı:** Elini tanka dokunduğunda elin yanıyorsa, sistem "hasta" demektir. Soğutucuyu kontrol et.

### Güvenlik: Enjeksiyon Yaralanması
Yüksek basınçlı (200 bar) bir hidrolik hortumda iğne ucu kadar bir delik varsa, oradan çıkan yağ jeti derinizi delip geçer ve kanınıza karışır.
*   **ASLA** sızıntıyı elinizle aramayın. Bir karton parçası kullanın.
*   Bu yaralanma ilk başta sivrisinek ısırığı gibi görünür, 6 saat sonra parmağınızı kangrenden kaybedersiniz.

---

## 💨 2. Pnömatik: Havanın Çevikliği (Pneumatics)

Hava sıkıştırılabilir. Bu yüzden pnömatik sistemler "yaylı" gibidir, esnektir ve çok hızlıdır. Otomasyon hatlarında "tak-tak-tak" çalışan pistonlar, tutucular (grippers) havalıdır.

### Havanın Düşmanları
1.  **Su (Nem):** Kompresörden gelen havada su buharı vardır. Bu su valflerin içinde yoğunlaşırsa, paslanma yapar ve valf kilitlenir (Stick-slip).
    *   **Çözüm:** Kurutucu (Dryer) ve Şartlandırıcı (FRL) bakımı hayatidir.
2.  **Kaçaklar:** Pnömatik sistemler genellikle "tıslar". Bu kaçaklar önemsenmez ama fabrikanın elektrik faturasının %30'u boşa çalışan kompresöre gider.
    *   **Metal Yaka Görevi:** Gece fabrika durduğunda sessizlikte dolaşın ve "tıslamaları" dinleyip işaretleyin.

---

## 🔧 Saha Rehberi: Valfler ve Diyagramlar

### Yön Denetim Valfleri (5/2, 3/2)
Şemaya baktığınızda P, R, A, B portlarını karıştırıyorsanız valfi yakarsınız.
*   **P (Pressure):** Basınç girişi (1 numara).
*   **R/S (Exhaust):** Egzoz (3, 5 numara). Susturucu takılmazsa kulakları sağır eder.
*   **A/B:** Pistona giden iş hatları (2, 4 numara).

### Hız Kontrolü
*   **Kural:** Hızı, havayı *gönderirken* değil, *tahliye ederken* kısarak ayarlarız (Meter-out).
*   Girişi kısarsanız piston "sarsılarak" (jerky) hareket eder. Çıkışı kısarsanız piston "yağda kayar gibi" pürüzsüz gider.

---

> **Ustanın Tavsiyesi:**
> "Hidrolik yağını değiştirmek, makineye 'kan nakli' yapmak gibidir. Kirli yağ ile çalışan makine, damarlarında zehir dolaşan insan gibidir; yavaşlar, ateşi çıkar ve sonunda kalbi (pompa) durur. Filtrelere ve yağ temizliğine, kendi böbreklerinize baktığınız gibi bakın."
