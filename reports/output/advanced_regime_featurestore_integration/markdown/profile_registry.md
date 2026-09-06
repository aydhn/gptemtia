# Phase 134: Regime FeatureStore Profile Registry Report

> [!NOTE]
> **Yasal ve Operasyonel Sınır**: Bu çıktı Phase 134 Regime FeatureStore Integration raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, FeatureStore’daki rejim kaydını trade sinyali olarak kullanma, validation/store readiness değerini production-ready/official approval/broker-ready olarak sunma, strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target/label üretimi, sentiment model output, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

- **Active Profile**: `balanced_local_regime_featurestore_integration`
- **Total Profiles**: `3`
- **Current Phase**: `134`
- **Target Final Phase**: `160`
- **Status**: `regime_store_ready`

## Registered Profiles

| profile_name | description | current_phase | target_final_phase | next_phase | min_readiness_score | dry_run_default | local_only | non_production | research_only | non_signal | source_preserved | official_approval | production_ready | broker_ready | is_active | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| balanced_local_regime_featurestore_integration | Standard balanced local profile connecting Phase 126-133 regime outputs to FeatureStore metadata catalogs. | 134 | 160 | 135 | 0.45 | True | True | True | True | True | True | False | False | False | True | regime_store_ready |
| strict_non_signal_regime_featurestore_safety | Strict safety profile enforcing zero-signal claims, metadata-only news purity, and source preservation. | 134 | 160 | 135 | 0.6 | True | True | True | True | True | True | False | False | False | False | regime_store_ready |
| dry_run_regime_store_catalog_focus | Dry-run audit profile for contract validation, schema checks, and simulated catalog lookups. | 134 | 160 | 135 | 0.4 | True | True | True | True | True | True | False | False | False | False | regime_store_ready |
