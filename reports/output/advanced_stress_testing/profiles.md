# Phase 148: Stres Testi Profil Raporu

> [!IMPORTANT]
> **YASAL UYARI VE ARAŞTIRMA BEYANI (PHASE 148)**:
> Bu çıktı Phase 148 Stress Testing and Scenario Simulation raporudur. > Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, stress/readiness/scenario/robustness > değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, > gerçek stress test execution, scenario simulation, optimizer, Monte Carlo, > gerçek model training, model fit/predict/inference, dataset materialization, > target/label/prediction üretimi, gerçek stress PnL/drawdown/VaR/ES hesaplama, > performans garantisi, model deployment, model registry write, model artifact persistence, > scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı > veya gerçek provider API çağrısı değildir.

## Profil Özeti
- **Aktif Profil**: `balanced_local_stress_testing_contracts`
- **Toplam Profil Sayısı**: `3`
- **Yerel Çalışma (Local Only)**: `True`
- **Non-Production**: `True`

## Profil Kayıt Defteri

| profile_name | description | current_phase | target_final_phase | next_phase | local_only | dry_run | non_production | non_signal | broker_ready | production_ready | live_trading_ready | official_approval | min_readiness_score | is_active |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| balanced_local_stress_testing_contracts | Dengeli yerel stres testi sozlesmeleri, senaryo kutuphanesi ve sok yer tutuculari profili. | 148 | 160 | 149 | True | True | True | True | False | False | False | False | 0.5 | True |
| strict_safety_stress_contracts | Siki guvenlik, sifir canli islem, sifir broker, sifir lookahead ve genisletilmis sok muhafizlari profili. | 148 | 160 | 149 | True | True | True | True | False | False | False | False | 0.65 | False |
| dry_run_scenario_contracts | Dry-run odakli senaryo sozlesmeleri, sok katalogu ve Phase 149 handoff hazirlik profili. | 148 | 160 | 149 | True | True | True | True | False | False | False | False | 0.45 | False |
