# Phase 135: Regime Block Contract Audit Report

> [!CAUTION]
> **PHASE 135 YÖNETİŞİM VE NON-SIGNAL UYARISI**
> Bu çıktı Phase 135 Regime Classification Acceptance Report raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, rejim/validation/acceptance/FeatureStore değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target/label üretimi, sentiment model output, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı, production-ready/official approval/broker-ready iddiası, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Summary
- **Domain**: regime_block_test_contract_domain
- **Status**: READY

## Contract Audit Ledger
| phase | test_file | exists | non_signal | status_label |
| --- | --- | --- | --- | --- |
| 126 | tests/test_regime_foundation_manifest.py | True | True | acceptance_pass |
| 127 | tests/test_regime_matrix_integrity_manifest.py | True | True | acceptance_pass |
| 128 | tests/test_regime_candidate_state_integrity_manifest.py | True | True | acceptance_pass |
| 129 | tests/test_behavior_diagnostics_manifest.py | True | True | acceptance_pass |
| 130 | tests/test_transition_diagnostics_manifest.py | True | True | acceptance_pass |
| 131 | tests/test_cross_asset_regime_context_manifest.py | True | True | acceptance_pass |
| 132 | tests/test_macro_event_news_regime_context_manifest.py | True | True | acceptance_pass |
| 133 | tests/test_regime_validation_acceptance_manifest.py | True | True | acceptance_pass |
| 134 | tests/test_regime_featurestore_metadata_manifest.py | True | True | acceptance_pass |
| 135 | tests/test_phase_126_135_acceptance_manifest.py | True | True | acceptance_pass |