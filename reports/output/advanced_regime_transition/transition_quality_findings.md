# Phase 130: Transition Quality Findings & Review Report

> [!IMPORTANT]
> Bu çıktı Phase 130 Regime Transition and Stability Analysis raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, transition veya stability değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, unsupervised execution, dimensionality reduction execution, prediction/target/label üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

- **Total Findings**: 2
- **Manual Review Required**: 2
- **Auto-Fixing Prohibited**: True
- **Zero Destructive Cleaning**: True

## Finding Registry
| finding_id | finding_type | transition_family | severity_label | message | recommendation | manual_review_required | destructive_action_allowed | auto_fix_allowed | auto_drop_allowed | non_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FIND-130-001 | transition_ambiguity_warning | trend_range | transition_medium | Elevated transition ambiguity observed during range boundary transition rehearsal | Perform manual review of candidate state thresholds without automated modification | True | False | False | False | True |
| FIND-130-002 | transition_continuity_warning | commodity_energy | transition_low | Minor weekend session gap noted in commodity sequence timestamps | Confirm calendar alignment contract covers exchange holiday sessions | True | False | False | False | True |


---

# Phase 130: Transition Stability Scoring Report

> [!IMPORTANT]
> Bu çıktı Phase 130 Regime Transition and Stability Analysis raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, transition veya stability değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, unsupervised execution, dimensionality reduction execution, prediction/target/label üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

- **Stability Score**: 0.82
- **Classification**: high_stability
- **Non-Signal Certified**: True
- **Zero Production / Broker Approval**: True

## Score Summary Table
| profile_name | stability_score | classification | finding_count | manual_review_count | non_signal | source_preserved | official_approval | production_ready | broker_ready |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| balanced_local_regime_transition | 0.82 | high_stability | 2 | 2 | True | True | False | False | False |
