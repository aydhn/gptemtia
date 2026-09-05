# Phase 123: Feature Distribution Drift Report

> **UYARI VE BİLGİLENDİRME:** Bu çıktı Phase 123 Feature Quality and Drift Diagnostics raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, quality/drift score’u trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, production-ready/official approval iddiası, otomatik feature silme/düzeltme, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

- **Features Compared:** 5
- **Critical Drift:** 0
- **Warning Drift:** 0
- **Stable Features:** 5
- **Status:** diagnostic_pass
- **Manual Review Required:** False

## Distribution Drift Details (Baseline vs Current)
| column | baseline_rows | current_rows | mean_baseline | mean_current | mean_abs_delta | std_baseline | std_current | std_abs_delta | q25_delta | q50_delta | q75_delta | drift_status | severity | manual_review_required | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| feat_rsi_14 | 100 | 100 | -0.1038 | -0.0153 | 0.0967 | 0.9082 | 0.9235 | 0.0169 | 0.0506 | 0.1267 | 0.2208 | diagnostic_pass | drift_low | False | Distribution aligned with baseline |
| feat_macd_line | 100 | 100 | 0.0223 | 0.0241 | 0.0018 | 0.9537 | 1.0672 | 0.1191 | 0.1949 | 0.1261 | 0.1823 | diagnostic_pass | drift_low | False | Distribution aligned with baseline |
| feat_bb_upper_20 | 100 | 100 | 0.0649 | -0.0062 | 0.0689 | 1.0843 | 0.9747 | 0.101 | 0.0526 | 0.0249 | 0.0886 | diagnostic_pass | drift_low | False | Distribution aligned with baseline |
| feat_atr_14 | 100 | 100 | 0.1068 | 0.2286 | 0.1337 | 0.8841 | 0.9371 | 0.0599 | 0.0545 | 0.1168 | 0.3427 | diagnostic_pass | drift_low | False | Distribution aligned with baseline |
| feat_volatility_parkinson_20 | 100 | 100 | -0.056 | 0.0279 | 0.0824 | 1.0637 | 0.9687 | 0.0893 | 0.3203 | 0.1604 | 0.0079 | diagnostic_pass | drift_low | False | Distribution aligned with baseline |