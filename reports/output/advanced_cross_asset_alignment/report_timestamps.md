# Phase 119: Timestamp & Session Alignment Report

> Bu çıktı Phase 119 Cross-Asset Feature Alignment ve Multi-Domain Feature Matrix Contracts raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, cross-asset hizalanmış feature'ları trade sinyali veya çoklu varlık arbitraj/al-sat kuralı olarak kullanma, strateji üretimi, backtest, optimizer, target/label/prediction üretimi, production deployment, model deployment, scraping, gerçek provider API çağrısı veya official approval sağlamaz.

## Zaman & Seans Özeti
- **Zaman Damgası Sözleşmeleri**: 5
- **Seans Politikaları**: 0
- **UTC Standartlaştırma**: `Zorunlu`
- **Durum**: `READY`

## Detay Tablosu

| contract_id                     | domain    | canonical_timestamp_format | timezone | max_backward_lag | future_data_allowed | description                                                                       |
| ------------------------------- | --------- | -------------------------- | -------- | ---------------- | ------------------- | --------------------------------------------------------------------------------- |
| tac_fx_daily_utc                | fx        | YYYY-MM-DDTHH:MM:SSZ       | UTC      | 24h              | False               | FX günlük çubukları için UTC bazlı zaman hizalama sözleşmesi.                     |
| tac_commodity_daily_utc         | commodity | YYYY-MM-DDTHH:MM:SSZ       | UTC      | 24h              | False               | Emtia sürekli kontratları için UTC bazlı zaman hizalama sözleşmesi.               |
| tac_macro_release_lag_utc       | macro     | YYYY-MM-DDTHH:MM:SSZ       | UTC      | 90d              | False               | Makro veri açıklamaları için kesin geçmiş tarihli (<= bar) asof bağlantı kuralı.  |
| tac_calendar_event_window_utc   | calendar  | YYYY-MM-DDTHH:MM:SSZ       | UTC      | 7d               | False               | Ekonomik takvim duyuruları için olay anı ve öncesi pencere hizalaması.            |
| tac_news_metadata_timestamp_utc | news      | YYYY-MM-DDTHH:MM:SSZ       | UTC      | 48h              | False               | Haber metadata etiketleri için yayın anı timestamp eşleme kuralı (metadata-only). |
