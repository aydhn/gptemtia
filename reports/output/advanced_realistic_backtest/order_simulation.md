# Phase 146: Order Simulation Contracts Report

> **YASAL UYARI VE GUCLENDIRILMIS GUVENLIK SINIRI (PHASE 146)**:
> Bu cikti Phase 146 Realistic Backtest, Transaction Cost and Slippage Modeling raporudur. Canli emir, broker talimati, kesin AL/SAT, yatirim tavsiyesi, backtest/readiness/cost/slippage degerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gercek backtest execution, walk-forward, benchmark, optimizer, stress test, Monte Carlo, gercek model training, model fit/predict/inference, dataset materialization, target/label/prediction uretimi, gercek performans garantisi, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanimi veya gercek provider API cagrisi degildir.

## Simulation Summary
- **Total Order Types**: 6
- **Broker Orders Blocked**: True
- **Live Orders Blocked**: True

## Order Simulation Table

| simulation_type | order_type | description | fill_model_ref | latency_model_ref | liquidity_constraint_ref | broker_order_sent | live_order_sent | real_fill_occurred | manual_review_required | is_active | non_signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| market_order_simulation_contract | MARKET | Piyasa emri simule sozlesmesi. Sonraki barin acilisinda veya anlik teklifte gerceklesme modeli. | next_tick_fill_model | network_latency_placeholder | adv_participation_limit | False | False | False | True | True | True |
| limit_order_simulation_contract | LIMIT | Limit emir simule sozlesmesi. Fiyat belirlenen limit seviyeye ulastiginda gerceklesme kurali. | touch_or_cross_fill_model | exchange_queue_latency_placeholder | queue_priority_limit | False | False | False | True | True | True |
| stop_order_simulation_contract | STOP | Stop zarar kes emri sozlesmesi. Tetiklenme fiyati goruldugunde piyasa emrine donusur. | stop_trigger_fill_model | trigger_delay_placeholder | gap_slippage_limit | False | False | False | True | True | True |
| stop_limit_order_simulation_contract | STOP_LIMIT | Stop-limit emri sozlesmesi. Tetiklenme sonrasi limit emir olarak deftere yazilir. | stop_limit_fill_model | trigger_delay_placeholder | limit_bound_limit | False | False | False | True | True | True |
| partial_fill_simulation_contract | PARTIAL_FILL | Kismi gerceklesme simule sozlesmesi. Emir buyuklugu mevcut bar hacminin belirli bir yuzdesini asarsa. | liquidity_capped_fill_model | multi_slice_latency_placeholder | bar_volume_cap_limit | False | False | False | True | True | True |
| rejected_order_simulation_contract | REJECTED_ORDER | Reddedilen emir simule sozlesmesi. Yetersiz teminat, piyasa kapali veya fiyat limitleri disinda. | rejection_handler_model | instant_rejection_placeholder | market_halt_limit | False | False | False | True | True | True |

