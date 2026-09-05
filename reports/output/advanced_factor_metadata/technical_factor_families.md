# Phase 122: Technical Factor Families Report

> **Yasal Uyarı**: Bu çıktı Phase 122 Factor Metadata and Factor Families raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, factor değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, sentiment model output, haber tam metni kullanımı, production-ready/official approval iddiası, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Technical Families Overview
- **Total Technical Factors**: 3
- **Non-Signal Verified**: True
- **Status**: `factor_ready`

## Factor Inventory
| factor_name | factor_family | input_features | calculation_type | non_signal_usage | status_label | manual_review_required |
| --- | --- | --- | --- | --- | --- | --- |
| technical_factor_overview | technical | ['ohlcv_derived_indicators'] | composite_indicator_metadata | Technical indicator feature space mapping. | factor_ready | False |
| indicator_based_factor_placeholder | technical | ['rsi', 'atr', 'sma', 'macd'] | normalized_technical_composite | Research placeholder for multi-indicator contextual feature. | factor_placeholder_only | True |
| multi_window_technical_context_placeholder | technical | ['multi_window_feature_grid'] | multi_window_cross_sectional_grid | Research placeholder for multi-window grid aggregator. | factor_placeholder_only | True |
