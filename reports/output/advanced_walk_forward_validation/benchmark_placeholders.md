# Phase 147: Benchmark Placeholders Report

> [!IMPORTANT]
> Bu çıktı Phase 147 Walk-Forward Validation and Out-of-Sample Benchmarking raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, walk-forward/readiness/OOS/benchmark değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek walk-forward execution, benchmark execution, optimizer, stress test, Monte Carlo, gerçek model training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek performans garantisi, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

## Summary
- **Placeholders Registered**: `2`
- **Real Execution Disabled**: `True`
- **Non-Signal**: `True`

## Placeholders
| placeholder_name | baseline_type | formula_spec | description | execution_allowed | trade_recommendation | real_result_generated | non_signal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| buy_and_hold_single_asset_placeholder | BUY_AND_HOLD | R_bnh(t) = (P(t) - P(0)) / P(0) - TotalCost(entry, exit) | Varligin t0 aninda alinarak tn anina kadar tasindigi pasif referans yer tutucusu. | False | False | False | True |
| buy_and_hold_reinvested_placeholder | BUY_AND_HOLD_REINVESTED | R_bnh_div(t) = Product(1 + r_daily) - 1 | Temettu veya tasima maliyetinin eklenip cikarildigi bilesik pasif getiri yer tutucusu. | False | False | False | True |

