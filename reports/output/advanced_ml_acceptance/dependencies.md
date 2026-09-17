# Phase 145: Advanced ML Dependency Acceptance Report

> **Yasal Uyarı:** Bu çıktı Phase 145 Advanced ML Acceptance Report çıktısıdır. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, acceptance/readiness/governance değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek model training, model fit/predict/inference, probability prediction, calibration/uncertainty execution, drift calculation, explainability calculation, backtest/walk-forward/benchmark/transaction-cost/slippage execution, model deployment, production deployment, model registry write, model artifact persistence, official approval, production approval, broker-ready approval, live-trading approval, gerçek audit log, dataset materialization, target/label/prediction üretimi, gerçek metric/performance claim, strateji üretimi, optimizer, clustering, ensemble execution, sentiment model output, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı, scraping veya gerçek provider API çağrısı değildir.

- **Total Dependencies:** `14`
- **Satisfied Dependencies:** `14`
- **All Satisfied:** `True`
- **Status:** `READY`

## Dependency Ledger
| dep_id | name | type | phase_ref | satisfied | details | current_phase | target_final_phase | next_phase | status | non_signal | production_ready | broker_ready |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DEP-01 | data_lake | storage_layer | Core | True | DataLake persistence methods available. | 145 | 160 | 146 | acceptance_ready | True | False | False |
| DEP-02 | feature_store | feature_registry | Core | True | FeatureStore metadata loaders available. | 145 | 160 | 146 | acceptance_ready | True | False | False |
| DEP-03 | config_settings | configuration | Core | True | Phase 145 settings configured with strict guards. | 145 | 160 | 146 | acceptance_ready | True | False | False |
| DEP-04 | config_paths | filesystem_paths | Core | True | Phase 145 directories registered. | 145 | 160 | 146 | acceptance_ready | True | False | False |
| DEP-05 | report_builder | reporting_layer | Core | True | Report builder generators with disclaimer ready. | 145 | 160 | 146 | acceptance_ready | True | False | False |
| DEP-06 | phase_136_gpu_ml_runtime | ml_block_foundation | Phase 136 | True | Hardware discovery and runtime contracts verified. | 145 | 160 | 146 | acceptance_ready | True | False | False |
| DEP-07 | phase_137_dataset_registry | dataset_contracts | Phase 137 | True | ML dataset schemas and experiment contracts verified. | 145 | 160 | 146 | acceptance_ready | True | False | False |
| DEP-08 | phase_138_baseline_models | model_contracts | Phase 138 | True | Baseline model family contracts verified. | 145 | 160 | 146 | acceptance_ready | True | False | False |
| DEP-09 | phase_139_training_governance | resource_governance | Phase 139 | True | Resource budget and timeout contracts verified. | 145 | 160 | 146 | acceptance_ready | True | False | False |
| DEP-10 | phase_140_ensemble_registry | ensemble_contracts | Phase 140 | True | Candidate registry and strategy contracts verified. | 145 | 160 | 146 | acceptance_ready | True | False | False |
| DEP-11 | phase_141_calibration_uncertainty | calibration_contracts | Phase 141 | True | Calibration and interval contracts verified. | 145 | 160 | 146 | acceptance_ready | True | False | False |
| DEP-12 | phase_142_drift_monitoring | drift_contracts | Phase 142 | True | Model drift linkage contracts verified. | 145 | 160 | 146 | acceptance_ready | True | False | False |
| DEP-13 | phase_143_explainability | attribution_contracts | Phase 143 | True | Explainability schemas verified. | 145 | 160 | 146 | acceptance_ready | True | False | False |
| DEP-14 | phase_144_model_governance | governance_contracts | Phase 144 | True | Model cards and audit placeholders verified. | 145 | 160 | 146 | acceptance_ready | True | False | False |
