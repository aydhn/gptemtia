# Phase 126: Master Regime Family Registry Report

> **UYARI / DISCLAIMER:** Bu çıktı Phase 126 Regime Classification and Market Behavior Foundation raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, regime state değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Özet
- **Toplam Rejim Aileleri:** `9`
- **Hazır Aileler:** `7`
- **Yer Tutucu Aileler:** `2`
- **Model Eğitimi Çalıştırıldı mı:** `False`
- **Kümeleme (Clustering) Çalıştırıldı mı:** `False`
- **Non-Signal:** `True`

## Rejim Aileleri Tablosu
| family_id | family_name | family_category | description | primary_indicators | source_phases | non_signal | model_training_executed | clustering_executed | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fam_01_volatility | regime_family_volatility | dispersion_analysis | Volatility regime family analyzing realized volatility, ATR, and Bollinger bandwidth envelopes | atr, realized_volatility, bollinger_bandwidth, rolling_std | [117, 118, 122, 124] | True | False | False | regime_ready |
| fam_02_trend | regime_family_trend | directional_alignment | Trend regime family evaluating moving average slopes, Donchian channels, and trend persistence | sma_slope, ema_alignment, donchian_channel, adx_dmi | [117, 118, 122, 124] | True | False | False | regime_ready |
| fam_03_range | regime_family_range | mean_reversion | Range regime family assessing mean-reversion, zscore bounds, and channel envelope positions | rolling_zscore, bollinger_percent_b, channel_position, range_zscore | [117, 118, 122, 124] | True | False | False | regime_ready |
| fam_04_liquidity | regime_family_liquidity_placeholder | microstructure_placeholder | Liquidity regime placeholder tracking spread, staleness, and trading session alignment | quote_spread, quote_staleness, session_status | [117, 122, 124] | True | False | False | regime_placeholder_only |
| fam_05_macro | regime_family_macro_context | macroeconomic_environment | Macro regime context family analyzing inflation trends, rate differentials, and growth revisions | inflation_trend, rate_differential, growth_revisions | [109, 120, 122, 124] | True | False | False | regime_ready |
| fam_06_event | regime_family_event_context | scheduled_catalysts | Event regime context family evaluating pre/post event windows, release delays, and event importance | event_window_minutes, importance_score, release_delay_minutes | [110, 120, 122, 124] | True | False | False | regime_ready |
| fam_07_news | regime_family_news_metadata_context | news_metadata_attention | News metadata regime context analyzing count, topic concentration, and freshness without text/embeddings | news_item_count_1h, topic_entropy, news_freshness_minutes | [111, 120, 122, 124] | True | False | False | regime_ready |
| fam_08_cross_asset | regime_family_cross_asset_context | intermarket_dynamics | Cross-asset regime context evaluating DXY, US10Y, SPX coupling and commodity cross-spreads | dxy_rolling_corr, us10y_rolling_corr, brent_wti_spread | [119, 122, 124] | True | False | False | regime_ready |
| fam_09_composite | regime_family_composite_placeholder | multi_factor_synthesis | Composite regime placeholder for multi-family cross-checks, stability analysis, and transition detection | consensus_score, stability_index, transition_flag | [122, 123, 124, 125] | True | False | False | regime_placeholder_only |