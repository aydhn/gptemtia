# Phase 117 to Phase 118 Multi-Window Feature Grid Handoff Report

> **Yasal Uyarı / Sınır:** Bu çıktı Phase 117 Technical Indicator Expansion raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, indicator/feature değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, prediction/target/label üretimi, production deployment, model deployment, scraping, gerçek provider API çağrısı veya official approval değildir.

- **Devir Durumu:** `READY`
- **Hedef Faz:** 118
- **Devir Edilen Maddeler:** 10

## Devir Maddeleri
| domain                          | topic                                             | readiness | notes                                                                               |
| ------------------------------- | ------------------------------------------------- | --------- | ----------------------------------------------------------------------------------- |
| multi_window_moving_averages    | Multi-window SMA/EMA/WMA/DEMA grid                | READY     | Pencereler [5, 10, 20, 50, 100, 200] parametrik grid üretimine uygun.               |
| multi_window_momentum           | Multi-window RSI/ROC/Momentum grid                | READY     | RSI ve ROC için [7, 14, 21, 28] grid pencereleri hazır.                             |
| multi_window_volatility         | Multi-window ATR/Rolling STD/Realized Vol grid    | READY     | ATR ve oynaklık oranları pencereli yapıya uygun.                                    |
| multi_window_channels           | Multi-window Bollinger/Donchian grid              | READY     | Bant genişliği ve percent_b çoklu pencere üretimine hazır.                          |
| feature_naming_convention       | Grid feature adlandırma standardı                 | READY     | {indicator}_{window} formatı standartlaştırıldı.                                    |
| rolling_warmup_nan_handling     | Pencereye göre dinamik NaN politikası             | READY     | Pencere büyüdükçe beklenen NaN sayısı estimate_warmup_nan_count ile belirlenebilir. |
| no_lookahead_multi_window_guard | Çoklu pencere hesaplamalarında lookahead koruması | READY     | Tüm grid hesaplamaları geçmiş veriye dayalı (shift >= 0).                           |
| duplicate_feature_detection     | Tekrarlı feature kontrol altyapısı                | READY     | Aynı pencere ve indikatör için mükerrer kolon üretimi engellenir.                   |
| feature_dependency_expansion    | Bağımlılık grafiği genişletmesi                   | READY     | İndikatör girdi zincirleri indicator_dependency_registry ile hazırlandı.            |
| phase_121_validation_readiness  | Phase 121 doğrulama ve lookahead denetimine devir | READY     | Katmanlı no-lookahead ve non-signal sınırları devrediliyor.                         |
