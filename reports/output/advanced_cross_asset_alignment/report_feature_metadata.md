# Phase 119: Feature Namespace Standard Report

> Bu çıktı Phase 119 Cross-Asset Feature Alignment ve Multi-Domain Feature Matrix Contracts raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, cross-asset hizalanmış feature'ları trade sinyali veya çoklu varlık arbitraj/al-sat kuralı olarak kullanma, strateji üretimi, backtest, optimizer, target/label/prediction üretimi, production deployment, model deployment, scraping, gerçek provider API çağrısı veya official approval sağlamaz.

## Ad Alanı Standardı Özeti
- **Toplam Tanımlı Feature**: 6
- **Format**: `<domain>__<family>__<source_symbol>__<feature_name>__<window>`
- **Kapsanan Domainler**: fx, commodity, macro, calendar, news
- **Durum**: `READY`

## Tanımlı Feature İsimleri

| feature_name                       | source_domain | aligned_domain | canonical_symbol   | namespace                   | timestamp_policy | join_policy                          | no_lookahead_checked | non_signal | phase_120_fusion_ready | manual_review_required |
| ---------------------------------- | ------------- | -------------- | ------------------ | --------------------------- | ---------------- | ------------------------------------ | -------------------- | ---------- | ---------------------- | ---------------------- |
| fx_eur_usd_sma_w20                 | fx            | fx             | EUR/USD            | fx_eur_usd                  | canonical_utc    | join_policy_exact_timestamp          | True                 | True       | True                   | False                  |
| fx_eur_usd_rsi_w14                 | fx            | fx             | EUR/USD            | fx_eur_usd                  | canonical_utc    | join_policy_exact_timestamp          | True                 | True       | True                   | False                  |
| commodity_xau_usd_close            | commodity     | fx             | XAU/USD            | commodity_xau_usd           | canonical_utc    | join_policy_asof_backward            | True                 | True       | True                   | False                  |
| macro_us_10y_yield_yield_diff_1d   | macro         | fx             | US_10Y_YIELD       | macro_us_10y_yield          | canonical_utc    | join_policy_asof_backward            | True                 | True       | True                   | False                  |
| calendar_fomc_event_active_window  | calendar      | fx             | FOMC_RATE_DECISION | calendar_fomc_rate_decision | canonical_utc    | join_policy_event_window_placeholder | True                 | True       | True                   | False                  |
| news_central_bank_mention_count_1d | news          | fx             | CENTRAL_BANK       | news_central_bank           | canonical_utc    | join_policy_metadata_tag_link        | True                 | True       | True                   | False                  |
