# Phase 123: Feature Missingness Diagnostics Report

> **UYARI VE BİLGİLENDİRME:** Bu çıktı Phase 123 Feature Quality and Drift Diagnostics raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, quality/drift score’u trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, production-ready/official approval iddiası, otomatik feature silme/düzeltme, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

- **Total Features Evaluated:** 6
- **Critical Missingness (>50%):** 0
- **Warning Missingness (>25%):** 0
- **Clean Features:** 6
- **Max Missingness Ratio:** 0.1
- **Status:** diagnostic_pass
- **Manual Review Required:** False

## Feature Column Missingness Details
| column | total_rows | missing_count | missing_ratio | status | severity | manual_review_required |
| --- | --- | --- | --- | --- | --- | --- |
| feat_rsi_14 | 100 | 0 | 0.0 | diagnostic_pass | quality_info | False |
| feat_macd_line | 100 | 0 | 0.0 | diagnostic_pass | quality_info | False |
| feat_bb_upper_20 | 100 | 0 | 0.0 | diagnostic_pass | quality_info | False |
| feat_atr_14 | 100 | 0 | 0.0 | diagnostic_pass | quality_info | False |
| feat_volatility_parkinson_20 | 100 | 0 | 0.0 | diagnostic_pass | quality_info | False |
| feat_macro_cpi_surprise | 100 | 10 | 0.1 | diagnostic_pass | quality_info | False |