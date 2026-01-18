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

---
