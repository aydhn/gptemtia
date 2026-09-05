import os
from pathlib import Path

def patch_docs():
    
    # README.md
    readme_path = Path("README.md")
    if readme_path.exists():
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "Local Distribution Bundle, Portable Docs and Packaging Governance" not in content:
            new_readme_section = """
## Local Distribution Bundle, Portable Docs and Packaging Governance

- Final local distribution bundle rehearsal gercek release package degildir.
- Portable docs bundle official handover degildir.
- Offline release folder manifest gercek release degildir.
- Terminal handover ZIP-map gercek ZIP/archive uretmez.
- Final packaging governance binder official packaging approval degildir.
- Packaging readiness score release approval degildir.
- ZIP/TAR/RAR/7z, binary artifact, installer, package publish, Docker push, Git tag, cloud upload, deployment, live trading, broker execution ve yatirim tavsiyesi yoktur.
- Ciktilar data/lake/local_distribution_packaging ve reports/output/local_distribution_packaging altinda olusur.

Komutlar:
```bash
python -m scripts.run_packaging_domain_registry
python -m scripts.run_distribution_bundle_rehearsal
python -m scripts.run_portable_docs_bundle
python -m scripts.run_offline_release_folder_manifest
python -m scripts.run_terminal_handover_zip_map
python -m scripts.run_final_packaging_governance
python -m scripts.run_packaging_quality_report
python -m scripts.run_packaging_status
```
"""
            with open(readme_path, "a", encoding="utf-8") as f:
                f.write(new_readme_section)
            print("Patched README.md")

    # docs/ARCHITECTURE.md
    arch_path = Path("docs/ARCHITECTURE.md")
    if arch_path.exists():
        with open(arch_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "DistributionPackagingProfileRegistry" not in content:
            new_arch_section = """
-> DistributionPackagingProfileRegistry
-> DistributionPackagingDomainRegistry
-> FinalLocalDistributionBundleRehearsal
-> DistributionBundleManifest
-> DistributionBundleFolderSourceOutputMaps
-> InclusionExclusionMatrices
-> PortableDocsBundle
-> OfflineReleaseFolderManifest
-> TerminalHandoverZipMap
-> FinalPackagingGovernanceBinder
-> PackagingCriteria
-> PackagingEvidence
-> PackagingIssues
-> PackagingHandoff
-> PackagingSourceOutputCommandMaps
-> PackagingNoGoSafeGo
-> PackagingExceptions
-> PackagingGaps
-> PackagingRisks
-> PackagingReadinessScoring
-> PackagingValidation
-> PackagingQuality
-> Local Distribution Packaging Outputs
"""
            with open(arch_path, "a", encoding="utf-8") as f:
                f.write(new_arch_section)
            print("Patched docs/ARCHITECTURE.md")
            
    # docs/PHASE_LOG.md
    phase_log_path = Path("docs/PHASE_LOG.md")
    if phase_log_path.exists():
        with open(phase_log_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "Phase 96" not in content:
            new_phase_section = """
## Phase 96: Local Distribution Bundle Rehearsal & Packaging Governance
- Local distribution packaging profile sistemi eklendi.
- Packaging label registry eklendi.
- PackagingDomain, DistributionBundleItem, PortableDocsItem, ReleaseFolderItem, ZipMapItem ve PackagingFinding modelleri eklendi.
- Distribution packaging domain registry eklendi.
- Final local distribution bundle rehearsal eklendi.
- Distribution bundle manifest, folder map, source/output registry ve safety boundary registry eklendi.
- Inclusion/exclusion matrices eklendi.
- Portable docs bundle, manifest, reading order, role map, quickstart packet ve limitation register eklendi.
- Offline release folder manifest, folder tree, checklist, non-goals ve integrity rehearsal eklendi.
- Terminal handover ZIP-map, ZIP-map manifest, folder-to-file registry, compression non-goals, handover route ve recipient checklist eklendi.
- Final packaging governance binder eklendi.
- Packaging governance criteria matrix ve evidence index eklendi.
- Packaging issue/unresolved registerlari eklendi.
- Packaging handoff checklist eklendi.
- Packaging source/output/command maps eklendi.
- Packaging no-go/safe-go summary eklendi.
- Packaging exception/gap/risk registerlari eklendi.
- Packaging readiness score report eklendi.
- Packaging validation ve quality report eklendi.
- LocalDistributionPackagingPipeline eklendi.
- DataLake local distribution packaging kayit destegi aldi.
- Local packaging scriptleri eklendi.
- Testler genisletildi.
"""
            with open(phase_log_path, "a", encoding="utf-8") as f:
                f.write(new_phase_section)
            print("Patched docs/PHASE_LOG.md")
            
    # other docs
    other_docs = ["docs/OPERATOR_MANUAL.md", "docs/ANALYST_HANDBOOK.md", "docs/CODEX_AGENT_GUIDE.md", "docs/SAFE_USAGE_GUIDE.md", "docs/INSTALLATION.md", "docs/CONFIGURATION.md"]
    for doc in other_docs:
        doc_path = Path(doc)
        if doc_path.exists():
            with open(doc_path, "r", encoding="utf-8") as f:
                content = f.read()
            if "Local Distribution Packaging" not in content:
                new_doc_section = """
## Local Distribution Packaging
- Distribution bundle rehearsal nasil okunur? 
- Portable docs bundle nasil kullanilir?
- Offline release folder manifest neden gercek release degildir?
- Terminal handover ZIP-map neden gercek ZIP/archive uretmez?
- Packaging governance binder nasil yorumlanir?
- Inclusion/exclusion matrices ve source/output/command maps nasil okunur?
- Gercek ZIP/archive, installer, binary artifact, package publish, deployment, canli emir, broker execution ve yatirim tavsiyesi olmadigi acik yazilsin.
"""
                with open(doc_path, "a", encoding="utf-8") as f:
                    f.write(new_doc_section)
                print(f"Patched {doc}")
                
if __name__ == "__main__":
    patch_docs()
