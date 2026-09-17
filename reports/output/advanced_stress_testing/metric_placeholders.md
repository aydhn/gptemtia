# Phase 148: Stres Metrik Yer Tutucuları Raporu

> [!IMPORTANT]
> **YASAL UYARI VE ARAŞTIRMA BEYANI (PHASE 148)**:
> Bu çıktı Phase 148 Stress Testing and Scenario Simulation raporudur. > Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, stress/readiness/scenario/robustness > değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, > gerçek stress test execution, scenario simulation, optimizer, Monte Carlo, > gerçek model training, model fit/predict/inference, dataset materialization, > target/label/prediction üretimi, gerçek stress PnL/drawdown/VaR/ES hesaplama, > performans garantisi, model deployment, model registry write, model artifact persistence, > scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı > veya gerçek provider API çağrısı değildir.

## Metrik Özeti
- **Toplam Metrik Yer Tutucusu**: `0`
- **Gerçek Hesaplama Durumu**: `DEVRE DIŞI (CALCULATION_BLOCKED)`
- **Performans İddiası**: `YOK (ZERO_PERFORMANCE_CLAIMS)`

## Metrik Formül Tanımları

| metric_name | metric_category | description | formula_spec | benchmark_relative | metric_calculated | performance_claim_generated | non_signal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| stressed_return_placeholder | STRESS_PERFORMANCE | Şok altındaki portföy getirisi yer tutucusu. | R_stress = sum(w_i * (R_i + delta_R_i)) - total_stress_friction | False | False | False | True |
| stressed_volatility_placeholder | STRESS_RISK | Şok altındaki portföy oynaklığı yer tutucusu. | sigma_stress = sqrt(w.T * Sigma_stress * w) | False | False | False | True |
| stressed_var_placeholder | TAIL_RISK | Stresli Riske Maruz Değer (Stressed Value-at-Risk 99%) yer tutucusu. | VaR_99_stress = quantile(L_stress, 0.99) | False | False | False | True |
| stressed_expected_shortfall_placeholder | TAIL_RISK | Stresli Beklenen Kayıp (Stressed Expected Shortfall / CVaR) yer tutucusu. | ES_99_stress = E[L_stress | L_stress >= VaR_99_stress] | False | False | False | True |
