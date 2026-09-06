# Phase 135: Regime Acceptance Profile Registry Report

> [!CAUTION]
> **PHASE 135 YÖNETİŞİM VE NON-SIGNAL UYARISI**
> Bu çıktı Phase 135 Regime Classification Acceptance Report raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, rejim/validation/acceptance/FeatureStore değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target/label üretimi, sentiment model output, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı, production-ready/official approval/broker-ready iddiası, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Summary
- **Active Profile**: balanced_local_regime_acceptance
- **Total Profiles**: 3
- **Current Phase**: 135
- **Target Final Phase**: 160
- **Next Phase**: 136
- **Status**: READY

## Registered Profiles
| profile_name | description | current_phase | target_final_phase | next_phase | dry_run_default | local_only | non_production | research_only | min_score | is_active | non_signal | status_label |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| balanced_local_regime_acceptance | Dengeli yerel rejim siniflandirma blogu kabul ve yonetisim profili. | 135 | 160 | 136 | True | True | True | True | 0.45 | True | True | acceptance_pass |
| strict_non_signal_regime_block_acceptance | Siki non-signal, no-lookahead ve kaynak koruma odakli kabul guvenlik profili. | 135 | 160 | 136 | True | True | True | True | 0.6 | False | True | acceptance_pass |
| dry_run_regime_manifest_focus | Dry-run uyumlu, manifest ve Phase 136 ileri ML/GPU devri odakli kabul profili. | 135 | 160 | 136 | True | True | True | True | 0.4 | False | True | acceptance_pass |