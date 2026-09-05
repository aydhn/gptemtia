# Phase 129 Market Behavior Diagnostics Report

> [!NOTE]
> UYARI: Bu çıktı Phase 129 Market Behavior Diagnostics and Regime Quality raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, behavior quality veya candidate state quality değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, unsupervised execution, dimensionality reduction execution, prediction/target/label üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Özet Bilgiler
- **Toplam Tanı Konuları**: `0`
- **Ortalama Kapsama**: `0.00`
- **Tüm Bağlamlar Hazır**: `True`
- **Non-Signal**: `True`

## Davranış Tanı Detayları
| context_name | description | coverage_ratio | source_dependency | quality_drift_dependency_passed | expansion_compression_available | is_ready | non_signal | contains_target_or_prediction | model_training_executed | clustering_executed | current_phase | target_final_phase | next_phase |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volatility_high_context | High realized volatility and ATR expansion threshold context. | 1.0 | advanced_feature_engine.atr,realized_volatility | True | True | True | True | False | False | False | 129 | 160 | 130 |
| volatility_low_context | Low realized volatility and band contraction threshold context. | 1.0 | advanced_feature_engine.bollinger_bandwidth,atr | True | True | True | True | False | False | False | 129 | 160 | 130 |
| volatility_expansion_context | Widening range and increasing variance rate of change context. | 1.0 | advanced_factor_metadata.volatility_factor_families | True | True | True | True | False | False | False | 129 | 160 | 130 |
| volatility_compression_context | Narrowing historical range and tight channel regime context. | 1.0 | advanced_factor_metadata.volatility_factor_families | True | True | True | True | False | False | False | 129 | 160 | 130 |

