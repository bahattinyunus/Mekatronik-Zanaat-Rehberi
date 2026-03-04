# 🤖 Failsafe (Hata-Güvenli) Programlama Desenleri

> *"Kodunuz sadece 'çalışmak' için değil, 'hata yaptığında fabrikayı yakmamak' için tasarlanmalıdır. Bir gömülü sistem mimarı için en büyük başarı, kilitlenen bir sistemi kimseye zarar vermeden durdurabilmektir."*

Mekatronik sistemlerde yazılım fiziksel dünyayı kontrol eder. Bir hata durumunda yazılımın "donup kalması" veya "rastgele davranması", mekanik bir felakete yol açabilir. İşte endüstriyel standartlarda **Failsafe** desenleri:

---

## 🐕 1. Watchdog (Bekçi Köpeği) Donanımı

Sistem kilitlendiğinde (while(1) içinde takılma, stack overflow vb.) işlemciye otomatik reset atan mekanizmadır.

**Altın Kural:** Watchdog asla sadece "main loop"un sonunda beslenmez (kick).
- **Hatalı:** `main()` loop her döndüğünde watchdog besle. (Sistem mantıksal olarak kilitlenmiş ama hala loop dönüyor olabilir).
- **Doğru (Logic Watchdog):** Her kritik görev (Task), kendi kontrol bayrağını set eder. Watchdog sadece tüm bayraklar tamamlandığında beslenir.

```c
// Basit Logic Watchdog Örneği
bool task_a_alive = false;
bool task_b_alive = false;

void supervise_task() {
    if (task_a_alive && task_b_alive) {
        Hardware_Watchdog_Kick();
        task_a_alive = false; // Resetleyerek bir sonraki turda kontrol et
        task_b_alive = false;
    }
}
```

---

## ⚡ 2. Brown-Out Detection (BOD) ve Güç İzleme

Elektrik voltajı aniden düşerse (örneğin dev bir motor kalkarken), mikrodenetleyicinin logic kapıları kararsızlaşır. Bu sırada EEPROM'a yanlış veri yazılabilir veya yanlış GPIO tetiklenebilir.

- **Failsafe Stratejisi:** Borwn-out kesmesi (Interrupt) tetiklendiğinde tüm GPIO'ları yüksek empedanslı (High-Z) veya güvenli duruma çekin.
- **Kritik Veri:** Enerji giderken son kritik verileri (örneğin robotun son koordinatı) çok hızlı bir şekilde (Kapasitör boşalana kadar) kalıcı hafızaya kaydedin.

---

## ⚠️ 3. "Safe State" (Güvenli Durum) Tanımları

Her mekatronik sistemin bir **"Yazılımsal Acil Durdurma"** hali olmalıdır.

| Durum | Normal Çalışma | Failsafe (Güvenli Durum) |
| :--- | :--- | :--- |
| **Servo Motor** | Aktif Tork / Pozisyon | **Brake On (Fren Kapalı) / Torqueless** |
| **Isıtıcı Rezistans** | PWM Kontrol | **Relay Open (Açık Devre)** |
| **Basınç Valfi** | Lojik Kontrol | **Vent (Tahliye) Açık** |
| **Otonom Araç** | Gaz / Hızlanma | **Coast (Süzülme) / Active Brake** |

---

## 💾 4. Bellek Koruması ve Pointer Sağlığı

Gömülü C'de en büyük katil `NULL` pointerlar ve `Wild` pointerlardır.

- **Pointer Guard:** Bir fonksiyon pointer alıyorsa, işlem yapmadan önce mutlaka `if (ptr != NULL)` kontrolü yapın.
- **Buffer Overflow:** `scanf()` veya `gets()` gibi tehlikeli fonksiyonlardan kaçının. Her zaman `size` kontrolü olan fonksiyonları (`strncpy`, `snprintf`) kullanın.

---

> [!CAUTION]
> **Donanımsal Yedekleme (Redundancy):**
> Eğer bir sistemin "tek bir hatada" (Single Point of Failure) felakete yol açma ihtimali varsa, o sistemi sadece yazılımla koruyamazsınız. Donanımsal bir acil durdurma (E-Stop) devresi her zaman yazılımdan bağımsız olmalıdır.

---

### 📚 İleri Okuma
- [`04_Embedded_C_Traps.md`](./04_Embedded_C_Traps.md)
- [`05_ISO_26262_Functional_Safety.md`](../05_Control_Robotics/ISO_26262.md)
