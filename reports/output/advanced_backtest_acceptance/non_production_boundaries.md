> [!CAUTION]
> **YASAL UYARI VE GÜVENLİK BİLDİRİMİ (PHASE 152 BACKTEST ACCEPTANCE REPORT)**:
> Bu çıktı Phase 152 Backtest Acceptance Report çıktısıdır. Canlı emir, broker talimatı, > kesin AL/SAT, yatırım tavsiyesi, backtest/acceptance/readiness değerini trade sinyali veya > production-ready/broker-ready/onay olarak kullanma, gerçek backtest execution, benchmark > execution, metric calculation, optimizer, model training, model fit/predict/inference, > dataset materialization, target/label/prediction üretimi, gerçek Sharpe/win-rate/return/> alpha/beta/drawdown/VaR/ES hesaplama, performans garantisi, strategy approval, capital > allocation, portfolio construction, position sizing, model deployment, model registry write, > model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/> embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

## Backtest Acceptance Boundaries & Invariants
- **Domain**: `non_production_boundary_domain`
- **Total Rules**: 5
- **Status**: `ACCEPTED`

boundary_id              boundary_name                                                                           description  active  current_phase  target_final_phase  next_phase           status  non_signal  non_production  local_only
 NPB-152-01  research_only_environment  All backtest acceptance logic operates exclusively as an offline research framework.    True            152                 160         153 acceptance_ready        True            True        True
 NPB-152-02            dry_run_default      Operations default to dry-run contracts without stateful execution side-effects.    True            152                 160         153 acceptance_ready        True            True        True
 NPB-152-03   no_production_deployment Production deployment pipelines, endpoints, or release tags remain strictly disabled.    True            152                 160         153 acceptance_ready        True            True        True
 NPB-152-04 local_filesystem_isolation             Artifacts are stored locally in DataLake without remote cloud publishing.    True            152                 160         153 acceptance_ready        True            True        True
 NPB-152-05       zero_broker_coupling                        Zero coupling with real brokers or trading execution services.    True            152                 160         153 acceptance_ready        True            True        True