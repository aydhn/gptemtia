import re
from pathlib import Path

# ARCHITECTURE.md
arch = Path("docs/ARCHITECTURE.md")
content = arch.read_text()
if "Local Archive Outputs" not in content:
    add = """
### Phase 71: Local Archival Strategy & Preservation Layer
Docs / Reports / DataLake / Config / Scripts / Tests / Security / Backup / Packaging / Evidence / Metadata / Graph / Timeline / Consistency / Readiness / Maintenance
→ ArchiveDomainRegistry
→ ArchiveItemRegistry
→ ArchiveCandidateInventory
→ ArchiveExclusionRegistry
→ ProjectSnapshotCatalog
→ ColdStorageManifest
→ RetentionPolicy
→ RetentionReview
→ ArchiveHashManifest
→ IntegrityVerification
→ RestoreReadiness
→ ProvenanceRegistry
→ DependencySnapshot
→ DocumentationArchiveIndex
→ ReportArchiveIndex
→ DataLakeArchiveIndex
→ CrossLayerArchiveIndex
→ SecurityArchiveBoundary
→ SecretExclusionVerification
→ ArchiveGapRegister
→ ArchiveRiskSummary
→ LongHorizonPreservationBinder
→ ArchiveValidation
→ ArchiveQuality
→ Local Archive Outputs
"""
    arch.write_text(content + add)

# PHASE_LOG.md
phase = Path("docs/PHASE_LOG.md")
content = phase.read_text()
if "Phase 71" not in content:
    add = """
## Phase 71
- Local archive profile sistemi eklendi.
- Archive label registry eklendi.
- ArchiveDomain, ArchiveItem, SnapshotCatalogItem, RetentionPolicyItem ve ArchiveFinding modelleri eklendi.
- Archive domain registry eklendi.
- Archive item registry eklendi.
- Archive candidate inventory eklendi.
- Archive exclusion registry eklendi.
- Project snapshot catalog eklendi.
- Cold storage manifest eklendi.
- Retention policy ve retention review checklist eklendi.
- Archive hash manifest eklendi.
- Archive integrity verification plan eklendi.
- Restore-readiness checklist eklendi.
- Archive provenance registry eklendi.
- Dependency snapshot summary eklendi.
- Documentation/report/DataLake/cross-layer archive index eklendi.
- Security-sensitive archive boundary ve secret exclusion verification raporları eklendi.
- Archive gap register eklendi.
- Archive risk summary eklendi.
- Long-horizon preservation binder eklendi.
- Archive validation ve quality report eklendi.
- LocalArchivePipeline eklendi.
- DataLake local archive kayıt desteği aldı.
- Local archive scriptleri eklendi.
- Testler genişletildi.
"""
    phase.write_text(content + add)

def patch_manuals(file_name):
    p = Path(f"docs/{file_name}")
    if p.exists():
        content = p.read_text()
        if "Local Archive Strategy" not in content:
            add = """
### Local Archive Strategy & Preservation Layer (Phase 71)
- **Archive domain registry nasıl okunur?**: Tüm dosyalar çeşitli local retention domain'lere bölünür.
- **Snapshot catalog ne yapar/ne yapmaz?**: Cloud snapshot değildir, local file inventory'dir.
- **Cold storage manifest neden cloud backup değildir?**: Dosya yüklemez veya taşımaz, operatöre offline USB/drive'a neleri atması gerektiğini gösterir.
- **Retention policy neden resmi compliance değildir?**: Otomatik veri silmez, sadece tavsiye verir.
- **Integrity verification plan nasıl kullanılır?**: Geri yükleme tatbikatında dosyaların bozulup bozulmadığını kontrol eder.
- **Secret exclusion verification nasıl yorumlanır?**: .env gibi dosyaların arşivde HİÇ olmamasını denetler.
- **Preservation binder ne işe yarar?**: Sistemin 5-10 yıl boyunca tekrar ayağa kalkabilmesi için operatöre manual yönergeler veren kitaptır.
- **DİKKAT**: Sistemde cloud upload, auto archive, dosya taşıma/silme, canlı emir, broker execution, deployment ve yatırım tavsiyesi YOKTUR.
"""
            p.write_text(content + add)

for doc in ["OPERATOR_MANUAL.md", "ANALYST_HANDBOOK.md", "CODEX_AGENT_GUIDE.md", "SAFE_USAGE_GUIDE.md", "INSTALLATION.md", "CONFIGURATION.md"]:
    patch_manuals(doc)

print("Documentation patched")
