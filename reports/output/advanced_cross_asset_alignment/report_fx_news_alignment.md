# Phase 119: FX - News Metadata Alignment Report

> Bu çıktı Phase 119 Cross-Asset Feature Alignment ve Multi-Domain Feature Matrix Contracts raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, cross-asset hizalanmış feature'ları trade sinyali veya çoklu varlık arbitraj/al-sat kuralı olarak kullanma, strateji üretimi, backtest, optimizer, target/label/prediction üretimi, production deployment, model deployment, scraping, gerçek provider API çağrısı veya official approval sağlamaz.

## Hizalama Özeti
- **Toplam Hizalama Bağlantısı**: 4
- **Non-Signal İzolasyonu**: `Doğrulandı`
- **Durum**: `READY`

## Hizalama Detayları

| alignment_id                | fx_pair | news_tag       | metadata_only | full_text_collected | sentiment_signal_allowed | non_signal | notes                                                                                      |
| --------------------------- | ------- | -------------- | ------------- | ------------------- | ------------------------ | ---------- | ------------------------------------------------------------------------------------------ |
| fxnews_eur_usd_central_bank | EUR/USD | CENTRAL_BANK   | True          | False               | False                    | True       | Merkez bankası haber başlığı konusu; tam metin indirilmez, sentiment trade sinyali olamaz. |
| fxnews_eur_usd_inflation    | EUR/USD | INFLATION      | True          | False               | False                    | True       | Enflasyon haber metadata etiketi eşlemesi.                                                 |
| fxnews_usd_try_turkey       | USD/TRY | TURKEY_ECONOMY | True          | False               | False                    | True       | Türkiye ekonomisi haber metadata konusu bağlantısı.                                        |
| fxnews_global_risk          | EUR/USD | RISK_SENTIMENT | True          | False               | False                    | True       | Küresel risk iştahı başlık etiketi; telifli içerik kopyalanmaz.                            |
