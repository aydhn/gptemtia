# Phase 119: FX - Commodity Alignment Report

> Bu çıktı Phase 119 Cross-Asset Feature Alignment ve Multi-Domain Feature Matrix Contracts raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, cross-asset hizalanmış feature'ları trade sinyali veya çoklu varlık arbitraj/al-sat kuralı olarak kullanma, strateji üretimi, backtest, optimizer, target/label/prediction üretimi, production deployment, model deployment, scraping, gerçek provider API çağrısı veya official approval sağlamaz.

## Hizalama Özeti
- **Toplam Hizalama Bağlantısı**: 3
- **Non-Signal İzolasyonu**: `Doğrulandı`
- **Durum**: `READY`

## Hizalama Detayları

| alignment_id        | fx_pair | commodity_symbol                 | relation_type               | quote_currency | correlation_context_placeholder | non_signal | notes                                                                 |
| ------------------- | ------- | -------------------------------- | --------------------------- | -------------- | ------------------------------- | ---------- | --------------------------------------------------------------------- |
| fxc_eur_usd_xau_usd | EUR/USD | XAU/USD                          | dollar_denomination_context | USD            | rolling_corr_placeholder        | True       | Ortak karşıt para birimi (USD) bağlamı; sinyal içermez.               |
| fxc_usd_try_xau_usd | USD/TRY | XAU/USD                          | local_currency_gold_context | TRY            | gram_gold_synthetic_context     | True       | Yerel para birimi altın bağlamı (USD/TRY ve XAU/USD); sinyal üretmez. |
| fxc_usd_cad_wti     | USD/CAD | WTI_CRUDE_CONTINUOUS_PLACEHOLDER | petrocurrency_context       | USD            | energy_fx_context               | True       | Kanada Doları ve ham petrol ilişkisi araştırma bağlamı.               |
