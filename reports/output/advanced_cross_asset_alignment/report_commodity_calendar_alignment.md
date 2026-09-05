# Phase 119: Commodity - Calendar Alignment Report

> Bu çıktı Phase 119 Cross-Asset Feature Alignment ve Multi-Domain Feature Matrix Contracts raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, cross-asset hizalanmış feature'ları trade sinyali veya çoklu varlık arbitraj/al-sat kuralı olarak kullanma, strateji üretimi, backtest, optimizer, target/label/prediction üretimi, production deployment, model deployment, scraping, gerçek provider API çağrısı veya official approval sağlamaz.

## Hizalama Özeti
- **Toplam Hizalama Bağlantısı**: 3
- **Non-Signal İzolasyonu**: `Doğrulandı`
- **Durum**: `READY`

## Hizalama Detayları

| alignment_id          | commodity_symbol                   | calendar_event                  | event_window_policy                | direction_claim_allowed | non_signal | notes                                                                  |
| --------------------- | ---------------------------------- | ------------------------------- | ---------------------------------- | ----------------------- | ---------- | ---------------------------------------------------------------------- |
| comcal_wti_eia_crude  | WTI_CRUDE_CONTINUOUS_PLACEHOLDER   | EIA_CRUDE_INVENTORY_RELEASE     | event_timestamp_backward_alignment | False                   | True       | Haftalık EIA ham petrol stok değişimi açıklanma anı takvim hizalaması. |
| comcal_ng_eia_storage | NATURAL_GAS_CONTINUOUS_PLACEHOLDER | EIA_NATURAL_GAS_STORAGE_RELEASE | event_timestamp_backward_alignment | False                   | True       | Haftalık EIA doğal gaz depolama değişimi olay penceresi.               |
| comcal_gold_fomc      | XAU/USD                            | FOMC_RATE_DECISION              | event_timestamp_backward_alignment | False                   | True       | Altın ve FOMC faiz kararı zaman penceresi eşlemesi.                    |
