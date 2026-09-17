# Phase 147: Out-of-Sample Split Contracts

> [!IMPORTANT]
> Bu çıktı Phase 147 Walk-Forward Validation and Out-of-Sample Benchmarking raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, walk-forward/readiness/OOS/benchmark değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek walk-forward execution, benchmark execution, optimizer, stress test, Monte Carlo, gerçek model training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek performans garantisi, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

## Summary
- **Total OOS Splits**: `3`
- **All Splits Isolated**: `True`
- **Zero Real Splits Executed**: `True`

## OOS Splits
| oos_split_name | oos_type | horizon_months | embargo_days | description | is_isolated | split_executed | targets_generated | non_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| primary_oos_contract_1y | FINAL_HOLDOUT | 12 | 14 | Son 1 yili (12 ay) tamamen dokunulmamis nihai OOS test seti olarak kilitleyen sozlesme. | True | False | False | True |
| rolling_oos_quarterly_contract | ROLLING_CHUNK | 3 | 7 | Her ceyrekte 3 aylik dilimlerle OOS test araliklari olusturan sozlesme. | True | False | False | True |
| stress_regime_oos_contract | REGIME_SPECIFIC_OOS | 6 | 21 | Ozellikle yuksek volatilite ve kriz donemlerini OOS olarak ayiran rejim odakli sozlesme. | True | False | False | True |

