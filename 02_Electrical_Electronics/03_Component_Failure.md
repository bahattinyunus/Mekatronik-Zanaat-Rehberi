# 🩺 Komponent Arıza Kataloğu: Otopsi Raporları

> *"Her yanık komponent, bize bir şeyler anlatmaya çalışan bir şehittir. Onu çöpe atmadan önce neden öldüğünü dinleyin."*

Elektronik tamirinde en önemli yetenek, "Yanık İzlerini Okuma" sanatıdır. Bir parça durduk yere yanmaz. Onu yakan bir suçlu (katil) vardır. Eğer katili bulmadan sadece yanan parçayı değiştirirseniz, yeni taktığınız parça da saniyeler içinde ölecektir.

---

## 1. Direnç (Resistor): Sessiz Kurban
*   **Görüntü:** Kararmış, ortası çatlamış veya tamamen kömürleşmiş.
*   **Arıza Nedeni:** Dirençler kendi kendilerine bozulmazlar. Direnç yandıysa, üzerinden **Aşırı Akım** geçmiştir.
*   **Dedektiflik:** Direncin bağlı olduğu hattı takip et. Hattın devamında bir **Transistör, Kondansatör veya Entegre KISA DEVRE** olmuştur. O kısa devre akımı, gariban direncin üzerinden geçerek onu yakmıştır.
*   **Kural:** Yanık direnci değiştirirken, arkasındaki kısa devreyi bulmadan enerji verme!

## 2. Kondansatör (Capacitor): Saatli Bomba
*   **Elektrolitik (Silindir):**
    *   **Görüntü:** Tepesi şişmiş, patlamış, elektrolit sıvısı (asitli) dışarı akmış.
    *   **Neden:** Aşırı voltaj, Ters bağlantı (Polarite hatası) veya Zaman (Kuruma).
    *   **Olay:** Patlayan kondansatör kısa devre olabilir de olmayabilir de. Ancak devrenin voltajı dalgalanmaya başlar (Ripple artar).
*   **Seramik (Mercimek/SMD):**
    *   **Görüntü:** Çatlak veya hiçbir iz yok (Sinsi).
    *   **Neden:** Mekanik stres (kartın bükülmesi) veya voltaj piki.
    *   **Tehlike:** Seramik kondansatörler arızalanınca genellikle **KISA DEVRE (0 Ohm)** olurlar. Besleme hattındaki (VCC-GND arası) bir seramik kondansatör kısa devre olursa, tüm kartın ışıkları söner, güç kaynağı korumaya geçer. Arızalı olan o minik parçayı bulmak zordur (Isınmasını beklemek gerekir).

## 3. MOSFET ve Transistör: İntihar Komandosu
*   **Görüntü:** Gövdede delik, çatlak veya bacakların kopması.
*   **Neden:**
    *   **Aşırı Akım:** Yük (Motor/Lamba) kısa devre olmuştur.
    *   **Aşırı Voltaj (Spike):** Motor dururken oluşan ters EMK (Kickback) diyot tarafından sönümlenmediği için transistörü delmiştir.
    *   **Aşırı Isı:** Soğutucu yetersizdir veya montaj vidası gevşektir.
    *   **Gate Arızası:** Gate sürücüsü bozulmuş, MOSFET "Yarı açık" (Lineer bölge) kalmış ve ısınarak yanmıştır.
*   **Test:** Multimetrenin kısa devre modunda Drain ve Source bacaklarını ölç. "Biiip" ötüyorsa geçmiş olsun.

## 4. Diyot ve LED
*   **Diyot:** Genellikle kısa devre olarak bozulur. Yani akımı artık iki yöne de geçirir. Doğrultma köprüsündeki bir diyot kısa devre olursa, evin sigortasını attırır.
*   **LED:** İçindeki siyah nokta büyür. Genellikle "Açık Devre" (kopuk) olarak bozulur. Aşırı akım LED'i yakar.

## 5. Voltaj Regülatörü (LDO / Buck Converter)
*   **Görüntü:** Üzerinde delik veya yanık.
*   **Neden:** Çıkışında kısa devre olması veya Giriş voltajının çok yükselmesi.
*   **Büyük Tehlike:** Bir regülatör (örneğin 24V -> 5V çeviren) bozulduğunda bazen giriş voltajını direkt çıkışa verir. Yani 5V ile çalışan işlemcinize bir anda 24V gider.
*   **Sonuç:** İşlemci, RAM, Sensörler... Hattın devamındaki HER ŞEY yanar. Buna "Zincirleme Reaksiyon" denir.

---

> **Ustanın Özeti:** "Arıza ararken yanmış parçayı sök. Ama yenisini takmadan önce sor: **'Seni kim bu hale getirdi?'** Eğer katili bulamazsan, yeni parçanı da kurban edersin."
