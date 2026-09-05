# Data Quality Health Check Report

> Bu çıktı Phase 112 Data Quality Engine raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, quality score’u trade sinyali olarak kullanma, provider official approval, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu veya destructive auto-cleaning değildir.

## Summary
- Total Checks: 38
- Passing: 38
- Failing: 0
- Health Rate: 0.0%

## Health Findings
| check_id | description | passed | status_label |
| --- | --- | --- | --- |
| config_module | advanced_data_quality.data_quality_config importable | True | quality_pass |
| labels_module | advanced_data_quality.data_quality_labels importable | True | quality_pass |
| models_module | advanced_data_quality.data_quality_models importable | True | quality_pass |
| profile_registry | Profile registry builder available | True | quality_pass |
| domain_registry | Domain registry builder available | True | quality_pass |
| severity_registry | Severity registry available | True | quality_pass |
| rule_registry | Rule registry builder available | True | quality_pass |
| schema_rules | Schema compliance rules available | True | quality_pass |
| missing_rules | Missing data rules available | True | quality_pass |
| stale_rules | Stale data rules available | True | quality_pass |
| duplicate_rules | Duplicate data rules available | True | quality_pass |
| outlier_rules | Outlier placeholder rules available | True | quality_pass |
| timestamp_rules | Timestamp integrity rules available | True | quality_pass |
| frequency_rules | Frequency & unit consistency rules available | True | quality_pass |
| fx_rules | FX quality rules available | True | quality_pass |
| commodity_rules | Commodity quality rules available | True | quality_pass |
| macro_rules | Macro quality rules available | True | quality_pass |
| calendar_rules | Calendar quality rules available | True | quality_pass |
| news_rules | News metadata quality rules available | True | quality_pass |
| provider_metadata_rules | Provider metadata rules available | True | quality_pass |
| ohlc_consistency | OHLC consistency contract available | True | quality_pass |
| quote_consistency | Quote consistency contract available | True | quality_pass |
| event_release_consistency | Event release consistency contract available | True | quality_pass |
| news_copyright_rules | News copyright boundary rules available | True | quality_pass |
| findings_module | Quality findings registry available | True | quality_pass |
| manual_review_module | Manual review queue available | True | quality_pass |
| scoring_modules | Provider & dataset quality scoring available | True | quality_pass |
| phase_106_integration | Phase 106 advanced_data_providers available | True | quality_pass |
| phase_107_integration | Phase 107 advanced_fx_providers available | True | quality_pass |
| phase_108_integration | Phase 108 advanced_commodity_providers available | True | quality_pass |
| phase_109_integration | Phase 109 advanced_macro_providers available | True | quality_pass |
| phase_110_integration | Phase 110 advanced_economic_calendar available | True | quality_pass |
| phase_111_integration | Phase 111 advanced_news_metadata available | True | quality_pass |
| datalake_integration | DataLake save/load methods available | True | quality_pass |
| featurestore_integration | FeatureStore load methods available | True | quality_pass |
| scripts_present | Quality CLI run scripts present | True | quality_pass |
| tests_present | Quality test suite present | True | quality_pass |
| docs_present | Documentation updated for Phase 112 | True | quality_pass |
