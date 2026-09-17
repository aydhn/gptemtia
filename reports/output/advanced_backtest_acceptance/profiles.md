> [!CAUTION]
> **YASAL UYARI VE GÜVENLİK BİLDİRİMİ (PHASE 152 BACKTEST ACCEPTANCE REPORT)**:
> Bu çıktı Phase 152 Backtest Acceptance Report çıktısıdır. Canlı emir, broker talimatı, > kesin AL/SAT, yatırım tavsiyesi, backtest/acceptance/readiness değerini trade sinyali veya > production-ready/broker-ready/onay olarak kullanma, gerçek backtest execution, benchmark > execution, metric calculation, optimizer, model training, model fit/predict/inference, > dataset materialization, target/label/prediction üretimi, gerçek Sharpe/win-rate/return/> alpha/beta/drawdown/VaR/ES hesaplama, performans garantisi, strategy approval, capital > allocation, portfolio construction, position sizing, model deployment, model registry write, > model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/> embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

## Backtest Acceptance Profile Registry
- **Active Profile**: `balanced_local_backtest_acceptance_contracts`
- **Total Profiles**: 3
- **All Dry Run**: True
- **All Local Only**: True
- **Status**: `ACCEPTED`

                                    profile_name                                                                                     description  current_phase  target_final_phase  next_phase  dry_run_default  local_only  non_production  research_only  min_readiness_score  enabled  is_active           status  non_signal  production_ready  broker_ready
    balanced_local_backtest_acceptance_contracts         Dengeli yerel Backtest Acceptance kabul ve yonetisim profili (Phase 146-151 konsolide).            152                 160         153             True        True            True           True                 0.50     True       True acceptance_ready        True             False         False
strict_non_production_backtest_acceptance_safety Siki non-production, no-live-trading ve sifir backtest execution odakli guvenlik kabul profili.            152                 160         153             True        True            True           True                 0.65     True      False acceptance_ready        True             False         False
          dry_run_phase_146_152_acceptance_focus        Dry-run uyumlu, manifest ve Phase 153 portfolio construction devri odakli kabul profili.            152                 160         153             True        True            True           True                 0.45     True      False acceptance_ready        True             False         False