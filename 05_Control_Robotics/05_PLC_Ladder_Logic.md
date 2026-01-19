# 05. PLC & Ladder Mantığı: Endüstrinin Sarsılmaz Kalesi

> *"C++ kodu 'Segmentation Fault' verip çöker. Windows mavi ekran verir. Ama bir PLC (Programmable Logic Controller), tozun, yağın, gürültünün içinde 20 yıl boyunca, 7/24, milisaniye şaşmadan çalışmaya devam eder."*

---

## 🏭 Metal Yaka Perspektifi: Güvenilirlik (Reliability)

Bizler, "En yeni teknoloji" heyecanına kapılmayız. Bizim için en iyi teknoloji, gece saat 03:00'te bizi yataktan "Makine durdu!" diye kaldırmayan teknolojidir.
Bu yüzden fabrikaların beyni Raspberry Pi değil, **PLC**'dir.

PLC programlamak, kod yazmak değil, **mantık devresi çizmektir** (Ladder Logic). Elektrik şemalarının dijitalleşmiş halidir.

---

## 🪜 1. Ladder Diyagramı (Merdiven Mantığı)

Eski elektrikçilerin anlayabileceği dildedir.
*   **NO (Normally Open - | |):** Butona basılınca elektrik geçer. (Kod: `if input == 1`)
*   **NC (Normally Closed - |/|):** Butona basılmadığı sürece elektrik geçer. Basınca kesilir. (Kod: `if input == 0`)
*   **Coil (Bobin - ( )):** Çıkış / Motor / Lamba. (Kod: `output = 1`)

### Mühürleme (Latching)
Bir butona basıp çekseniz bile motorun çalışmaya devam etmesi.
*   Bu, otomasyonun "Merhaba Dünya"sıdır.
*   Start butonu enerjiyi verir, Motor kendi kontağı üzerinden enerjiyi tutmaya devam eder. Stop butonu devreyi kırana kadar.

---

## 🔄 2. Tarama Döngüsü (Scan Cycle)

PLC, sıradan bir bilgisayar gibi çalışmaz. Sonsuz bir döngüdedir:
1.  **Input Read:** Önce tüm düğmelere, sensörlere bakar, fotoğrafını çeker.
2.  **Program Execute:** Yazdığın mantığı (Ladder) yukarıdan aşağıya, soldan sağa çalıştırır.
3.  **Output Write:** Hesaplanan sonuçları (Lambayı yak, motoru durdur) fiziksel dünyaya gönderir.

**Kritik Hata:** Bir program içinde sonsuz döngü (`while(1)`) yapamazsınız! Yaparsanız PLC "Watchdog Timer" hatası verir ve kendini korumaya alıp durur. Tarama döngüsü asla aksamamalıdır.

---

## 🛑 3. Fail-Safe (Hatada Güvenli) Tasarım

Metal Yaka felsefesinin en önemli kuralı: **"Kablo koparsa ne olur?"**

*   **Start Butonu:** Genelde NO (Açık) kullanılır. Kablo koparsa start veremezsin. (Güvenli).
*   **Acil Stop / Stop Butonu:** **MUTLAKA NC (Kapalı)** kullanılmalıdır.
    *   *Senaryo:* Stop butonu kablosu fare tarafından kemirildi ve koptu.
    *   *NO olsaydı:* Acil durumda butona basardınız ama sinyal gitmezdi. Makine durmazdı. KAZA!
    *   *NC olduğu için:* Kablo koptuğu an elektrik kesilir (buton basılmış gibi) ve makine anında durur.
    *   **Kural:** Güvenlik sinyalleri, enerji varken "Ben buradayım, her şey yolunda" demelidir. Sessizlik (Kablo kopması), tehlike demektir.

---

## ⏱️ 4. Zamanlayıcılar ve Sayaçlar (Timers & Counters)

*   **TON (On Delay):** Basınca hemen çalışma, 5 saniye bekle sonra çalış. (Motorun yağlanması için bekleme süresi).
*   **TOF (Off Delay):** Düğmeyi bıraksam bile 10 saniye daha çalış fan, içerisi soğusun.

---

> **Ustanın Tavsiyesi:**
> "PLC programlarken 'Nasıl çalışır?' diye değil, '**Nasıl bozulabilir ve bozulduğunda güvenli kalır mı?**' diye düşünmelisin. İyi bir otomasyoncu, en kötü senaryoyu en başta planlayan kişidir."
