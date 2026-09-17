# Phase 157: Portfolio Acceptance Profile Registry Report

> [!WARNING]
> **YASAL UYARI VE NON-PRODUCTION / RESEARCH-ONLY KURALI**:
> Bu çıktı Phase 157 Portfolio Acceptance Report çıktısıdır. Canlı emir, broker talimatı, > kesin AL/SAT, yatırım tavsiyesi, portfolio/acceptance/readiness değerini trade sinyali veya > production-ready/broker-ready/onay olarak kullanma, gerçek portfolio construction, position sizing, > portfolio optimization, allocation generation, rebalance, risk reporting, exposure attribution, > limit monitoring, scenario execution, drawdown control, portfolio adjustment, hedge/de-risk, > alerting, dashboard generation, optimizer, model training, model fit/predict/inference, > dataset materialization, target/label/prediction üretimi, gerçek VaR/ES/exposure/drawdown/risk metric > hesaplama, performans garantisi, strategy approval, portfolio approval, model deployment, model > registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/> scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.


- **Active Profile**: `balanced_local_portfolio_acceptance_contracts`
- **Total Profiles**: `3`
- **All Dry-Run**: `True`
- **All Local-Only**: `True`
- **All Non-Production**: `True`
- **Status**: `portfolio_acceptance_ready`

## Configured Profiles

| profile_name | description | current_phase | target_final_phase | next_phase | min_readiness_score | dry_run_default | local_only | non_production | research_only | allow_live_trading | allow_broker_integration | allow_signal_generation | allow_portfolio_construction | allow_portfolio_optimization | allow_risk_reporting_execution | allow_scenario_execution | allow_drawdown_control_execution | is_active | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| balanced_local_portfolio_acceptance_contracts | Dengeli yerel Portfolio Acceptance kabul ve yonetisim profili (Phase 153-156 konsolide). | 157 | 160 | 158 | 0.5 | True | True | True | True | False | False | False | False | False | False | False | False | True | portfolio_acceptance_ready |
| strict_non_production_portfolio_acceptance_safety | Siki non-production, no-live-trading ve sifir portfoy/risk execution odakli guvenlik kabul profili. | 157 | 160 | 158 | 0.65 | True | True | True | True | False | False | False | False | False | False | False | False | False | portfolio_acceptance_ready |
| dry_run_phase_153_157_acceptance_focus | Dry-run uyumlu, manifest ve Phase 158 full-system integration devri odakli kabul profili. | 157 | 160 | 158 | 0.45 | True | True | True | True | False | False | False | False | False | False | False | False | False | portfolio_acceptance_ready |
