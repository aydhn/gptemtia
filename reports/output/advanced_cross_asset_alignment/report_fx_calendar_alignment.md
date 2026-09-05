# Phase 119: FX - Calendar Alignment Report

> Bu çıktı Phase 119 Cross-Asset Feature Alignment ve Multi-Domain Feature Matrix Contracts raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, cross-asset hizalanmış feature'ları trade sinyali veya çoklu varlık arbitraj/al-sat kuralı olarak kullanma, strateji üretimi, backtest, optimizer, target/label/prediction üretimi, production deployment, model deployment, scraping, gerçek provider API çağrısı veya official approval sağlamaz.

## Hizalama Özeti
- **Toplam Hizalama Bağlantısı**: 5
- **Non-Signal İzolasyonu**: `Doğrulandı`
- **Durum**: `READY`

## Hizalama Detayları

| alignment_id       | fx_pair | calendar_event              | event_window_policy               | direction_claim_allowed | non_signal | notes                                                                    |
| ------------------ | ------- | --------------------------- | --------------------------------- | ----------------------- | ---------- | ------------------------------------------------------------------------ |
| fxcal_eur_usd_fomc | EUR/USD | FOMC_RATE_DECISION          | pre_post_event_window_placeholder | False                   | True       | FOMC faiz duyurusu penceresi; yönlü beklenti ve işlem tavsiyesi içermez. |
| fxcal_eur_usd_ecb  | EUR/USD | ECB_RATE_DECISION           | pre_post_event_window_placeholder | False                   | True       | ECB faiz duyurusu penceresi; tarafsız olay zamanı eşlemesi.              |
| fxcal_eur_usd_nfp  | EUR/USD | US_NONFARM_PAYROLLS_RELEASE | pre_post_event_window_placeholder | False                   | True       | ABD Tarım Dışı İstihdam veri açıklanma anı hizalaması.                   |
| fxcal_usd_try_cbrt | USD/TRY | CBRT_RATE_DECISION          | pre_post_event_window_placeholder | False                   | True       | TCMB Para Politikası Kurulu faiz kararı takvim hizalaması.               |
| fxcal_usd_try_cpi  | USD/TRY | TR_CPI_RELEASE              | pre_post_event_window_placeholder | False                   | True       | TÜİK enflasyon verisi açıklanma anı pencere hizalaması.                  |
