# Phase 158: System Boundaries

> **UYARI VE KAPSAM SINIRI**:
> Bu çıktı Phase 158 Full-System Integration and Advanced Acceptance Rehearsal çıktısıdır. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, full-system/readiness/integration/rehearsal değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek full-system execution, end-to-end bot run, live trading, broker execution, order generation, signal generation, model training, model fit/predict/inference, target/label/prediction üretimi, backtest, benchmark, optimizer, portfolio construction, risk reporting, scenario execution, metric calculation, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

- **Total Rules**: `18`
- **Prohibited Count**: `15`
- **Allowed Count**: `3`

### Enforced Boundaries

| boundary_id | boundary_type | rule_name | action_type | is_allowed | reason |
| --- | --- | --- | --- | --- | --- |
| SFT-158-001 | safety_boundary | no_live_trading | execution | False | Live trading is strictly prohibited. |
| SFT-158-002 | safety_boundary | no_broker_integration | network | False | Connecting to live broker APIs is strictly prohibited. |
| SFT-158-003 | safety_boundary | no_real_order_generation | order | False | Generating real orders is strictly prohibited. |
| SFT-158-004 | safety_boundary | no_investment_advice | advice | False | Providing investment or financial advice is strictly prohibited. |
| SFT-158-005 | safety_boundary | no_signal_generation | signal | False | Outputting trade signals is strictly prohibited in Phase 158. |
| SFT-158-006 | safety_boundary | no_system_execution | execution | False | Real full-system execution is blocked by contract. |
| SFT-158-007 | safety_boundary | no_end_to_end_bot_run | execution | False | Running live bot workflows is blocked by policy. |
| SFT-158-008 | safety_boundary | no_model_training | ml | False | Training or fitting ML models is forbidden. |
| SFT-158-009 | safety_boundary | no_prediction_inference | ml | False | Running model prediction or inference is forbidden. |
| SFT-158-010 | safety_boundary | no_backtest_execution | backtest | False | Executing real backtests is forbidden. |
| SFT-158-011 | safety_boundary | no_portfolio_execution | portfolio | False | Executing portfolio construction or optimization is forbidden. |
| SFT-158-012 | safety_boundary | no_risk_execution | risk | False | Executing live risk calculations is forbidden. |
| SFT-158-013 | safety_boundary | no_scenario_execution | scenario | False | Executing real scenario stress testing is forbidden. |
| SFT-158-014 | safety_boundary | no_web_scraping | network | False | Scraping external websites or bypassing paywalls is forbidden. |
| SFT-158-015 | safety_boundary | no_credential_leakage | security | False | Exposing API keys, tokens, or secrets is forbidden. |
| SFT-158-016 | safety_boundary | source_preservation | storage | True | Raw source data must be preserved immutably. |
| SFT-158-017 | safety_boundary | dry_run_enforcement | runtime | True | All operations must run in dry-run mode. |
| SFT-158-018 | safety_boundary | local_offline_isolation | runtime | True | Operations must remain strictly local and offline. |

