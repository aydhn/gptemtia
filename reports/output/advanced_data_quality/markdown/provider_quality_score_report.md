# Provider Quality Score Report

> Bu çıktı Phase 112 Data Quality Engine raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, quality score’u trade sinyali olarak kullanma, provider official approval, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu veya destructive auto-cleaning değildir.

## Summary
- Total Providers Scored: 7
- Average Score: 0.83

> **Caution**: Quality score is strictly an internal research/diagnostic metric and NOT a trading signal or official certification.

## Provider Scores
| score_id | provider_name | dataset_type | score | status_label | critical_findings | high_findings | medium_findings | low_findings | manual_review_required | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pqs_fx_yahoo_finance_fixture_dataset_fx_ohlcv | fx_yahoo_finance_fixture | dataset_fx_ohlcv | 0.69 | quality_pass_with_warnings | 0 | 3 | 0 | 1 | True | İç kalite değerlendirmesidir; resmi sağlayıcı onayı veya benchmark değildir. |
| pqs_commodity_cbot_fixture_dataset_commodity_ohlcv | commodity_cbot_fixture | dataset_commodity_ohlcv | 1.0 | quality_pass | 0 | 0 | 1 | 0 | False | İç kalite değerlendirmesidir; resmi sağlayıcı onayı veya benchmark değildir. |
| pqs_macro_worldbank_fixture_dataset_macro_timeseries | macro_worldbank_fixture | dataset_macro_timeseries | 1.0 | quality_pass | 0 | 0 | 0 | 0 | False | İç kalite değerlendirmesidir; resmi sağlayıcı onayı veya benchmark değildir. |
| pqs_calendar_trading_economics_fixture_dataset_calendar_event | calendar_trading_economics_fixture | dataset_calendar_event | 1.0 | quality_pass | 0 | 0 | 0 | 0 | False | İç kalite değerlendirmesidir; resmi sağlayıcı onayı veya benchmark değildir. |
| pqs_news_reuters_fixture_dataset_news_metadata | news_reuters_fixture | dataset_news_metadata | 0.3 | quality_fail | 2 | 0 | 0 | 0 | True | İç kalite değerlendirmesidir; resmi sağlayıcı onayı veya benchmark değildir. |
| pqs_fx_yahoo_finance_fixture_dataset_fx_quote | fx_yahoo_finance_fixture | dataset_fx_quote | 0.85 | quality_pass | 0 | 3 | 0 | 1 | True | İç kalite değerlendirmesidir; resmi sağlayıcı onayı veya benchmark değildir. |
| pqs_commodity_cbot_fixture_dataset_commodity_spot | commodity_cbot_fixture | dataset_commodity_spot | 0.95 | quality_pass | 0 | 0 | 1 | 0 | False | İç kalite değerlendirmesidir; resmi sağlayıcı onayı veya benchmark değildir. |
