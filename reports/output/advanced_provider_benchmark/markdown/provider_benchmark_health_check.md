# Phase 115: Provider Benchmark Health Check
> **UYARI VE SINIRLAR**:
> Bu çıktı Phase 115 Data Provider Benchmark Report raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, benchmark score’u trade sinyali olarak kullanma, provider official approval, production-ready/broker-ready iddiası, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.

- **Genel Durum**: PASS
- **Toplam Kontrol Sayısı**: 44
- **Başarılı Kontroller**: 44
- **Başarısız Kontroller**: 0

### Sağlık Kontrol Detayları
| check_category | component | phase | status | detail |
| --- | --- | --- | --- | --- |
| upstream_layer | advanced_data_providers | 106 | PASS | Phase 106 upstream layer package is present |
| upstream_layer | advanced_fx_providers | 107 | PASS | Phase 107 upstream layer package is present |
| upstream_layer | advanced_commodity_providers | 108 | PASS | Phase 108 upstream layer package is present |
| upstream_layer | advanced_macro_providers | 109 | PASS | Phase 109 upstream layer package is present |
| upstream_layer | advanced_economic_calendar | 110 | PASS | Phase 110 upstream layer package is present |
| upstream_layer | advanced_news_metadata | 111 | PASS | Phase 111 upstream layer package is present |
| upstream_layer | advanced_data_quality | 112 | PASS | Phase 112 upstream layer package is present |
| upstream_layer | advanced_data_normalization | 113 | PASS | Phase 113 upstream layer package is present |
| upstream_layer | advanced_data_lineage | 114 | PASS | Phase 114 upstream layer package is present |
| phase_115_core_module | provider_benchmark_config | 115 | PASS | Module provider_benchmark_config.py exists |
| phase_115_core_module | provider_benchmark_labels | 115 | PASS | Module provider_benchmark_labels.py exists |
| phase_115_core_module | provider_benchmark_models | 115 | PASS | Module provider_benchmark_models.py exists |
| phase_115_core_module | provider_benchmark_profile_registry | 115 | PASS | Module provider_benchmark_profile_registry.py exists |
| phase_115_core_module | provider_benchmark_domain_registry | 115 | PASS | Module provider_benchmark_domain_registry.py exists |
| phase_115_core_module | provider_benchmark_metric_registry | 115 | PASS | Module provider_benchmark_metric_registry.py exists |
| phase_115_core_module | provider_benchmark_weight_registry | 115 | PASS | Module provider_benchmark_weight_registry.py exists |
| phase_115_core_module | provider_coverage_benchmark | 115 | PASS | Module provider_coverage_benchmark.py exists |
| phase_115_core_module | provider_capability_benchmark | 115 | PASS | Module provider_capability_benchmark.py exists |
| phase_115_core_module | provider_quality_benchmark | 115 | PASS | Module provider_quality_benchmark.py exists |
| phase_115_core_module | provider_normalization_benchmark | 115 | PASS | Module provider_normalization_benchmark.py exists |
| phase_115_core_module | provider_traceability_benchmark | 115 | PASS | Module provider_traceability_benchmark.py exists |
| phase_115_core_module | provider_license_provenance_benchmark | 115 | PASS | Module provider_license_provenance_benchmark.py exists |
| phase_115_core_module | provider_no_scraping_compliance | 115 | PASS | Module provider_no_scraping_compliance.py exists |
| phase_115_core_module | provider_metadata_only_compliance | 115 | PASS | Module provider_metadata_only_compliance.py exists |
| phase_115_core_module | provider_manual_review_benchmark | 115 | PASS | Module provider_manual_review_benchmark.py exists |
| phase_115_core_module | fx_provider_benchmark | 115 | PASS | Module fx_provider_benchmark.py exists |
| phase_115_core_module | commodity_provider_benchmark | 115 | PASS | Module commodity_provider_benchmark.py exists |
| phase_115_core_module | macro_provider_benchmark | 115 | PASS | Module macro_provider_benchmark.py exists |
| phase_115_core_module | calendar_provider_benchmark | 115 | PASS | Module calendar_provider_benchmark.py exists |
| phase_115_core_module | news_metadata_provider_benchmark | 115 | PASS | Module news_metadata_provider_benchmark.py exists |
| phase_115_core_module | cross_domain_provider_benchmark | 115 | PASS | Module cross_domain_provider_benchmark.py exists |
| phase_115_core_module | provider_benchmark_scoring | 115 | PASS | Module provider_benchmark_scoring.py exists |
| phase_115_core_module | provider_ranking_research | 115 | PASS | Module provider_ranking_research.py exists |
| phase_115_core_module | provider_benchmark_findings | 115 | PASS | Module provider_benchmark_findings.py exists |
| phase_115_core_module | provider_benchmark_manual_review_queue | 115 | PASS | Module provider_benchmark_manual_review_queue.py exists |
| phase_115_core_module | provider_benchmark_report_builder | 115 | PASS | Module provider_benchmark_report_builder.py exists |
| phase_115_core_module | provider_benchmark_pipeline | 115 | PASS | Module provider_benchmark_pipeline.py exists |
| phase_115_core_module | provider_benchmark_health | 115 | PASS | Module provider_benchmark_health.py exists |
| phase_115_core_module | provider_benchmark_validation | 115 | PASS | Module provider_benchmark_validation.py exists |
| phase_115_core_module | provider_benchmark_safety_boundary | 115 | PASS | Module provider_benchmark_safety_boundary.py exists |
| phase_115_core_module | phase_116_handoff | 115 | PASS | Module phase_116_handoff.py exists |
| directory_structure | advanced_provider_benchmark | 115 | PASS | Directory data\lake\advanced_provider_benchmark exists |
| directory_structure | advanced_provider_benchmark | 115 | PASS | Directory reports\output\advanced_provider_benchmark exists |
| directory_structure | advanced_provider_benchmark | 115 | PASS | Directory docs\generated\advanced_provider_benchmark exists |
