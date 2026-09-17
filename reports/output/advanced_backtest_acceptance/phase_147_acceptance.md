> [!CAUTION]
> **YASAL UYARI VE GÜVENLİK BİLDİRİMİ (PHASE 152 BACKTEST ACCEPTANCE REPORT)**:
> Bu çıktı Phase 152 Backtest Acceptance Report çıktısıdır. Canlı emir, broker talimatı, > kesin AL/SAT, yatırım tavsiyesi, backtest/acceptance/readiness değerini trade sinyali veya > production-ready/broker-ready/onay olarak kullanma, gerçek backtest execution, benchmark > execution, metric calculation, optimizer, model training, model fit/predict/inference, > dataset materialization, target/label/prediction üretimi, gerçek Sharpe/win-rate/return/> alpha/beta/drawdown/VaR/ES hesaplama, performans garantisi, strategy approval, capital > allocation, portfolio construction, position sizing, model deployment, model registry write, > model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/> embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

## Phase 147 Acceptance Report: Walk-Forward Validation and Out-of-Sample Benchmarking
- **Active Profile**: `balanced_local_backtest_acceptance_contracts`
- **Total Checks**: 10
- **Passed Checks**: 10
- **All Passed**: True
- **Status**: `ACCEPTED`

  check_id                           name                                     topic  passed                                                            details phase_ref  current_phase  target_final_phase  next_phase           status  non_signal  production_ready  broker_ready
CHK-147-01                 module_present advanced_walk_forward_validation presence    True                     Core walk-forward validation package verified. Phase 147            152                 160         153 acceptance_ready        True             False         False
CHK-147-02 walk_forward_contracts_present              Walk-forward split contracts    True       Anchored and rolling walk-forward window contracts verified. Phase 147            152                 160         153 acceptance_ready        True             False         False
CHK-147-03    oos_split_contracts_present             Out-of-sample split contracts    True                Train/validation/test isolation contracts verified. Phase 147            152                 160         153 acceptance_ready        True             False         False
CHK-147-04    benchmark_contracts_present              Benchmark baseline contracts    True Buy-and-hold, equal weight, and cash benchmark contracts verified. Phase 147            152                 160         153 acceptance_ready        True             False         False
CHK-147-05   purge_embargo_guards_present                  Purge and embargo guards    True           Information leakage buffer rules between folds verified. Phase 147            152                 160         153 acceptance_ready        True             False         False
CHK-147-06      no_walk_forward_execution           Walk-forward execution disabled    True                       Zero simulation loops or fold runs executed. Phase 147            152                 160         153 acceptance_ready        True             False         False
CHK-147-07         no_benchmark_execution              Benchmark execution disabled    True                         Zero real benchmark calculations executed. Phase 147            152                 160         153 acceptance_ready        True             False         False
CHK-147-08          no_metric_calculation               Metric calculation disabled    True                         Zero performance ratios or stats computed. Phase 147            152                 160         153 acceptance_ready        True             False         False
CHK-147-09                no_live_trading                   Live trading prohibited    True                        Strict prohibition of live orders enforced. Phase 147            152                 160         153 acceptance_ready        True             False         False
CHK-147-10       handoff_to_148_completed                         Phase 148 handoff    True                 Phase 148 stress testing handoff report satisfied. Phase 147            152                 160         153 acceptance_ready        True             False         False