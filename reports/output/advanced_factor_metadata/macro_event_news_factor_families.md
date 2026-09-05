# Phase 122: Macro, Calendar Event & News Factor Families Report

> **Yasal Uyarı**: Bu çıktı Phase 122 Factor Metadata and Factor Families raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, factor değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, sentiment model output, haber tam metni kullanımı, production-ready/official approval iddiası, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Macro & Event Factor Overview
- **Total Factors**: 5
- **Metadata-Only News Verified**: True
- **Point-in-Time Macro Verified**: True
- **Status**: `factor_ready`

## Factor Inventory
| factor_name | factor_family | input_features | calculation_type | non_signal_usage | status_label | manual_review_required |
| --- | --- | --- | --- | --- | --- | --- |
| factor_macro_inflation_context | macro_context | ['fusion__macro_cpi_rate', 'fusion__macro_ppi_rate'] | point_in_time_inflation_level | Inflation environment context. Backward-asof lagged only. | factor_ready | False |
| factor_macro_rate_context | macro_context | ['fusion__macro_policy_rate', 'fusion__macro_10y_yield'] | interest_rate_level_and_slope | Monetary policy rate backdrop observation. | factor_ready | False |
| factor_macro_growth_context | macro_context | ['fusion__macro_gdp_growth', 'fusion__macro_pmi'] | macro_growth_composite | Economic expansion and business cycle observation. | factor_ready | False |
| factor_macro_revision_context | macro_context | ['fusion__macro_revision_flag'] | vintage_revision_indicator | Data quality flag indicating post-release revision occurred. | factor_ready | False |
| factor_macro_surprise_placeholder_context | macro_context | ['fusion__macro_surprise_value'] | actual_vs_consensus_differential | Macroeconomic release surprise placeholder. | factor_placeholder_only | True |
