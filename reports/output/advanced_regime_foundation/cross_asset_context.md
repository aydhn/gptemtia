# Phase 126: Regime Environmental Contexts Report

> **UYARI / DISCLAIMER:** Bu çıktı Phase 126 Regime Classification and Market Behavior Foundation raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, regime state değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Özet
- **Bağlam Tipi:** `Cross-Asset Context`
- **Toplam Kayıt:** `6`
- **Haberler Sadece Metaveri:** `True`
- **Non-Signal:** `True`

## Bağlam Tablosu
| context_id | context_name | regime_family | description | coupled_assets | source_phases | non_signal | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cross_ctx_01_fx_comm | fx_commodity_context | regime_family_cross_asset_context | Intermarket dynamics between USD pairs and gold/oil (e.g. XAU/USD vs USD/TRY, WTI vs DXY) | EUR_USD, USD_TRY, XAU_USD, WTI_CRUDE | [119, 122] | True | regime_ready |
| cross_ctx_02_fx_macro | fx_macro_context | regime_family_cross_asset_context | Sensitivity of foreign exchange pairs to rate differential expectations and DXY index | EUR_USD, USD_TRY, DXY_INDEX, US10Y_YIELD | [119, 120, 122] | True | regime_ready |
| cross_ctx_03_comm_macro | commodity_macro_context | regime_family_cross_asset_context | Sensitivity of commodities (gold, energy) to real yields, breakeven inflation, and global PMI | XAU_USD, BRENT_CRUDE, US_TIPS_10Y, GLOBAL_PMI | [119, 120, 122] | True | regime_ready |
| cross_ctx_04_macro_cal | macro_calendar_context | regime_family_cross_asset_context | Coupling of cyclical economic releases with sovereign yield curve repositioning | CALENDAR_EVENTS, US2Y_YIELD, US10Y_YIELD | [110, 120, 122] | True | regime_ready |
| cross_ctx_05_cal_news | calendar_news_context | regime_family_cross_asset_context | Temporal alignment between scheduled event publication windows and surge in headline volume | ECONOMIC_CALENDAR, NEWS_METADATA_STREAM | [110, 111, 120] | True | regime_ready |
| cross_ctx_06_cross_domain | cross_domain_context_placeholder | regime_family_cross_asset_context | Placeholder for multi-asset composite spillover indexes and cross-correlation matrix eigenvalues | FULL_CROSS_ASSET_UNIVERSE | [119, 122, 124] | True | regime_placeholder_only |