# Phase 115: provider_domain_news_metadata Provider Benchmark Report
> **UYARI VE SINIRLAR**:
> Bu çıktı Phase 115 Data Provider Benchmark Report raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, benchmark score’u trade sinyali olarak kullanma, provider official approval, production-ready/broker-ready iddiası, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.

- **Domain**: provider_domain_news_metadata
- **Değerlendirilen Metrik Sayısı**: 8
- **Ortalama Domain Puanı**: 0.9125

### Alan Bazlı Değerlendirme Tablosu
| record_id | provider_name | provider_domain | metric_label | raw_score | weighted_score | status_label | evidence_ref | limitation_note | manual_review_required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pb_rec::advanced_news_metadata_engine::metric_coverage | advanced_news_metadata_engine | provider_domain_news_metadata | metric_coverage | 0.85 | 0.1062 | benchmark_pass | Cross-asset topic coverage (FX pairs, commodities, central banks) | News metadata benchmark is diagnostic research only; zero full-text articles collected | False |
| pb_rec::advanced_news_metadata_engine::metric_capability | advanced_news_metadata_engine | provider_domain_news_metadata | metric_capability | 0.83 | 0.1037 | benchmark_pass | Headline metadata, tag extraction, calendar event linking | News metadata benchmark is diagnostic research only; zero full-text articles collected | False |
| pb_rec::advanced_news_metadata_engine::metric_quality | advanced_news_metadata_engine | provider_domain_news_metadata | metric_quality | 0.88 | 0.11 | benchmark_pass | Spam filtering and duplicate headline slug prevention from Phase 112 | News metadata benchmark is diagnostic research only; zero full-text articles collected | False |
| pb_rec::advanced_news_metadata_engine::metric_normalization | advanced_news_metadata_engine | provider_domain_news_metadata | metric_normalization | 0.89 | 0.1113 | benchmark_pass | Canonical uppercase asset tags and slugified topic categories from Phase 113 | News metadata benchmark is diagnostic research only; zero full-text articles collected | False |
| pb_rec::advanced_news_metadata_engine::metric_traceability | advanced_news_metadata_engine | provider_domain_news_metadata | metric_traceability | 0.9 | 0.1125 | benchmark_pass | Source provenance and publication timestamp tracking from Phase 114 | News metadata benchmark is diagnostic research only; zero full-text articles collected | False |
| pb_rec::advanced_news_metadata_engine::metric_license_provenance | advanced_news_metadata_engine | provider_domain_news_metadata | metric_license_provenance | 0.95 | 0.1187 | benchmark_pass | Strict fair-use metadata indexing boundary; no copyrighted article reuse | News metadata benchmark is diagnostic research only; zero full-text articles collected | False |
| pb_rec::advanced_news_metadata_engine::metric_no_scraping_compliance | advanced_news_metadata_engine | provider_domain_news_metadata | metric_no_scraping_compliance | 1.0 | 0.125 | benchmark_pass | Zero web page scraping, zero browser automation | News metadata benchmark is diagnostic research only; zero full-text articles collected | False |
| pb_rec::advanced_news_metadata_engine::metric_metadata_only_compliance | advanced_news_metadata_engine | provider_domain_news_metadata | metric_metadata_only_compliance | 1.0 | 0.125 | benchmark_pass | Strict zero full-text boundary; no article bodies gathered | News metadata benchmark is diagnostic research only; zero full-text articles collected | False |
