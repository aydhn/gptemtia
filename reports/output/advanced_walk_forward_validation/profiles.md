# Phase 147: Walk-Forward Validation Profiles Report

> [!IMPORTANT]
> Bu çıktı Phase 147 Walk-Forward Validation and Out-of-Sample Benchmarking raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, walk-forward/readiness/OOS/benchmark değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek walk-forward execution, benchmark execution, optimizer, stress test, Monte Carlo, gerçek model training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek performans garantisi, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

## Summary
- **Active Profile**: `balanced_local_walk_forward_validation_contracts`
- **Total Profiles**: `3`
- **Current Phase**: `147`
- **Target Final Phase**: `160`
- **Next Phase**: `148`
- **Local Only**: `True`
- **Zero Live Trading**: `True`

## Configured Profiles
| profile_name | description | current_phase | target_final_phase | next_phase | dry_run_default | local_only | non_production | research_only | min_readiness_score | allow_live_trading | allow_broker_integration | allow_optimizer_execution | allow_walk_forward_execution | allow_benchmark_execution | allow_model_training | allow_prediction_generation | allow_performance_claim | is_active | non_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| balanced_local_walk_forward_validation_contracts | Dengeli yerel walk-forward dogrulama, OOS bolumleme ve benchmark sozlesmeleri profili. | 147 | 160 | 148 | True | True | True | True | 0.5 | False | False | False | False | False | False | False | False | True | True |
| strict_safety_walk_forward_contracts | Siki guvenlik, sifir canli islem, sifir broker, sifir lookahead ve genisletilmis purge/embargo profili. | 147 | 160 | 148 | True | True | True | True | 0.65 | False | False | False | False | False | False | False | False | False | True |
| dry_run_oos_benchmark_contracts | Dry-run odakli, benchmark universe/baseline karsilastirma ve Phase 148 handoff hazirlik profili. | 147 | 160 | 148 | True | True | True | True | 0.45 | False | False | False | False | False | False | False | False | False | True |

