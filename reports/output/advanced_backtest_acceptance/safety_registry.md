> [!CAUTION]
> **YASAL UYARI VE GÜVENLİK BİLDİRİMİ (PHASE 152 BACKTEST ACCEPTANCE REPORT)**:
> Bu çıktı Phase 152 Backtest Acceptance Report çıktısıdır. Canlı emir, broker talimatı, > kesin AL/SAT, yatırım tavsiyesi, backtest/acceptance/readiness değerini trade sinyali veya > production-ready/broker-ready/onay olarak kullanma, gerçek backtest execution, benchmark > execution, metric calculation, optimizer, model training, model fit/predict/inference, > dataset materialization, target/label/prediction üretimi, gerçek Sharpe/win-rate/return/> alpha/beta/drawdown/VaR/ES hesaplama, performans garantisi, strategy approval, capital > allocation, portfolio construction, position sizing, model deployment, model registry write, > model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/> embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

## Backtest Acceptance Boundaries & Invariants
- **Domain**: `safety_boundary_domain`
- **Total Rules**: 12
- **Status**: `ACCEPTED`

boundary_id                     boundary_name                                                           rule  enforced  current_phase  target_final_phase  next_phase           status  non_signal  non_production  local_only
 SFT-152-01             prohibit_live_trading          Live trading and order generation strictly forbidden.      True            152                 160         153 acceptance_ready        True            True        True
 SFT-152-02               prohibit_broker_api Broker API calls, FIX engines, web sockets strictly forbidden.      True            152                 160         153 acceptance_ready        True            True        True
 SFT-152-03       prohibit_backtest_execution     Real backtest loop execution and PnL generation forbidden.      True            152                 160         153 acceptance_ready        True            True        True
 SFT-152-04      prohibit_benchmark_execution              Real benchmark performance computation forbidden.      True            152                 160         153 acceptance_ready        True            True        True
 SFT-152-05       prohibit_metric_calculation      Sharpe, drawdown, VaR, alpha, beta calculation forbidden.      True            152                 160         153 acceptance_ready        True            True        True
 SFT-152-06        prohibit_strategy_approval           Strategy approval and production sign-off forbidden.      True            152                 160         153 acceptance_ready        True            True        True
 SFT-152-07       prohibit_capital_allocation       Capital allocation and portfolio construction forbidden.      True            152                 160         153 acceptance_ready        True            True        True
 SFT-152-08          prohibit_position_sizing             Position sizing execution forbidden in this phase.      True            152                 160         153 acceptance_ready        True            True        True
 SFT-152-09      prohibit_optimizer_execution       Parameter grid search and optimizer execution forbidden.      True            152                 160         153 acceptance_ready        True            True        True
 SFT-152-10 prohibit_model_training_inference                  Model training, fitting, inference forbidden.      True            152                 160         153 acceptance_ready        True            True        True
 SFT-152-11    prohibit_model_registry_writes      Model registry writes and artifact persistence forbidden.      True            152                 160         153 acceptance_ready        True            True        True
 SFT-152-12   prohibit_scraping_and_full_text   Web scraping, credential exposure, full text news forbidden.      True            152                 160         153 acceptance_ready        True            True        True