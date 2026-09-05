# Phase 118: Indicator Parameter Grid Registry Report

> Bu çıktı Phase 118 Multi-Window Feature Grid raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, feature grid değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, prediction/target/label üretimi, production deployment, model deployment, scraping, gerçek provider API çağrısı veya official approval değildir.

## Parametre Grid Özeti
- **Toplam Grid Sayısı**: 11
- **Toplam Aile**: 6
- **Beklenen Toplam Feature Sayısı**: 54
- **Non-Signal**: True
- **Durum**: `READY`

## Parametre Gridleri

| grid_id                            | indicator_name      | indicator_family | parameter_grid                                       | output_naming_template    | expected_output_count | non_signal | manual_review_required |
| ---------------------------------- | ------------------- | ---------------- | ---------------------------------------------------- | ------------------------- | --------------------- | ---------- | ---------------------- |
| ipg_moving_average_sma             | sma                 | moving_average   | {'window': [5, 10, 20, 50, 100, 200]}                | sma_w{window}             | 6                     | True       | False                  |
| ipg_moving_average_ema             | ema                 | moving_average   | {'window': [5, 10, 20, 50, 100, 200]}                | ema_w{window}             | 6                     | True       | False                  |
| ipg_moving_average_wma             | wma                 | moving_average   | {'window': [5, 10, 20, 50]}                          | wma_w{window}             | 4                     | True       | False                  |
| ipg_momentum_rsi                   | rsi                 | momentum         | {'window': [7, 14, 21, 28]}                          | rsi_w{window}             | 4                     | True       | False                  |
| ipg_momentum_roc                   | roc                 | momentum         | {'window': [5, 10, 20, 30]}                          | roc_w{window}             | 4                     | True       | False                  |
| ipg_volatility_atr                 | atr                 | volatility       | {'window': [7, 14, 20, 30]}                          | atr_w{window}             | 4                     | True       | False                  |
| ipg_range_channel_bollinger        | bollinger           | range_channel    | {'window': [10, 20, 30], 'num_std': [1.5, 2.0, 2.5]} | bb_w{window}_std{num_std} | 9                     | True       | False                  |
| ipg_range_channel_donchian         | donchian            | range_channel    | {'window': [10, 20, 55]}                             | donchian_w{window}        | 3                     | True       | False                  |
| ipg_mean_reversion_rolling_zscore  | rolling_zscore      | mean_reversion   | {'window': [10, 20, 50, 100]}                        | zscore_w{window}          | 4                     | True       | False                  |
| ipg_volatility_realized_volatility | realized_volatility | volatility       | {'window': [5, 10, 20, 30, 60]}                      | realized_vol_w{window}    | 5                     | True       | False                  |
| ipg_return_simple_return           | simple_return       | return           | {'window': [1, 3, 5, 10, 20]}                        | return_w{window}          | 5                     | True       | False                  |
