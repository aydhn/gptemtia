# Phase 118: Feature Grid Computation Rehearsal Report

> Bu çıktı Phase 118 Multi-Window Feature Grid raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, feature grid değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, prediction/target/label üretimi, production deployment, model deployment, scraping, gerçek provider API çağrısı veya official approval değildir.

## Prova ve Doğrulama Özeti
- **Toplam Prova Koşumu**: 7
- **Tüm Provalar Başarılı**: True
- **In-Place Mutasyon Engellendi**: True
- **Üretilen Toplam Feature**: 60
- **Non-Signal**: True
- **Durum**: `PASS`

## Prova Detayları

| rehearsal_name      | input_rows | generated_features_count | in_place_mutated | forbidden_columns_count | max_warmup_nan | status |
| ------------------- | ---------- | ------------------------ | ---------------- | ----------------------- | -------------- | ------ |
| moving_average_grid | 120        | 6                        | False            | 0                       | 19             | PASS   |
| momentum_grid       | 120        | 9                        | False            | 0                       | 21             | PASS   |
| volatility_grid     | 120        | 9                        | False            | 0                       | 20             | PASS   |
| bollinger_grid      | 120        | 16                       | False            | 0                       | 19             | PASS   |
| donchian_grid       | 120        | 8                        | False            | 0                       | 19             | PASS   |
| mean_reversion_grid | 120        | 6                        | False            | 0                       | 19             | PASS   |
| return_grid         | 120        | 6                        | False            | 0                       | 5              | PASS   |
