# Phase 126: Regime State Taxonomy Report

> **UYARI / DISCLAIMER:** Bu çıktı Phase 126 Regime Classification and Market Behavior Foundation raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, regime state değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Özet
- **Toplam Rejim Durumları:** `11`
- **Hazır Durumlar:** `9`
- **Yer Tutucu Durumlar:** `2`
- **Zorunlu Önek ('regime_state_') Uyumlu:** `True`
- **Hedef / Tahmin (Target/Prediction) Yok:** `True`
- **İşlem Tavsiyesi Yok:** `True`

## Rejim Durumları Tablosu
| state_id | regime_state_name | regime_family | state_description | source_feature_contract | validation_dependency | quality_dependency | non_signal | contains_target_or_prediction | contains_trading_recommendation | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| state_01_trend | regime_state_trend_context | regime_family_trend | Market environment exhibiting consistent moving average alignment and directional persistence | contract_trend_features | val_trend_no_lookahead | qual_trend_factor_drift | True | False | False | regime_ready |
| state_02_range | regime_state_range_context | regime_family_range | Market environment exhibiting mean-reversion characteristics bounded within volatility channels | contract_range_features | val_range_no_lookahead | qual_range_factor_drift | True | False | False | regime_ready |
| state_03_vol_high | regime_state_volatility_high_context | regime_family_volatility | Market environment with realized volatility in the top historical quintile | contract_volatility_features | val_vol_no_lookahead | qual_vol_factor_drift | True | False | False | regime_ready |
| state_04_vol_low | regime_state_volatility_low_context | regime_family_volatility | Market environment with realized volatility in the bottom historical quintile | contract_volatility_features | val_vol_no_lookahead | qual_vol_factor_drift | True | False | False | regime_ready |
| state_05_vol_expansion | regime_state_volatility_expansion_context | regime_family_volatility | Market environment characterized by opening volatility envelopes and increasing true range | contract_volatility_features | val_vol_no_lookahead | qual_vol_factor_drift | True | False | False | regime_ready |
| state_06_vol_compression | regime_state_volatility_compression_context | regime_family_volatility | Market environment characterized by narrowing Bollinger bandwidth and compressed price action | contract_volatility_features | val_vol_no_lookahead | qual_vol_factor_drift | True | False | False | regime_ready |
| state_07_macro_event | regime_state_macro_event_context | regime_family_event_context | Market environment during high-impact scheduled economic releases or monetary policy announcements | contract_macro_event_features | val_event_window_alignment | qual_calendar_staleness | True | False | False | regime_ready |
| state_08_news_attention | regime_state_news_attention_context | regime_family_news_metadata_context | Market environment with elevated metadata-only news item count and topic concentration | contract_news_metadata_features | val_news_metadata_only | qual_news_staleness | True | False | False | regime_ready |
| state_09_cross_asset | regime_state_cross_asset_context | regime_family_cross_asset_context | Market environment influenced by macro benchmarks (DXY, US10Y, SPX) alignment | contract_cross_asset_features | val_cross_asset_alignment | qual_cross_asset_drift | True | False | False | regime_ready |
| state_10_transition | regime_state_transition_placeholder | regime_family_composite_placeholder | Placeholder state indicating boundary shift or regime breakdown between trend and range | contract_composite_features | val_transition_alignment | qual_stability_score | True | False | False | regime_placeholder_only |
| state_11_uncertain | regime_state_uncertain_placeholder | regime_family_composite_placeholder | Placeholder state indicating insufficient factor consensus or elevated missingness | contract_composite_features | val_uncertain_diagnostics | qual_missingness_score | True | False | False | regime_placeholder_only |