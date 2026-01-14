# 👁️ Osiloskop Rehberi: Görünmezi Görmek

> *"Multimetre sana yalan söyler, osiloskop gerçeği haykırır."*

Elektronik tamirinde en büyük sorun, elektriğin görünmez olmasıdır. Osiloskop, elektriği zamana karşı çizen bir makinedir. O olmadan "körsünüz".

## 1. Neden Multimetre Yetmez?

*   **PWM Sinyali:** Multimetreye 5V PWM (%50 Duty) ölçtürürseniz size "2.5V DC" der. Bu koca bir yalandır. Orada 2.5V yoktur; 5V ve 0V arasında gidip gelen bir kare dalga vardır.
*   **Gürültü (Noise):** 3.3V'luk hattınız temiz mi? Multimetre "3.3V" der. Osiloskopta bakarsınız, aslında 2.8V ile 3.8V arasında çılgınca salınan testere dişi bir sinyal vardır. İşlemci neden reset atıyor? İşte bu yüzden.

## 2. Temel Ayarlar: Tetiği Çekmek (Triggering)

Ekranda kayan çizgiler görüyorsanız, "Trigger" ayarınız yanlıştır.
*   **Trigger Level:** Sinyalin hangi voltajı geçtiğinde fotoğrafını çekeceğini belirler.
*   **Mode (Auto/Normal/Single):**
    *   **Auto:** Sinyal olmasa da ekranda bir şey gösterir. Genel bakış için.
    *   **Normal:** Sadece tetiği yakalarsa gösterir.
    *   **Single (Tek Atış):** En önemlisi budur. Nadir olan bir olayı (mesela sistem açılırken oluşan voltaj dikenini) yakalamak için tuzak kurmaktır. Tetiği kur, git kahve iç. Sinyal geldiğinde osiloskop onu yakalar ve dondurur.

## 3. Saha Dedektifliği: Sinyal Okuma

### İletişim Hatları (UART/I2C)
*   Sinyal kareye mi benziyor yoksa köpekbalığı yüzgecine mi?
*   **Yüzgeç Gibiyse:** Hattın kapasitansı yüksektir. Kablo çok uzundur veya pull-up direnci çok büyüktür. Veri kayıpları buradan olur.

### Motor Sürücü Çıkışları
*   Voltaj aniden eksiye mi düşüyor? (Inductive Kickback).
*   Koruma diyotlarınız (Flyback Diodes) çalışmıyor demektir. Sürücünüz yakında yanacak.

---
> **Ustanın Notu:** "Osiloskop probunun şasesini (timsah ağzı) asla rastgele bir yere bağlama. Eğer şebeke elektriği (220V) ile çalışıyorsan ve probu faz'a değdirirsen, osiloskobu patlatırsın. Her zaman önce toprak (GND) referansını kontrol et."
