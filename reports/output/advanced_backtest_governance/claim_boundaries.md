# Phase 150: Backtest Claim Boundaries Report

> **Disclaimer**: Bu çıktı Phase 150 Backtest Governance and Bias Control raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, backtest/governance/bias-control/readiness değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek backtest execution, benchmark execution, metric calculation, optimizer, model training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek Sharpe/win-rate/return/alpha/drawdown hesaplama, performans garantisi, strategy approval, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

- **Domain**: `metric_claim_boundary_domain`
- **Total Boundaries**: `6`
- **All Claims Blocked**: `None`
- **Status**: `governance_contract_ready`

## Boundary Enforcement

                 boundary_name   target_metric                                                                 policy  is_blocked  calculation_allowed           status  non_signal  local_only  phase
  boundary_block_actual_sharpe   actual_sharpe               Block calculation of realized Sharpe ratio in Phase 150.        True                False ENFORCED_BLOCKED        True        True    150
boundary_block_actual_win_rate actual_win_rate            Block calculation of realized trade win rates in Phase 150.        True                False ENFORCED_BLOCKED        True        True    150
   boundary_block_actual_alpha    actual_alpha           Block calculation of annualized strategy alpha in Phase 150.        True                False ENFORCED_BLOCKED        True        True    150
  boundary_block_actual_return   actual_return  Block calculation of cumulative or CAGR strategy return in Phase 150.        True                False ENFORCED_BLOCKED        True        True    150
boundary_block_actual_drawdown actual_drawdown           Block calculation of realized maximum drawdown in Phase 150.        True                False ENFORCED_BLOCKED        True        True    150
  boundary_block_actual_var_es   actual_var_es Block calculation of realized VaR and Expected Shortfall in Phase 150.        True                False ENFORCED_BLOCKED        True        True    150
