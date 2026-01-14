# ⚠️ Fiziğin Kanunları ve İş Güvenliği (Physics of Safety)

> *"Fizik kurallarına itiraz edemezsiniz, rüşvet veremezsiniz ve onları kandıramazsınız. İhmal ederseniz, bedelini canınızla ödersiniz."*

Atölyede ve fabrikada en büyük amir "Ustabaşı" değil, Isaac Newton'dur. Onun yasalarına uymayan herkes kazaya davetiye çıkarır.

## 1. Eylemsizlik (Inertia): "Duran Durmak, Giden Gitmek İster"

Robot kolu 200kg yükü taşıyor ve saniyede 2 metre hızla gidiyor. Acil stop'a bastınız.
*   **Yanlış İnanış:** Robot anında durur.
*   **Fiziksel Gerçek:** Robotun motoru durur, freni kilitlenir. Ama 200kg'lık yük "gitmek istemeye" devam eder.
*   **Sonuç:** Robotun mili burulur, dişlileri sıyırır veya robot yerinden sökülür.
*   **Ders:** Yüksek ataletli (High Inertia) yükleri durdurmak, hareket ettirmekten zordur. Yavaşlama rampalarını (Deceleration Ramp) asla "0" yapma.

## 2. Moment ve Kaldıraç: "Beni Yerimden Oynatın"

Arşimet "Bana bir dayanak noktası verin, dünyayı yerinden oynatayım" demiştir. Robotik'te bu kural şöyle işler:
"Bana yeterince uzun bir robot kolu ver, en güçlü motoru bile yakayım."
*   **Kural:** Tork = Kuvvet x Yol.
*   Yükü motorun dibinde (10cm) tutmak ile ucunda (2m) tutmak arasında 20 kat fark vardır.
*   **Saha Hatası:** Robotun ucuna ağır bir kaynak pensesi takıp kolu tam açmak.
*   **Sonuç:** Motor aşırı akımdan yanar veya redüktör dağılır.

## 3. Potansiyel Enerji: "Gizli Tehlike"

Bir pres makinesi havada duruyorsa, o bir bombadır. Hidrolik hortum patlarsa, o pres yerçekimi ivmesiyle (9.81 m/s²) düşer.
*   **Kural:** Havada asılı yükün altına asla girilmez.
*   **Çözüm:** Mekanik pim (Pinning). Hidroliğe veya yazılıma güvenme, araya çelik bir takoz koy.

---
> **Ustanın Notu:** "Yerçekimi asla uyumaz, asla mola vermez ve asla hata yapmaz. Siz de yapmayın."
