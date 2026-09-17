# Phase 146: Slippage Models Report

> **YASAL UYARI VE GUCLENDIRILMIS GUVENLIK SINIRI (PHASE 146)**:
> Bu cikti Phase 146 Realistic Backtest, Transaction Cost and Slippage Modeling raporudur. Canli emir, broker talimati, kesin AL/SAT, yatirim tavsiyesi, backtest/readiness/cost/slippage degerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gercek backtest execution, walk-forward, benchmark, optimizer, stress test, Monte Carlo, gercek model training, model fit/predict/inference, dataset materialization, target/label/prediction uretimi, gercek performans garantisi, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanimi veya gercek provider API cagrisi degildir.

## Slippage Models Summary
- **Total Slippage Models**: 6
- **Zero Performance Guarantee**: True

## Slippage Models Table

| slippage_model_name | slippage_type | description | formula | default_parameter | real_slippage_calculated | performance_guaranteed | is_active | non_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fixed_bps_slippage_contract | FIXED_BPS | Her islem icin sabit baz puan (orn: 3 bps) fiyattan olumsuz kayma sozlesmesi. | price * (fixed_bps / 10000.0) | {'bps': 3.0} | False | False | True | True |
| spread_based_slippage_contract | SPREAD_BASED | Alis-satis makasinin bir carpani olarak hesaplanan kayma modeli. | spread * spread_multiplier | {'spread_multiplier': 0.5} | False | False | True | True |
| volatility_based_slippage_contract | VOLATILITY_BASED | ATR veya gerceklesen volatiliteye bagli dinamik kayma sozlesmesi. | volatility_factor * ATR_14 | {'volatility_factor': 0.1} | False | False | True | True |
| liquidity_based_slippage_contract | LIQUIDITY_BASED | Emir hacminin ortalama gunluk hacme oranina gore artan kayma modeli. | base_slippage * (order_size / (ADV_20 * max_participation)) ** alpha | {'alpha': 0.5, 'max_participation': 0.1} | False | False | True | True |
| participation_rate_slippage_contract | PARTICIPATION_RATE | Piyasa katilim oranina dayali piyasa etki ve kayma modeli. | gamma * participation_rate ** 0.5 | {'gamma': 0.05} | False | False | True | True |
| regime_aware_slippage_contract | REGIME_AWARE | Phase 126-135 rejim durumuna (Stres, Kirilganlik, Trend, Sıkışma) gore olceklenen kayma. | base_slippage * regime_slippage_multiplier | {'stress_multiplier': 2.5, 'calm_multiplier': 1.0} | False | False | True | True |

