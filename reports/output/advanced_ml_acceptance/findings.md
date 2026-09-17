# Phase 145: Advanced ML Findings Registry Report

> **Yasal Uyarı:** Bu çıktı Phase 145 Advanced ML Acceptance Report çıktısıdır. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, acceptance/readiness/governance değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek model training, model fit/predict/inference, probability prediction, calibration/uncertainty execution, drift calculation, explainability calculation, backtest/walk-forward/benchmark/transaction-cost/slippage execution, model deployment, production deployment, model registry write, model artifact persistence, official approval, production approval, broker-ready approval, live-trading approval, gerçek audit log, dataset materialization, target/label/prediction üretimi, gerçek metric/performance claim, strateji üretimi, optimizer, clustering, ensemble execution, sentiment model output, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı, scraping veya gerçek provider API çağrısı değildir.

- **Total Findings:** `3`
- **Manual Review Findings:** `2`
- **Status:** `RECORDED`

## Findings Register
| finding_id | finding_type | phase_ref | severity_label | message | recommendation | manual_review_required | current_phase | target_final_phase | next_phase | status_label | non_signal | production_ready | broker_ready |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FND-CONTRA | contract_only_audit | Phase 136-144 | INFO | Phase 136-144 components verified at contract and schema level. | Retain contract-only status until formal execution gates are designed. | True | 145 | 160 | 146 | acceptance_manual_review_required | True | False | False |
| FND-MANUAL | manual_review_audit | Phase 144 | LOW | Model cards and risk disclosures await human committee inspection. | Perform manual inspection of model card limitations. | True | 145 | 160 | 146 | acceptance_manual_review_required | True | False | False |
| FND-HANDOF | handoff_readiness_audit | Phase 145 | INFO | Readiness scores computed without granting live or broker permissions. | Proceed to Phase 146 realistic backtest contract planning. | False | 145 | 160 | 146 | RESOLVED | True | False | False |
