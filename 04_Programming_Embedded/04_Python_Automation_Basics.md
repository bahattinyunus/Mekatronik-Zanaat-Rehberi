# 04. Python Otomasyonu: Mühendisin İsviçre Çakısı

> *"C++ ile makinenin ruhunu (Firmware) yazarsın. Python ile makineyi test eden, verisini toplayan ve onu dünyaya bağlayan sistemi yazarsın. Biri derinlik, diğeri genişlik içindir."*

---

## 🐍 Metal Yaka Perspektifi: "Betik" Yazmak (Scripting)

Biz Python'u web sitesi yapmak (Django/Flask) veya oyun yazmak için öğrenmiyoruz. Biz Python'u **"Dijital Tutkal"** olarak kullanıyoruz.
*   Bir osiloskoptan veri çekip Excel'e kaydetmek için.
*   Bir motor sürücüye seri porttan binlerce rastgele komut gönderip "tıkanacak mı?" diye test etmek (Stress Test) için.
*   Sahada hızlıca bir grafik çizdirip müşteriye "Bakın voltaj burada düşüyor" demek için.

Python, bizim **dijital multimetremizdir**.

---

## 🔌 1. PySerial: Donanımla Konuşmak

Arduino, STM32, PLC veya CNC... Hepsi genellikle Seri Port (UART/USB) üzerinden konuşur. Elle Terminal programından (Putty, RealTerm) komut göndermek yavaştır.

```python
import serial
import time

# Portu aç (Windows'ta COM3, Linux'ta ttyUSB0)
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2) # Arduino reset atabilir, bekle

# Otomatik Test Senaryosu
for i in range(100):
    komut = f"MOTOR_HIZ {i}\n"
    ser.write(komut.encode('utf-8'))
    print(f"Gönderildi: {komut.strip()}")
    
    cevap = ser.readline().decode('utf-8').strip()
    print(f"Cevap: {cevap}")
    
    if "ERROR" in cevap:
        print(f"⚠️ HATA YAKALANDI! Hız: {i}")
        break
    
    time.sleep(0.1)

ser.close()
```
Bu 10 satırlık kod, bir teknikerin 5 saat elle yapacağı testi 5 dakikada yapar ve hatayı kaçırmaz.

---

## 📊 2. Veri Görselleştirme: Görmediğini Yönetemezsin

Makineden gelen ham veriler (örneğin: `23, 24, 25, 105, 26`) sayılar yığınıdır. Aradaki `105` değerini (Ani yükselme/Spike) gözle kaçırabilirsiniz. Python (`matplotlib`) ile bunu grafiğe dökmek saniyeler sürer.

*   **Senaryo:** Motor ısınıyor mu?
*   **Metal Yaka Çözümü:** Sıcaklık sensörünü oku -> CSV dosyasına kaydet -> Akşam grafiğini çizdir.
*   **Sonuç:** "Evet, her sabah 10:00'da vardiya değişimi sırasında makine dur-kalk yaparken ısınıyor." (Teşhis konuldu).

---

## GUI (Arayüz) Yapımı: Basit Test Jig'leri

Operatörün veya teknisyenin kullanması için 3 butonlu basit bir pencere yapmak.
*   `Tkinter` veya `PyQt` ile.
*   **[BAŞLAT]**, **[DURDUR]**, **[ACİL STOP]**.
*   Arka planda Python, karmaşık seri port komutlarını yönetir; kullanıcı sadece butona basar.

---

## 🤖 Otomasyonun Ötesi: Yapay Zeka Entegrasyonu

Python, AI dünyasının ana dilidir.
*   Kamera görüntüsünü al (`OpenCV`).
*   Hatalı ürünü tespit et (`YOLO`, `TensorFlow`).
*   PLC'ye "O parçayı reddet" sinyali gönder (`PyModbus`).

İşte **Metal Yaka** vizyonunun zirvesi budur: Yapay Zekayı, fiziksel dünyadaki bir pistonu itmek için kullanmak.

> **Ustanın Notu:**
> "Python yavaştır (Milisaniye gecikebilir). Asla bir hava yastığını patlatmak veya acil freni tetiklemek için Python kullanma. Güvenlik kritikleri her zaman gömülü sistemde (C/C++) veya donanımda kalmalı. Python, o sistemin **orkestra şefidir**, enstrümanı çalan değil."
