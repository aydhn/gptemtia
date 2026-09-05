# Phase 129 Market Behavior Diagnostics Profile Registry

> [!NOTE]
> UYARI: Bu çıktı Phase 129 Market Behavior Diagnostics and Regime Quality raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, behavior quality veya candidate state quality değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, unsupervised execution, dimensionality reduction execution, prediction/target/label üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Özet Bilgiler
- **Aktif Profil**: `balanced_local_market_behavior_diagnostics`
- **Toplam Profil Sayısı**: `3`
- **Mevcut Faz**: `129`
- **Hedef Final Faz**: `160`
- **Sıradaki Faz**: `130`
- **Non-Signal Güvencesi**: `True`

## Profil Detayları
| profile_name | description | current_phase | target_final_phase | next_phase | min_quality_score | dry_run_default | local_only | non_production | research_only | allow_live_trading | allow_broker_integration | allow_quality_as_signal | allow_behavior_as_signal | allow_candidate_state_as_signal | allow_model_training | allow_clustering_execution | allow_unsupervised_execution | allow_target_label_generation | allow_prediction_generation | allow_source_overwrite | allow_auto_destructive_cleaning | non_signal | source_preserved | official_approval | production_ready | broker_ready |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| balanced_local_market_behavior_diagnostics | Standard balanced local offline market behavior diagnostics and candidate state quality profile. | 129 | 160 | 130 | 0.45 | True | True | True | True | False | False | False | False | False | False | False | False | False | False | False | False | True | True | False | False | False |
| strict_non_signal_behavior_quality_safety | Strict safety profile enforcing zero-tolerance non-signal behavior boundaries and heightened quality thresholds. | 129 | 160 | 130 | 0.6 | True | True | True | True | False | False | False | False | False | False | False | False | False | False | False | False | True | True | False | False | False |
| dry_run_behavior_diagnostics_focus | Dry-run focused profile prioritizing offline diagnostics execution, reporting rehearsal, and non-executable quality checks. | 129 | 160 | 130 | 0.45 | True | True | True | True | False | False | False | False | False | False | False | False | False | False | False | False | True | True | False | False | False |

