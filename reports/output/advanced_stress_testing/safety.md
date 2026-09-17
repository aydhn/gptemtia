# Phase 148: Stres Testi Güvenlik Sınırları Raporu

> [!IMPORTANT]
> **YASAL UYARI VE ARAŞTIRMA BEYANI (PHASE 148)**:
> Bu çıktı Phase 148 Stress Testing and Scenario Simulation raporudur. > Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, stress/readiness/scenario/robustness > değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, > gerçek stress test execution, scenario simulation, optimizer, Monte Carlo, > gerçek model training, model fit/predict/inference, dataset materialization, > target/label/prediction üretimi, gerçek stress PnL/drawdown/VaR/ES hesaplama, > performans garantisi, model deployment, model registry write, model artifact persistence, > scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı > veya gerçek provider API çağrısı değildir.

## Güvenlik Özeti
- **Güvenlik Durumu**: `SECURE`
- **NO-GO Kuralları Aktif**: `14 adet`
- **SAFE-GO Kuralları Aktif**: `7 adet`

## Güvenlik Kural Tablosu

| type | rule_id | rule_name | description | non_signal | local_only |
| --- | --- | --- | --- | --- | --- |
| NO_GO | NO_GO_01 | no_live_trading | Gerçek sermaye ile piyasada işlem açmak kesinlikle yasaktır. | True | True |
| NO_GO | NO_GO_02 | no_broker_integration | Aracı kurum API entegrasyonu ve emir iletimi yasaktır. | True | True |
| NO_GO | NO_GO_03 | no_investment_advice | Kesin AL/SAT veya yatırım tavsiyesi üretmek yasaktır. | True | True |
| NO_GO | NO_GO_04 | no_signal_generation | Stres hazırlık skorunu trade sinyali olarak sunmak yasaktır. | True | True |
| NO_GO | NO_GO_05 | no_true_stress_execution | Gerçek stres testi çalıştırmak yasaktır; yalnızca sözleşme kurulabilir. | True | True |
| NO_GO | NO_GO_06 | no_scenario_simulation_execution | Gerçek senaryo simülasyonu yürütmek yasaktır. | True | True |
| NO_GO | NO_GO_07 | no_metric_calculation | Gerçek stres PnL, VaR veya drawdown hesaplamak yasaktır. | True | True |
| NO_GO | NO_GO_08 | no_optimizer_execution | Stres parametrelerine göre optimizasyon çalıştırmak yasaktır. | True | True |
| NO_GO | NO_GO_09 | no_monte_carlo_execution | Monte Carlo çalıştırmak yasaktır (Phase 149 konusudur). | True | True |
| NO_GO | NO_GO_10 | no_model_training_prediction | Model eğitimi, fit, predict veya hedef etiket üretimi yasaktır. | True | True |
| NO_GO | NO_GO_11 | no_model_registry_write | Model kaydı yazmak veya yapay zeka modeli deploy etmek yasaktır. | True | True |
| NO_GO | NO_GO_12 | no_performance_guarantee | Geleceğe dönük getiri veya başarı garantisi vermek yasaktır. | True | True |
| NO_GO | NO_GO_13 | no_web_scraping_credentials | Haber kazıma, tam metin indirme veya API anahtarı yazdırma yasaktır. | True | True |
| NO_GO | NO_GO_14 | no_source_overwrite | Kaynak verileri silmek veya üzerine yazmak yasaktır. | True | True |
| SAFE_GO | SAFE_GO_01 | local_scenario_contract_generation | Yerel stres ve kriz senaryo sözleşmelerini tanımlamak. | True | True |
| SAFE_GO | SAFE_GO_02 | shock_placeholder_generation | Volatilite, likidite, spread ve gap şok yer tutucularını oluşturmak. | True | True |
| SAFE_GO | SAFE_GO_03 | scenario_library_metadata | Tarihsel ve varsayımsal senaryo kütüphane metaverisini derlemek. | True | True |
| SAFE_GO | SAFE_GO_04 | stress_metric_placeholders | VaR, ES ve drawdown için hesaplama yapmayan formül yer tutucuları oluşturmak. | True | True |
| SAFE_GO | SAFE_GO_05 | bias_and_leakage_guards | No-lookahead, senaryo sızıntısı ve yasaklı kolon muhafızlarını kurmak. | True | True |
| SAFE_GO | SAFE_GO_06 | disabled_execution_reporting | Yasaklı yürütme yollarını belgeleyen engelleme raporları üretmek. | True | True |
| SAFE_GO | SAFE_GO_07 | phase_149_handoff_preparation | Phase 149 Monte Carlo ve parametre stabilitesi devir paketini hazırlamak. | True | True |
