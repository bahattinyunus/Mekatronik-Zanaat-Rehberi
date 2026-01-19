# 💣 C Dilinin Tuzakları: Gömülü Sistem Mayın Tarlası

> *"C dili size silahı verir, tetiği çeker ve ayağınızdan kendinizi vurmanızı izler. Hata affetmez, koruması yoktur. Sen ne yazarsan işlemci onu yapar; kendini yok etmek olsa bile."*

Modern diller (Python, Java) sizi korur. C dili sizi korumaz. Donanıma en yakın dil olduğu için sınırsız güce sahiptir ama bu güç kontrolsüz kullanılırsa felaket getirir.

---

## 1. Pointer Cehennemi ve Hard Fault

Pointer, hafızadaki bir adresi gösteren değişkendir.
*   **Senaryo:** `int *ptr = NULL;` dedin ve sonra `*ptr = 5;` diyerek o adrese veri yazmaya çalıştın.
*   **Sonuç:** Adres "0x00000000"dır. Burası genellikle korumalı bölgedir. İşlemci "Yassak!" der ve **Hard Fault** hatasına düşer. Sistem donar.
*   **Buffer Overflow:** 10 elemanlı bir diziye (`arr[10]`) 11. elemanı (`arr[11]`) yazarsan, hafızada o dizinin hemen bitişiğindeki başka bir değişkeni (belki de motor hızını) bozmuş olursun. Bu en sinsi hatadır; sistem çökmez ama saçmalar.

## 2. `volatile` Anahtar Kelimesi

Derleyici (Compiler) akıllıdır. Kodunuzu hızlandırmak için optimizasyon yapar.
*   **Kod:** `while(buton == 0) {};` (Butona basılana kadar bekle).
*   **Derleyici Mantığı:** "Bu döngünün içinde `buton` değeri hiç değişmiyor. O zaman ben her seferinde hafızadan okumayayım, bir kere okuyup kaydedeyim."
*   **Sonuç:** Sen butona bassan bile, derleyici hafızaya bakmadığı için (ilk okuduğu değeri -0- kullandığı için) sonsuza kadar bekler.
*   **Çözüm:** `volatile int buton;` derseniz, derleyiciye şu emri verirsiniz: "Bu değişkene optimizasyon yapma! Her satırda git, donanımdan (RAM'den) tekrar fiziksel olarak oku. Çünkü bu değer benim kontrolüm dışında (donanım tarafından) değişebilir."

## 3. Kesme (Interrupt) Önceliği ve Atomik İşlemler

*   **Senaryo:** Ana döngüde `sayac = sayac + 1;` yapıyorsun. Kesme fonksiyonunda da `sayac` değerini 0 yapıyorsun.
*   **Hata:** Toplama işlemi makine dilinde 3 adımdır: (1) Oku, (2) Ekle, (3) Yaz.
    *   İşlemci tam 2. adımdakyen Kesme gelir ve sayacı 0 yapar.
    *   İşlemci kesmeden döner, elindeki eski değeri (Ekleme yaptığı değeri) yazar.
    *   **Sonuç:** Kesmenin yaptığı sıfırlama işlemi kayboldu! Buna **Race Condition** denir.
*   **Çözüm:** Kritik işlemleri yaparken kesmeleri geçici olarak kapat (`__disable_irq()`) veya Atomik fonksiyonlar kullan.

---

## 4. Stack ve Heap Yönetimi

*   **Stack:** Fonksiyonların yerel değişkenleri buraya konur. Hızlıdır ama küçüktür.
*   **Heap:** `malloc()` ile alınan hafıza. Yavaştır, parçalanır (fragmentation).
*   **Metal Yaka Kuralı:** Gömülü sistemde **Dinamik Bellek (malloc/free)** KULLANMA!
    *   Neden? Çünkü 1 yıl çalışan bir cihazda, Heap hafızası delik deşik olur (İsviçre peyniri gibi) ve sonunda yeni yer ayıramaz hale gelir.
    *   Tüm değişkenlerini, dizilerini en başta (Global veya Static) tanımla. Hafızanın yettiğinden emin ol.

---

---

## 🛡️ 5. Savunma Sanatları: Canary ve Watchdog

Hata kaçınılmazdır. Önemli olan hatayı yakalamaktır.

### A. Stack Canary (Kömür Madenindeki Kanarya)
Taşmayı (Overflow) nasıl anlarsın?
*   **Teknik:** Stack hafızasının en sonuna özel bir sayı (Canary Word) yazarsın. Örn: `0xDEADBEEF`.
*   **Kontrol:** Ana döngüde ara sıra bu adrese bak. Eğer `0xDEADBEEF` yerine başka bir şey görüyorsan, stack taşmış ve orayı ezmiştir.
*   **Aksiyon:** Sistemi güvenli bir şekilde kapat (Fail-Safe Reset).

### B. Watchdog Timer (Bekçi Köpeği)
İşlemci donarsa (Sonsuz döngü, kilitlenme) kim reset atacak?
*   **Mantık:** İşlemcinin içinde bağımsız bir sayaç vardır (Örn: 100ms'den geriye sayar).
*   **Görevin:** Ana döngüde bu sayacı sürekli sıfırlamaktır (Köpeği sevmek / Kick the dog).
*   **Olay:** Eğer yazılımın donarsa, köpeği sevemezsin. Sayaç sıfıra iner ve "Hav!" diyerek işlemciye **Hard Reset** atar.
*   **Metal Yaka Kuralı:** Watchdog olmadan endüstriyel ürün olmaz.

---

> **Ustanın Özeti:** "Derleyici uyarılarını (Warnings) asla görmezden gelme. 'Warning' demek, 'Şimdilik çalışıyorum ama ilk virajda kaza yapacağım' demektir. Code Analysis araçlarını (MISRA-C) kullan."
