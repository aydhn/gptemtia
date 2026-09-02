import os
from pathlib import Path

base_dir = Path(r"c:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia\commodity_fx_signal_bot")

def append_docs(filepath, append_str):
    if not filepath.exists(): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if "Local Archival Seal Rehearsal" not in content and "Phase 79" not in content:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(f"\\n\\n{append_str}")

readme_append = """## Local Archival Seal Rehearsal and Provenance Lockfile

- Final archival seal rehearsal gerçek arşiv mühürü değildir.
- Immutable-manifest rehearsal gerçek immutable storage veya chmod lock uygulamaz.
- Local provenance lockfile hukuki lockfile veya compliance belgesi değildir.
- Hash-of-hashes catalog blockchain notarization veya timestamp authority değildir.
- Custody rehearsal gerçek chain-of-custody değildir.
- Sensitive dosyalar hashlenmez ve raw secret yazılmaz.
- Cloud archive, package publish, legal hold, deployment ve canlı trading yoktur.
- Çıktılar `data/lake/local_archival` ve `reports/output/local_archival` altında oluşur.

### Commands
```bash
python -m scripts.run_archival_domain_registry
python -m scripts.run_final_archival_seal_rehearsal
python -m scripts.run_provenance_lockfile
python -m scripts.run_hash_catalogs
python -m scripts.run_custody_rehearsal
python -m scripts.run_archival_quality_report
python -m scripts.run_archival_status
```
"""
append_docs(base_dir / "README.md", readme_append)

arch_append = """### Phase 79: Local Archival

Delivery / Acceptance / Hardening / Synthesis / Docs / Reports / DataLake / Scripts / Tests / Safety
-> ArchivalProfileRegistry
-> ArchivalDomainRegistry
-> HashPolicyRegistry
-> SensitiveFileExclusionRegistry
-> ArchiveCandidateInventory
-> FinalHashCatalog
-> FinalHashOfHashesCatalog
-> FinalArchivalSealRehearsalManifest
-> ImmutableManifestRehearsalCatalog
-> LocalProvenanceLockfile
-> HashRehearsalReports
-> CustodyChainSimulation
-> LongTermCustodyGuide
-> RetentionNotes
-> TamperEvidenceDryRun
-> ReproducibilityPointers
-> ProvenanceTraceMatrices
-> ArchivalNoGoSafeGo
-> ArchivalExceptions
-> ArchivalGaps
-> ArchivalRisks
-> ArchivalReadinessScoring
-> ArchivalValidation
-> ArchivalQuality
-> Local Archival Outputs
"""
append_docs(base_dir / "docs" / "ARCHITECTURE.md", arch_append)

phase_log_append = """### Phase 79: Local Archival Seal Rehearsal
- Local archival profile sistemi eklendi.
- Archival label registry eklendi.
- ArchivalDomain, ArchivalItem, ProvenanceLockEntry, CustodyRehearsalItem ve ArchivalFinding modelleri eklendi.
- Archival domain registry eklendi.
- Hash policy ve hash exclusion policy registry eklendi.
- Sensitive file exclusion registry eklendi.
- Archive candidate inventory eklendi.
- Final hash catalog eklendi.
- Final hash-of-hashes catalog eklendi.
- Final archival seal rehearsal manifest eklendi.
- Immutable-manifest rehearsal catalog eklendi.
- Local provenance lockfile eklendi.
- Delivery/handoff/generated docs/reports/DataLake/scripts-tests/safety/evidence hash rehearsal raporları eklendi.
- Custody chain simulation registry eklendi.
- Long-term custody rehearsal guide eklendi.
- Retention note registry eklendi.
- Tamper-evidence dry-run report eklendi.
- Reproducibility pointer registry eklendi.
- Provenance trace matrixleri eklendi.
- Archival no-go/safe-go summary eklendi.
- Archival exception/gap/risk registerları eklendi.
- Archival readiness score report eklendi.
- Archival validation ve quality report eklendi.
- LocalArchivalPipeline eklendi.
- DataLake local archival kayıt desteği aldı.
- Local archival scriptleri eklendi.
- Testler genişletildi.
"""
append_docs(base_dir / "docs" / "PHASE_LOG.md", phase_log_append)

guide_append = """### Local Archival Guidelines
- **Final archival seal rehearsal** nasıl okunur? It's a dry-run local documentation, not a legal seal.
- **Hash catalog ve hash-of-hashes catalog** ne yapar/ne yapmaz? They document state, but do not provide blockchain/timestamp notarization.
- **Local provenance lockfile** neden hukuki lockfile değildir? No legal guarantees or immutable storage.
- **Sensitive file exclusion registry** nasıl yorumlanır? Lists excluded files, doesn't print raw secrets.
- **Custody rehearsal** neden gerçek chain-of-custody değildir? It's a simulation, no legal handoff.
- **Archival readiness score** neden compliance/legal approval değildir? It's purely an internal dry-run readiness metric.
- Immutable lock, chmod, cloud archive, blockchain notarization, legal hold, package publish, canlı emir, broker execution ve yatırım tavsiyesi YOKTUR.
"""
for doc in ["OPERATOR_MANUAL.md", "ANALYST_HANDBOOK.md", "CODEX_AGENT_GUIDE.md", "SAFE_USAGE_GUIDE.md", "INSTALLATION.md", "CONFIGURATION.md"]:
    append_docs(base_dir / "docs" / doc, guide_append)

print("generate_phase79_docs.py created.")
