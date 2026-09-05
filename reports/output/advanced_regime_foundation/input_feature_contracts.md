# Phase 126: Regime Contracts and Dependencies Report

> **UYARI / DISCLAIMER:** Bu çıktı Phase 126 Regime Classification and Market Behavior Foundation raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, regime state değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Özet
- **Toplam Bağımlılık / Sözleşme:** `9`
- **Tüm Bağımlılıklar Doğrulandı:** `True`
- **No-Lookahead Zorunlu:** `True`
- **Non-Signal Zorunlu:** `True`

## Bağımlılıklar Tablosu
| contract_name | regime_family | required_feature_families | required_factor_families | source_phase_refs | validation_required | quality_required | no_lookahead_required | non_signal_required | manual_review_required | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| contract_volatility_features | regime_family_volatility | volatility_indicators, multi_window_volatility, atr_features | factor_volatility_realized, factor_volatility_expansion | [117, 118, 122, 124] | True | True | True | True | True | regime_ready |
| contract_trend_features | regime_family_trend | moving_averages, multi_window_trend, donchian_channels | factor_trend_ma_slope, factor_trend_alignment | [117, 118, 122, 124] | True | True | True | True | True | regime_ready |
| contract_range_features | regime_family_range | mean_reversion_indicators, multi_window_range, bollinger_bands | factor_mean_reversion, factor_zscore_bounds | [117, 118, 122, 124] | True | True | True | True | True | regime_ready |
| contract_liquidity_features | regime_family_liquidity_placeholder | quote_spread_features, quote_staleness_features | factor_liquidity_placeholder | [117, 122, 124] | True | True | True | True | True | regime_placeholder_only |
| contract_macro_features | regime_family_macro_context | macro_indicator_features, yield_spread_features | factor_macro_differential, factor_macro_trend | [109, 120, 122, 124] | True | True | True | True | True | regime_ready |
| contract_macro_event_features | regime_family_event_context | calendar_window_features, surprise_indicators | factor_calendar_event, factor_event_window | [110, 120, 122, 124] | True | True | True | True | True | regime_ready |
| contract_news_metadata_features | regime_family_news_metadata_context | news_volume_features, topic_entropy_features | factor_news_attention, factor_news_tag_density | [111, 120, 122, 124] | True | True | True | True | True | regime_ready |
| contract_cross_asset_features | regime_family_cross_asset_context | cross_asset_returns, benchmark_correlations | factor_cross_asset_coupling, factor_intermarket_spread | [119, 120, 122, 124] | True | True | True | True | True | regime_ready |
| contract_composite_features | regime_family_composite_placeholder | all_validated_features | all_validated_factors | [121, 122, 123, 124, 125] | True | True | True | True | True | regime_placeholder_only |