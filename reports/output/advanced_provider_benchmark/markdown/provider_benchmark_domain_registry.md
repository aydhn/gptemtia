# Phase 115: Domain Provider Benchmark Report
> **UYARI VE SINIRLAR**:
> Bu çıktı Phase 115 Data Provider Benchmark Report raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, benchmark score’u trade sinyali olarak kullanma, provider official approval, production-ready/broker-ready iddiası, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.

- **Domain**: N/A
- **Değerlendirilen Metrik Sayısı**: 0
- **Ortalama Domain Puanı**: 0.0

### Alan Bazlı Değerlendirme Tablosu
| domain_id | domain_label | domain_name | description | required_outputs | warnings |
| --- | --- | --- | --- | --- | --- |
| pb_domain::provider_benchmark_profile_domain | provider_benchmark_profile_domain | Provider Benchmark Profile Domain | Configuration profiles for local provider benchmarking | ['profile_registry'] | [] |
| pb_domain::provider_benchmark_domain | provider_benchmark_domain | Provider Benchmark Master Domain | Master provider benchmark abstraction and registries | ['domain_registry'] | [] |
| pb_domain::benchmark_metric_domain | benchmark_metric_domain | Benchmark Metric Domain | Metrics registry for provider capability and quality | ['metric_registry'] | [] |
| pb_domain::benchmark_weight_domain | benchmark_weight_domain | Benchmark Weight Domain | Weight specifications for multi-metric aggregation | ['weight_registry'] | [] |
| pb_domain::coverage_benchmark_domain | coverage_benchmark_domain | Coverage Benchmark Domain | Assessment of asset/symbol/indicator coverage breadth | ['coverage_report'] | [] |
| pb_domain::capability_benchmark_domain | capability_benchmark_domain | Capability Benchmark Domain | Assessment of technical timeseries/quote/event capabilities | ['capability_report'] | [] |
| pb_domain::quality_benchmark_domain | quality_benchmark_domain | Quality Benchmark Domain | Evaluation of data quality findings and clean rates | ['quality_report'] | [] |
| pb_domain::normalization_benchmark_domain | normalization_benchmark_domain | Normalization Benchmark Domain | Canonical schema conformance and normalization adherence | ['normalization_report'] | [] |
| pb_domain::traceability_benchmark_domain | traceability_benchmark_domain | Traceability Benchmark Domain | Provenance and audit trail traceability evaluation | ['traceability_report'] | [] |
| pb_domain::license_provenance_benchmark_domain | license_provenance_benchmark_domain | License & Provenance Benchmark Domain | Licensing terms and redistribution limitations | ['license_report'] | [] |
| pb_domain::no_scraping_compliance_domain | no_scraping_compliance_domain | No-Scraping Compliance Domain | Strict verification of zero web scraping boundaries | ['no_scraping_report'] | [] |
| pb_domain::metadata_only_compliance_domain | metadata_only_compliance_domain | Metadata-Only Compliance Domain | Zero full-text article extraction validation | ['metadata_only_report'] | [] |
| pb_domain::manual_review_benchmark_domain | manual_review_benchmark_domain | Manual Review Benchmark Domain | Evaluation of manual review queue load and non-destructive action | ['manual_review_report'] | [] |
| pb_domain::fx_provider_benchmark_domain | fx_provider_benchmark_domain | FX Provider Benchmark Domain | FX specific pair coverage, quote sanity and OHLCV readiness | ['fx_benchmark_report'] | [] |
| pb_domain::commodity_provider_benchmark_domain | commodity_provider_benchmark_domain | Commodity Provider Benchmark Domain | Commodity spot/futures contract and roll metadata readiness | ['commodity_benchmark_report'] | [] |
| pb_domain::macro_provider_benchmark_domain | macro_provider_benchmark_domain | Macro Provider Benchmark Domain | Macroeconomic indicator universe and revision metadata | ['macro_benchmark_report'] | [] |
| pb_domain::calendar_provider_benchmark_domain | calendar_provider_benchmark_domain | Calendar Provider Benchmark Domain | Economic calendar event universe and release timestamp precision | ['calendar_benchmark_report'] | [] |
| pb_domain::news_metadata_provider_benchmark_domain | news_metadata_provider_benchmark_domain | News Metadata Provider Benchmark Domain | News headline/topic taxonomy and event linkage without full text | ['news_benchmark_report'] | [] |
| pb_domain::cross_domain_provider_benchmark_domain | cross_domain_provider_benchmark_domain | Cross-Domain Provider Benchmark Domain | Cross-asset alignment and symbol-tag consistency | ['cross_domain_report'] | [] |
| pb_domain::benchmark_scoring_domain | benchmark_scoring_domain | Benchmark Scoring Domain | Non-trading comparative diagnostic score calculation | ['score_report'] | [] |
| pb_domain::provider_ranking_research_domain | provider_ranking_research_domain | Provider Ranking Research Domain | Offline research ranking matrix (strictly non-approval) | ['ranking_report'] | [] |
| pb_domain::benchmark_finding_domain | benchmark_finding_domain | Benchmark Finding Domain | Registry of benchmark observations and limitations | ['findings_registry'] | [] |
| pb_domain::benchmark_manual_review_domain | benchmark_manual_review_domain | Benchmark Manual Review Domain | Non-destructive manual review queue for benchmark gaps | ['manual_review_queue'] | [] |
| pb_domain::benchmark_health_domain | benchmark_health_domain | Benchmark Health Domain | Subsystem readiness and component availability verification | ['health_check'] | [] |
| pb_domain::benchmark_validation_domain | benchmark_validation_domain | Benchmark Validation Domain | Integrity validation and forbidden claims enforcement | ['validation_report'] | [] |
| pb_domain::benchmark_safety_domain | benchmark_safety_domain | Benchmark Safety Domain | Strict safety boundaries, No-Go rules and Safe-Go conditions | ['safety_boundary'] | [] |
| pb_domain::phase_116_handoff_domain | phase_116_handoff_domain | Phase 116 Handoff Domain | Data readiness delivery for indicator/feature/factor engine | ['phase_116_handoff'] | [] |
| pb_domain::unknown_benchmark_domain | unknown_benchmark_domain | Unknown Benchmark Domain | Fallback domain for unclassified benchmark records | ['unknown_report'] | [] |
