# Phase 130: State Transition Diagnostics Report

> [!IMPORTANT]
> Bu çıktı Phase 130 Regime Transition and Stability Analysis raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, transition veya stability değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, unsupervised execution, dimensionality reduction execution, prediction/target/label üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

- **Diagnostics Status**: Complete
- **All Non-Signal**: True
- **Contains Predictive Scores**: False

## Diagnostic Observations
| candidate_state | entity_family | observed_run_count | average_duration_periods | persistence_score | exit_frequency | stability_category | non_signal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| volatility_compression | volatility | 42 | 6.8 | 0.85 | 0.15 | stable_persistent | True |
| volatility_expansion | volatility | 28 | 3.4 | 0.7 | 0.3 | moderate_transient | True |
| trend_persistent_bullish | trend | 35 | 8.2 | 0.88 | 0.12 | highly_persistent | True |
| trend_persistent_bearish | trend | 31 | 7.5 | 0.86 | 0.14 | stable_persistent | True |
| range_bound_consolidation | range | 55 | 11.4 | 0.91 | 0.09 | highly_persistent | True |
| macro_release_reaction | macro_event | 18 | 2.1 | 0.52 | 0.48 | transient_event | True |
