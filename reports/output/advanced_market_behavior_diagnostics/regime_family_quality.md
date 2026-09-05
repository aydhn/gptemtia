# Phase 129 Regime Family Quality Report

> [!NOTE]
> UYARI: Bu çıktı Phase 129 Market Behavior Diagnostics and Regime Quality raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, behavior quality veya candidate state quality değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, unsupervised execution, dimensionality reduction execution, prediction/target/label üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Özet Bilgiler
- **Toplam Rejim Ailesi**: `8`
- **Hazır Aile Sayısı**: `0`
- **Ortalama Tutarlılık**: `0.00`
- **Phase 130 Geçişe Hazır**: `True`

## Rejim Ailesi Kalite Tablosu
| family_name | description | source_features_available | source_factors_available | source_context_available | quality_drift_dependency_available | validation_dependency_available | coverage_ratio | consistency_score | manual_review_blocker_count | phase_130_readiness | quality_status | non_signal | current_phase | target_final_phase | next_phase |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volatility | Volatility expansion, compression, and clustering dynamics. | True | True | True | True | True | 1.0 | 1.0 | 0 | True | behavior_quality_ready | True | 129 | 160 | 130 |
| trend | Directional persistence, continuation, and exhaustion dynamics. | True | True | True | True | True | 1.0 | 1.0 | 0 | True | behavior_quality_ready | True | 129 | 160 | 130 |
| range | Mean-reversion, channel boundary, and oscillation dynamics. | True | True | True | True | True | 1.0 | 1.0 | 0 | True | behavior_quality_ready | True | 129 | 160 | 130 |
| macro_event | Scheduled macroeconomic release and interest rate shock dynamics. | True | True | True | True | True | 1.0 | 1.0 | 0 | True | behavior_quality_ready | True | 129 | 160 | 130 |
| news_metadata | Metadata-only news attention, topic clustering, and tag frequency. | True | True | True | True | True | 1.0 | 1.0 | 0 | True | behavior_quality_ready | True | 129 | 160 | 130 |
| cross_asset | Inter-market alignment, FX/commodity co-movement, and divergence. | True | True | True | True | True | 1.0 | 1.0 | 0 | True | behavior_quality_ready | True | 129 | 160 | 130 |
| transition | Boundary crossing, regime mutation, and temporal shift states. | True | True | True | True | True | 1.0 | 0.95 | 0 | True | behavior_quality_ready | True | 129 | 160 | 130 |
| uncertain | High entropy, low confidence, or unclassified market behavior. | True | True | True | True | True | 1.0 | 0.9 | 0 | True | behavior_quality_ready | True | 129 | 160 | 130 |

