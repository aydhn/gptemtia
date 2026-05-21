import re

with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "a") as f:
    f.write("""
## Regime-Aware Portfolio Research

Portfolio Research / Returns / Baskets / Correlation
-> RegimeClassifier
-> RegimeConditionedReturns
-> RegimeCorrelation
-> MacroScenarios
-> ScenarioSensitivity
-> StressWindows
-> BasketStressTest
-> DrawdownClustering
-> RecoveryAnalysis
-> TailRisk
-> RiskRegimeExposure
-> RegimeQuality
-> Regime-Aware Portfolio Reports
""")

with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "a") as f:
    f.write("""
## Phase 42: Regime-Aware Portfolio Research
- Portfolio regime profile sistemi eklendi.
- Regime label registry eklendi.
- RegimeClassificationResult, MacroScenarioDefinition, BasketStressTestResult ve DrawdownCluster modelleri eklendi.
- PortfolioRegimeDataAdapter eklendi.
- Regime classifier eklendi.
- Regime-conditioned returns eklendi.
- Regime-conditioned correlation eklendi.
- Macro scenarios eklendi.
- Scenario sensitivity eklendi.
- Historical stress windows eklendi.
- Basket stress test eklendi.
- Drawdown clustering eklendi.
- Recovery analysis eklendi.
- Tail risk proxy modülü eklendi.
- Risk regime exposure eklendi.
- Regime quality report eklendi.
- PortfolioRegimePipeline eklendi.
- DataLake portfolio regime kayıt desteği aldı.
- Portfolio regime scriptleri eklendi.
- Testler genişletildi.
""")

with open("commodity_fx_signal_bot/README.md", "a") as f:
    f.write("""
## Regime-Aware Portfolio Research and Stress Tests

- Regime-aware portfolio research gerçek portföy yönetimi değildir.
- Risk-on/risk-off label’ları canlı sinyal değildir.
- Macro scenario sensitivity tahmin değildir.
- Basket stress test gerçek risk limiti değildir.
- Drawdown clustering geçmiş/sanal sepet analizidir.
- Tail risk historical proxy’dir.
- Çıktılar data/lake/portfolio_regime ve reports/output/portfolio_regime altında oluşur.

Komutları:
```bash
python -m scripts.run_regime_portfolio_report --timeframe 1d --limit 20
python -m scripts.run_macro_scenario_sensitivity_report --timeframe 1d --limit 20
python -m scripts.run_basket_stress_test_report --timeframe 1d --limit 20
python -m scripts.run_drawdown_cluster_report --timeframe 1d
python -m scripts.run_risk_regime_exposure_report --timeframe 1d
python -m scripts.run_portfolio_regime_status
```
""")
