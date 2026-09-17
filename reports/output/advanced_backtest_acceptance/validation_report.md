> [!CAUTION]
> **YASAL UYARI VE GÜVENLİK BİLDİRİMİ (PHASE 152 BACKTEST ACCEPTANCE REPORT)**:
> Bu çıktı Phase 152 Backtest Acceptance Report çıktısıdır. Canlı emir, broker talimatı, > kesin AL/SAT, yatırım tavsiyesi, backtest/acceptance/readiness değerini trade sinyali veya > production-ready/broker-ready/onay olarak kullanma, gerçek backtest execution, benchmark > execution, metric calculation, optimizer, model training, model fit/predict/inference, > dataset materialization, target/label/prediction üretimi, gerçek Sharpe/win-rate/return/> alpha/beta/drawdown/VaR/ES hesaplama, performans garantisi, strategy approval, capital > allocation, portfolio construction, position sizing, model deployment, model registry write, > model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/> embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

## Backtest Acceptance Validation Report
- **Validation Status**: `VALIDATION_PASS`
- **Total Checks**: 6
- **All Passed**: True
- **Forbidden Claims Clean**: True

  check_id                           check_name  passed  current_phase  target_final_phase  next_phase           status  non_signal  non_production  local_only
VAL-152-01                     phase_invariants    True            152                 160         153 acceptance_ready        True            True        True
VAL-152-02            offline_research_boundary    True            152                 160         153 acceptance_ready        True            True        True
VAL-152-03         prohibit_live_trading_broker    True            152                 160         153 acceptance_ready        True            True        True
VAL-152-04  prohibit_backtest_benchmark_metrics    True            152                 160         153 acceptance_ready        True            True        True
VAL-152-05 prohibit_strategy_approval_portfolio    True            152                 160         153 acceptance_ready        True            True        True
VAL-152-06               forbidden_claims_clean    True            152                 160         153 acceptance_ready        True            True        True