# Phase 125 Feature Engine Block Manual Review Queue

> [!WARNING]
> **YASAL UYARI VE NON-SIGNAL GÜVENCESİ**:
> Bu çıktı Phase 125 Feature/Factor Engine Acceptance Report raporudur. > Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, acceptance score’u trade sinyali olarak kullanma, > strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, > production-ready/official approval/broker-ready iddiası, otomatik feature silme/düzeltme, > haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.


## Summary
- **Total Items**: 5
- **Pending Items**: 1
- **Resolved Safe Items**: 4
- **Destructive Actions Prevented**: True
- **Auto-Imputation Prevented**: True
- **Auto-Feature-Drop Prevented**: True

## Manual Review Ledger
| review_id | phase_number | module_name | review_reason | severity | suggested_action | status | destructive_action_allowed | auto_fix_allowed | auto_drop_allowed | non_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rev_01_news_boundary | 120 | advanced_feature_fusion | Haber metaveri sınırlarının (no-full-text) periyodik denetimi. | LOW | Haber şemalarında metin gövdesi veya scraping çıktısı olmadığını doğrula; ham dosyaları koru. | RESOLVED_SAFE | False | False | False | True |
| rev_02_lookahead_asof | 121 | advanced_feature_validation | Backward asof join ve strictly increasing zaman damgası kuralları. | MEDIUM | Zaman serisi hizalamalarında geleceğe sızıntı olmadığını doğrula; otomatik kolon silme yapma. | RESOLVED_SAFE | False | False | False | True |
| rev_03_quality_drift_blockers | 123 | advanced_feature_quality_drift | Tanısal anomaliler ve PSI/KS drift eşik aşımları incelemesi. | MEDIUM | Kalite kusurlarını raporla, otomatik doldurma (imputation) veya otomatik feature silme yapma. | RESOLVED_SAFE | False | False | False | True |
| rev_04_feature_store_immutability | 124 | advanced_feature_store_integration | Feature store kaynak koruma ve bölümleme (partition) immutability kontrolü. | LOW | Ham veri gölü çıktılarının üzerine yazılmadığını teyit et. | RESOLVED_SAFE | False | False | False | True |
| rev_05_phase_126_handoff_readiness | 125 | phase_126_handoff | Phase 126 rejim sınıflandırma girdi önkoşullarının gözden geçirilmesi. | INFO | Phase 126 rejim modellerinin sinyal/alım-satım tavsiyesi olmadığını baştan teyit et. | PENDING_HANDOFF | False | False | False | True |