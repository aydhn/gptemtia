# Phase 148: Stres Testi Muhafızları Raporu

> [!IMPORTANT]
> **YASAL UYARI VE ARAŞTIRMA BEYANI (PHASE 148)**:
> Bu çıktı Phase 148 Stress Testing and Scenario Simulation raporudur. > Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, stress/readiness/scenario/robustness > değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, > gerçek stress test execution, scenario simulation, optimizer, Monte Carlo, > gerçek model training, model fit/predict/inference, dataset materialization, > target/label/prediction üretimi, gerçek stress PnL/drawdown/VaR/ES hesaplama, > performans garantisi, model deployment, model registry write, model artifact persistence, > scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı > veya gerçek provider API çağrısı değildir.

## Muhafız Özeti
- **No-Lookahead Muhafızı**: `AKTİF`
- **Senaryo Sızıntı Muhafızı**: `AKTİF`
- **Veri Gözetleme ve Aşırı Uyum Muhafızı**: `AKTİF`
- **Yasaklı Kolon Politikası**: `AKTİF`

## Muhafız Listesi

| guard_name | guard_type | description | enforcement_level | active | prohibited_column_count | non_signal | local_only |
| --- | --- | --- | --- | --- | --- | --- | --- |
| stress_no_lookahead_guard | TEMPORAL_ORDER | Geleceğe bakış (lookahead) içeren sütunları ve ileri zamanlı birleştirmeleri engeller. | STRICT | True | 9 | True | True |
