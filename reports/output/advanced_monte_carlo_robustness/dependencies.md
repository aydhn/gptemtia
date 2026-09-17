# Phase 149: Monte Carlo Dependencies Report

> **Disclaimer**: Bu çıktı Phase 149 Monte Carlo Robustness and Parameter Stability raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, Monte-Carlo/readiness/robustness/parameter-stability değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek Monte Carlo execution, bootstrap, resampling, parameter optimization, parameter sweep, optimizer, gerçek model training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek VaR/ES/distribution/robustness metric hesaplama, performans garantisi, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

- **Total Dependencies**: `2`
- **All Satisfied**: `True`
- **Status**: `monte_carlo_contract_ready`

## Dependency Matrix

                   dependency_id  source_phase                                                                        description    status                                    profile_name  current_phase            domain
DEP_REALISTIC_BACKTEST_CONTRACTS           146 Realistic backtest execution schema, fill modeling, and cash accounting contracts. SATISFIED balanced_local_monte_carlo_robustness_contracts            149 dependency_domain
     DEP_REALISTIC_TRADE_BLOTTER           146     Trade sequence ledger and execution timestamps required for trade reshuffling. SATISFIED balanced_local_monte_carlo_robustness_contracts            149 dependency_domain
