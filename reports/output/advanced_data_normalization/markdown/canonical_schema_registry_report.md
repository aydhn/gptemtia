# Phase 113 — Canonical Schema Registry Report

> [!IMPORTANT]
> **YASAL UYARI VE GÜVENLİK SINIRI**:
> Bu çıktı Phase 113 Data Normalization Layer raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, normalized data’yı trade sinyali olarak kullanma, official approval, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.


## Şema Özeti
- **Toplam Kanonik Şema Sayısı**: 12
- **Veri Seti Tipleri**: dataset_fx_quote, dataset_fx_ohlcv, dataset_commodity_spot, dataset_commodity_ohlcv, dataset_macro_timeseries, dataset_calendar_event, dataset_release_event, dataset_news_metadata, dataset_provider_metadata

## Şemalar
| schema_id | dataset_type | schema_name | schema_version | canonical_fields | primary_key_fields | timestamp_field | provider_field | manual_review_required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| schema_dataset_fx_quote_v1_0 | dataset_fx_quote | fx_quote_v1 | v1.0 | ['timestamp', 'pair', 'bid', 'ask', 'provider'] | ['timestamp', 'pair', 'provider'] | timestamp | provider | False |
| schema_dataset_fx_ohlcv_v1_0 | dataset_fx_ohlcv | fx_ohlcv_v1 | v1.0 | ['timestamp', 'pair', 'open', 'high', 'low', 'close', 'volume', 'provider'] | ['timestamp', 'pair', 'provider'] | timestamp | provider | False |
| schema_dataset_commodity_spot_v1_0 | dataset_commodity_spot | commodity_spot_v1 | v1.0 | ['timestamp', 'symbol', 'price', 'currency', 'unit', 'provider'] | ['timestamp', 'symbol', 'provider'] | timestamp | provider | False |
| schema_dataset_commodity_ohlcv_v1_0 | dataset_commodity_ohlcv | commodity_ohlcv_v1 | v1.0 | ['timestamp', 'symbol', 'open', 'high', 'low', 'close', 'volume', 'provider'] | ['timestamp', 'symbol', 'provider'] | timestamp | provider | False |
| schema_dataset_commodity_spot_v1_0 | dataset_commodity_spot | commodity_futures_metadata_v1 | v1.0 | ['contract_code', 'root_symbol', 'expiry_date', 'roll_rule', 'provider'] | ['contract_code', 'provider'] | expiry_date | provider | True |
| schema_dataset_macro_timeseries_v1_0 | dataset_macro_timeseries | macro_timeseries_v1 | v1.0 | ['timestamp', 'indicator', 'value', 'region', 'frequency', 'unit', 'provider'] | ['timestamp', 'indicator', 'region', 'provider'] | timestamp | provider | False |
| schema_dataset_macro_timeseries_v1_0 | dataset_macro_timeseries | macro_release_metadata_v1 | v1.0 | ['release_id', 'indicator', 'scheduled_time', 'actual_time', 'status', 'provider'] | ['release_id', 'provider'] | scheduled_time | provider | True |
| schema_dataset_calendar_event_v1_0 | dataset_calendar_event | calendar_event_v1 | v1.0 | ['event_id', 'canonical_event', 'country', 'currency', 'scheduled_time', 'impact', 'provider'] | ['event_id', 'provider'] | scheduled_time | provider | False |
| schema_dataset_release_event_v1_0 | dataset_release_event | release_event_v1 | v1.0 | ['event_id', 'actual', 'forecast', 'previous', 'revised', 'unit', 'provider'] | ['event_id', 'provider'] | event_id | provider | False |
| schema_dataset_news_metadata_v1_0 | dataset_news_metadata | news_metadata_v1 | v1.0 | ['news_id', 'headline', 'source_name', 'published_at', 'tags', 'sentiment', 'provider'] | ['news_id', 'provider'] | published_at | provider | False |
| schema_dataset_news_metadata_v1_0 | dataset_news_metadata | news_item_reference_v1 | v1.0 | ['reference_id', 'news_id', 'url_reference_only', 'external_id', 'provider'] | ['reference_id', 'provider'] | news_id | provider | False |
| schema_dataset_provider_metadata_v1_0 | dataset_provider_metadata | provider_metadata_v1 | v1.0 | ['provider_id', 'provider_name', 'provider_type', 'version', 'status'] | ['provider_id'] | provider_id | provider_name | False |
