# 📉 Metal Yaka Arıza Kayıt Defteri (Failure Log)

> *"Bir hatayı bir kez yaparsan tecrübedir. İkinci kez yaparsan aptallıktır. Yazıya dökülmeyen tecrübe uçar gider, kaydedilen tecrübe bilgiye dönüşür."*

Her proje için bu şablonu kopyalayın ve her büyük çöküşte/patlamada doldurun.

---

## 📋 Vaka Kaydı #[001]

**Tarih:** DD/MM/YYYY
**Proje:** [Proje Adı, örn: Çizgi İzleyen Robot]
**Parça/Modül:** [Örn: L298N Motor Sürücü]

### 1. Olay (Ne Oldu?)
*Açıklama:* [Kısa ve net. "Motor sürücüden duman çıktı ve durdu."]

### 2. Belirtiler (Patlamadan Önce Ne Gördün?)
*   [ ] Isınma var mıydı?
*   [ ] Garip sesler geliyordu mu?
*   [ ] LED'ler yanıp sönüyor muydu?
*   *Not:* [Örn: Sürücü aşırı sıcaktı, el değmiyordu.]

### 3. Kök Neden Analizi (Root Cause - 5 Neden)
1.  **Neden yandı?** -> Aşırı akım çekti.
2.  **Neden aşırı akım çekti?** -> Motor zorlandı.
3.  **Neden motor zorlandı?** -> Tekerlekler sıkışmıştı.
4.  **Neden sıkıştı?** -> Dişli kutusuna kablo girmiş.
5.  **Kök Neden:** Kablolama hatası ve kablo bağının (zip tie) atılmaması.

### 4. Kanıtlar (Olay Yeri İnceleme)
*   **Fotoğraflar:** (Yanmış parçanın, dağılmış mekaniğin fotosunu buraya ekle)
*   **Kod/Devre Kesiti:** (Hataya sebep olan o kod bloğu veya yanlış çizilmiş devre şeması)
    ```c
    // Hatalı Kod Örneği
    while(1) {
        motor_run(SPEED_MAX); // Sonsuz köngüde motoru zorladık
    }
    ```

### 5. Çözüm (Fix)
*   **Geçici Çözüm:** Sürücü değiştirildi, kablo kenara çekildi.
*   **Kalıcı Çözüm:** Tüm kablolar spirale alındı ve şaseye sabitlendi. Dişli kutusu kapalı hale getirildi.

### 5. Öğrenilen Ders (Lesson Learned)
*   [ ] **Altın Kural:** Hareketli parçaların (dişli, kayış) yanından geçen kabloları **mutlaka** sabitle. Asla boşta bırakma.

### 6. Ishikawa (Balık Kılçığı) Analizi
Sorunun kaynağını kategorize et. Sadece "parça bozuk" deyip geçme.

*   **Man (İnsan):** Yorgunluk, eğitim eksikliği, yanlış montaj?
*   **Machine (Makine):** Bakımsızlık, kalibrasyon hatası, aşınma?
*   **Material (Malzeme):** Yan sanayi parça, hatalı hammadde?
*   **Method (Yöntem):** Prosedür yanlış mı? Hatalı spek?
*   **Environment (Ortam):** Aşırı sıcak, tozlu, nemli?

*Not: Çoğu arıza %80 İnsan veya Yöntem (Method) hatasıdır. Malzeme hatası nadirdir.*

### 7. 8D Problem Çözme (Özet)
Global şirketler (Ford, Toyota) bu formu kullanır. Bizim Metal Yaka versiyonumuz:
D1: Ekibi Kur -> D2: Sorunu Tanımla -> D3: Geçici Yama -> **D4: Kök Neden (5 Why)** -> D5: Kalıcı Çözüm Seç -> D6: Uygula -> D7: Tekrarını Önle -> D8: Ekibi Kutla (Çay Ismarla).

---
