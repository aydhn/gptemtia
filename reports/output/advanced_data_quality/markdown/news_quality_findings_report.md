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
| find_rule_news_forbidden_body_dataset_news_metadata_full_text | rule_news_metadata_quality_news_copyright_safe_boundary | finding_news_copyright_boundary | dataset_news_metadata | news_reuters_fixture | full_text | quality_critical | quality_fail | Forbidden full article / scraped body field 'full_text' detected in news dataset! | Immediately remove raw article body; only metadata and references are permitted. | Phase 113 | True |
| find_rule_copyright_forbidden_col_dataset_news_metadata_full_text | rule_news_copyright_quality_no_full_text_storage | finding_news_copyright_boundary | dataset_news_metadata | news_reuters_fixture | full_text | quality_critical | quality_fail | CRITICAL COPYRIGHT BREACH: Column 'full_text' contains scraped full text or raw HTML. | Remove raw body content immediately. Only store headline/summary metadata references. | Phase 113 | True |
