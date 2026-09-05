# Phase 115: provider_domain_commodity Provider Benchmark Report
> **UYARI VE SINIRLAR**:
> Bu çıktı Phase 115 Data Provider Benchmark Report raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, benchmark score’u trade sinyali olarak kullanma, provider official approval, production-ready/broker-ready iddiası, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.

- **Domain**: provider_domain_commodity
- **Değerlendirilen Metrik Sayısı**: 6
- **Ortalama Domain Puanı**: 0.9233

### Alan Bazlı Değerlendirme Tablosu
| record_id | provider_name | provider_domain | metric_label | raw_score | weighted_score | status_label | evidence_ref | limitation_note | manual_review_required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pb_rec::advanced_commodity_providers_engine::metric_coverage | advanced_commodity_providers_engine | provider_domain_commodity | metric_coverage | 0.9 | 0.15 | benchmark_pass | Spot and futures for Gold, Silver, Brent, WTI, Natural Gas, Copper | Commodity benchmark is diagnostic research only; does not provide trading signals | False |
| pb_rec::advanced_commodity_providers_engine::metric_capability | advanced_commodity_providers_engine | provider_domain_commodity | metric_capability | 0.88 | 0.1467 | benchmark_pass | Futures contract codes, roll schedules, physical settlement metadata | Commodity benchmark is diagnostic research only; does not provide trading signals | False |
| pb_rec::advanced_commodity_providers_engine::metric_quality | advanced_commodity_providers_engine | provider_domain_commodity | metric_quality | 0.92 | 0.1533 | benchmark_pass | Commodity price boundary sanity, zero negative prices from Phase 112 | Commodity benchmark is diagnostic research only; does not provide trading signals | False |
| pb_rec::advanced_commodity_providers_engine::metric_normalization | advanced_commodity_providers_engine | provider_domain_commodity | metric_normalization | 0.93 | 0.155 | benchmark_pass | Canonical symbol and unit normalization (USD/bbl, USD/oz) from Phase 113 | Commodity benchmark is diagnostic research only; does not provide trading signals | False |
| pb_rec::advanced_commodity_providers_engine::metric_traceability | advanced_commodity_providers_engine | provider_domain_commodity | metric_traceability | 0.91 | 0.1517 | benchmark_pass | Commodity contract lineage and unit conversion audit trail from Phase 114 | Commodity benchmark is diagnostic research only; does not provide trading signals | False |
| pb_rec::advanced_commodity_providers_engine::metric_no_scraping_compliance | advanced_commodity_providers_engine | provider_domain_commodity | metric_no_scraping_compliance | 1.0 | 0.1667 | benchmark_pass | Strict offline fixtures; zero exchange terminal scraping | Commodity benchmark is diagnostic research only; does not provide trading signals | False |
