# Phase 149: Monte Carlo Validation Report

> **Disclaimer**: Bu çıktı Phase 149 Monte Carlo Robustness and Parameter Stability raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, Monte-Carlo/readiness/robustness/parameter-stability değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek Monte Carlo execution, bootstrap, resampling, parameter optimization, parameter sweep, optimizer, gerçek model training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek VaR/ES/distribution/robustness metric hesaplama, performans garantisi, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

- **Validation Status**: `PASS`
- **Total Checks**: `5`
- **All Passed**: `True`
- **Status**: `None`

## Validation Checks

          suite_name status                                                                                                                                                                                                                                                                                   details  non_signal  local_only
    profile_registry   PASS                                                                                                                                                          {'passed': True, 'all_non_production': True, 'all_non_signal': True, 'zero_broker_ready': True, 'zero_live_trading_ready': True}        True        True
robustness_contracts   PASS {'passed': True, 'all_monte_carlo_execution_blocked': True, 'all_bootstrap_execution_blocked': True, 'all_resampling_execution_blocked': True, 'all_live_trading_blocked': True, 'all_broker_blocked': True, 'all_metric_calc_blocked': True, 'all_parameter_optimization_blocked': True}        True        True
 stability_contracts   PASS                                                                                                                                                                                                            {'passed': True, 'all_optimization_blocked': True, 'all_sweeps_blocked': True}        True        True
            manifest   PASS                                                                                                                                                                                                                                 {'passed': True, 'checks_passed': 19, 'total_checks': 19}        True        True
    forbidden_claims   PASS                                                                                                                                                                                                                                  {'is_clean': True, 'violations': [], 'non_signal': True}        True        True
