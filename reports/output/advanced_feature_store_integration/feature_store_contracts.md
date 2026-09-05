# Phase 124 Feature Store Contracts Report

> Bu cikti Phase 124 Feature Store Integration Expansion raporudur. Canli emir, broker talimati, kesin AL/SAT, yatirim tavsiyesi, feature store kaydini trade sinyali olarak kullanma, strateji uretimi, backtest, optimizer, model training, prediction/target/label uretimi, production-ready/official approval/broker-ready iddiasi, otomatik feature silme/duzeltme, haber tam metni kullanimi, production deployment, model deployment, scraping veya gercek provider API cagrisi degildir.

## Contract Summary
- Total Contracts: `7`
- All Non-Signal: `True`
- All Source Preserved: `True`
- Validation Required: `True`

## Contracts Table
| store_name | entity_keys | timestamp_field | symbol_field | feature_namespace_policy | schema_policy | validation_status_required | quality_score_required | drift_score_required | lineage_reference_required | manual_review_blocker_policy | non_signal_required | source_preserved_required | source_phase | official_approval | production_ready | broker_ready | entity_keys_str | current_phase | target_final_phase |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| technical_feature_store_contract | ['fx_pair', 'commodity_symbol'] | timestamp | symbol | entity__symbol__technical__indicator__window | strict_canonical_types | True | True | True | True | block_on_unresolved | True | True | 117 | False | False | False | fx_pair,commodity_symbol | 124 | 160 |
| multi_window_feature_grid_store_contract | ['fx_pair', 'commodity_symbol'] | timestamp | symbol | entity__symbol__grid__window | strict_multi_window_grid | True | True | True | True | block_on_unresolved | True | True | 118 | False | False | False | fx_pair,commodity_symbol | 124 | 160 |
| cross_asset_feature_store_contract | ['cross_asset_context', 'fx_pair', 'commodity_symbol'] | timestamp | context_id | cross_asset__pair__metric__window | asof_backward_alignment_only | True | True | True | True | block_on_unresolved | True | True | 119 | False | False | False | cross_asset_context,fx_pair,commodity_symbol | 124 | 160 |
| macro_calendar_news_fusion_store_contract | ['macro_indicator', 'calendar_event', 'news_metadata_tag'] | timestamp | event_id | fusion__domain__feature__window | metadata_only_no_full_text | True | True | True | True | block_on_unresolved | True | True | 120 | False | False | False | macro_indicator,calendar_event,news_metadata_tag | 124 | 160 |
| factor_metadata_store_contract | ['factor_family'] | timestamp | factor_id | factor__family__asset__symbol__factor_name__window | canonical_factor_registry | True | True | True | True | block_on_unresolved | True | True | 122 | False | False | False | factor_family | 124 | 160 |
| quality_drift_metadata_store_contract | ['fx_pair', 'commodity_symbol', 'factor_family'] | timestamp | feature_or_factor_id | quality_drift__metric__target_ref | diagnostic_bounds_zero_to_one | True | True | True | True | block_on_unresolved | True | True | 123 | False | False | False | fx_pair,commodity_symbol,factor_family | 124 | 160 |
| validation_status_store_contract | ['fx_pair', 'commodity_symbol', 'macro_indicator', 'calendar_event', 'factor_family'] | timestamp | item_id | validation__status__item_ref | no_lookahead_and_leakage_audit | True | True | True | True | block_on_unresolved | True | True | 121 | False | False | False | fx_pair,commodity_symbol,macro_indicator,calendar_event,factor_family | 124 | 160 |
