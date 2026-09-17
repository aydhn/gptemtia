# Phase 147: Validation and Bias Guards

> [!IMPORTANT]
> Bu çıktı Phase 147 Walk-Forward Validation and Out-of-Sample Benchmarking raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, walk-forward/readiness/OOS/benchmark değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek walk-forward execution, benchmark execution, optimizer, stress test, Monte Carlo, gerçek model training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek performans garantisi, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

## Summary
- **Total Guards**: `2`
- **Strict Enforcement**: `True`
- **All Active**: `True`

## Guards
| guard_name | guard_type | description | enforcement_level | active | non_signal |
| --- | --- | --- | --- | --- | --- |
| column_name_lookahead_guard | NO_LOOKAHEAD | Kolon isimlerinde gelecege yonelik getiri veya etiket tespit edici muhafiz. | STRICT | True | True |
| asof_backward_join_guard | TIME_ALIGNMENT | Veri seti birlestirmelerinde geriye donuk asof kurali zorlayan muhafiz. | STRICT | True | True |

