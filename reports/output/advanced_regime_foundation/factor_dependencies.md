# Phase 126: Regime Contracts and Dependencies Report

> **UYARI / DISCLAIMER:** Bu çıktı Phase 126 Regime Classification and Market Behavior Foundation raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, regime state değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Özet
- **Toplam Bağımlılık / Sözleşme:** `15`
- **Tüm Bağımlılıklar Doğrulandı:** `True`
- **No-Lookahead Zorunlu:** `True`
- **Non-Signal Zorunlu:** `True`

## Bağımlılıklar Tablosu
| dependency_id | target_regime_family | dependency_type | source_phase | prerequisite_name | description | verification_status | non_signal | blocking |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dep_01_vol_factor | regime_family_volatility | factor | 122 | Phase 122 Volatility Factor Families | Requires realized volatility, ATR, Parkinson, and Bollinger width factor definitions | VERIFIED | True | True |
| dep_02_vol_quality | regime_family_volatility | quality | 123 | Phase 123 Volatility Quality & Drift Diagnostics | Requires missingness and stability scores for volatility indicators | VERIFIED | True | True |
| dep_03_trend_factor | regime_family_trend | factor | 122 | Phase 122 Trend Factor Families | Requires moving average slope, trend alignment, and Donchian channel factor definitions | VERIFIED | True | True |
| dep_04_trend_quality | regime_family_trend | quality | 123 | Phase 123 Trend Quality & Drift Diagnostics | Requires drift bounds and stability metrics for trend indicators | VERIFIED | True | True |
| dep_05_range_factor | regime_family_range | factor | 122 | Phase 122 Mean-Reversion and Range Factors | Requires z-score, mean distance, and range-boundedness factors | VERIFIED | True | True |
| dep_06_macro_fusion | regime_family_macro_context | feature_fusion | 120 | Phase 120 Macro Feature Fusion | Requires point-in-time publication lag aligned macro features | VERIFIED | True | True |
| dep_07_macro_factor | regime_family_macro_context | factor | 122 | Phase 122 Macro Context Factors | Requires inflation surprise and rate differential factor definitions | VERIFIED | True | True |
| dep_08_event_fusion | regime_family_event_context | feature_fusion | 120 | Phase 120 Calendar Event Windows | Requires pre/post announcement time envelopes | VERIFIED | True | True |
| dep_09_event_factor | regime_family_event_context | factor | 122 | Phase 122 Calendar Event Factors | Requires event importance and release delay factors | VERIFIED | True | True |
| dep_10_news_fusion | regime_family_news_metadata_context | feature_fusion | 120 | Phase 120 News Metadata Features | Requires strictly metadata-only news volume and topic tags | VERIFIED | True | True |
| dep_11_news_factor | regime_family_news_metadata_context | factor | 122 | Phase 122 News Attention Factors | Requires headline count and topic concentration factors | VERIFIED | True | True |
| dep_12_cross_asset_align | regime_family_cross_asset_context | alignment | 119 | Phase 119 Cross-Asset Feature Alignment | Requires synchronized multi-domain timestamp alignment across FX and commodities | VERIFIED | True | True |
| dep_13_cross_asset_factor | regime_family_cross_asset_context | factor | 122 | Phase 122 Cross-Asset Factors | Requires DXY, US10Y, and intermarket spread coupling factors | VERIFIED | True | True |
| dep_14_all_regimes_val | all_regime_families | validation | 121 | Phase 121 Feature Validation and No-Lookahead Guard | Requires no-lookahead and forbidden column verification across all inputs | VERIFIED | True | True |
| dep_15_all_regimes_store | all_regime_families | feature_store | 124 | Phase 124 FeatureStore Metadata | Requires central store registry entries and point-in-time query contracts | VERIFIED | True | True |