# 🔍 İleri Düzey Arıza Teşhisi ve Kök Neden Analizi (Advanced Diagnostics)

> *"Arıza çözmek, sadece bozulan parçayı değiştirmek değil; o parçanın neden bozulduğuna dair sinsi hikayeyi okumaktır. Gerçek bir Metal Yaka, semptomu değil, hastalığı tedavi eder."*

Endüstriyel dünyada karmaşıklık arttıkça, deneme-yanılma (trial and error) yöntemi hem pahalı hem de tehlikeli hale gelir. Bu modülde, sistematik arıza teşhisi metodolojilerini inceleyeceğiz.

---

## 🛠️ 1. "5 Neden" (5 Whys) Tekniği: Derine İnmek

Bir robot dursa, "Sürücü hata verdi" demek yüzeyseldir. 5 Neden tekniği sizi asıl tasarım hatasına götürür.

**Senaryo:** Servo Sürücü 'Aşırı Akım' (Overcurrent) hatası veriyor ve hat durdu.
1. **Neden sürücü hata verdi?** Çünkü servo motor mili dönemiyor.
2. **Neden mil dönemiyor?** Çünkü mekanik kaplin sıkışmış.
3. **Neden kaplin sıkışmış?** Çünkü rulman yatağı aşırı ısınmış ve kilitlenmiş.
4. **Neden rulman kilitlendi?** Çünkü yağlama kanalı metal çapaklarıyla tıkanmış.
5. **Neden kanal tıkandı?** Çünkü bakım periyodu sırasında kullanılan filtre standart dışıydı. (KÖK NEDEN!)

**Metal Yaka Dersi:** Sürücüyü resetlemek 10 saniye sürer, kaplini değiştirmek 1 saat, ama filtre standardını düzeltmek bir fabrikanın geleceğini kurtarır.

---

## ⚡ 2. 8D Metodolojisi (Arıza Çözme Disiplini)

Endüstri devlerinin (Ford, Bosch vb.) kullandığı bu disiplin, hatanın bir daha asla tekrarlanmamasını garanti altına alır.

- **D1 (Ekip):** İlgili tekniker, mühendis ve operatörü bir araya getir.
- **D2 (Problem Tanımı):** "Lazer kesim makinesi bazen sapıtıyor" değil; "Y ekseni 500mm/sn üzerindeki hızlarda 2mm kayma yapıyor."
- **D3 (Geçici Önlem):** Hat durmasın diye hızı 300mm/sn'ye sabitle. (Kanamayı durdur!)
- **D4 (Kök Neden):** Motor enkoder kablosundaki ekranlama (shielding) yırtılmış, parazit alıyor.
- **D5 (Düzeltici Faaliyet):** Kabloyu yüksek kaliteli endüstriyel kabloyla değiştir ve 360 derece topraklama yap.
- **D6 (Doğrulama):** Sistemi test et, 500mm/sn hızda hata var mı?
- **D7 (Önleyici Tedbir):** Tüm makinelerin kablo kanallarını sürtünmeye karşı kontrol et, bakım planına ekle.
- **D8 (Takdir):** Başarıyı kaydet ve ekibi tebrik et.

---

## 🧠 3. Balık Kılçığı (Ishikawa) Diyagramı

Karmaşık arızalarda suçluyu bulmak için 6 temel kategoriyi (6M) sorgulayın:
1. **Method (Yöntem):** Yazılım algoritması yanlış mı?
2. **Machine (Makine):** Mekanik aşınma mı var?
3. **Man (İnsan):** Operatör mü yanlış kullandı?
4. **Material (Malzeme):** Metal yorgunluğu veya kalitesiz parça mı?
5. **Measurement (Ölçüm):** Sensör mü yanlış okuyor?
6. **Mother Nature (Çevre):** Aşırı nem veya ısı mı etkiliyor?

---

> [!IMPORTANT]
> **Kök Neden Analizi (RCA) Formülü:**
> Semptom (Ağrı) $\neq$ Problem (Hastalık).
> Penseyi eline almadan önce multimetreyi, multimetreyi almadan önce zihnini kullan.

---

| Dosya | Durum | Açıklama |
| :--- | :--- | :--- |
| [`01_Calculus_Diagnostics.md`](./01_Calculus_Diagnostics.md) | Güncel | Matematiksel yaklaşım. |
| [`01_Advanced_Diagnostics.md`](./01_Advanced_Diagnostics.md) | **YENİ** | Metodolojik yaklaşım. |
| [`01_Physics_Safety.md`](./01_Physics_Safety.md) | Güncel | Fiziksel güvenlik. |
