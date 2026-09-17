# Phase 158: System Contract Integration

> **UYARI VE KAPSAM SINIRI**:
> Bu çıktı Phase 158 Full-System Integration and Advanced Acceptance Rehearsal çıktısıdır. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, full-system/readiness/integration/rehearsal değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek full-system execution, end-to-end bot run, live trading, broker execution, order generation, signal generation, model training, model fit/predict/inference, target/label/prediction üretimi, backtest, benchmark, optimizer, portfolio construction, risk reporting, scenario execution, metric calculation, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

- **Total Contracts**: `11`
- **Zero Execution Guaranteed**: `True`

### Integrated Contracts

| contract_id | subsystem_name | contract_type | version | status | contract_only | non_production | manual_review_required | zero_execution_guaranteed | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CNT-001 | data_contracts | data_providers | v1.0 | INTEGRATED | True | True | True | True | Contracts for data ingestion, economic calendar, and news metadata. |
| CNT-002 | feature_factor_contracts | feature_store | v1.0 | INTEGRATED | True | True | True | True | Contracts for technical indicators, factors, and feature quality. |
| CNT-003 | regime_contracts | regime_engine | v1.0 | INTEGRATED | True | True | True | True | Contracts for market behavior diagnostics, regimes, and transitions. |
| CNT-004 | ml_governance_contracts | ml_governance | v1.0 | INTEGRATED | True | True | True | True | Contracts for model governance, explainability, drift, and calibration. |
| CNT-005 | backtest_acceptance_contracts | backtest_engine | v1.0 | INTEGRATED | True | True | True | True | Contracts for realistic backtesting, walk-forward, and acceptance. |
| CNT-006 | portfolio_acceptance_contracts | portfolio_engine | v1.0 | INTEGRATED | True | True | True | True | Contracts for portfolio construction, optimization, and acceptance. |
| CNT-007 | risk_reporting_contracts | risk_engine | v1.0 | INTEGRATED | True | True | True | True | Contracts for risk limits, exposure attribution, and risk reporting. |
| CNT-008 | scenario_control_contracts | scenario_engine | v1.0 | INTEGRATED | True | True | True | True | Contracts for stress scenarios, drawdown controls, and derisking. |
| CNT-009 | safety_boundary_contracts | safety_layer | v1.0 | INTEGRATED | True | True | True | True | Contracts strictly enforcing no-live-trading, no-broker, and dry-run boundaries. |
| CNT-010 | reporting_contracts | reporting_layer | v1.0 | INTEGRATED | True | True | True | True | Contracts for markdown, txt, csv, and json status report builders. |
| CNT-011 | documentation_contracts | docs_layer | v1.0 | INTEGRATED | True | True | True | True | Contracts for operator manual, architecture, and safe usage guidelines. |

