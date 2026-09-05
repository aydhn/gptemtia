# Data Lineage Validation Report
> **YASAL UYARI VE FERAGATNAME**
> Bu çıktı Phase 114 Data Lineage and Provenance raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, lineage/traceability score’u trade sinyali olarak kullanma, official approval, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.

- **Toplam Doğrulama Kuralı**: 14
- **Doğrulama Sonucu**: PASS
- **Yasaklı İddia Tespiti**: 0

| rule_id | rule_name | status | enforced | current_phase |
| --- | --- | --- | --- | --- |
| val_001 | profile_registry_integrity | PASS | True | 114 |
| val_002 | domain_registry_integrity | PASS | True | 114 |
| val_003 | provenance_source_integrity | PASS | True | 114 |
| val_004 | source_reference_integrity | PASS | True | 114 |
| val_005 | provider_provenance_integrity | PASS | True | 114 |
| val_006 | dataset_provenance_integrity | PASS | True | 114 |
| val_007 | schema_provenance_integrity | PASS | True | 114 |
| val_008 | transformation_provenance_integrity | PASS | True | 114 |
| val_009 | license_provenance_integrity | PASS | True | 114 |
| val_010 | copyright_boundary_integrity | PASS | True | 114 |
| val_011 | metadata_only_integrity | PASS | True | 114 |
| val_012 | audit_trail_integrity | PASS | True | 114 |
| val_013 | traceability_score_integrity | PASS | True | 114 |
| val_014 | safety_boundary_integrity | PASS | True | 114 |