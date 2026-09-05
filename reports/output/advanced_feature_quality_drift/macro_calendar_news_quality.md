# Phase 123: Macro, Calendar, News & Cross-Asset Quality Report

> **UYARI VE BİLGİLENDİRME:** Bu çıktı Phase 123 Feature Quality and Drift Diagnostics raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, quality/drift score’u trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, production-ready/official approval iddiası, otomatik feature silme/düzeltme, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

- **Total Checks:** 5
- **Passed Checks:** 5
- **Failed Checks:** 0
- **Metadata-Only Boundary Compliant:** True
- **Status:** diagnostic_pass

## Diagnostic Checks Breakdown
| check_id | domain | description | passed | severity | status | manual_review_required | notes | non_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| macro_release_timestamp_quality | macro_calendar_news_quality_domain | Verify macro release timestamps are monotonically ordered and timezone-aware. | True | quality_info | diagnostic_pass | False | Boundary checks satisfied | True |
| calendar_timestamp_completeness | macro_calendar_news_quality_domain | Check scheduled vs actual event release timestamp completeness. | True | quality_info | diagnostic_pass | False | Boundary checks satisfied | True |
| release_lag_metadata_availability | macro_calendar_news_quality_domain | Ensure release lag features are explicitly calculated and non-negative. | True | quality_info | diagnostic_pass | False | Boundary checks satisfied | True |
| news_metadata_only_boundary | macro_calendar_news_quality_domain | Enforce strict prohibition on full-text, scraped HTML, and vector embeddings in feature matrix. | True | quality_info | diagnostic_pass | False | Boundary checks satisfied | True |
| news_tag_topic_event_completeness | macro_calendar_news_quality_domain | Validate taxonomy completeness of news topic tags and event links. | True | quality_info | diagnostic_pass | False | Boundary checks satisfied | True |