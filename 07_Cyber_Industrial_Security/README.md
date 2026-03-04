# 🛡️ Siber-Endüstriyel Güvenlik ve OT Savunması (07)

> *"Geleceği fabrikasında bir hacker, bir robota en büyük zararı kodla değil, o robotun güvenlik limitlerini (Safe Limits) yazılımla devre dışı bırakarak verebilir. Bizler sadece sistemi çalıştıran değil, onu siber saldırılara karşı fiziksel olarak savunan koruyucularız."*

Modern fabrikalar artık izole birer ada değil; internete, bulut sistemlerine ve yapay zeka ağlarına bağlı devasa birer siber-fiziksel organizmadır. Bu bağlantı, verimlilik getirdiği kadar büyük riskler de getirir.

---

## 🔒 1. IT vs OT Güvenliği: Farkı Anlamak

Geleneksel bilişim (IT) güvenliğinde öncelik **"Gizlilik"** (Confidentiality) iken; endüstriyel otomasyon (OT) dünyasında öncelik **"Süreklilik/Kullanılabilirlik"** (Availability) ve **"Güvenlik"** (Safety) dir.

- **IT Yaklaşımı:** "Sistemde açık var, hemen kapat ve patch yap (resetle)."
- **OT Yaklaşımı:** "Sistemi resetleyemezsin! Hat durursa saniyede 10.000$ kaybederiz. Açığı yamalamadan önce sistemi fiziksel olarak izole et."

---

## 🛠️ 2. Hava Boşluğu (Air-Gapping) ve Savunma Derinliği

Sanal dünyada "Hile" yapmanın en etkili yolu, fiziksel bağlantıyı kesmektir.

- **Air-Gap:** PLC ağını (Profinet/EtherCAT) fabrikanın ofis internetinden fiziksel olarak ayırın.
- **Kritik Kural:** Mühendislik laptopunu hem fabrikanın PLC hattına hem de ofis Wi-Fi hattına **aynı anda asla bağlamayın.** Arada "Bridge" (Köprü) olmayın.
- **LOTO 2.0 (Digital Lock-Out):** Bir makine bakımdayken sadece elektriğini kesmek yetmez; USB portlarını kapatın ve ağ erişimini (Admin password ile) dondurun.

---

## ☣️ 3. Stuxnet Dersleri: USB ve Sosyal Mühendislik

Endüstriyel tarihin en meşhur saldırısı olan Stuxnet, internet üzerinden değil, yere bırakılan bir **USB bellek** ile bulaşmıştır.

- **USB Hijacking:** Sahada bulduğunuz, markasını bilmediğiniz USB'yi asla programlama laptopunuza sokmayın.
- **Default Şifreler:** Siemens, ABB, Fanuc sistemlerinin "1234", "admin" gibi varsayılan şifrelerini kurulum anında değiştirin. Dünya üzerindeki saldırıların %60'ı varsayılan şifreleri deneyerek içeri girer.

---

## 🦾 4. Fiziksel Güvenlik Sınırları (Safety Limits)

Siber bir saldırgan PLC kodunu değiştirse dahi, makinenin fiziksel olarak zarar görmesini engelleyen **Donanımsal Limit Switch**'ler ve **Mekanik Emniyet Valfleri** sarsılmaz son kaledir.

- **Yazılımsal Limit:** Yazılımla "Maksimum 3000 RPM" set edilebilir. (Hacklenebilir).
- **Donanımsal Limit:** Motor 3100 RPM'e çıktığında enerjiyi fiziksel olarak kesen bir santrifüj anahtarı veya aşırı hız rölesi. (Hacklenemez).

---

> [!WARNING]
> **Siber Sabotaj Sinyalleri:**
> Eğer bir süreçte nedenini açıklayamadığınız mikro gecikmeler (jitter), sensör verilerinde periyodik ve mantık dışı sapmalar veya ağ trafiğinde (Wireshark ile izlenen) anormal bir yoğunluk varsa; sisteminiz bir "Penetrasyon" veya "DOS" saldırısı altında olabilir.

---

### 📚 Modül İçeriği
1. **[`07_ICS_Security_Framework.md`](./07_ICS_Security_Framework.md)**: NIST ve IEC 62443 standartları.
2. **[`07_PLC_Hardening.md`](./07_PLC_Hardening.md)**: PLC'leri siber saldırılara karşı zırhlama teknikleri.
3. **[`07_OT_Network_Monitoring.md`](./07_OT_Network_Monitoring.md)**: Ağ trafiğini izleyerek anomali tespiti.
