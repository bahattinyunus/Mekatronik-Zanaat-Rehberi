# 🏭 Üretim Yöntemleri: Dijital Koddan Fiziksel Nesneye

> *"En iyi tasarım, sadece kağıt üzerinde çalışan değil, 'üretilebilir' olandır. Usta 'Bu çıkmaz' diyorsa, o tasarım çöptür."*

Metal Yaka Mimarı, tasarladığı parçanın hangi tezgahta, hangi uçla, kaç dakikada ve hangi maliyetle üretileceğini bilir.

---

## 1. Talaşlı İmalat (Subtractive Manufacturing - CNC)

Büyük bir bloktan parça kopararak şekil verme. Heykeltraşlık.
*   **Malzemeler:** Çelik, Alüminyum, Pirinç, Delrin.
*   **Hassasiyet:** Mikron seviyesi (0.001mm - 0.05mm).
*   **Saha Notu:** İç köşe radyüsleri. Freze ucu yuvarlaktır. Bu yüzden CNC ile üretilen bir parçada, dik bir iç köşe (90 derece) asla tam keskin olamaz. Tasarımda buraya "köpek kemiği" (dogbone) veya radyüs koymazsan, parçan montajda yerine oturmaz.

## 2. Katmanlı İmalat (Additive Manufacturing - 3D Print)

Yoktan var etme. Katman katman örme.
*   **FDM (Plastik):** Hızlı prototip. Ancak Z ekseninde (katman yönünde) zayıftır. Yük binen parçayı 3D basacaksan, katman yönünü yüke dik yapmalısın.
*   **SLA (Reçine):** Çok hassas ama kırılgandır. Dişli prototipi için iyidir ama darbeye gelmez.
*   **Metal Sinterleme (SLS/DMLS):** Metal tozu lazerle eritilir. Uçak parçaları basılır. Pahalıdır.

## 3. Lazer ve Plazma Kesim

Sac metal (Sheet Metal) işleme.
*   **Büküm (Abkant):** Saca şekil verirken metalin "geri esneme" (springback) yapacağını unutma.
*   **Lazer:** Çok hassastır. 0.1mm delik açabilir.
*   **Plazma:** Kabadır. Kalın gemi saclarını keser. Kenarları pürüzlü ve cürufludur.

---

## 🆚 CNC mi, 3D Yazıcı mı?

| Özellik | CNC (Talaşlı) | 3D Yazıcı (FDM) |
| :--- | :--- | :--- |
| **Malzeme** | Metal, Sert Plastik | Termoplastik (PLA, ABS, PETG) |
| **Mukavemet** | Çok Yüksek (İzotropik) | Orta/Düşük (Anizotropik) |
| **Hız** | Seri üretimde hızlı | Yavaş (Saatler sürer) |
| **Geometri** | Sınırlı (Ters açı sorunu) | Sınırsız (Hollow iç yapı) |
| **Kullanım** | Nihai ürün, Kalıp | Prototip, Hobi, Aparat |

---

---

## 4. Karar Matrisi: Hangi Yöntem? (Cost vs Performance)

Mühendislik "en iyisini" yapmak değil, "işi gören en ucuzunu" yapmaktır.

| Özellik | CNC (Alüminyum) | 3D Baskı (FDM) | Lazer (Sac) |
| :--- | :--- | :--- | :--- |
| **Mukavemet** | 10/10 (Tank gibi) | 3/10 (Katmandan kırılır) | 8/10 (Büküme bağlı) |
| **Hassasiyet** | ±0.01 mm | ±0.2 mm | ±0.1 mm |
| **Maliyet (1 Adet)** | 💰💰💰💰💰 (Çok Pahalı) | 💰 (Bedava gibi) | 💰💰 (Makul) |
| **Hız** | Yavaş (Setup gerekir) | Orta (Gece bas sabah al) | Çok Hızlı |
| **En İyi Kullanım**| Robot Gövdesi, Motor Yatağı | Sensör Tutucu, Kablo Kanalı | Şase Kapakları, Braket |

### DFM (Design for Manufacturing) İlkeleri
1.  **CNC için:** İç köşelere radyüs at. Matkap kare delik açamaz.
2.  **3D Baskı için:** 45 dereceden fazla çıkıntı (overhang) yapma, destek (support) gerekir.
3.  **Lazer için:** Delik çapı sac kalınlığından küçük olamaz (Lazer geri teper).

---

> **Ustanın Notu:** "3D yazıcı, fikirleri denemek içindir. CNC, o fikirleri kalıcı kılmak içindir. Bir robotun ana gövdesini PLA plastikten basarsan, yazın güneş altında eridiğini veya cıvataların plastiği ezip gevşediğini görürsün (Creep). Mühendislik plastiğe güvenmez demiyorum; doğru plastiği (PETG/ABS/Nylon) seçmeyi bil diyorum."
