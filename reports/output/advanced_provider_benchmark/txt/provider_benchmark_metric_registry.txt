# Phase 115: Provider Benchmark Metric Registry
> **UYARI VE SINIRLAR**:
> Bu çıktı Phase 115 Data Provider Benchmark Report raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, benchmark score’u trade sinyali olarak kullanma, provider official approval, production-ready/broker-ready iddiası, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.

- **Toplam Metrik Sayısı**: 11
- **Manuel İnceleme Gerektiren Metrik Sayısı**: 3

### Tanımlı Metrikler
| metric_id | metric_label | metric_name | description | score_direction | safe_usage_note | manual_review_required |
| --- | --- | --- | --- | --- | --- | --- |
| pb_metric::metric_coverage | metric_coverage | Asset and Universe Coverage | Breadth and depth of supported symbols, pairs, indicators, and events | higher_is_better | Diagnostic metric; does not certify completeness or live availability | False |
| pb_metric::metric_capability | metric_capability | Technical Capabilities | Presence of quote, OHLCV, tick, timestamp granularity, and metadata feeds | higher_is_better | Diagnostic metric; does not imply broker execution or latency guarantees | False |
| pb_metric::metric_quality | metric_quality | Data Quality Integrity | Absence of stale, missing, duplicate, or outlier anomalies from Phase 112 | higher_is_better | Diagnostic metric; historical quality does not guarantee future reliability | False |
| pb_metric::metric_normalization | metric_normalization | Schema & Normalization Adherence | Conformity to canonical schema, uppercase tokens, and UTC time from Phase 113 | higher_is_better | Diagnostic metric; normalization is non-destructive and source-preserving | False |
| pb_metric::metric_traceability | metric_traceability | Lineage and Traceability | Completeness of source-to-canonical transformation audit trail from Phase 114 | higher_is_better | Diagnostic metric; internal auditability evaluation only | False |
| pb_metric::metric_license_provenance | metric_license_provenance | License and Redistribution Boundary | Adherence to open research, offline usage, and non-commercial boundaries | higher_is_better | Requires manual review for proprietary vendor contracts | True |
| pb_metric::metric_no_scraping_compliance | metric_no_scraping_compliance | Strict No-Scraping Compliance | 100% adherence to zero web scraping, zero HTML parsing, zero bot automation | higher_is_better | Mandatory binary/fractional compliance filter; non-compliant providers rejected | False |
| pb_metric::metric_metadata_only_compliance | metric_metadata_only_compliance | Metadata-Only & Zero Full Text | Strict verification that no full article texts or copyrighted news bodies are gathered | higher_is_better | Mandatory for news metadata providers; protects against copyright infringement | False |
| pb_metric::metric_manual_review_load | metric_manual_review_load | Manual Review Burden | Volume of outstanding non-destructive manual review items required for safety | lower_is_better | High review load requires operational attention before feature ingestion | True |
| pb_metric::metric_cross_domain_consistency | metric_cross_domain_consistency | Cross-Domain Alignment | Consistency of cross-asset entity mappings (FX, commodities, macro, news tags) | higher_is_better | Diagnostic metric; cross-asset alignment supports multi-factor research | False |
| pb_metric::metric_unknown | metric_unknown | Unknown Metric Fallback | Fallback category for unclassified benchmark measurements | neutral | Fallback record only | True |
