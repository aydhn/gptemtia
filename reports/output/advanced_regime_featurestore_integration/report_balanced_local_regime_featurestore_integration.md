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

---
# Phase 134: Regime FeatureStore Contract Registry Report

> [!NOTE]
> **Yasal ve Operasyonel Sınır**: Bu çıktı Phase 134 Regime FeatureStore Integration raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, FeatureStore’daki rejim kaydını trade sinyali olarak kullanma, validation/store readiness değerini production-ready/official approval/broker-ready olarak sunma, strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target/label üretimi, sentiment model output, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

- **Total Contracts**: `10`
- **All Non-Signal Required**: `True`
- **All Source Preservation Required**: `True`
- **Production Ready**: `False`

## Canonical Contracts

| contract_name | store_entity_type | entity_keys | timestamp_field | namespace_policy_ref | schema_policy_ref | validation_acceptance_required | no_lookahead_acceptance_required | metadata_only_news_acceptance_required | source_preservation_required | non_signal_required | quality_dependency_required | lineage_required | manual_review_required | production_ready | broker_ready |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| regime_taxonomy_store_contract | store_entity_regime_taxonomy | ['taxonomy_id', 'family_id'] | timestamp_utc | regime_store_taxonomy_namespace | regime_taxonomy_schema_v1 | True | True | False | True | True | True | True | False | False | False |
| regime_matrix_store_contract | store_entity_regime_matrix | ['matrix_id', 'feature_set_id'] | timestamp_utc | regime_store_matrix_namespace | regime_matrix_schema_v1 | True | True | False | True | True | True | True | False | False | False |
| candidate_state_store_contract | store_entity_candidate_state | ['candidate_state_id', 'cluster_prep_id'] | timestamp_utc | regime_store_candidate_state_namespace | candidate_state_schema_v1 | True | True | False | True | True | True | True | False | False | False |
| pseudo_state_store_contract | store_entity_pseudo_state | ['pseudo_state_id', 'prep_label_id'] | timestamp_utc | regime_store_pseudo_state_namespace | pseudo_state_schema_v1 | True | True | False | True | True | True | True | False | False | False |
| transition_store_contract | store_entity_transition | ['transition_id', 'matrix_state_id'] | timestamp_utc | regime_store_transition_namespace | transition_schema_v1 | True | True | False | True | True | True | True | False | False | False |
| cross_asset_regime_context_store_contract | store_entity_cross_asset_context | ['cross_asset_id', 'pair_symbol'] | timestamp_utc | regime_store_cross_asset_namespace | cross_asset_schema_v1 | True | True | False | True | True | True | True | False | False | False |
| macro_event_news_context_store_contract | store_entity_macro_event_news_context | ['macro_context_id', 'event_id'] | timestamp_utc | regime_store_macro_news_namespace | macro_news_schema_v1 | True | True | True | True | True | True | True | False | False | False |
| regime_validation_acceptance_store_contract | store_entity_validation_acceptance | ['acceptance_id', 'gate_id'] | timestamp_utc | regime_store_validation_namespace | validation_acceptance_schema_v1 | True | True | True | True | True | True | True | False | False | False |
| regime_acceptance_manifest_store_contract | acceptance_manifest_entity | ['manifest_id'] | timestamp_utc | regime_store_manifest_namespace | manifest_schema_v1 | True | True | True | True | True | True | True | False | False | False |
| phase_135_handoff_store_contract | phase_135_handoff_entity | ['handoff_id', 'prerequisite_id'] | timestamp_utc | regime_store_handoff_namespace | handoff_schema_v1 | True | True | True | True | True | True | True | False | False | False |

---
# Phase 134: Regime FeatureStore Metadata Manifest Report

> [!NOTE]
> **Yasal ve Operasyonel Sınır**: Bu çıktı Phase 134 Regime FeatureStore Integration raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, FeatureStore’daki rejim kaydını trade sinyali olarak kullanma, validation/store readiness değerini production-ready/official approval/broker-ready olarak sunma, strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target/label üretimi, sentiment model output, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

- **Manifest Name**: `regime_featurestore_metadata_manifest`
- **Readiness Score**: `1.0`
- **Current Phase**: `134`
- **Next Phase**: `135`
- **Manifest Valid**: `True`

## Manifest Attributes

| manifest_name | generated_at_utc | current_phase | target_final_phase | next_phase | contract_count | catalog_count | accepted_reference_count | dependency_count | manual_review_count | readiness_score | manual_review_required | non_signal | source_preserved | official_approval | production_ready | broker_ready | contains_target_or_prediction | contains_trading_recommendation | contains_full_article_text | contains_article_body | contains_raw_content | contains_scraped_html | contains_embedding | contains_vector | sentiment_model_output | model_training_executed | model_fit_executed | model_predict_executed | clustering_executed | unsupervised_execution | destructive_action_allowed | auto_fix_allowed | auto_drop_allowed | active_profile | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| regime_featurestore_metadata_manifest | 2026-09-06T01:00:21.354079+00:00 | 134 | 160 | 135 | 10 | 8 | 21 | 12 | 0 | 1.0 | False | True | True | False | False | False | False | False | False | False | False | False | False | False | False | False | False | False | False | False | False | False | False | balanced_local_regime_featurestore_integration | regime_store_ready |

---
# Phase 134: Regime FeatureStore Validation Report

> [!NOTE]
> **Yasal ve Operasyonel Sınır**: Bu çıktı Phase 134 Regime FeatureStore Integration raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, FeatureStore’daki rejim kaydını trade sinyali olarak kullanma, validation/store readiness değerini production-ready/official approval/broker-ready olarak sunma, strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target/label üretimi, sentiment model output, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

- **Validation Status**: `regime_store_ready`
- **Total Checks**: `6`
- **Failed Checks**: `0`
- **Non-Signal Invariant Maintained**: `True`

## Validation Items

| check_name | passed | error_count | errors | non_signal |
| --- | --- | --- | --- | --- |
| profile_registry_validation | True | 0 | None | True |
| contract_registry_validation | True | 0 | None | True |
| schema_registry_validation | True | 0 | None | True |
| component_catalogs_validation | True | 0 | None | True |
| metadata_manifest_validation | True | 0 | None | True |
| forbidden_claims_validation | True | 0 | None | True |

---
# Phase 134 to Phase 135 Handoff Report

> [!NOTE]
> **Yasal ve Operasyonel Sınır**: Bu çıktı Phase 134 Regime FeatureStore Integration raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, FeatureStore’daki rejim kaydını trade sinyali olarak kullanma, validation/store readiness değerini production-ready/official approval/broker-ready olarak sunma, strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target/label üretimi, sentiment model output, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

- **Handoff Target**: `Phase 135: Regime Classification Acceptance Report`
- **Handoff Status**: `READY`
- **Prerequisites Count**: `14`
- **All Prerequisites Satisfied**: `True`

## Handoff Prerequisites

| prerequisite_id | phase_origin | title | status | validation_status | non_signal | description |
| --- | --- | --- | --- | --- | --- | --- |
| prereq_p126_taxonomy_catalog | 126 | Regime Taxonomy Catalog & Specification | READY | ACCEPTED | True | 4 canonical regime families integrated into FeatureStore catalog. |
| prereq_p127_matrix_contracts | 127 | Regime Feature Matrix & State Dataset Contracts | READY | ACCEPTED | True | Daily/weekly/hourly aligned matrix contracts cataloged without forward return fields. |
| prereq_p128_candidate_pseudo_states | 128 | Candidate States & Pseudo-State Labeling Contracts | READY | ACCEPTED | True | Unsupervised candidate feature sets and non-directional pseudo-state contracts verified. |
| prereq_p129_behavior_diagnostics | 129 | Market Behavior Diagnostics & Quality Scores | READY | ACCEPTED | True | Behavioral diagnostics and cluster quality metrics satisfied. |
| prereq_p130_transition_stability | 130 | Regime Transition & Stability Analysis Catalogs | READY | ACCEPTED | True | Transition frequency matrices and persistence scores stored without signal implications. |
| prereq_p131_cross_asset_context | 131 | Cross-Asset Regime Alignment & Divergence Context | READY | ACCEPTED | True | Multi-market alignment and divergence context registered in FeatureStore. |
| prereq_p132_macro_event_news | 132 | Macro, Event, and News Metadata Context | READY | ACCEPTED | True | Economic releases and calendar events cataloged with strict metadata-only news purity. |
| prereq_p133_validation_acceptance | 133 | Regime Validation & No-Lookahead Acceptance Gates | READY | ACCEPTED | True | 19 canonical acceptance gates verified with 1.0 acceptance score. |
| prereq_p134_featurestore_integration | 134 | Regime FeatureStore Integration & Read/Write/Query Contracts | READY | ACCEPTED | True | FeatureStore contracts, namespaces, schemas, and catalogs established. |
| prereq_no_lookahead_references | 134 | No-Lookahead Accepted References | READY | ACCEPTED | True | Backward-asof temporal integrity verified for all store entries. |
| prereq_metadata_only_news_references | 134 | Metadata-Only News Accepted References | READY | ACCEPTED | True | Full text, HTML, and sentiment model outputs verified absent. |
| prereq_source_preservation_references | 134 | Source Preservation Accepted References | READY | ACCEPTED | True | Zero source file overwrites, deletions, or destructive mutations guaranteed. |
| prereq_manual_review_blocker_audit | 134 | Manual Review Blocker Audit Ledger | READY | ACCEPTED | True | Zero active blockers preventing Phase 135 acceptance report generation. |
| prereq_non_signal_boundary_affirmation | 134 | Non-Signal Invariant Affirmation for Phase 135 | READY | ACCEPTED | True | Phase 135 closes the regime block acceptance; it does not produce trade signals. |
