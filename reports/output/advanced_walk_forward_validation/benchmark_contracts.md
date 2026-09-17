# Phase 147: Out-of-Sample Benchmark Contracts

> [!IMPORTANT]
> Bu çıktı Phase 147 Walk-Forward Validation and Out-of-Sample Benchmarking raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, walk-forward/readiness/OOS/benchmark değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek walk-forward execution, benchmark execution, optimizer, stress test, Monte Carlo, gerçek model training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek performans garantisi, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

## Summary
- **Total Benchmarks**: `7`
- **All Execution Blocked**: `True`
- **Zero Investment Advice**: `True`

## Benchmark Contracts
| benchmark_name | benchmark_type | description | universe_ref | baseline_strategy_ref | rebalance_policy | transaction_cost_aware | slippage_aware | benchmark_executed | metric_calculated | investment_advice_allowed | non_signal | manual_review_required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| naive_no_trade_baseline_contract | NO_TRADE_ZERO_RETURN | Hicbir pozisyon acilmayan, sifir getiri ve sifir islem maliyeti iceren temel referans sozlesmesi. | single_asset_universe | naive_no_trade_baseline | NONE | True | True | False | False | False | True | True |
| cash_baseline_contract | RISK_FREE_CASH | Portfoyun nakit veya risksiz faizde tutuldugu getiri referans sozlesmesi. | cash_risk_free_rate | cash_benchmark_placeholder | DAILY_ACCRUAL | True | False | False | False | False | True | True |
| buy_and_hold_placeholder_contract | PASSIVE_BUY_HOLD | Varlik donem basinda alinarak donem sonuna kadar tutulan klasik Buy & Hold referans sozlesmesi. | single_asset_universe | buy_and_hold_benchmark_placeholder | BUY_ONCE | True | True | False | False | False | True | True |
| equal_weight_placeholder_contract | MULTI_ASSET_EQUAL_WEIGHT | Sepetteki tum emtia ve doviz paritelerine esit agirlik veren 1/N portfoy referans sozlesmesi. | multi_asset_commodity_forex_universe | equal_weight_benchmark_placeholder | MONTHLY_REBALANCE | True | True | False | False | False | True | True |
| regime_aware_baseline_placeholder_contract | REGIME_CONDITIONED_BASELINE | Yuksek volatilite donemlerinde nakde gecen, sakin donemlerde Buy & Hold uygulayan rejim tabanli referans. | regime_conditioned_universe | regime_benchmark_placeholder | ON_REGIME_CHANGE | True | True | False | False | False | True | True |
| cost_aware_baseline_placeholder_contract | COST_AWARE_BASELINE | Islem komisyonu ve kayma maliyetlerini net olarak hesaba katan maliyet duyarli benchmark sozlesmesi. | cost_aware_universe | cost_aware_benchmark_placeholder | PERIODIC | True | True | False | False | False | True | True |
| random_policy_baseline_placeholder_contract | RANDOM_ENTRY_EXIT | Sans faktoru ve sans eseri basariyi test etmek amaciyla rastgele sinyal ureten referans yer tutucu sozlesme. | single_asset_universe | random_policy_baseline | RANDOM | True | True | False | False | False | True | True |

