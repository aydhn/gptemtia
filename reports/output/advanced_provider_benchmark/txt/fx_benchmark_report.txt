# Phase 115: provider_domain_fx Provider Benchmark Report
> **UYARI VE SINIRLAR**:
> Bu çıktı Phase 115 Data Provider Benchmark Report raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, benchmark score’u trade sinyali olarak kullanma, provider official approval, production-ready/broker-ready iddiası, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.

- **Domain**: provider_domain_fx
- **Değerlendirilen Metrik Sayısı**: 6
- **Ortalama Domain Puanı**: 0.9517

### Alan Bazlı Değerlendirme Tablosu
| record_id | provider_name | provider_domain | metric_label | raw_score | weighted_score | status_label | evidence_ref | limitation_note | manual_review_required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pb_rec::advanced_fx_providers_engine::metric_coverage | advanced_fx_providers_engine | provider_domain_fx | metric_coverage | 0.94 | 0.1567 | benchmark_pass | EUR/USD, GBP/USD, USD/JPY, USD/CHF, AUD/USD, USD/CAD, USD/TRY, EUR/TRY coverage | FX benchmark evaluation is for research only; no trade signals or live execution | False |
| pb_rec::advanced_fx_providers_engine::metric_capability | advanced_fx_providers_engine | provider_domain_fx | metric_capability | 0.92 | 0.1533 | benchmark_pass | Tick quote, 1m/5m/1h/1d OHLCV capability, timestamp precision | FX benchmark evaluation is for research only; no trade signals or live execution | False |
| pb_rec::advanced_fx_providers_engine::metric_quality | advanced_fx_providers_engine | provider_domain_fx | metric_quality | 0.95 | 0.1583 | benchmark_pass | Bid/Ask positive spread sanity, zero stale quotes from Phase 112 | FX benchmark evaluation is for research only; no trade signals or live execution | False |
| pb_rec::advanced_fx_providers_engine::metric_normalization | advanced_fx_providers_engine | provider_domain_fx | metric_normalization | 0.96 | 0.16 | benchmark_pass | Uppercase slash-separated canonical pairs, UTC timestamp format from Phase 113 | FX benchmark evaluation is for research only; no trade signals or live execution | False |
| pb_rec::advanced_fx_providers_engine::metric_traceability | advanced_fx_providers_engine | provider_domain_fx | metric_traceability | 0.94 | 0.1567 | benchmark_pass | Source to normalized quote transformation lineage verified from Phase 114 | FX benchmark evaluation is for research only; no trade signals or live execution | False |
| pb_rec::advanced_fx_providers_engine::metric_no_scraping_compliance | advanced_fx_providers_engine | provider_domain_fx | metric_no_scraping_compliance | 1.0 | 0.1667 | benchmark_pass | Strict offline fixtures; zero web scraping or browser automation | FX benchmark evaluation is for research only; no trade signals or live execution | False |
