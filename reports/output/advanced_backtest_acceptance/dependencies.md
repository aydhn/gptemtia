> [!CAUTION]
> **YASAL UYARI VE GÜVENLİK BİLDİRİMİ (PHASE 152 BACKTEST ACCEPTANCE REPORT)**:
> Bu çıktı Phase 152 Backtest Acceptance Report çıktısıdır. Canlı emir, broker talimatı, > kesin AL/SAT, yatırım tavsiyesi, backtest/acceptance/readiness değerini trade sinyali veya > production-ready/broker-ready/onay olarak kullanma, gerçek backtest execution, benchmark > execution, metric calculation, optimizer, model training, model fit/predict/inference, > dataset materialization, target/label/prediction üretimi, gerçek Sharpe/win-rate/return/> alpha/beta/drawdown/VaR/ES hesaplama, performans garantisi, strategy approval, capital > allocation, portfolio construction, position sizing, model deployment, model registry write, > model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/> embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

## Backtest Acceptance Dependency Verification
- **Total Dependencies**: 11
- **Satisfied**: 11
- **All Satisfied**: True
- **Status**: `ACCEPTED`

 dep_id phase_ref                           source                                            requirement  satisfied  current_phase  target_final_phase  next_phase           status  non_signal  non_production  local_only
DEP-146 Phase 146      advanced_realistic_backtest         Realistic backtest and cost/slippage contracts       True            152                 160         153 acceptance_ready        True            True        True
DEP-147 Phase 147 advanced_walk_forward_validation                   Walk-forward and OOS split contracts       True            152                 160         153 acceptance_ready        True            True        True
DEP-148 Phase 148          advanced_stress_testing       Stress testing and scenario simulation contracts       True            152                 160         153 acceptance_ready        True            True        True
DEP-149 Phase 149  advanced_monte_carlo_robustness         Monte Carlo robustness and stability contracts       True            152                 160         153 acceptance_ready        True            True        True
DEP-150 Phase 150     advanced_backtest_governance         Backtest governance and bias control contracts       True            152                 160         153 acceptance_ready        True            True        True
DEP-151 Phase 151    advanced_benchmark_evaluation Benchmark comparison and strategy evaluation contracts       True            152                 160         153 acceptance_ready        True            True        True
DEP-145 Phase 145           advanced_ml_acceptance              Consolidated Advanced ML block acceptance       True            152                 160         153 acceptance_ready        True            True        True
DEP-144 Phase 144        advanced_model_governance              Model governance and model card contracts       True            152                 160         153 acceptance_ready        True            True        True
DEP-137 Phase 137     advanced_ml_dataset_registry                   Dataset contracts and split registry       True            152                 160         153 acceptance_ready        True            True        True
DEP-134 Phase 134                 ml.feature_store            FeatureStore contracts and metadata catalog       True            152                 160         153 acceptance_ready        True            True        True
DEP-135 Phase 135       advanced_regime_acceptance                 Regime classification block acceptance       True            152                 160         153 acceptance_ready        True            True        True