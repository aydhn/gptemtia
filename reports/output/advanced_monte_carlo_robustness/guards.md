# Phase 149: Monte Carlo Bias & Lookahead Guards Report

> **Disclaimer**: Bu çıktı Phase 149 Monte Carlo Robustness and Parameter Stability raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, Monte-Carlo/readiness/robustness/parameter-stability değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek Monte Carlo execution, bootstrap, resampling, parameter optimization, parameter sweep, optimizer, gerçek model training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek VaR/ES/distribution/robustness metric hesaplama, performans garantisi, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

- **Total Guards**: `3`
- **All Active**: `True`
- **Status**: `monte_carlo_contract_ready`

## Active Guards

                              guard_id                   guard_type                                                                              description enforcement_action                                    profile_name  current_phase status  violations_found            domain
             GUARD_NO_LOOKAHEAD_149_01        column_name_inspector Scans DataFrame columns for forward-looking returns, future PnL, or shift(-1) artifacts.  QUARANTINE_COLUMN balanced_local_monte_carlo_robustness_contracts            149 ACTIVE                 0 bias_guard_domain
           GUARD_NO_FUTURE_JOIN_149_02     timestamp_join_validator      Verifies that right-side timestamps never exceed left-side conditioning timestamps.         BLOCK_JOIN balanced_local_monte_carlo_robustness_contracts            149 ACTIVE                 0 bias_guard_domain
GUARD_RESAMPLING_TEMPORAL_ORDER_149_03 chronological_sequence_guard      Enforces that within each resampled block, temporal ordering is strictly preserved.   BLOCK_RESAMPLING balanced_local_monte_carlo_robustness_contracts            149 ACTIVE                 0 bias_guard_domain
