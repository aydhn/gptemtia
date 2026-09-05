# Phase 113 — Manual Review Normalization Queue Report

> [!IMPORTANT]
> **YASAL UYARI VE GÜVENLİK SINIRI**:
> Bu çıktı Phase 113 Data Normalization Layer raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, normalized data’yı trade sinyali olarak kullanma, official approval, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.


## İnceleme Kuyruğu Özeti
- **Kuyruktaki Kayıt Sayısı**: 2
- **Yıkıcı Eylem Engellendi**: True
- **Kaynak Korundu**: True

## Kuyruk Kayıtları
| queue_id | finding_id | rule_id | dataset_type | source_field | original_value_repr | severity_label | suggested_action | destructive_action_allowed | source_preserved | lineage_required | status_label |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| queue_nfind_fx_symbol_std_dataset_fx_quote_pair_2 | nfind_fx_symbol_std_dataset_fx_quote_pair_2 | norm_rule_fx_symbol_fx_symbol_slashed_standard | dataset_fx_quote | pair | INVALID_P | normalization_medium | manual inspect; lineage record in Phase 114; benchmark mapping in Phase 115 | False | True | True | normalization_manual_review_required |
| queue_nfind_num_cast_dataset_numeric_bid_2 | nfind_num_cast_dataset_numeric_bid_2 | norm_rule_numeric_type_numeric_type_safe_cast | dataset_numeric | bid | bad | normalization_high | manual inspect; lineage record in Phase 114; benchmark mapping in Phase 115 | False | True | True | normalization_manual_review_required |
