# Phase 129 Behavior Quality Findings and Manual Review Queue

> [!NOTE]
> UYARI: Bu çıktı Phase 129 Market Behavior Diagnostics and Regime Quality raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, behavior quality veya candidate state quality değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, unsupervised execution, dimensionality reduction execution, prediction/target/label üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Özet Bilgiler
- **Toplam Bulgu Sayısı**: `2`
- **Engelleyici Bulgu Sayısı**: `0`
- **Yıkıcı İşlem İzni**: `False`

## Bulgular Tablosu
| finding_id | finding_type | behavior_family | severity | message | recommendation | manual_review_required | destructive_action_allowed | auto_fix_allowed | auto_drop_allowed | non_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| finding_p129_001 | candidate_state_ambiguity_warning | transition | behavior_low | Candidate state breakout transition exhibits expected boundary overlap with continuation. | Inspect candidate state ambiguity without modifying source schemas. | False | False | False | False | True |
| finding_p129_002 | news_metadata_boundary_risk | news_metadata | behavior_info | News metadata boundary strictly enforced: zero full-text and zero scraping validated. | Maintain metadata-only news boundary across all diagnostics pipelines. | False | False | False | False | True |

