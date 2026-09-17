# Phase 146: Transaction Cost Models Report

> **YASAL UYARI VE GUCLENDIRILMIS GUVENLIK SINIRI (PHASE 146)**:
> Bu cikti Phase 146 Realistic Backtest, Transaction Cost and Slippage Modeling raporudur. Canli emir, broker talimati, kesin AL/SAT, yatirim tavsiyesi, backtest/readiness/cost/slippage degerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gercek backtest execution, walk-forward, benchmark, optimizer, stress test, Monte Carlo, gercek model training, model fit/predict/inference, dataset materialization, target/label/prediction uretimi, gercek performans garantisi, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanimi veya gercek provider API cagrisi degildir.

## Cost Models Summary
- **Total Cost Models**: 3
- **Real Calculation Blocked**: True

## Cost Models Table

| cost_model_name | description | aggregation_formula | real_cost_calculated | broker_connected | execution_allowed | is_active | non_signal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| standard_realistic_cost_model | Komisyon, borsa ucreti, alis-satis farki ve kaymayi toplayan standart maliyet modeli. | commission + exchange_fee + spread_cost + slippage_cost | False | False | False | True | True |
| institutional_market_impact_cost_model | Standart maliyetlere ek olarak buyuk emirler icin piyasa etki maliyetini toplayan kurumsal model. | commission + fee + spread_cost + slippage_cost + market_impact | False | False | False | True | True |
| leveraged_holding_cost_model | Gunici maliyetlere ek olarak gecelik tasima ve borclanma maliyetlerini iceren sozlesme. | standard_cost + borrow_fee + funding_fee | False | False | False | True | True |

