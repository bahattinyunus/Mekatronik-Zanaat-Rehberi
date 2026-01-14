# 📉 Başarısızlık Günlüğü (Failure Log) Şablonu

> *"Başarısızlık bir sonuç değil, veridir. Kaydedilmeyen bir hata, boşa gitmiş bir acıdır."*

Mükemmel çalışan bir robot size çok az şey öğretir. Patlayan, yanan, çarpan bir robot ise size mühendisliği öğretir. Her projede bu günlüğü tutun.

## 1. Olay Raporu

*   **Tarih/Saat:** 14.01.2025 - 03:45 (Gece vardiyası)
*   **Proje/Modül:** Çizgi İzleyen Robot - Motor Sürücü Kartı
*   **Olay Tanımı:** Robot viraja hızlı girdiğinde aniden durdu, sürücü entegresinden duman çıktı.
*   **Hata Kodu (Varsa):** Yok. (Sistem tamamen kapandı)

## 2. Kök Neden Analizi (5 Neden Tekniği)

1.  **Neden durdu?** Sürücü (L298N) yandı.
2.  **Neden yandı?** Aşırı akım çekti.
3.  **Neden aşırı akım çekti?** Motorlar kilitlendi (Stall Current).
4.  **Neden kilitlendi?** Robot virajda savrulmamak için ters tork uyguladı ama tekerlekler kaymadı, motor zorlandı.
5.  **KÖK NEDEN:** Sürücü kartında akım sınırlama (Current Limiting) özelliği yoktu ve sigorta koymamıştık.

## 3. Çözüm ve Dersler

*   **Geçici Çözüm:** Sürücü değiştirildi.
*   **Kalıcı Çözüm:** L298N yerine akım korumalı TB6612FNG sürücüsüne geçilecek. Yazılıma "Motor 1 saniyeden fazla zorlanırsa durdur" koruması eklenecek.
*   **Maliyet:** 1 adet sürücü kartı (150 TL) + 2 saat işçilik.
*   **Kazanım:** Bir daha asla akım korumasız sürücü kullanmamayı öğrendim.

---
> **Ustanın Notu:** "Bu günlüğü iş görüşmesinde önüne koyarsan, işe alınırsın. Çünkü herkes başarılarını anlatır; hatalarını ve onlardan ne öğrendiğini anlatan kişi ise tecrübelidir."
