# Phase 150: Disabled Execution Report

> **Disclaimer**: Bu çıktı Phase 150 Backtest Governance and Bias Control raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, backtest/governance/bias-control/readiness değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek backtest execution, benchmark execution, metric calculation, optimizer, model training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek Sharpe/win-rate/return/alpha/drawdown hesaplama, performans garantisi, strategy approval, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

- **Domain**: `disabled_execution_domain`
- **Total Disabled Operations**: `3`
- **All Executions Disabled**: True
- **Status**: `governance_contract_ready`

## Blocked Execution Engines

  operation_name                                            description   status  execution_permitted  phase  non_signal  local_only
    run_backtest Historical backtest execution engine across bar feeds. DISABLED                False    150        True        True
execute_backtest       Execution wrapper for multi-asset strategy runs. DISABLED                False    150        True        True
   run_benchmark   Benchmark simulation and relative return generation. DISABLED                False    150        True        True
