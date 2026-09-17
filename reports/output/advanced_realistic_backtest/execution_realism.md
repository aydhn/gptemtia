# Phase 146: Execution Realism Assumptions Report

> **YASAL UYARI VE GUCLENDIRILMIS GUVENLIK SINIRI (PHASE 146)**:
> Bu cikti Phase 146 Realistic Backtest, Transaction Cost and Slippage Modeling raporudur. Canli emir, broker talimati, kesin AL/SAT, yatirim tavsiyesi, backtest/readiness/cost/slippage degerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gercek backtest execution, walk-forward, benchmark, optimizer, stress test, Monte Carlo, gercek model training, model fit/predict/inference, dataset materialization, target/label/prediction uretimi, gercek performans garantisi, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanimi veya gercek provider API cagrisi degildir.

## Realism Summary
- **Total Assumptions**: None
- **All Enforced**: None
- **Naive Backtest Prevented**: True

## Assumptions Table

| model_name | description | formula_placeholder | is_placeholder | execution_allowed | is_active | non_signal |
| --- | --- | --- | --- | --- | --- | --- |
| square_root_market_impact_placeholder | Emir boyutunun gunluk hacme oraninin karekoku ile olceklenen standart piyasa etki kurali. | Y * sigma * sqrt(order_size / ADV) | True | False | True | True |
| linear_temporary_impact_placeholder | Islem aninda piyasayi gecici olarak iten dogrusal etki modeli. | eta * (order_size / bar_volume) | True | False | True | True |

