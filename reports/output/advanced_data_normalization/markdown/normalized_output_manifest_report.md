# Phase 113 — Normalized Output Manifest Report

> [!IMPORTANT]
> **YASAL UYARI VE GÜVENLİK SINIRI**:
> Bu çıktı Phase 113 Data Normalization Layer raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, normalized data’yı trade sinyali olarak kullanma, official approval, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.


## Çıktı Manifestosu Özeti
- **Toplam Görünüm Kaydı**: 5
- **Kaynak Korundu**: True
- **Yıkıcı Eylem İzni**: True

## Manifest Detayları
| manifest_id | dataset_name | dataset_type | provider_name | original_ref | normalized_ref | schema_version | row_count | normalized_field_count | source_preserved | destructive_action_allowed | manual_review_required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| man_fx_quote_dry_run | fx_quote_contract | dataset_fx_quote | fx_dry_run_fixture_provider | data/raw/fx/quotes_raw.csv | data/lake/advanced_data_normalization/normalized_views/fx_quotes_normalized.csv | v1.0 | 100 | 5 | True | False | False |
| man_commodity_spot_dry_run | commodity_spot_contract | dataset_commodity_spot | commodity_dry_run_fixture_provider | data/raw/commodity/spot_raw.csv | data/lake/advanced_data_normalization/normalized_views/commodity_spot_normalized.csv | v1.0 | 100 | 6 | True | False | False |
| man_macro_timeseries_dry_run | macro_timeseries_contract | dataset_macro_timeseries | macro_official_api_provider_placeholder | data/raw/macro/macro_raw.csv | data/lake/advanced_data_normalization/normalized_views/macro_timeseries_normalized.csv | v1.0 | 100 | 7 | True | False | False |
| man_calendar_event_dry_run | calendar_event_contract | dataset_calendar_event | calendar_licensed_provider_placeholder | data/raw/calendar/events_raw.csv | data/lake/advanced_data_normalization/normalized_views/calendar_events_normalized.csv | v1.0 | 100 | 7 | True | False | False |
| man_news_metadata_dry_run | news_metadata_contract | dataset_news_metadata | news_public_dataset_provider_placeholder | data/raw/news/metadata_raw.csv | data/lake/advanced_data_normalization/normalized_views/news_metadata_normalized.csv | v1.0 | 100 | 7 | True | False | False |
