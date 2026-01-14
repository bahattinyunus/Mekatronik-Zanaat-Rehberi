# ⏱️ RTOS Temelleri: Zamanın Efendisi Olmak

> *"Sıradan yazılımda 'hızlı olması' iyidir. Gerçek zamanlı sistemde 'zamanında olması' zorunluluktur. Geç kalan veri, yanlış veridir."*

Arduino'daki `loop()` döngüsü, profesyonel hayatta yetmez. Aynı anda hem motoru sürmek, hem ekranı güncellemek, hem de sensör okumak istiyorsanız RTOS (Real-Time Operating System) şarttır.

## 1. Görevler (Tasks) ve Öncelik (Priority)
Her iş bir "Görev"dir.
*   **Task_MotorControl:** Öncelik Yüksek (High). Çünkü motor durursa robot düşer.
*   **Task_WiFi:** Öncelik Düşük (Low). İnternet koparsa robot sadece offline olur, düşmez.
*   **Preemption (Ele Geçirme):** RTOS, yüksek öncelikli bir iş geldiğinde (Motor), düşük öncelikli işi (WiFi) acımasızca böler, motor işini yapar ve sonra WiFi'ye döner.

## 2. Semaphore ve Mutex: Kaynak Kavgası
İki görev aynı anda LCD ekrana yazı yazmaya çalışırsa ne olur?
*   **Task A:** "Hız: 10" yazmaya başlar. "Hız:" yazar, kesilir.
*   **Task B:** "Sıcaklık: 40" yazmaya başlar.
*   **Ekranda Çıkan:** "Hız: Sıcaklık: 40 10". Çorba oldu.
*   **Çözüm (Mutex):** "Tuvalet Anahtarı" gibidir. Anahtarı (Mutex) alan odaya (LCD) girer. İşini bitirene kadar başkası giremez.

## 3. Queue (Kuyruk): Güvenli Haberleşme
Görevler birbirine nasıl veri atar? Global değişken kullanmak tehlikelidir (Data Coruption).
*   **Queue:** Boru hattı gibidir. Sensör görevi borunun ucundan veriyi atar, Motor görevi diğer ucundan alır. FIFO (İlk giren ilk çıkar) mantığıyla çalışır. Veri kaybolmaz.

---
> **Ustanın Notu:** "RTOS kullanmak, `while(1)` içinde `if` yazmaktan zordur ama sistem büyüdükçe hayat kurtarır. En büyük tuzak 'Stack Overflow'dur. Her göreve yetecek kadar RAM ayırdığından emin ol."
