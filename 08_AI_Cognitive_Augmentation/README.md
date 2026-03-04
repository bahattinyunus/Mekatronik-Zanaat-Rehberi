# 🧠 AI Bilişsel Kaldıraç: Yapay Zeka ile Hibrit Mühendislik (08)

> *"Yapay zeka zekamızı elimizden alan bir rakip değil; biyolojik sınırlarımızı yıkan bir bilişsel protezdir. Usta, AI'ya ne yaptıracağını bilen değil, AI'nın yaptığı hatayı santimetrelerce öteden hissedebilendir."*

Bu modül, bir mekatronik teknikerinin/mühendisinin yapay zekayı (LLM'ler, Vision modelleri, Analitik AI) operasyonel bir kaldıraç olarak nasıl kullanacağını anlatır.

---

## 🛠️ 1. Gömülü Sistemler İçin Prompt Engineering

Artık kodun sözdizimini (syntax) ezberlemek yerine, sistemin mimarisini AI'ya doğru tarif etmek daha değerlidir.

- **Teknik Bağlam (Context) Verme:** "Bana bir STM32 kodu yaz" yerine...
- **Master Prompt:** "STM32G4 serisi için, HAL kütüphanesi kullanarak, DMA üzerinden 4 kanallı ADC okuması yapan ve bu verileri I2C ekran üzerinde 10Hz hızında güncelleyen, non-blocking ve bellek korumalı bir C++ iskeleti oluştur. Kesme (Interrupt) yönetimi için öncelikleri belirle."

## 🔍 2. AI ile Akıllı Hata Ayıklama (Debug Partner)

Binlerce satırlık ham telemetri verisini veya karmaşık PLC loglarını manuel analiz etmek yerine AI'yı "Filtre" olarak kullanın.

- **Kullanım:** Log verilerini AI'ya besleyin ve şu soruyu sorun: *"Bu zaman damgaları arasındaki voltaj dalgalanması ile motor torku arasındaki korelasyonu bul ve olası mekanik rezonans noktalarını işaretle."*

## 🎨 3. Üretken AI ile Mekanizma Tasarımı

- **Generative Design:** Belirli stres ve ağırlık limitlerini AI'ya vererek, geleneksel yöntemlerle hayal edilemeyecek, organik ve ultra-hafif mekanik parçaların (Topoloji Optimizasyonu) tasarlanması.
- **Circuit Analysis:** Şema (Schematic) üzerindeki olası darboğazları AI ile "Review" etmek.

---

## 🚀 Sahada AI: Pratik İpuçları

> [!TIP]
> **AI Asistanı ile Saha Diyaloğu:**
> Bir makinenin sesini telefonunuzla kaydedip, AI'ya bu sesin spektrum analizini (FFT) yaptırarak arızalı rulmanı saniyeler içinde tespit edebilirsiniz. Kod yazan AI değil, teşhis koyan AI sizi "Usta" yapar.

---

### 📚 Modül İçeriği
1. **[`08_Prompt_Engineering_for_Hardware.md`](./08_Prompt_Engineering_for_Hardware.md)**: Donanım odaklı komut sanatı.
2. **[`08_LLM_PLC_Integration.md`](./08_LLM_PLC_Integration.md)**: Eski PLC kodlarını modernize etme.
3. **[`08_AI_Vision_Industrial.md`](./08_AI_Vision_Industrial.md)**: Kamerayla otonom kalite kontrol.
