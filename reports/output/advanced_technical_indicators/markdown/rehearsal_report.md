# Phase 117 Indicator Computation Rehearsal Report

> **Yasal Uyarı / Sınır:** Bu çıktı Phase 117 Technical Indicator Expansion raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, indicator/feature değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, prediction/target/label üretimi, production deployment, model deployment, scraping, gerçek provider API çağrısı veya official approval değildir.

- **Toplam Prova Sayısı:** 62
- **Tüm Provalar Başarılı:** `True`
- **Input Mutation-Free:** `True`
- **Non-Signal Çıktı:** `True`

## Prova Sonuçları
| indicator_name          | status | no_mutation | no_forbidden_columns | output_column_count | output_columns                                                        |
| ----------------------- | ------ | ----------- | -------------------- | ------------------- | --------------------------------------------------------------------- |
| high_low_range          | PASS   | True        | True                 | 1                   | high_low_range                                                        |
| close_open_range        | PASS   | True        | True                 | 1                   | close_open_range                                                      |
| range_pct               | PASS   | True        | True                 | 1                   | range_pct                                                             |
| gap_from_prev_close     | PASS   | True        | True                 | 1                   | gap_from_prev_close                                                   |
| close_location_value    | PASS   | True        | True                 | 1                   | close_location_value                                                  |
| simple_return           | PASS   | True        | True                 | 1                   | simple_return_1                                                       |
| log_return              | PASS   | True        | True                 | 1                   | log_return_1                                                          |
| cumulative_return       | PASS   | True        | True                 | 1                   | cumulative_return_20                                                  |
| rolling_return_sum      | PASS   | True        | True                 | 1                   | rolling_return_sum_20                                                 |
| return_volatility_ratio | PASS   | True        | True                 | 1                   | return_vol_ratio_20                                                   |
| sma                     | PASS   | True        | True                 | 1                   | sma_20                                                                |
| ema                     | PASS   | True        | True                 | 1                   | ema_20                                                                |
| wma                     | PASS   | True        | True                 | 1                   | wma_20                                                                |
| dema                    | PASS   | True        | True                 | 1                   | dema_20                                                               |
| tema                    | PASS   | True        | True                 | 1                   | tema_20                                                               |
| ma_distance             | PASS   | True        | True                 | 1                   | ma_distance_20                                                        |
| macd                    | PASS   | True        | True                 | 3                   | macd_line, macd_smooth, macd_hist                                     |
| ppo                     | PASS   | True        | True                 | 3                   | ppo_line, ppo_smooth, ppo_hist                                        |
| donchian_channel        | PASS   | True        | True                 | 3                   | donchian_upper_20, donchian_lower_20, donchian_mid_20                 |
| aroon                   | PASS   | True        | True                 | 3                   | aroon_up_25, aroon_down_25, aroon_osc_25                              |
| adx_dmi                 | PASS   | True        | True                 | 3                   | adx_plus_di_14, adx_minus_di_14, adx_val_14                           |
| ichimoku                | PASS   | True        | True                 | 4                   | ichimoku_tenkan, ichimoku_kijun, ichimoku_senkou_a, ichimoku_senkou_b |
| momentum                | PASS   | True        | True                 | 1                   | momentum_10                                                           |
| roc                     | PASS   | True        | True                 | 1                   | roc_10                                                                |
| rsi                     | PASS   | True        | True                 | 1                   | rsi_14                                                                |
| cmo                     | PASS   | True        | True                 | 1                   | cmo_14                                                                |
| tsi                     | PASS   | True        | True                 | 1                   | tsi_25_13                                                             |
| stochastic              | PASS   | True        | True                 | 2                   | stoch_k_14, stoch_d_14_3                                              |
| williams_r              | PASS   | True        | True                 | 1                   | williams_r_14                                                         |
| cci                     | PASS   | True        | True                 | 1                   | cci_20                                                                |
| ultimate_oscillator     | PASS   | True        | True                 | 1                   | ultimate_osc                                                          |
| mfi                     | PASS   | True        | True                 | 1                   | mfi_14                                                                |
| true_range              | PASS   | True        | True                 | 1                   | true_range                                                            |
| atr                     | PASS   | True        | True                 | 1                   | atr_14                                                                |
| rolling_std             | PASS   | True        | True                 | 1                   | rolling_std_20                                                        |
| realized_volatility     | PASS   | True        | True                 | 1                   | realized_vol_20                                                       |
| parkinson_volatility    | PASS   | True        | True                 | 1                   | parkinson_vol_20                                                      |
| garman_klass_volatility | PASS   | True        | True                 | 1                   | garman_klass_vol_20                                                   |
| rolling_high_low_range  | PASS   | True        | True                 | 1                   | rolling_hl_range_20                                                   |
| rolling_range_pct       | PASS   | True        | True                 | 1                   | rolling_range_pct_20                                                  |
| average_range           | PASS   | True        | True                 | 1                   | average_range_20                                                      |
| range_zscore            | PASS   | True        | True                 | 1                   | range_zscore_20                                                       |
| bollinger_bands         | PASS   | True        | True                 | 3                   | bb_upper_20, bb_mid_20, bb_lower_20                                   |
| bollinger_bandwidth     | PASS   | True        | True                 | 1                   | bb_bandwidth_20                                                       |
| bollinger_percent_b     | PASS   | True        | True                 | 1                   | bb_percent_b_20                                                       |
| keltner_channel         | PASS   | True        | True                 | 3                   | keltner_upper_20, keltner_mid_20, keltner_lower_20                    |
| donchian_position       | PASS   | True        | True                 | 1                   | donchian_position_20                                                  |
| candle_body_size        | PASS   | True        | True                 | 1                   | candle_body_size                                                      |
| candle_body_pct         | PASS   | True        | True                 | 1                   | candle_body_pct                                                       |
| upper_wick_size         | PASS   | True        | True                 | 1                   | upper_wick_size                                                       |
| lower_wick_size         | PASS   | True        | True                 | 1                   | lower_wick_size                                                       |
| wick_balance            | PASS   | True        | True                 | 1                   | wick_balance                                                          |
| quote_mid               | PASS   | True        | True                 | 1                   | quote_mid                                                             |
| quote_spread            | PASS   | True        | True                 | 1                   | quote_spread                                                          |
| quote_spread_pct        | PASS   | True        | True                 | 1                   | quote_spread_pct                                                      |
| bid_ask_ratio           | PASS   | True        | True                 | 1                   | bid_ask_ratio_placeholder                                             |
| quote_staleness         | PASS   | True        | True                 | 1                   | quote_staleness_placeholder                                           |
| rolling_zscore          | PASS   | True        | True                 | 1                   | rolling_zscore_20                                                     |
| distance_to_sma         | PASS   | True        | True                 | 1                   | dist_to_sma_20                                                        |
| distance_to_ema         | PASS   | True        | True                 | 1                   | dist_to_ema_20                                                        |
| rolling_percentile_rank | PASS   | True        | True                 | 1                   | rolling_percentile_rank_100                                           |
| rolling_deviation_ratio | PASS   | True        | True                 | 1                   | rolling_deviation_ratio_20                                            |
