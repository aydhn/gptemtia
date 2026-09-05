# Provenance Source Registry Report
> **YASAL UYARI VE FERAGATNAME**
> Bu çıktı Phase 114 Data Lineage and Provenance raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, lineage/traceability score’u trade sinyali olarak kullanma, official approval, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.

- **Toplam Kaynak Sayısı**: 10
- **Kaynak Tipleri**: dry_run_fixture, manual_file, local_cache, official_api, licensed_provider, public_dataset
- **Manuel İnceleme Gereken**: 3
- **Tümü No-Scraping**: True

| source_id | source_name | source_type | provider_name | dataset_type | license_note | retrieval_mode | no_scraping_policy | manual_review_required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| prov_src_fx_fixture_provider_fx_dry_run_fixture_source | fx_dry_run_fixture_source | dry_run_fixture | fx_fixture_provider | dataset_fx_quote | Internal local research mock - non-commercial | dry_run_offline | Strict no-scraping | False |
| prov_src_commodity_fixture_provider_commodity_dry_run_fixture_source | commodity_dry_run_fixture_source | dry_run_fixture | commodity_fixture_provider | dataset_commodity_spot | Internal local research mock - non-commercial | dry_run_offline | Strict no-scraping | False |
| prov_src_macro_fixture_provider_macro_dry_run_fixture_source | macro_dry_run_fixture_source | dry_run_fixture | macro_fixture_provider | dataset_macro_timeseries | Internal local research mock - non-commercial | dry_run_offline | Strict no-scraping | False |
| prov_src_calendar_fixture_provider_calendar_dry_run_fixture_source | calendar_dry_run_fixture_source | dry_run_fixture | calendar_fixture_provider | dataset_calendar_event | Internal local research mock - non-commercial | dry_run_offline | Strict no-scraping | False |
| prov_src_news_fixture_provider_news_metadata_dry_run_fixture_source | news_metadata_dry_run_fixture_source | dry_run_fixture | news_fixture_provider | dataset_news_metadata | Internal local metadata mock - non-commercial, zero full text | dry_run_offline | Strict no-scraping | False |
| prov_src_manual_file_provider_manual_file_placeholder_source | manual_file_placeholder_source | manual_file | manual_file_provider | dataset_provider_metadata | User-provided local flat file | file_system | Strict no-scraping | True |
| prov_src_local_cache_provider_local_cache_placeholder_source | local_cache_placeholder_source | local_cache | local_cache_provider | dataset_provider_metadata | Cached offline snapshot | file_cache | Strict no-scraping | False |
| prov_src_official_api_placeholder_official_api_placeholder_source | official_api_placeholder_source | official_api | official_api_placeholder | dataset_provider_metadata | Official REST/GraphQL endpoint contract placeholder | api_placeholder | Strict no-scraping | True |
| prov_src_licensed_provider_placeholder_licensed_provider_placeholder_source | licensed_provider_placeholder_source | licensed_provider | licensed_provider_placeholder | dataset_provider_metadata | Commercial vendor contract placeholder | licensed_placeholder | Strict no-scraping | True |
| prov_src_public_dataset_placeholder_public_dataset_placeholder_source | public_dataset_placeholder_source | public_dataset | public_dataset_placeholder | dataset_provider_metadata | Public domain / open research archive placeholder | public_placeholder | Strict no-scraping | False |