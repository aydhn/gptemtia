# Transformation Provenance Registry Report
> **YASAL UYARI VE FERAGATNAME**
> Bu çıktı Phase 114 Data Lineage and Provenance raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, lineage/traceability score’u trade sinyali olarak kullanma, official approval, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.

- **Toplam Dönüşüm Sayısı**: 12
- **Tüm Kaynaklar Korundu**: True
- **Sıfır Yıkıcı Eylem**: True

| provenance_id | dataset_type | transformation_rule | source_field | target_field | original_value_repr | normalized_value_repr | source_preserved | destructive_action_allowed | manual_review_required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trans_prov_dataset_fx_quote_pair_to_normalized_pair | dataset_fx_quote | fx_symbol_slashing | pair | normalized_pair | 'EURUSD' | 'EUR/USD' | True | False | False |
| trans_prov_dataset_commodity_spot_symbol_to_normalized_symbol | dataset_commodity_spot | commodity_symbol_root_mapping | symbol | normalized_symbol | 'GOLD' | 'XAU/USD' | True | False | False |
| trans_prov_dataset_macro_timeseries_indicator_to_normalized_indicator | dataset_macro_timeseries | macro_indicator_slugification | indicator | normalized_indicator | 'US10Y' | 'US_10Y_YIELD' | True | False | False |
| trans_prov_dataset_calendar_event_event_to_normalized_event | dataset_calendar_event | calendar_event_name_normalization | event | normalized_event | 'FOMC' | 'FOMC_RATE_DECISION' | True | False | False |
| trans_prov_dataset_news_metadata_tags_to_normalized_tags | dataset_news_metadata | news_topic_tag_normalization | tags | normalized_tags | ['central bank', 'inflation'] | ['CENTRAL_BANK', 'INFLATION'] | True | False | False |
| trans_prov_dataset_provider_metadata_provider_name_to_normalized_provider_name | dataset_provider_metadata | provider_name_slugification | provider_name | normalized_provider_name | 'Provider A' | 'provider_a' | True | False | False |
| trans_prov_dataset_provider_metadata_schema_version_to_normalized_schema_version | dataset_provider_metadata | schema_version_normalization | schema_version | normalized_schema_version | '1.0' | 'v1.0' | True | False | False |
| trans_prov_dataset_fx_ohlcv_timestamp_to_normalized_timestamp | dataset_fx_ohlcv | timestamp_utc_iso8601_conversion | timestamp | normalized_timestamp | '2026-01-01 10:00:00+03:00' | '2026-01-01T07:00:00Z' | True | False | False |
| trans_prov_dataset_macro_timeseries_frequency_to_normalized_frequency | dataset_macro_timeseries | frequency_vocabulary_standardization | frequency | normalized_frequency | 'Daily' | '1d' | True | False | False |
| trans_prov_dataset_macro_timeseries_unit_to_normalized_unit | dataset_macro_timeseries | unit_vocabulary_standardization | unit | normalized_unit | 'Percent' | 'percent' | True | False | False |
| trans_prov_dataset_calendar_event_country_to_normalized_region | dataset_calendar_event | region_country_iso_normalization | country | normalized_region | 'United States' | 'US' | True | False | False |
| trans_prov_dataset_fx_quote_pair__timestamp_to_canonical_duplicate_key | dataset_fx_quote | duplicate_key_composite_derivation | pair, timestamp | canonical_duplicate_key | ('EUR/USD', '2026-01-01T00:00:00Z') | 'EUR/USD_2026-01-01T00:00:00Z' | True | False | False |