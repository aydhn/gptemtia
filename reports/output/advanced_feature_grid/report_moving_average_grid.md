# Phase 118: Window Grid Family Report

> Bu çıktı Phase 118 Multi-Window Feature Grid raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, feature grid değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, prediction/target/label üretimi, production deployment, model deployment, scraping, gerçek provider API çağrısı veya official approval değildir.

## Aile Özeti
- **Toplam Grid Feature**: 22
- **Toplam İndikatör**: 5
- **Non-Signal**: True
- **Durum**: `READY`

## Grid Feature Listesi

| grid_name        | indicator_name | family         | window | column_name | non_signal | lookahead_free | performance_tier |
| ---------------- | -------------- | -------------- | ------ | ----------- | ---------- | -------------- | ---------------- |
| sma_window_grid  | sma            | moving_average | 5      | sma_w5      | True       | True           | light            |
| sma_window_grid  | sma            | moving_average | 10     | sma_w10     | True       | True           | light            |
| sma_window_grid  | sma            | moving_average | 20     | sma_w20     | True       | True           | light            |
| sma_window_grid  | sma            | moving_average | 50     | sma_w50     | True       | True           | light            |
| sma_window_grid  | sma            | moving_average | 100    | sma_w100    | True       | True           | standard         |
| sma_window_grid  | sma            | moving_average | 200    | sma_w200    | True       | True           | standard         |
| ema_window_grid  | ema            | moving_average | 5      | ema_w5      | True       | True           | light            |
| ema_window_grid  | ema            | moving_average | 10     | ema_w10     | True       | True           | light            |
| ema_window_grid  | ema            | moving_average | 20     | ema_w20     | True       | True           | light            |
| ema_window_grid  | ema            | moving_average | 50     | ema_w50     | True       | True           | light            |
| ema_window_grid  | ema            | moving_average | 100    | ema_w100    | True       | True           | standard         |
| ema_window_grid  | ema            | moving_average | 200    | ema_w200    | True       | True           | standard         |
| wma_window_grid  | wma            | moving_average | 5      | wma_w5      | True       | True           | light            |
| wma_window_grid  | wma            | moving_average | 10     | wma_w10     | True       | True           | light            |
| wma_window_grid  | wma            | moving_average | 20     | wma_w20     | True       | True           | light            |
| wma_window_grid  | wma            | moving_average | 50     | wma_w50     | True       | True           | light            |
| dema_window_grid | dema           | moving_average | 10     | dema_w10    | True       | True           | light            |
| dema_window_grid | dema           | moving_average | 20     | dema_w20    | True       | True           | light            |
| dema_window_grid | dema           | moving_average | 50     | dema_w50    | True       | True           | light            |
| tema_window_grid | tema           | moving_average | 10     | tema_w10    | True       | True           | light            |
| tema_window_grid | tema           | moving_average | 20     | tema_w20    | True       | True           | light            |
| tema_window_grid | tema           | moving_average | 50     | tema_w50    | True       | True           | light            |
