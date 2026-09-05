# Phase 128: Candidate State Schema Report

> [!WARNING]
> **YASAL UYARI VE NON-SIGNAL PREP BEYANI**
> Bu çıktı Phase 128 Regime Rule-Free Labeling Contracts and Unsupervised Prep raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, candidate state veya pseudo-state değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, unsupervised execution, dimensionality reduction execution, prediction/target/label üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Schema Summary
- **Total Fields**: `12`
- **Mandatory Fields**: `12`
- **All Non-Signal**: `True`
- **All Not Target/Prediction**: `True`
- **Forbidden Terms Guarded**: `True`

## Schema Definitions
| column_name | data_type | description | is_mandatory | forbidden_terms_checked | is_target_or_prediction | is_signal | non_signal | current_phase | next_phase | target_final_phase |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| candidate_state_key | string | Canonical unique identifier for candidate state record | True | True | False | False | True | 128 | 129 | 160 |
| entity_type | string | Entity type e.g. commodity, fx | True | True | False | False | True | 128 | 129 | 160 |
| entity_id | string | Entity identifier e.g. BRENT, USDTRY | True | True | False | False | True | 128 | 129 | 160 |
| timestamp_utc | datetime64[ns, UTC] | Point-in-time timestamp in UTC | True | True | False | False | True | 128 | 129 | 160 |
| candidate_state_family | string | Candidate state family classification | True | True | False | False | True | 128 | 129 | 160 |
| candidate_state_context | string | Contextual research annotation | True | True | False | False | True | 128 | 129 | 160 |
| source_matrix_ref | string | Reference to Phase 127 regime feature matrix | True | True | False | False | True | 128 | 129 | 160 |
| assignment_policy_ref | string | Reference to assignment policy specification | True | True | False | False | True | 128 | 129 | 160 |
| validation_status_ref | string | Reference to validation gate check | True | True | False | False | True | 128 | 129 | 160 |
| quality_status_ref | string | Reference to quality and drift metrics | True | True | False | False | True | 128 | 129 | 160 |
| manual_review_required | boolean | Flag indicating human researcher review is required | True | True | False | False | True | 128 | 129 | 160 |
| non_signal | boolean | Mandatory invariant certifying record is not a trading signal | True | True | False | False | True | 128 | 129 | 160 |

