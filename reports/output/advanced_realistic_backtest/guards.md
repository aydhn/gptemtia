# Phase 146: Backtest Bias & Lookahead Guards Report

> **YASAL UYARI VE GUCLENDIRILMIS GUVENLIK SINIRI (PHASE 146)**:
> Bu cikti Phase 146 Realistic Backtest, Transaction Cost and Slippage Modeling raporudur. Canli emir, broker talimati, kesin AL/SAT, yatirim tavsiyesi, backtest/readiness/cost/slippage degerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gercek backtest execution, walk-forward, benchmark, optimizer, stress test, Monte Carlo, gercek model training, model fit/predict/inference, dataset materialization, target/label/prediction uretimi, gercek performans garantisi, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanimi veya gercek provider API cagrisi degildir.

## Guards Summary
- **No-Lookahead Guard**: ACTIVE
- **Survivorship Guard**: ACTIVE
- **Data Snooping Guard**: ACTIVE
- **Overfitting Guard**: ACTIVE

## Guard Policies

| rule_name | enforcement | description | forbidden_patterns | active |
| --- | --- | --- | --- | --- |
| prohibit_future_return_columns | STRICT | Gelecek getiri veya sonraki bar fiyatini gosteren kolonlarin engellenmesi. | ['future_return', 'forward_return', 'next_return', 'lookahead_return', 'future_close', 'future_open', 'realized_future_pnl', 'future_pnl', 'perfect_fill', 'leak', 'leakage'] | True |
| prohibit_forward_shifts | STRICT | shift(-1) veya ileri yonlu zaman kaydirmalarinin kesinlikle engellenmesi. | shift(-*) | True |

