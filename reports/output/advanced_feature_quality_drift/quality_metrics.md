# Phase 123: Feature Quality Metric Registry

> **UYARI VE BİLGİLENDİRME:** Bu çıktı Phase 123 Feature Quality and Drift Diagnostics raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, quality/drift score’u trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, production-ready/official approval iddiası, otomatik feature silme/düzeltme, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

- **Active Profile:** balanced_local_feature_quality_drift
- **Total Quality Metrics:** 9
- **Current Phase:** 123

## Registered Quality Metrics
| metric_id | metric_name | domain | description | metric_type | severity | default_warning_threshold | default_critical_threshold | non_signal | destructive_action_allowed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| missingness_ratio | Missingness Ratio | missingness_domain | Proportion of missing (NaN/None) values in feature column. | ratio | quality_medium | 0.25 | 0.5 | True | False |
| infinite_value_ratio | Infinite Value Ratio | infinite_value_domain | Proportion of infinite (+/-inf) values in feature column. | ratio | quality_critical | 0.0 | 0.0 | True | False |
| all_nan_flag | All-NaN Flag | all_nan_domain | Flag indicating column contains exclusively NaN values. | flag | quality_critical | 0.0 | 1.0 | True | False |
| zero_variance_flag | Zero Variance Flag | zero_variance_domain | Flag indicating column standard deviation is zero (constant value). | flag | quality_high | 1.0 | 1.0 | True | False |
| duplicate_value_ratio | Duplicate Value Ratio | duplicate_value_domain | Ratio of modal repeated value frequency to total rows. | ratio | quality_medium | 0.9 | 0.99 | True | False |
| numeric_sanity_flag | Numeric Sanity Flag | quality_metric_domain | Flag indicating numeric types comply with expected dtype ranges. | flag | quality_high | 0.0 | 1.0 | True | False |
| namespace_validity_flag | Namespace Validity Flag | namespace_quality_domain | Flag indicating absence of forward-looking or forbidden name tokens. | flag | quality_critical | 0.0 | 1.0 | True | False |
| source_validation_status | Source Validation Status | quality_metric_domain | Status of upstream Phase 121 validation checks. | status | quality_high | 0.0 | 1.0 | True | False |
| manual_review_blocker_count | Manual Review Blocker Count | manual_review_domain | Number of critical issues requiring manual inspection. | count | quality_high | 1.0 | 5.0 | True | False |