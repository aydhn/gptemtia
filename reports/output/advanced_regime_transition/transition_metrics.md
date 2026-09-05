# Phase 130: Transition & Stability Metric Registry Report

> [!IMPORTANT]
> Bu çıktı Phase 130 Regime Transition and Stability Analysis raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, transition veya stability değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, unsupervised execution, dimensionality reduction execution, prediction/target/label üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

- **Total Metrics**: 9
- **All Non-Signal**: True
- **All Source Preserved**: True
- **Requires No-Lookahead**: True

## Metric Specifications
| metric_name | metric_family | description | formula_placeholder | expected_range | non_signal | source_preserved | requires_no_lookahead |
| --- | --- | --- | --- | --- | --- | --- | --- |
| transition_frequency_placeholder | transition_frequency | Rate of state transitions per unit time in sequence history | count(transitions) / total_valid_intervals | [0.0, 1.0] | True | True | True |
| transition_count_placeholder | transition_frequency | Total integer count of state changes observed in sequence | sum(state_t != state_{t-1}) | [0, inf) | True | True | True |
| transition_rate_placeholder | transition_rate | Normalized ratio of transition occurrences over sequence length | transition_count / sequence_length | [0.0, 1.0] | True | True | True |
| state_switch_ratio_placeholder | transition_rate | Frequency ratio of switching out of a specific candidate regime | exits_from_state_k / total_observations_in_state_k | [0.0, 1.0] | True | True | True |
| transition_ambiguity_score_placeholder | transition_ambiguity | Diagnostic metric measuring boundary uncertainty during transition points | 1.0 - abs(prob_candidate_1 - prob_candidate_2) | [0.0, 1.0] | True | True | True |
| transition_continuity_score_placeholder | transition_continuity | Continuity ratio measuring lack of missing timestamps during sequence | observed_timestamp_count / expected_timestamp_count | [0.0, 1.0] | True | True | True |
| transition_readiness_score | transition_readiness | Readiness indicator evaluating if candidate sequence is sufficiently clean for transition analysis | mean(coverage, consistency, 1 - ambiguity) | [0.0, 1.0] | True | True | True |
| timestamp_continuity_score | timestamp_policy | Integrity score verifying monotonic chronological order without negative time deltas | count(delta_t > 0) / count(delta_t) | [0.0, 1.0] | True | True | True |
| manual_review_blocker_count | governance | Count of open blockers requiring manual analyst inspection | sum(review_items_blocking) | [0, inf) | True | True | True |
