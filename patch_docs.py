import re

with open("commodity_fx_signal_bot/README.md", "r") as f:
    readme = f.read()

if "Data Retention, Archive Strategy and Local Maintenance" not in readme:
    readme += """

## Data Retention, Archive Strategy and Local Maintenance

Maintenance katmanı otomatik silme sistemi değildir. Default mod dry-run’dır. Cleanup candidates sadece incelenecek adaylardır.
Archive candidates otomatik taşınmaz. Source code, config, tests ve docs protected kabul edilir.
Retention policies local araştırma çıktıları içindir. Storage lifecycle health production readiness değildir.
Çıktılar `data/lake/maintenance` ve `reports/output/maintenance` altında oluşur.

```bash
python -m scripts.run_storage_inventory_report
python -m scripts.run_retention_policy_report
python -m scripts.run_cleanup_dry_run_report
python -m scripts.run_archive_dry_run_report
python -m scripts.run_storage_lifecycle_report
python -m scripts.run_maintenance_status
```
"""
    with open("commodity_fx_signal_bot/README.md", "w") as f:
        f.write(readme)

with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "r") as f:
    arch = f.read()

if "StorageInventory" not in arch:
    arch += """
### Maintenance Architecture
DataLake / Reports Output / Logs / Cache / Checkpoints / Archives
→ StorageInventory
→ RetentionPolicies
→ ArchiveStrategy
→ CleanupPlanner
→ RotationPlanner
→ DuplicateDetection
→ StaleDetection
→ LargeArtifactReview
→ StorageGrowth
→ SafeFileOps
→ MaintenanceChecklist
→ LifecycleHealth
→ MaintenanceQuality
→ Maintenance Reports
"""
    with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "w") as f:
        f.write(arch)

with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "r") as f:
    phase_log = f.read()

if "Phase 53" not in phase_log:
    phase_log += """
## Phase 53
- Maintenance profile sistemi eklendi.
- Maintenance label registry eklendi.
- StorageArtifactRecord, RetentionPolicy, MaintenanceCandidate, ArchiveManifest ve MaintenancePlan modelleri eklendi.
- Storage inventory eklendi.
- Retention policies eklendi.
- Archive strategy dry-run eklendi.
- Cleanup planner dry-run eklendi.
- Report/log/cache/checkpoint rotation planları eklendi.
- Duplicate detection eklendi.
- Stale detection eklendi.
- Large artifact review eklendi.
- Storage growth snapshot eklendi.
- Safe file ops korumalı modül olarak eklendi.
- Maintenance checklist eklendi.
- Storage lifecycle health eklendi.
- Maintenance quality report eklendi.
- MaintenancePipeline eklendi.
- DataLake maintenance kayıt desteği aldı.
- Maintenance scriptleri eklendi.
- Testler genişletildi.
"""
    with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "w") as f:
        f.write(phase_log)

print("Docs updated")
