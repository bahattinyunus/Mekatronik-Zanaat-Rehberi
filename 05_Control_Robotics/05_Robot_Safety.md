# 🚷 Robot Güvenliği: Kanla Yazılmış Kurallar

> *"Güvenlik kuralları mürekkeple değil, ölen işçilerin kanıyla yazılmıştır. Bir kuralı ihlal ettiğinde, sadece işini değil, hayatını riske atarsın. Robotun Asimov Kanunlarından haberi yoktur."*

Endüstriyel robotlar (KUKA, FANUC, ABB) oyuncak değildir. Tonlarca kuvvet uygulayabilirler ve insan reflekslerinden çok daha hızlıdırlar. Bir robotun kolu saniyede 2 metre hızla hareket ettiğinde, o kütle bir <u>Balyoz</u> etkisi yaratır.

---

## 1. Teslimiyet Alanı (Kill Zone / Danger Zone)

Robotun kolunun erişebileceği maksimum mesafenin (Maximum Reach) oluşturduğu dairedir.
*   **Altın Kural:** Robot enerjiliyken (Servo ON) bu alana **ASLA** girilmez.
*   **Fiziksel Bariyerler:** Işık bariyerleri, lazer tarayıcılar (Lidar) ve güvenlik çitleri bu yüzden vardır.
*   **Bypass Suçu:** Güvenlik sensörünü bantlamak veya kilidi (Interlock) kısa devre yapmak, **Cinayete Teşebbüs** suçudur. Asla yapma, yaptırtma.

---

## 2. Teach Pendant (El Terminali) Disiplini

Robotu manuel modda (T1/Manual) sürerken (Jogging):
*   **Ölü Adam Anahtarı (Deadman Switch):** Terminalin arkasındaki 3 konumlu butondur.
    *   **Bırakırsan:** Robot DURUR.
    *   **Yarım Basarsan:** Robot ÇALIŞIR.
    *   **Tam Sıkarsan (Panik/Kramp):** Robot DURUR. (Bu mekanizma, elektrik çarpması veya korku anında kasılan eli algılamak içindir).
*   **Hız Limiti:** Manuel modda hız asla **250mm/s**'yi geçmemelidir. Refleksleriniz bundan hızlısına yetmez.

---

## 3. LOTO (Lock Out, Tag Out) - Etiketle ve Kilitle

Bakım yapmak için hücreye gireceksen:
1.  **Enerjiyi Kes:** Ana şalteri indir.
2.  **Kilitle (Lock):** Şaltere **kendi** asma kilidini tak. Anahtarı sadece cebine koy.
3.  **Etiketle (Tag):** Kilit üzerine "BAKIM VAR - AÇMAYIN - [İsim Soyisim] - [Tarih]" yazan etiketi as.
4.  **Doğrula:** Robotun elektriğinin gerçekten kesildiğini kontrol et (LED'ler sönük mü?).

**Neden?** Sen içeride bakım yaparken, çay molasından dönen diğer vardiya operatörü "Aaa şalter atmış" diyip şalteri kaldırabilir. Bu, endüstrideki en yaygın ve korkunç ölüm sebebidir.

---

## 4. Görünmeyen Tehlikeler: Enerji Depolayanlar

Fişi çekmek yetmez. Sistemde **Potansiyel Enerji** saklanmış olabilir.
*   **Yerçekimi:** Robot kolu havada olabilir. Frenler bozulursa veya freni "manuel" açarsan kol düşer. **Altına takoz koymadan freni açma.**
*   **Pnömatik Basınç:** Hava hortumlarında 6-8 bar basınç hapsolmuş olabilir. Bir hortumu sökerken kamçı gibi çarpıp gözünü çıkarabilir. Havasını boşalt (Bleed Valve).
*   **Kapasitörler:** Sürücü kartındaki dev kondansatörler (DC Bus), elektrik kesildikten sonra bile 10 dakika boyunca ölümcül voltaj (600V) tutabilir. Deşarj olmasını bekle.

---

> **Ustanın Notu:** "Bir kaza olduğunda robot hapse girmez, servise gider. Sen mezara gidersin, mühendis de mahkemeye. Güvenlik kuralları bürokrasi değil, yaşam sigortasıdır."
