# Phase 151: Evaluation Guards and Boundary Report

> [!WARNING]
> **YASAL UYARI VE GÜVENLİK SINIRI:**
> Bu çıktı Phase 151 Benchmark Comparison and Strategy Evaluation Reports raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, benchmark/evaluation/readiness/strategy-evaluation değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek backtest execution, benchmark execution, metric calculation, optimizer, model training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek Sharpe/win-rate/return/alpha/beta/drawdown hesaplama, performans garantisi, strategy approval, capital allocation, portfolio construction, position sizing, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.


## Summary
- **Total Guards:** 3
- **All Active:** True
- **Status:** evaluation_contract_ready

## Active Guards
                    guard_id                         guard_name               detection_target                                                                           description  is_active                    status  non_signal
     GUARD_NO_LOOKAHEAD_COLS  No-Lookahead Column Pattern Guard future_return_and_lead_columns             Geleceğe bakan veya shift(-1) içeren kolon isimlerini engelleyen muhafız.       True evaluation_contract_ready        True
        GUARD_NO_FUTURE_JOIN Backward Monotonic Asof Join Guard       future_timestamp_leakage Zaman serisi birleştirmelerinde geleceğe yönelik join yapılmasını engelleyen muhafız.       True evaluation_contract_ready        True
GUARD_STRICT_TIMESTAMP_ORDER   Chronological Monotonicity Guard        out_of_order_timestamps          Veri satırlarının kesin monoton artan zaman sıralamasını denetleyen muhafız.       True evaluation_contract_ready        True