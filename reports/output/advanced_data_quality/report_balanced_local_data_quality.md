# Quality Findings Registry Report

> Bu çıktı Phase 112 Data Quality Engine raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, quality score’u trade sinyali olarak kullanma, provider official approval, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu veya destructive auto-cleaning değildir.

## Summary
- Total Findings: 7
- Critical: 2
- High: 3
- Medium: 1
- Low: 1
- Info: 0

## Findings Table
| finding_id | rule_id | finding_type | dataset_type | provider_name | field_name | severity_label | status_label | message | recommendation | future_phase_owner | manual_review_required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| find_rule_fx_quote_inverted_dataset_fx_quote_bid_ask | rule_fx_quality_fx_spread_sanity | finding_quote_inconsistency | dataset_fx_quote | fx_yahoo_finance_fixture | bid | quality_high | quality_fail | Found 1 records with inverted quotes (bid > ask). | Quarantine or review inverted quotes in Manual Review Queue. | Phase 113 | True |
| find_rule_fx_volume_missing_dataset_fx_ohlcv_volume | rule_fx_quality_fx_ohlcv_integrity | finding_missing_value | dataset_fx_ohlcv | fx_yahoo_finance_fixture | volume | quality_low | quality_pass_with_warnings | Volume column is omitted in FX OHLCV data (tick volume may be substituted). | Document tick vs traded volume in Phase 114 Lineage. | Phase 114 | False |
| find_rule_fx_high_low_dataset_fx_ohlcv_high_low | rule_fx_quality_fx_ohlcv_integrity | finding_ohlc_inconsistency | dataset_fx_ohlcv | fx_yahoo_finance_fixture | high | quality_high | quality_fail | Found 1 bars where high < low. | Flag invalid bars for review; do not auto-clean destructively. | Phase 113 | True |
| find_rule_fx_open_close_bounds_dataset_fx_ohlcv_bounds | rule_fx_quality_fx_ohlcv_integrity | finding_ohlc_inconsistency | dataset_fx_ohlcv | fx_yahoo_finance_fixture | close | quality_high | quality_fail | Found 1 bars where open or close is outside [low, high]. | Review corrupted bars in Manual Review Queue. | Phase 113 | True |
| find_rule_comm_spot_negative_dataset_commodity_spot_spot_price | rule_commodity_quality_commodity_spot_sanity | finding_ohlc_inconsistency | dataset_commodity_spot | commodity_cbot_fixture | spot_price | quality_medium | quality_pass_with_warnings | Detected 1 records with negative spot prices. | Verify historical context (e.g. WTI 2020) in Phase 113 Normalization. | Phase 113 | True |
| find_rule_news_forbidden_body_dataset_news_metadata_full_text | rule_news_metadata_quality_news_copyright_safe_boundary | finding_news_copyright_boundary | dataset_news_metadata | news_reuters_fixture | full_text | quality_critical | quality_fail | Forbidden full article / scraped body field 'full_text' detected in news dataset! | Immediately remove raw article body; only metadata and references are permitted. | Phase 113 | True |
| find_rule_copyright_forbidden_col_dataset_news_metadata_full_text | rule_news_copyright_quality_no_full_text_storage | finding_news_copyright_boundary | dataset_news_metadata | news_reuters_fixture | full_text | quality_critical | quality_fail | CRITICAL COPYRIGHT BREACH: Column 'full_text' contains scraped full text or raw HTML. | Remove raw body content immediately. Only store headline/summary metadata references. | Phase 113 | True |
