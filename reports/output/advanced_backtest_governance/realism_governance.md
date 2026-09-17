# Phase 150: Execution Realism Governance Report

> **Disclaimer**: Bu çıktı Phase 150 Backtest Governance and Bias Control raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, backtest/governance/bias-control/readiness değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek backtest execution, benchmark execution, metric calculation, optimizer, model training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek Sharpe/win-rate/return/alpha/drawdown hesaplama, performans garantisi, strategy approval, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

- **Domain**: `realism_governance_domain`
- **Subdomain**: `transaction_cost_realism`
- **Status**: `governance_contract_ready`

## Realism Rules

                           rule_id                                     rule_name                                                                                  description             enforcement  zero_cost_allowed  broker_execution_allowed   status  non_signal  local_only  phase
              CST_01_ZERO_COST_BAN             zero_transaction_cost_prohibition        Strict prohibition against assuming zero transaction fees or commission-free trading. BLOCKING_ZERO_TOLERANCE              False                     False ENFORCED        True        True    150
CST_02_TIERED_COMMISSION_STRUCTURE           tiered_commission_model_requirement              Require broker commission tiers (per-contract for commodities, bps for FX/CFD).      BLOCKING_MANDATORY              False                     False ENFORCED        True        True    150
   CST_03_EXCHANGE_REGULATORY_FEES               exchange_clearing_fee_inclusion         Mandate inclusion of exchange, clearing, NFA/FINRA, and regulatory transaction fees.      BLOCKING_MANDATORY              False                     False ENFORCED        True        True    150
       CST_04_FINANCING_CARRY_FEES overnight_financing_and_borrow_cost_inclusion Simulate swap rates, repo financing, and short-borrow carry costs across multi-day holdings.              HIGH_AUDIT              False                     False ENFORCED        True        True    150
