# 🚷 Robot Güvenliği: Kanla Yazılmış Kurallar

> *"Robotun Asimov Kanunlarından haberi yoktur. Önüne geçerseniz sizi sadece 'fiziksel bir engel' olarak görür ve o engeli aşmak için torku artırır."*

Endüstriyel robotlar (KUKA, FANUC, ABB) oyuncak değildir. Tonlarca kuvvet uygulayabilirler ve insan reflekslerinden çok daha hızlıdırlar.

## 1. Teslimiyet Alanı (Kill Zone)
Robotun maksimum erişim mesafesinin (Maximum Reach) oluşturduğu dairedir.
*   **Kural:** Robot enerjiliyken bu alana girilmez.
*   **Önlem:** Işık bariyerleri, lazer tarayıcılar (Lidar) ve güvenlik çitleri bu yüzden vardır. Bunları "bypass" etmek (devre dışı bırakmak) intihardır.

## 2. Teach Pendant (El Terminali) Disiplini
Robotu el terminaliyle manuel sürerken (Jogging):
*   **Ölü Adam Anahtarı (Deadman Switch):** Terminalin arkasındaki butondur. Yarım basarsan robot çalışır. Bırakırsan durur. Panikleyip tam sıkarsan (kramp durumunda) yine durur. Bu mekanizma hayat kurtarır.
*   **Hız Limiti:** Manuel modda (T1/Manual) hız asla %10'u veya 250mm/s'yi geçmemelidir. Refleksleriniz bundan hızlısına yetmez.

## 3. LOTO (Lock Out, Tag Out) - Etiketle ve Kilitle
Bakım yapacaksanız:
1.  Enerjiyi kes.
2.  Şaltere kendi asma kilidini tak.
3.  Üzerine "BAKIM VAR - AÇMAYIN" etiketi as.
4.  Anahtarı cebine koy.
Bunu yapmazsanız, siz içeride bakım yaparken başka biri "kim kapattı bunu" deyip şalteri kaldırabilir. Bu, endüstrideki en yaygın ölüm sebebidir.

## 4. Yerçekimi ve Pnömatik Enerji
Elektriği kesseniz bile tehlike bitmez.
*   **Yerçekimi:** Robot kolu havada olabilir. Frenler bozulursa düşer. Altına takoz koy.
*   **Basınç:** Pnömatik hortumlarda hala 6 bar basınç olabilir. Bir hortumu sökerken kamçı gibi çarpabilir. Havasını boşalt (Bleed Valve).

---
> **Ustanın Notu:** "Bir kaza olduğunda robot hapse girmez, siz mezara girersiniz, mühendis de mahkemeye gider. Güvenlik kuralları bürokrasi değil, yaşam sigortasıdır."
