# Phase 126: Regime Environmental Contexts Report

> **UYARI / DISCLAIMER:** Bu çıktı Phase 126 Regime Classification and Market Behavior Foundation raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, regime state değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Özet
- **Bağlam Tipi:** `Macro Context`
- **Toplam Kayıt:** `5`
- **Haberler Sadece Metaveri:** `True`
- **Non-Signal:** `True`

## Bağlam Tablosu
| context_id | context_name | regime_family | description | underlying_features | source_phases | non_signal | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| macro_ctx_01_inflation | inflation_context | regime_family_macro_context | Inflation trajectory context tracking CPI/PPI surprises and headline vs core divergences | cpi_yoy_trend, ppi_momentum, inflation_surprise_index | [109, 120, 122] | True | regime_ready |
| macro_ctx_02_rate | rate_context | regime_family_macro_context | Central bank policy rate and sovereign yield curve differential context (e.g., Fed vs ECB / TCMB) | policy_rate_differential, 2y_yield_spread, 10y2y_curve_slope | [109, 120, 122] | True | regime_ready |
| macro_ctx_03_growth | growth_context | regime_family_macro_context | Economic growth momentum tracking manufacturing PMI, industrial production, and GDP revisions | pmi_composite, industrial_prod_growth, gdp_revision_trend | [109, 120, 122] | True | regime_ready |
| macro_ctx_04_revision | macro_revision_context | regime_family_macro_context | Systematic revisions to prior economic releases indicating historical bias or reporting lags | nfp_revision_magnitude, gdp_first_to_final_revision | [109, 110, 120] | True | regime_ready |
| macro_ctx_05_release | macro_release_context | regime_family_macro_context | Temporal proximity to major cyclical releases with publication time normalization | days_since_last_cpi, days_until_fomc_decision | [110, 120, 122] | True | regime_ready |