# Phase 148: Stres Senaryo Sözleşmeleri Raporu

> [!IMPORTANT]
> **YASAL UYARI VE ARAŞTIRMA BEYANI (PHASE 148)**:
> Bu çıktı Phase 148 Stress Testing and Scenario Simulation raporudur. > Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, stress/readiness/scenario/robustness > değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, > gerçek stress test execution, scenario simulation, optimizer, Monte Carlo, > gerçek model training, model fit/predict/inference, dataset materialization, > target/label/prediction üretimi, gerçek stress PnL/drawdown/VaR/ES hesaplama, > performans garantisi, model deployment, model registry write, model artifact persistence, > scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı > veya gerçek provider API çağrısı değildir.

## Sözleşme Özeti
- **Toplam Senaryo Sözleşmesi**: `9`
- **Stres Yürütmesi Engelli**: `True`
- **Senaryo Simülasyonu Engelli**: `True`
- **Metrik Hesaplama Engelli**: `True`
- **Canlı İşlem Engelli**: `True`
- **Operatör İncelemesi Zorunlu**: `True`

## Sözleşme Detayları

| contract_name | scenario_family | description | realistic_backtest_ref | walk_forward_ref | transaction_cost_ref | slippage_model_ref | regime_context_ref | no_lookahead_guard_ref | scenario_leakage_guard_ref | stress_execution_allowed | scenario_simulation_allowed | metric_calculation_allowed | optimizer_execution_allowed | live_trading_allowed | broker_execution_allowed | signal_generation_allowed | manual_review_required | non_signal | local_only |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| local_stress_testing_contract | LOCAL_GENERIC | Yerel genel stres testi sozlesmesi. | realistic_backtest_engine_v1 | walk_forward_engine_v1 | cost_model_v1 | slippage_model_v1 | regime_context_v1 | strict_no_lookahead_guard | strict_scenario_leakage_guard | False | False | False | False | False | False | False | True | True | True |
| historical_scenario_contract | HISTORICAL_CRISIS | Tarihsel kriz donemleri simülasyon sozlesmesi. | realistic_backtest_engine_v1 | walk_forward_engine_v1 | cost_model_v1 | slippage_model_v1 | regime_context_v1 | strict_no_lookahead_guard | strict_scenario_leakage_guard | False | False | False | False | False | False | False | True | True | True |
| hypothetical_scenario_contract | HYPOTHETICAL_SHOCK | Varsayimsal makro ve jeopolitik kriz sozlesmesi. | realistic_backtest_engine_v1 | walk_forward_engine_v1 | cost_model_v1 | slippage_model_v1 | regime_context_v1 | strict_no_lookahead_guard | strict_scenario_leakage_guard | False | False | False | False | False | False | False | True | True | True |
| regime_shock_contract | REGIME_TRANSITION | Ani rejim degisimi ve kirilma soku sozlesmesi. | realistic_backtest_engine_v1 | walk_forward_engine_v1 | cost_model_v1 | slippage_model_v1 | regime_context_v1 | strict_no_lookahead_guard | strict_scenario_leakage_guard | False | False | False | False | False | False | False | True | True | True |
| volatility_shock_contract | VOLATILITY_EXPANSION | Ani volatilite genislemesi ve patlamasi sozlesmesi. | realistic_backtest_engine_v1 | walk_forward_engine_v1 | cost_model_v1 | slippage_model_v1 | regime_context_v1 | strict_no_lookahead_guard | strict_scenario_leakage_guard | False | False | False | False | False | False | False | True | True | True |
| liquidity_shock_contract | LIQUIDITY_DROUGHT | Derinlik kaybi ve likidite kurakligi sozlesmesi. | realistic_backtest_engine_v1 | walk_forward_engine_v1 | cost_model_v1 | slippage_model_v1 | regime_context_v1 | strict_no_lookahead_guard | strict_scenario_leakage_guard | False | False | False | False | False | False | False | True | True | True |
| spread_widening_contract | SPREAD_DISRUPTION | Asiri spread genislemesi ve alis-satis sok sozlesmesi. | realistic_backtest_engine_v1 | walk_forward_engine_v1 | cost_model_v1 | slippage_model_v1 | regime_context_v1 | strict_no_lookahead_guard | strict_scenario_leakage_guard | False | False | False | False | False | False | False | True | True | True |
| cross_asset_contagion_contract | CONTAGION_SPREAD | Varliklar arasi kriz bulasma sozlesmesi. | realistic_backtest_engine_v1 | walk_forward_engine_v1 | cost_model_v1 | slippage_model_v1 | regime_context_v1 | strict_no_lookahead_guard | strict_scenario_leakage_guard | False | False | False | False | False | False | False | True | True | True |
| cost_slippage_shock_contract | EXECUTION_FRICTION | Stresli maliyet ve katastrofik kayma sozlesmesi. | realistic_backtest_engine_v1 | walk_forward_engine_v1 | cost_model_v1 | slippage_model_v1 | regime_context_v1 | strict_no_lookahead_guard | strict_scenario_leakage_guard | False | False | False | False | False | False | False | True | True | True |
