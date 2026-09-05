# Phase 115: provider_domain_calendar Provider Benchmark Report
> **UYARI VE SINIRLAR**:
> Bu çıktı Phase 115 Data Provider Benchmark Report raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, benchmark score’u trade sinyali olarak kullanma, provider official approval, production-ready/broker-ready iddiası, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.

- **Domain**: provider_domain_calendar
- **Değerlendirilen Metrik Sayısı**: 6
- **Ortalama Domain Puanı**: 0.935

### Alan Bazlı Değerlendirme Tablosu
| record_id | provider_name | provider_domain | metric_label | raw_score | weighted_score | status_label | evidence_ref | limitation_note | manual_review_required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pb_rec::advanced_economic_calendar_engine::metric_coverage | advanced_economic_calendar_engine | provider_domain_calendar | metric_coverage | 0.92 | 0.1533 | benchmark_pass | Global tier-1 and tier-2 scheduled events (NFP, CPI, FOMC, ECB, CBRT) | Calendar benchmark is diagnostic research only; does not provide trading signals | False |
| pb_rec::advanced_economic_calendar_engine::metric_capability | advanced_economic_calendar_engine | provider_domain_calendar | metric_capability | 0.89 | 0.1483 | benchmark_pass | Scheduled vs actual timestamp precision, consensus/prior comparison | Calendar benchmark is diagnostic research only; does not provide trading signals | False |
| pb_rec::advanced_economic_calendar_engine::metric_quality | advanced_economic_calendar_engine | provider_domain_calendar | metric_quality | 0.94 | 0.1567 | benchmark_pass | Consensus vs actual surprise precision and anomaly filtering from Phase 112 | Calendar benchmark is diagnostic research only; does not provide trading signals | False |
| pb_rec::advanced_economic_calendar_engine::metric_normalization | advanced_economic_calendar_engine | provider_domain_calendar | metric_normalization | 0.93 | 0.155 | benchmark_pass | Event classification taxonomy and country ISO codes from Phase 113 | Calendar benchmark is diagnostic research only; does not provide trading signals | False |
| pb_rec::advanced_economic_calendar_engine::metric_traceability | advanced_economic_calendar_engine | provider_domain_calendar | metric_traceability | 0.93 | 0.155 | benchmark_pass | Scheduled release event lineage and update audit trail from Phase 114 | Calendar benchmark is diagnostic research only; does not provide trading signals | False |
| pb_rec::advanced_economic_calendar_engine::metric_no_scraping_compliance | advanced_economic_calendar_engine | provider_domain_calendar | metric_no_scraping_compliance | 1.0 | 0.1667 | benchmark_pass | Strict offline fixtures; zero calendar website scraping | Calendar benchmark is diagnostic research only; does not provide trading signals | False |
