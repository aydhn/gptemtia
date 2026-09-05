# Phase 128: Unsupervised Preparation Contracts Report

> [!WARNING]
> **YASAL UYARI VE NON-SIGNAL PREP BEYANI**
> Bu çıktı Phase 128 Regime Rule-Free Labeling Contracts and Unsupervised Prep raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, candidate state veya pseudo-state değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, unsupervised execution, dimensionality reduction execution, prediction/target/label üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Prep Summary
- **Total Prep Contracts**: `6`
- **All Non-Signal**: `True`
- **No Model Training**: `True`
- **No Clustering**: `True`
- **Prep Status**: `VALID`

## Registered Prep Contracts
| contract_name | prep_category | description | fit_transform_allowed | model_training_allowed | clustering_allowed | dimensionality_reduction_allowed | no_lookahead_required | non_signal | status | current_phase | next_phase | target_final_phase |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| unsupervised_matrix_readiness_contract | matrix_readiness | Verifies that Phase 127 regime feature matrix satisfies completeness, schema, and alignment prerequisites. | False | False | False | False | True | True | rule_free_ready | 128 | 129 | 160 |
| candidate_state_feature_selection_placeholder_contract | feature_selection | Defines criteria for non-signal candidate feature subsetting for future clustering pipelines. | False | False | False | False | True | True | rule_free_ready | 128 | 129 | 160 |
| unsupervised_normalization_prep_contract | normalization_prep | Specifies scaling parameters (min-max, robust, z-score) required prior to distance computations. | False | False | False | False | True | True | rule_free_ready | 128 | 129 | 160 |
| unsupervised_distance_metric_prep_contract | metric_prep | Specifies geometry and metric requirements (Euclidean, Cosine, Correlation) for candidate state distances. | False | False | False | False | True | True | rule_free_ready | 128 | 129 | 160 |
| unsupervised_cluster_validation_prep_contract | cluster_validation_prep | Defines statistical validation placeholders (silhouette, Davies-Bouldin) for future cluster diagnostics. | False | False | False | False | True | True | rule_free_ready | 128 | 129 | 160 |
| unsupervised_manual_review_prep_contract | manual_review_prep | Specifies governance protocols for manual inspection of unsupervised partition boundaries. | False | False | False | False | True | True | rule_free_ready | 128 | 129 | 160 |

