# Traceability Score Report
> **YASAL UYARI VE FERAGATNAME**
> Bu çıktı Phase 114 Data Lineage and Provenance raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, lineage/traceability score’u trade sinyali olarak kullanma, official approval, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.

- **Toplam İzlenen Varlık**: 10
- **Ortalama İzlenebilirlik Skoru**: 0.941
- **Minimum İzlenebilirlik Skoru**: 0.9
- **Tam Soy Kütüğüne Sahip Varlıklar**: 10

| score_id | entity_name | entity_type | dataset_type | provider_name | score | status_label | missing_links | manual_review_count | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trace_score_dataset_fx_quote_contract_dataset | fx_quote_contract_dataset | dataset | dataset_fx_quote | advanced_fx_providers_engine | 0.95 | lineage_complete | 0 | 0 | Source-to-normalized quote traceability verified |
| trace_score_dataset_fx_ohlcv_contract_dataset | fx_ohlcv_contract_dataset | dataset | dataset_fx_ohlcv | advanced_fx_providers_engine | 0.96 | lineage_complete | 0 | 0 | Source-to-normalized OHLCV traceability verified |
| trace_score_dataset_commodity_spot_contract_dataset | commodity_spot_contract_dataset | dataset | dataset_commodity_spot | advanced_commodity_providers_engine | 0.92 | lineage_complete | 0 | 0 | Spot commodity symbol and price traceability verified |
| trace_score_dataset_commodity_ohlcv_contract_dataset | commodity_ohlcv_contract_dataset | dataset | dataset_commodity_ohlcv | advanced_commodity_providers_engine | 0.93 | lineage_complete | 0 | 0 | Commodity OHLCV traceability verified |
| trace_score_dataset_macro_timeseries_contract_dataset | macro_timeseries_contract_dataset | dataset | dataset_macro_timeseries | advanced_macro_providers_engine | 0.9 | lineage_complete | 0 | 1 | Macro indicator and frequency mapping verified |
| trace_score_dataset_calendar_event_contract_dataset | calendar_event_contract_dataset | dataset | dataset_calendar_event | advanced_economic_calendar_engine | 0.94 | lineage_complete | 0 | 0 | Calendar event schedule traceability verified |
| trace_score_dataset_release_event_contract_dataset | release_event_contract_dataset | dataset | dataset_release_event | advanced_economic_calendar_engine | 0.91 | lineage_complete | 0 | 0 | Release event actual/forecast traceability verified |
| trace_score_dataset_news_metadata_contract_dataset | news_metadata_contract_dataset | dataset | dataset_news_metadata | advanced_news_metadata_engine | 0.98 | lineage_complete | 0 | 0 | Metadata-only and topic taxonomy traceability verified |
| trace_score_dataset_provider_metadata_contract_dataset | provider_metadata_contract_dataset | dataset | dataset_provider_metadata | advanced_data_providers_abstraction | 0.95 | lineage_complete | 0 | 0 | Provider identity and capability traceability verified |
| trace_score_dataset_normalized_view_manifest_dataset | normalized_view_manifest_dataset | dataset | dataset_unknown | advanced_data_normalization_engine | 0.97 | lineage_complete | 0 | 0 | Output manifest source-target linkage verified |