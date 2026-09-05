# Phase 126: Market Behavior Taxonomy Report

> **UYARI / DISCLAIMER:** Bu çıktı Phase 126 Regime Classification and Market Behavior Foundation raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, regime state değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Özet
- **Toplam Davranış Sayısı:** `12`
- **Hazır Davranışlar:** `9`
- **Yer Tutucu (Placeholder) Davranışlar:** `3`
- **Tümü Non-Signal:** `True`
- **Ticari Al/Sat Tavsiyesi Yok:** `True`

## Piyasa Davranışları Tablosu
| behavior_id | behavior_name | behavior_category | description | associated_regime_family | key_characteristics | non_signal | contains_trading_recommendation | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| beh_01_trending | trending_behavior | directional_persistence | Persistent directional price movement across moving average and channel indicators without trade recommendation | regime_family_trend | ma_slope_high, channel_penetration_sustained, persistence_high | True | False | regime_ready |
| beh_02_ranging | ranging_behavior | mean_reversion_envelope | Oscillating price behavior bounded between support and resistance envelopes | regime_family_range | bounded_envelope, zscore_reversion, flat_ma_slope | True | False | regime_ready |
| beh_03_high_volatility | high_volatility_behavior | dispersion_level | Elevated realized volatility and wide true range relative to historical baseline | regime_family_volatility | atr_elevated, realized_vol_upper_quartile, wide_candle_bodies | True | False | regime_ready |
| beh_04_low_volatility | low_volatility_behavior | dispersion_level | Subdued realized dispersion and narrow true range relative to historical baseline | regime_family_volatility | atr_subdued, realized_vol_lower_quartile, narrow_candle_bodies | True | False | regime_ready |
| beh_05_volatility_expansion | volatility_expansion_behavior | dispersion_dynamics | Rapid widening of Bollinger bandwidth and accelerating true range | regime_family_volatility | bollinger_bandwidth_widening, atr_acceleration_positive | True | False | regime_ready |
| beh_06_volatility_compression | volatility_compression_behavior | dispersion_dynamics | Squeezing of volatility bands and decelerating realized dispersion | regime_family_volatility | bollinger_bandwidth_squeeze, atr_acceleration_negative | True | False | regime_ready |
| beh_07_event_sensitive | event_sensitive_behavior | catalyst_sensitivity | Heightened sensitivity surrounding scheduled economic calendar events and announcements | regime_family_event_context | event_window_active, surprise_reaction_amplified | True | False | regime_ready |
| beh_08_macro_sensitive | macro_sensitive_behavior | macro_factor_alignment | Asset dynamics driven primarily by rate differential, inflation, and growth revisions | regime_family_macro_context | rate_diff_correlation, inflation_surprise_alignment | True | False | regime_ready |
| beh_09_cross_asset_sensitive | cross_asset_sensitive_behavior | intermarket_coupling | Behavior governed by macro benchmarks such as DXY, US10Y, SPX, or commodity spreads | regime_family_cross_asset_context | dxy_coupling_high, us10y_coupling_high, brent_wti_spread_impact | True | False | regime_ready |
| beh_10_liquidity_sensitive | liquidity_sensitive_placeholder | microstructure_placeholder | Placeholder behavior for spread widening, session transition, and quote staleness | regime_family_liquidity_placeholder | spread_widening_placeholder, off_session_staleness_placeholder | True | False | regime_placeholder_only |
| beh_11_transition_behavior | transition_behavior_placeholder | regime_shift_placeholder | Regime boundary transition placeholder indicating state instability or boundary crossing | regime_family_composite_placeholder | mixed_indicators, trend_breakdown, volatility_shift | True | False | regime_placeholder_only |
| beh_12_uncertain_behavior | uncertain_behavior_placeholder | diagnostics_placeholder | Uncertain behavior classification where contradictory factor metrics prevent clear attribution | regime_family_composite_placeholder | insufficient_quality_score, conflicting_factor_readings | True | False | regime_placeholder_only |