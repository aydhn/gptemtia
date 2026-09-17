# FINAL OPERATOR HANDOVER — YEREL/OFFLINE KULLANIM VE DEVİR REHBERİ

> **YASAL UYARI VE OPERATÖR TALİMATI:**
> Bu yazılım paketi **kesinlikle canlı alım-satım ve broker bağlantısı için kullanılamaz**.
> Yalnızca yerel araştırma, offline simülasyon ve analiz için tasarlanmıştır.
> **YATIRIM TAVSİYESİ DEĞİLDİR.**

---

## 1. Operatör Giriş ve Genel İlkeler

Bu el kitabı, Phase 160 ile nihai teslimatı gerçekleştirilen sistemin yerel ortamda güvenli, kararlı ve sözleşmelere uygun şekilde çalıştırılması için operatörlere yönelik rehber niteliğindedir.

### Altın Kurallar:
1. **Asla Canlıya Alma (Never Go Live):** Sistemi hiçbir koşulda gerçek bir aracı kurum (broker) hesabına, canlı API'ye veya üretim ortamına bağlamayınız.
2. **Korumalı Çalıştırma:** Tüm analiz ve raporlama betiklerini varsayılan olarak `--dry-run` bayrağı ile çalıştırınız.
3. **Kaynak Kod Bütünlüğü:** `advanced_final_delivery/` ve diğer faz modüllerini elle düzenlemeyiniz; sözleşme bütünlüğü bozulabilir.

---

## 2. CLI Betiklerini Çalıştırma Rehberi

Tüm Phase 160 betikleri proje kök dizininden Python modül çağrısı ile koşturulmalıdır:

### 2.1. Sağlık Kontrolü (Health Check)
Sistemin genel sağlık durumunu ve dosya sistemi izinlerini denetlemek için:
```bash
python -m scripts.run_final_delivery_health_check --dry-run --no-save
```
*Çıktı:* Tüm kontrollerin `PASS` durumunda olduğunu teyit ediniz.

### 2.2. Doğrulama Raporu (Validation Report)
Sistem sözleşmeleri, güvenlik sınırları ve kanıt kayıtlarını denetlemek için:
```bash
python -m scripts.run_final_delivery_validation_report --dry-run --no-save
```

### 2.3. Sistem Durumu ve Dashboard
Tüm teslimat bileşenlerinin genel özetini görmek için:
```bash
python -m scripts.run_final_delivery_status --dry-run --no-save
```

### 2.4. 160-Faz Kapanış Raporu
Nihai plan kapanış beyanını ve hazırlık skorunu görüntülemek için:
```bash
python -m scripts.run_final_160_phase_completion_report --dry-run --no-save
```

### 2.5. Diğer Envanter ve Denetim Betikleri
- **Sözleşme Denetimi:** `python -m scripts.run_final_delivery_package_contracts --dry-run --no-save`
- **Sistem Envanteri:** `python -m scripts.run_final_delivery_inventory --dry-run --no-save`
- **Güvenlik Sınırları:** `python -m scripts.run_final_delivery_boundaries --dry-run --no-save`
- **Engelleme Raporları:** `python -m scripts.run_final_delivery_disabled_execution_reports --dry-run --no-save`
- **Bulgular & Manifest:** `python -m scripts.run_final_delivery_findings_manifest --dry-run --no-save`

---

## 3. Parametreler ve Bayraklar (Flags)

- `--dry-run`: Disk veya veri tabanı üzerinde kalıcı yan etki yaratmadan çalıştırır. (Varsayılan ve zorunlu öneri)
- `--no-save`: DataLake veya rapor dizinlerine dosya yazılmasını engeller, yalnızca konsola çıktı verir.
- `--profile <profile_name>`: Özel bir teslimat profili seçmek için kullanılır (Varsayılan: `balanced_local_final_delivery_package`).

---

## 4. Olası Hata Durumları ve Çözüm Prosedürleri

| Hata / Durum | Olası Neden | Müdahale Yöntemi |
|---|---|---|
| `ContractValidationError` | Değişmez sözleşme kurallarında uyuşmazlık. | Ortam değişkenlerini kontrol ediniz; canlı işlem bayraklarının `False` olduğunu doğrulayınız. |
| `FileNotFoundError` | Eksik dizin veya dosya. | `python -c "from config.paths import ensure_project_directories; ensure_project_directories()"` komutunu çalıştırınız. |
| `ExecutionDisabledError` | Devre dışı bırakılmış bir bileşeni (canlı işlem, broker) tetikleme girişimi. | Bu beklenen bir güvenlik korumasıdır. Canlı işlem fonksiyonlarını çağırmayınız. |
| `DataLakeWriteError` | Yazma izinleri veya disk doluluğu. | Disk alanını ve `data/datalake/` dizin izinlerini kontrol ediniz. |

---

## 5. Acil Durum Prosedürü (Emergency Shutdown)

Beklenmedik bir süreç veya arka plan görevi tespit edilirse:
1. Çalışan tüm Python süreçlerini sonlandırınız:
   - Windows: `Stop-Process -Name python -Force`
2. `.env` dosyasındaki tüm acil durum bayraklarının (`DRY_RUN_DEFAULT=true`, `ALLOW_LIVE_TRADING=false`) aktif olduğunu teyit ediniz.
3. Sağlık kontrolü betiğini (`run_final_delivery_health_check.py`) çalıştırarak sistem bütünlüğünü doğrulayınız.

---

## 6. Devir Onay Beyanı

Bu teslimat paketi, 160 fazlık planın başarıyla tamamlandığını, tüm güvenlik testlerinden geçtiğini ve yerel araştırma kullanımına hazır olduğunu belgeler.
