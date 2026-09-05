# Phase 119: Commodity - News Metadata Alignment Report

> Bu çıktı Phase 119 Cross-Asset Feature Alignment ve Multi-Domain Feature Matrix Contracts raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, cross-asset hizalanmış feature'ları trade sinyali veya çoklu varlık arbitraj/al-sat kuralı olarak kullanma, strateji üretimi, backtest, optimizer, target/label/prediction üretimi, production deployment, model deployment, scraping, gerçek provider API çağrısı veya official approval sağlamaz.

## Hizalama Özeti
- **Toplam Hizalama Bağlantısı**: 4
- **Non-Signal İzolasyonu**: `Doğrulandı`
- **Durum**: `READY`

## Hizalama Detayları

| alignment_id                 | commodity_symbol                   | news_tag        | metadata_only | full_text_collected | sentiment_signal_allowed | non_signal | notes                                                       |
| ---------------------------- | ---------------------------------- | --------------- | ------------- | ------------------- | ------------------------ | ---------- | ----------------------------------------------------------- |
| comnews_wti_crude_tag        | WTI_CRUDE_CONTINUOUS_PLACEHOLDER   | CRUDE_OIL       | True          | False               | False                    | True       | Ham petrol haber başlığı ve konu metadata etiketi eşlemesi. |
| comnews_wti_energy_tag       | WTI_CRUDE_CONTINUOUS_PLACEHOLDER   | ENERGY          | True          | False               | False                    | True       | Enerji sektörü haber etiketi; makale metni toplanmaz.       |
| comnews_gold_precious_metals | XAU/USD                            | PRECIOUS_METALS | True          | False               | False                    | True       | Kıymetli madenler haber etiketi eşlemesi.                   |
| comnews_ng_energy_tag        | NATURAL_GAS_CONTINUOUS_PLACEHOLDER | NATURAL_GAS     | True          | False               | False                    | True       | Doğal gaz depolama/arz haber etiketi eşlemesi.              |
