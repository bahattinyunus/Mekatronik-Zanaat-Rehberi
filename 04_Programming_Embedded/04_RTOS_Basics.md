# ⏱️ RTOS Temelleri: Zamanın Efendisi Olmak

> *"Sıradan yazılımda 'hızlı olması' (Fast) iyidir. Gerçek zamanlı sistemde 'zamanında olması' (Predictable) zorunluluktur. Çok hızlı ama yanlış zamanda gelen veri, çöp veridir."*

Arduino'nun `loop()` döngüsü hobi için harikadır ama bir fabrikayı veya otonom aracı yönetmek için yetersizdir. Aynı anda hem motoru sürmek (10kHz), hem ekranı güncellemek (60Hz), hem de WiFi'dan veri okumak istiyorsanız; sistemi bir "İşletim Sistemi"ne (OS) emanet etmelisiniz.

---

## 1. Süper Döngü (Super Loop) vs RTOS

*   **Super Loop:** `while(1) { A(); B(); C(); }`
    *   Sırayla gider. Eğer A fonksiyonu (mesela sensör okuma) takılırsa, B (motor kontrolü) asla çalışmaz ve robot düşer.
*   **RTOS (FreeRTOS, ThreadX):**
    *   İşlemciyi mikrosaniyeler içinde dilimler (Time Slicing).
    *   Siz fark etmeden A'yı azıcık çalıştırır, durdurur, B'ye geçer, C'ye geçer. Sanki hepsi **aynı anda** çalışıyormuş gibi (Concurrency) olur.

---

## 2. Kritik Kavramlar

### A. Öncelik (Priority) ve Preemption (Zorla Alma)
En önemli iş, en önde yapılır.
*   **Yüksek Öncelik:** Motor Kontrolü (Acil).
*   **Düşük Öncelik:** Ekrana yazı yazma.
*   **Senaryo:** İşlemci ekranı güncellerken aniden motor sensöründen veri geldi.
*   **RTOS:** "Dur!" der. Ekran işlemini olduğu yerde dondurur (**Context Switch**), motor işlemini halleder ve sonra kaldığı yerden ekrana devam eder.

### B. Mutex (Tuvalet Anahtarı)
İki görev (Task) aynı anda tek bir kaynağa (örneğin LCD Ekrana veya I2C hattına) erişmeye çalışırsa ne olur?
*   **Task A:** "Hız: 10" yazmaya başladı. "Hız:" yazdı.
*   **Task B:** Araya girdi, "Isı: 40" yazdı.
*   **Sonuç:** "Hız: Isı: 40 10". Ekran çorba oldu.
*   **Çözüm:** **Mutex (Mutual Exclusion).** Odaya giren kapıyı kilitler (Mutex Take). İşini bitirene kadar başkası giremez. Çıkınca anahtarı bırakır (Mutex Give).

### C. Deadlock (Ölümcül Kilitlenme)
*   **Task A:** İşi yapmak için Kaynak 1 ve Kaynak 2'ye ihtiyacı var. Kaynak 1'i aldı.
*   **Task B:** İşi yapmak için Kaynak 2 ve Kaynak 1'e ihtiyacı var. Kaynak 2'yi aldı.
*   **Sonuç:** Task A, Kaynak 2'yi bekliyor. Task B, Kaynak 1'i bekliyor. İkisi de sonsuza kadar birbirini bekler. Sistem donar.
*   **Çözüm:** Kaynakları her zaman aynı sırayla işte. Veya "Timeout" kullan (Belli süre bekledim, gelmedi, elimdekini bırakıyorum).

---

## 3. Priority Inversion (Öncelik Tersinmesi): Mars Pathfinder Hatası
NASA'nın Mars aracı bu yüzden az kalsın görevini kaybediyordu.
1.  **Düşük Öncelikli Görev**, bir Mutex'i aldı.
2.  **Yüksek Öncelikli Görev** uyandı, o Mutex'e ihtiyacı var ama alamıyor, bekliyor.
3.  **Orta Öncelikli Görev** uyandı. Düşük görevden daha önemli olduğu için işlemciyi aldı ve çalışmaya başladı.
4.  **Sonuç:** Orta görev çalıştığı için Düşük görev işini bitirip Mutex'i bırakamıyor. Yüksek görev ise Düşük görevi beklediği için çalışamıyor. Yani **Orta Öncelikli Görev, Yüksek Öncelikli Görevi bloklamış oldu!**
5.  **Çözüm:** **Priority Inheritance.** RTOS, Mutex'i tutan Düşük görevin önceliğini geçici olarak Yüksek seviyeye çıkarır ki işini hemen bitirip yolu açsın.

---

> **Ustanın Notu:** "RTOS kullanmak, çok şeritli otobanda araba sürmek gibidir. Trafik kurallarına (Mutex, Semaphore) uymazsanız kaza (Crash) kaçınılmazdır. En büyük düşman 'Stack Overflow'dur. Her göreve yetecek kadar hafıza ayırdığından emin ol."
