# Phase 129 Candidate State Quality Report

> [!NOTE]
> UYARI: Bu çıktı Phase 129 Market Behavior Diagnostics and Regime Quality raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, behavior quality veya candidate state quality değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, unsupervised execution, dimensionality reduction execution, prediction/target/label üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Özet Bilgiler
- **Toplam Aday Durum Sayısı**: `10`
- **Hazır Durum Sayısı**: `0`
- **Ortalama Tamlık Skoru**: `0.00`
- **Model Eğitimi Engellendi**: `True`
- **Non-Signal Durumu**: `True`

## Aday Durum Kalite Tablosu
| candidate_state_name | candidate_state_family | schema_completeness | assignment_policy_ref_available | source_matrix_ref_available | validation_dependency_passed | quality_dependency_passed | manual_review_required | quality_status | non_signal | contains_target_or_prediction | contains_trading_recommendation | model_training_executed | clustering_executed | unsupervised_execution | current_phase | target_final_phase | next_phase |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| candidate_state_volatility_expansion | volatility | 1.0 | True | True | True | True | False | behavior_quality_ready | True | False | False | False | False | False | 129 | 160 | 130 |
| candidate_state_volatility_compression | volatility | 1.0 | True | True | True | True | False | behavior_quality_ready | True | False | False | False | False | False | 129 | 160 | 130 |
| candidate_state_trend_continuation | trend | 1.0 | True | True | True | True | False | behavior_quality_ready | True | False | False | False | False | False | 129 | 160 | 130 |
| candidate_state_trend_exhaustion | trend | 1.0 | True | True | True | True | False | behavior_quality_ready | True | False | False | False | False | False | 129 | 160 | 130 |
| candidate_state_range_bound_oscillation | range | 1.0 | True | True | True | True | False | behavior_quality_ready | True | False | False | False | False | False | 129 | 160 | 130 |
| candidate_state_range_breakout_transition | range | 1.0 | True | True | True | True | False | behavior_quality_ready | True | False | False | False | False | False | 129 | 160 | 130 |
| candidate_state_macro_event_shock | macro_event | 1.0 | True | True | True | True | False | behavior_quality_ready | True | False | False | False | False | False | 129 | 160 | 130 |
| candidate_state_news_attention_surge | news_metadata | 1.0 | True | True | True | True | False | behavior_quality_ready | True | False | False | False | False | False | 129 | 160 | 130 |
| candidate_state_cross_asset_divergence | cross_asset | 1.0 | True | True | True | True | False | behavior_quality_ready | True | False | False | False | False | False | 129 | 160 | 130 |
| candidate_state_uncertain_regime | uncertain | 1.0 | True | True | True | True | False | behavior_quality_ready | True | False | False | False | False | False | 129 | 160 | 130 |

