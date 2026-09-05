# Phase 119: FX - Macro Alignment Report

> Bu çıktı Phase 119 Cross-Asset Feature Alignment ve Multi-Domain Feature Matrix Contracts raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, cross-asset hizalanmış feature'ları trade sinyali veya çoklu varlık arbitraj/al-sat kuralı olarak kullanma, strateji üretimi, backtest, optimizer, target/label/prediction üretimi, production deployment, model deployment, scraping, gerçek provider API çağrısı veya official approval sağlamaz.

## Hizalama Özeti
- **Toplam Hizalama Bağlantısı**: 5
- **Non-Signal İzolasyonu**: `Doğrulandı`
- **Durum**: `READY`

## Hizalama Detayları

| alignment_id      | fx_pair | macro_indicator    | indicator_category | macro_context_placeholder  | non_signal | notes                                                              |
| ----------------- | ------- | ------------------ | ------------------ | -------------------------- | ---------- | ------------------------------------------------------------------ |
| fxm_eur_usd_rates | EUR/USD | FED_POLICY_RATE    | central_bank_rate  | rate_differential_context  | True       | Fed politika faizi; trade sinyali veya kesin yön tahmini değildir. |
| fxm_eur_usd_ecb   | EUR/USD | ECB_POLICY_RATE    | central_bank_rate  | ecb_rate_context           | True       | ECB politika faizi bağlamı; sinyal içermez.                        |
| fxm_eur_usd_dxy   | EUR/USD | DXY_PLACEHOLDER    | dollar_index       | dxy_inverse_context        | True       | Dolar endeksi bağlamı; sinyal üretimi kesin yasaktır.              |
| fxm_usd_try_cbrt  | USD/TRY | CBRT_POLICY_RATE   | central_bank_rate  | cbrt_one_week_repo_context | True       | TCMB bir hafta vadeli repo faizi bağlamı; araştırma amaçlıdır.     |
| fxm_usd_try_cpi   | USD/TRY | TR_CPI_PLACEHOLDER | inflation          | tr_cpi_context             | True       | Yurt içi TÜFE yıllık/aylık değişim bağlamı.                        |
