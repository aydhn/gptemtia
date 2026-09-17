# FINAL SAFETY BOUNDARY — GÜVENLİK SINIRLARI VE NO-GO DÖKÜMÜ

> **YASAL UYARI:**
> Bu belge, sistemin güvenlik taahhütlerini, kısıtlamalarını ve yasaklı eylem listesini resmileştirir.
> **BU SİSTEM YATIRIM TAVSİYESİ VERMEZ. GERÇEK ALIM SATIM YAPMAZ.**

---

## 1. Temel Güvenlik Felsefesi

Sistemin temel felsefesi "Fail-Safe, Zero-Live, Pure-Research" prensibine dayanır. Sistem, herhangi bir şüpheli durumda veya sözleşme ihlalinde otomatik olarak güvenli moda geçer ve çalışmayı durdurur.

---

## 2. No-Go Kuralları (Kesinlikle Yasaklı Eylemler)

Sistem mimarisinde aşağıda listelenen eylemler **kesinlikle yasaktır** ve sistemik kontrollerle engellenmiştir:

1. **NO-GO-01: Canlı Borsa/Broker Bağlantısı (Live Broker Connection):**
   - Herhangi bir gerçek broker veya borsa API uç noktasına (Fix, REST, WebSocket) canlı bağlantı kurulamaz.
2. **NO-GO-02: Canlı Emir Üretimi ve İletimi (Order Generation & Execution):**
   - Gerçek piyasaya emir gönderilmesini sağlayacak hiçbir fonksiyon veya sınıf aktif değildir (`final_delivery_order_generation_disabled.py`).
3. **NO-GO-03: Canlı Al-Sat Sinyali Dağıtımı (Signal Generation):**
   - Operatöre veya üçüncü şahıslara al/sat tavsiyesi oluşturacak canlı sinyal motorları teslimat safhasında kilitlenmiştir.
4. **NO-GO-04: Teslimatta Model Eğitimi & Tahmin (Training & Inference):**
   - Teslimat ve denetim anında kontrolsüz kaynak tüketimini ve sızıntıları önlemek amacıyla model eğitimi ve tahmin fonksiyonları engellenmiştir.
5. **NO-GO-05: Yetkisiz Dış Ağ Kazıma (Web Scraping):**
   - Onaysız veya robots.txt ihlali oluşturabilecek canlı web kazıma yasaktır.
6. **NO-GO-06: Kimlik Bilgisi Sızıntısı (Credential Leakage):**
   - API anahtarları, parolalar, özel anahtarlar loglara veya raporlara yazılamaz; maskeleme zorunludur.
7. **NO-GO-07: Kaynak Kod Ezilmesi (Source Code Overwrite):**
   - Çalışma anında sistemin kendi kod tabanını (`*.py`) değiştirmesi, dinamik kod derlemesi yasaktır.

---

## 3. Go Koşulları (İzin Verilen Güvenli Eylemler)

Sistem yalnızca aşağıdaki güvenli koşullar altında çalıştırılabilir:

1. **GO-01: Yerel Çevrimdışı Çalışma (Offline Local Execution):**
   - Dış ağa bağlanmadan, tamamen izole yerel dosya sistemi üzerinde çalışma.
2. **GO-02: Dry-Run Modu:**
   - Kalıcı yan etki oluşturmayan simülasyon ve raporlama süreçleri.
3. **GO-03: Sentetik ve Geçmiş Veri Analizi:**
   - Yerel DataLake içindeki arşivlenmiş geçmiş veriler veya sentetik veriler üzerinde araştırma yapılması.
4. **GO-04: Denetim ve Doğrulama Betikleri:**
   - Sözleşme, envanter, sağlık kontrolü ve kanıt raporlama betiklerinin koşturulması.

---

## 4. Yasaklı Kolon Politikaları ve Veri Sızıntısı Önleme

FeatureStore ve DataLake veri setlerinde geleceğe dair sızıntı (look-ahead bias) yaratabilecek sütunlar katı kurallarla filtrelenir:

- **Yasaklı Kolon Tipleri:** Gelecekteki fiyat (`future_close`, `next_day_return`), yayınlanmamış makroekonomik veriler, hesaplanmamış hedef etiketleri (`target_lead_*`).
- **Uygulanan Denetim:** `final_delivery_forbidden_column_policies.py` modülü veri setlerini tarayarak yetkisiz kolon tespit ettiğinde işlemi derhal durdurur.

---

## 5. Yatırım Tavsiyesi Olmama Taahhüdü

Bu yazılımın ürettiği tüm raporlar, metrikler, skorlar ve göstergeler:
- Yalnızca **akademik metodoloji testi ve simülasyon çıktısı** niteliğindedir.
- 6362 sayılı Sermaye Piyasası Kanunu ve ilgili mevzuat uyarınca yatırım danışmanlığı faaliyeti **değildir**.
- Gerçek finansal kararlar için bir dayanak teşkil edemez.
