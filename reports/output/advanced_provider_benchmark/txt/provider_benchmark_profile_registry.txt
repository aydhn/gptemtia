# Phase 115: Provider Benchmark Profile Registry
> **UYARI VE SINIRLAR**:
> Bu çıktı Phase 115 Data Provider Benchmark Report raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, benchmark score’u trade sinyali olarak kullanma, provider official approval, production-ready/broker-ready iddiası, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.

- **Toplam Profil Sayısı**: 3
- **Yerel / Offline Zorunluluğu**: True
- **Production-Dışı**: True
- **Mevcut Faz**: 115 | **Hedef Faz**: 160

### Tanımlı Benchmark Profilleri
| profile_id | profile_name | current_phase | target_final_phase | next_phase | local_only | non_production | research_only | dry_run | status_label | warnings |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pb_profile::balanced_local_provider_benchmark | balanced_local_provider_benchmark | 115 | 160 | 116 | True | True | True | True | benchmark_pass | [] |
| pb_profile::strict_provider_benchmark_safety | strict_provider_benchmark_safety | 115 | 160 | 116 | True | True | True | True | benchmark_pass | ['High minimum benchmark score threshold configured'] |
| pb_profile::dry_run_provider_benchmark_focus | dry_run_provider_benchmark_focus | 115 | 160 | 116 | True | True | True | True | benchmark_pass | [] |
