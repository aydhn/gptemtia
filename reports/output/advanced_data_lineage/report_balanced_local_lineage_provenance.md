# Data Lineage Profile Registry Report
> **YASAL UYARI VE FERAGATNAME**
> Bu çıktı Phase 114 Data Lineage and Provenance raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, lineage/traceability score’u trade sinyali olarak kullanma, official approval, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.

- **Toplam Profil Sayısı**: 3
- **Mevcut Faz**: 114
- **Hedef Final Faz**: 160
- **Tümü Local-Only**: True
- **Tümü Non-Destructive**: True

| profile_id | profile_name | current_phase | target_final_phase | next_phase | local_only | non_production | research_only | dry_run | non_destructive | status_label | warnings |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lineage_profile_balanced_local_lineage_provenance | balanced_local_lineage_provenance | 114 | 160 | 115 | True | True | True | True | True | lineage_complete | [] |
| lineage_profile_strict_lineage_provenance_safety | strict_lineage_provenance_safety | 114 | 160 | 115 | True | True | True | True | True | lineage_complete | ['High traceability score threshold enforced'] |
| lineage_profile_dry_run_lineage_contract_focus | dry_run_lineage_contract_focus | 114 | 160 | 115 | True | True | True | True | True | lineage_complete | [] |