with open("commodity_fx_signal_bot/README.md", "r") as f:
    readme = f.read()

if "## Portable Packaging, Environment Snapshot and Install Verification" not in readme:
    readme += """
## Portable Packaging, Environment Snapshot and Install Verification
Bu proje local/offline bir bot altyapısıdır. Portable packaging özellikleri, environment snapshot, dependency inventory, install verification ve portable bundle manifest süreçlerini otomatikleştirir. Bu çıktıların hiçbiri production release, package publish, broker deploy veya canlı yatırım tavsiyesi değildir.

Komutlar:
```bash
python -m scripts.run_environment_snapshot
python -m scripts.run_dependency_inventory
python -m scripts.run_requirements_export
python -m scripts.run_install_verification
python -m scripts.run_portable_bundle_manifest
python -m scripts.run_reproducible_setup_guide
python -m scripts.run_packaging_status
```
"""

with open("commodity_fx_signal_bot/README.md", "w") as f:
    f.write(readme)

with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "a") as f:
    f.write("""
### Phase 61: Portable Packaging
Project Source / Config / Docs / Tests / Reports / DataLake
→ EnvironmentSnapshot
→ DependencyInventory
→ RequirementsExport
→ InstallVerification
→ ImportVerification
→ ScriptVerification
→ ConfigVerification
→ SourcePolicy
→ BundleManifest
→ ArchiveManifest
→ ReproducibleSetupGuide
→ EnvironmentDrift
→ PackagingSafety
→ PackagingQuality
→ Portable Packaging Outputs
""")

with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "a") as f:
    f.write("""
### Phase 61: Portable Packaging and Install Verification
- Portable packaging profile sistemi eklendi.
- Packaging label registry eklendi.
- EnvironmentSnapshot, DependencyRecord, BundleArtifact, InstallVerificationResult ve PortableBundleManifest modelleri eklendi.
- Environment snapshot eklendi.
- Dependency inventory eklendi.
- Requirements export eklendi.
- Install/import/script/config verification eklendi.
- Source inclusion/exclusion policy eklendi.
- Portable bundle manifest eklendi.
- Archive manifest dry-run eklendi.
- Reproducible setup guide eklendi.
- Environment drift report eklendi.
- Packaging safety report eklendi.
- Packaging quality report eklendi.
- PortablePackagingPipeline eklendi.
- DataLake portable packaging kayıt desteği aldı.
- Portable packaging scriptleri eklendi.
- Testler genişletildi.
""")

for doc in ["INSTALLATION.md", "CONFIGURATION.md", "OPERATOR_MANUAL.md", "CODEX_AGENT_GUIDE.md"]:
    with open(f"commodity_fx_signal_bot/docs/{doc}", "a") as f:
        f.write("""
## Portable Packaging
Environment snapshot, requirements export ve install verification işlemleri için Phase 61 scriptlerini kullanın (örn. `run_environment_snapshot.py`, `run_portable_bundle_manifest.py`). Package publish, Docker deploy, cloud deploy, canlı trading ve broker execution KESİNLİKLE YOKTUR.
""")
