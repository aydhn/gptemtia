# Phase 150: Result Reporting Governance Report

> **Disclaimer**: Bu çıktı Phase 150 Backtest Governance and Bias Control raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, backtest/governance/bias-control/readiness değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek backtest execution, benchmark execution, metric calculation, optimizer, model training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek Sharpe/win-rate/return/alpha/drawdown hesaplama, performans garantisi, strategy approval, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

- **Domain**: `result_reporting_domain`
- **Total Requirements**: `None`
- **All Claims Prohibited**: `None`
- **Status**: `governance_contract_ready`

## Reporting Standards

                            contract_name                                                                              description                                                                        requirement  actual_metrics_calculated  performance_claim_allowed  result_claim_allowed  non_signal  local_only  dry_run  phase
            hypothesis_treatment_contract      All backtest outputs must be explicitly labeled as unverified empirical hypotheses.        Preclude affirmative performance guarantees or forward efficacy assertions.                      False                      False                 False        True        True     True    150
mandatory_full_period_disclosure_contract     Mandatory disclosure of entire evaluated timeline including severe drawdown windows.            Prohibit truncation of unprofitable periods or selective date trimming.                      False                      False                 False        True        True     True    150
 negative_performance_disclosure_contract  Exhaustive reporting of loss clusters, continuous losing streaks, and worst-case paths.     Highlight stress periods and parameter fragility alongside central tendencies.                      False                      False                 False        True        True     True    150
  transaction_friction_breakdown_contract Detailed line-item reporting of simulated fees, financing carry, and execution slippage.                  Demonstrate net returns under zero-cost vs realistic cost models.                      False                      False                 False        True        True     True    150
   benchmark_relative_disclosure_contract      Mandatory side-by-side comparison against pre-committed passive and cash baselines. Forbid reporting strategy returns in isolation without standard benchmark context.                      False                      False                 False        True        True     True    150
 uncalculated_metric_placeholder_contract  All numerical metric fields (Sharpe, win-rate, alpha) remain placeholders in Phase 150.  Block numerical performance calculation until formal validation in Phase 151-152.                      False                      False                 False        True        True     True    150
