# Phase 123: Feature Drift Metric Registry

> **UYARI VE BİLGİLENDİRME:** Bu çıktı Phase 123 Feature Quality and Drift Diagnostics raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, quality/drift score’u trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, production-ready/official approval iddiası, otomatik feature silme/düzeltme, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

- **Active Profile:** balanced_local_feature_quality_drift
- **Total Drift Metrics:** 10
- **Current Phase:** 123

## Registered Drift Metrics
| metric_id | metric_name | domain | description | drift_type | severity | default_warning_threshold | default_critical_threshold | non_signal | destructive_action_allowed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| distribution_mean_shift | Distribution Mean Shift | distribution_drift_domain | Absolute delta between baseline and current window sample means. | central_tendency | drift_medium | 0.5 | 1.0 | True | False |
| distribution_std_shift | Distribution Std Shift | distribution_drift_domain | Absolute delta between baseline and current window standard deviations. | dispersion | drift_medium | 0.5 | 1.0 | True | False |
| quantile_shift | Quantile Shift | distribution_drift_domain | Composite absolute shift across 25th, 50th, and 75th percentiles. | shape | drift_medium | 0.6 | 1.2 | True | False |
| missingness_shift | Missingness Shift | missingness_domain | Increase in missingness ratio compared to baseline window. | data_integrity | drift_high | 0.15 | 0.3 | True | False |
| zero_variance_new_flag | New Zero Variance Flag | zero_variance_domain | Flag indicating feature became constant in current window while non-constant in baseline. | collapse | drift_critical | 1.0 | 1.0 | True | False |
| stability_score | Rolling Stability Score | rolling_stability_domain | Normalized stability score over rolling observation windows. | stability | drift_low | 0.6 | 0.4 | True | False |
| rolling_mean_stability | Rolling Mean Stability | rolling_stability_domain | Coefficient of variation of rolling means. | stability | drift_medium | 0.4 | 0.8 | True | False |
| rolling_std_stability | Rolling Std Stability | rolling_stability_domain | Coefficient of variation of rolling standard deviations. | stability | drift_medium | 0.4 | 0.8 | True | False |
| population_shift_placeholder | Population Shift Placeholder | distribution_drift_domain | Placeholder for multivariate covariate shift diagnostics. | multivariate | drift_info | 0.5 | 1.0 | True | False |
| factor_family_drift_placeholder | Factor Family Drift Placeholder | factor_drift_domain | Placeholder for factor family aggregate distribution drift. | factor_level | drift_info | 0.5 | 1.0 | True | False |