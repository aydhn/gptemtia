# Phase 119: Calendar - News Metadata Alignment Report

> Bu çıktı Phase 119 Cross-Asset Feature Alignment ve Multi-Domain Feature Matrix Contracts raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, cross-asset hizalanmış feature'ları trade sinyali veya çoklu varlık arbitraj/al-sat kuralı olarak kullanma, strateji üretimi, backtest, optimizer, target/label/prediction üretimi, production deployment, model deployment, scraping, gerçek provider API çağrısı veya official approval sağlamaz.

## Hizalama Özeti
- **Toplam Hizalama Bağlantısı**: 4
- **Non-Signal İzolasyonu**: `Doğrulandı`
- **Durum**: `READY`

## Hizalama Detayları

| alignment_id              | calendar_event              | news_topic   | linkage_type     | full_text_collected | sentiment_signal_allowed | non_signal | notes                                                                          |
| ------------------------- | --------------------------- | ------------ | ---------------- | ------------------- | ------------------------ | ---------- | ------------------------------------------------------------------------------ |
| calnews_fomc_central_bank | FOMC_RATE_DECISION          | CENTRAL_BANK | event_topic_link | False               | False                    | True       | FOMC kararı ve merkez bankası haber konusu bağlantısı; makale metni toplanmaz. |
| calnews_cpi_inflation     | US_CPI_RELEASE              | INFLATION    | event_topic_link | False               | False                    | True       | Enflasyon takvimi ve enflasyon haber konu başlığı eşlemesi.                    |
| calnews_eia_energy        | EIA_CRUDE_INVENTORY_RELEASE | CRUDE_OIL    | event_topic_link | False               | False                    | True       | EIA ham petrol stok duyurusu ve ham petrol haber etiketleri eşlemesi.          |
| calnews_nfp_labor         | US_NONFARM_PAYROLLS_RELEASE | LABOR_MARKET | event_topic_link | False               | False                    | True       | Tarım dışı istihdam verisi ve istihdam piyasası haber etiketleri eşlemesi.     |
