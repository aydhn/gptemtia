# Phase 119: Timestamp & Session Alignment Report

> Bu çıktı Phase 119 Cross-Asset Feature Alignment ve Multi-Domain Feature Matrix Contracts raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, cross-asset hizalanmış feature'ları trade sinyali veya çoklu varlık arbitraj/al-sat kuralı olarak kullanma, strateji üretimi, backtest, optimizer, target/label/prediction üretimi, production deployment, model deployment, scraping, gerçek provider API çağrısı veya official approval sağlamaz.

## Zaman & Seans Özeti
- **Zaman Damgası Sözleşmeleri**: 0
- **Seans Politikaları**: 7
- **UTC Standartlaştırma**: `Zorunlu`
- **Durum**: `READY`

## Detay Tablosu

| session_policy                    | description                                                                        | bucket_granularity |
| --------------------------------- | ---------------------------------------------------------------------------------- | ------------------ |
| utc_day                           | UTC gün kovası (YYYY-MM-DD), standart günlük hizalama için kullanılır.             | 1d                 |
| utc_hour                          | UTC saatlik kova (YYYY-MM-DDTHH:00:00Z), saatlik çubuk hizalama için kullanılır.   | 1h                 |
| fx_24_5_placeholder               | FX 24/5 işlem seansı kovası; Pazar açılışı ve Cuma kapanışı aralığını temsil eder. | session_week       |
| commodity_session_placeholder     | Emtia elektronik işlem saatleri (CME/NYMEX) seans kovası.                          | session_daily      |
| macro_release_session_placeholder | Makro veri yayın saatleri (ör. 08:30 ET / 12:30 UTC) seans öncesi/sonrası kovası.  | event_session      |
| calendar_event_window_placeholder | Ekonomik takvim olay penceresi kovası (duyuru anı +/- tolerans penceresi).         | window             |
| news_metadata_window_placeholder  | Haber metadata kümelenme penceresi kovası (4h / 24h konu etiketleri).              | metadata_window    |
