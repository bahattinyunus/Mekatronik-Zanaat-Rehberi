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

> **Ustanın Notu:** "3D yazıcı, fikirleri denemek içindir. CNC, o fikirleri kalıcı kılmak içindir. Bir robotun ana gövdesini PLA plastikten basarsan, yazın güneş altında eridiğini veya cıvataların plastiği ezip gevşediğini görürsün (Creep). Mühendislik plastiğe güvenmez demiyorum; doğru plastiği (PETG/ABS/Nylon) seçmeyi bil diyorum."
