import datetime
import os

def create_failure_log():
    print("🤖 Metal Yaka - Arıza Kayıt Oluşturucu v1.0")
    print("-" * 40)

    title = input("📝 Arıza Başlığı (Örn: Servo Sürücü Haberleşme Hatası): ")
    component = input("🔧 Arızalı Komponent/Sistem: ")
    symptom = input("🚨 Belirti (Ne oldu?): ")
    root_cause = input("🔍 Kök Neden (Neden oldu?): ")
    solution = input("✅ Çözüm (Nasıl düzeltildi?): ")
    preventive = input("🛡️ Önleyici Tedbir (Tekrar etmemesi için ne yapılmalı?): ")
    technician = input("👷 Tekniker İsmi: ")

    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    log_content = f"""# 📝 Arıza Kayıt Raporu: {title}

| Bilgi | Detay |
| :--- | :--- |
| **Tarih** | {date_str} |
| **Tekniker** | {technician} |
| **Sistem** | {component} |
| **Durum** | ÇÖZÜLDÜ ✅ |

---

## 🚨 1. Belirti ve Semptomlar
{symptom}

## 🔍 2. Kök Neden Analizi
{root_cause}

## ✅ 3. Uygulanan Çözüm
{solution}

## 🛡️ 4. Önleyici Faaliyetler
{preventive}

---
> *Bu rapor 'Mekatronik-Zanaat-Rehberi' standardına uygun olarak otomatik oluşturulmuştur.*
"""

    filename = f"FAILURE_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.md"
    
    # Save to the projects/labs directory if possible
    save_path = os.path.join(os.getcwd(), filename)
    
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(log_content)

    print(f"\n✨ Arıza kaydı başarıyla oluşturuldu: {filename}")
    print("Lütfen bu dosyayı '06_Projects_Labs/logs/' dizinine taşıyın.")

if __name__ == "__main__":
    create_failure_log()
