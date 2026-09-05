# Phase 115: Provider Benchmark Score Report
> **UYARI VE SINIRLAR**:
> Bu çıktı Phase 115 Data Provider Benchmark Report raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, benchmark score’u trade sinyali olarak kullanma, provider official approval, production-ready/broker-ready iddiası, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.

- **Toplam Puanlanan Sağlayıcı**: 9
- **Ortalama Benchmark Skoru**: 0.8462
- **En Yüksek Skor**: 0.954
- **En Düşük Skor**: 0.5775
- **Official Approval Garantisi**: False
- **Production/Live Ready Garantisi**: False

### Sağlayıcı Benchmark Puanları
| score_id | provider_name | provider_domain | total_score | coverage_score | capability_score | quality_score | normalization_score | traceability_score | compliance_score | manual_review_penalty | status_label | official_approval | production_ready | broker_ready | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pb_score::advanced_fx_providers_engine::provider_domain_fx | advanced_fx_providers_engine | provider_domain_fx | 0.954 | 0.94 | 0.92 | 0.95 | 0.96 | 0.94 | 1.0 | 0.0 | benchmark_pass | False | False | False | Offline comparative diagnostic benchmark score; not a trading signal or approval |
| pb_score::advanced_commodity_providers_engine::provider_domain_commodity | advanced_commodity_providers_engine | provider_domain_commodity | 0.927 | 0.9 | 0.88 | 0.92 | 0.93 | 0.91 | 1.0 | 0.0 | benchmark_pass | False | False | False | Offline comparative diagnostic benchmark score; not a trading signal or approval |
| pb_score::advanced_macro_providers_engine::provider_domain_macro | advanced_macro_providers_engine | provider_domain_macro | 0.914 | 0.88 | 0.85 | 0.9 | 0.92 | 0.91 | 1.0 | 0.0 | benchmark_pass | False | False | False | Offline comparative diagnostic benchmark score; not a trading signal or approval |
| pb_score::advanced_economic_calendar_engine::provider_domain_calendar | advanced_economic_calendar_engine | provider_domain_calendar | 0.9385 | 0.92 | 0.89 | 0.94 | 0.93 | 0.93 | 1.0 | 0.0 | benchmark_pass | False | False | False | Offline comparative diagnostic benchmark score; not a trading signal or approval |
| pb_score::advanced_news_metadata_engine::provider_domain_news_metadata | advanced_news_metadata_engine | provider_domain_news_metadata | 0.8965 | 0.85 | 0.83 | 0.88 | 0.89 | 0.9 | 1.0 | 0.0 | benchmark_pass | False | False | False | Offline comparative diagnostic benchmark score; not a trading signal or approval |
| pb_score::manual_file_provider_adapter::provider_domain_cross_domain | manual_file_provider_adapter | provider_domain_cross_domain | 0.5775 | 0.6 | 0.65 | 0.7 | 0.68 | 0.72 | 0.95 | 0.15 | benchmark_pass_with_warnings | False | False | False | Offline comparative diagnostic benchmark score; not a trading signal or approval |
| pb_score::local_cache_provider_adapter::provider_domain_cross_domain | local_cache_provider_adapter | provider_domain_cross_domain | 0.8815 | 0.75 | 0.78 | 0.88 | 0.91 | 0.93 | 1.0 | 0.0 | benchmark_pass | False | False | False | Offline comparative diagnostic benchmark score; not a trading signal or approval |
| pb_score::official_api_provider_placeholder::provider_domain_cross_domain | official_api_provider_placeholder | provider_domain_cross_domain | 0.762 | 0.8 | 0.85 | 0.82 | 0.85 | 0.82 | 1.0 | 0.1 | benchmark_pass_with_warnings | False | False | False | Offline comparative diagnostic benchmark score; not a trading signal or approval |
| pb_score::licensed_vendor_provider_placeholder::provider_domain_cross_domain | licensed_vendor_provider_placeholder | provider_domain_cross_domain | 0.7645 | 0.85 | 0.88 | 0.85 | 0.86 | 0.84 | 1.0 | 0.12 | benchmark_pass_with_warnings | False | False | False | Offline comparative diagnostic benchmark score; not a trading signal or approval |
