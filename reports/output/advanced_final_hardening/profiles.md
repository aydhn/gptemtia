# Phase 159: Final Hardening Profile Registry Report

> [!WARNING]
> **YASAL VE GÜVENLİK FERAGATNAMESİ (PHASE 159)**:
> Bu çıktı Phase 159 Final Hardening, Operator Runbook and Release Candidate çıktısıdır. > Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, final-hardening/release-candidate/readiness/runbook > değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek full-system execution, > end-to-end bot run, live trading, broker execution, order generation, signal generation, model training, > model fit/predict/inference, target/label/prediction üretimi, backtest, benchmark, optimizer, portfolio construction, > risk reporting, scenario execution, metric calculation, release deployment, production deployment, model deployment, > model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/> embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

## Profile Registry Summary

- **Active Profile**: `balanced_local_final_hardening_contracts`
- **Profile Count**: 3
- **Current Phase**: 159
- **Target Final Phase**: 160
- **Next Phase**: 160
- **All Local Only**: True
- **Status**: `final_hardening_contract_ready`

## Profiles Table

| profile_name | description | current_phase | target_final_phase | next_phase | default_language | dry_run_default | local_only | non_production | research_only | allow_live_trading | allow_broker_integration | allow_production_deployment | allow_release_deployment | min_readiness_score | enabled | domain | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| balanced_local_final_hardening_contracts | Dengeli yerel Final Hardening, Operator Runbook ve Release Candidate profili (Phases 1-158 konsolide). | 159 | 160 | 160 | tr | True | True | True | True | False | False | False | False | 0.5 | True | final_hardening_profile_domain | final_hardening_contract_ready |
| strict_non_production_hardening_safety | Siki non-production, no-live-trading ve sifir execution odakli final hardening guvenlik profili. | 159 | 160 | 160 | tr | True | True | True | True | False | False | False | False | 0.65 | True | final_hardening_profile_domain | final_hardening_contract_ready |
| dry_run_release_candidate_focus | Dry-run uyumlu, release candidate kontrol listesi ve Phase 160 final devri odakli profil. | 159 | 160 | 160 | tr | True | True | True | True | False | False | False | False | 0.45 | True | final_hardening_profile_domain | final_hardening_contract_ready |

