import os
from pathlib import Path

# README.md
readme_path = Path("commodity_fx_signal_bot/README.md")
with open(readme_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

readme_add = """
## Local Project Atlas and Meta-Index
Final local meta-index official knowledge index değildir.
Universal navigation map official SOP değildir.
Cross-phase lookup engine enterprise search değildir.
Offline semantic table of contents embedding/vector search değildir.
Terminal project atlas legal/compliance evidence değildir.
Meta-index readiness score official approval değildir.
Cloud index, vector DB, embedding API, external LLM, package publish, Docker push, Git tag, deployment, live trading, broker execution ve yatırım tavsiyesi yoktur.
Çıktılar data/lake/local_project_atlas ve reports/output/local_project_atlas altında oluşur.

Komutlar:
```bash
python -m scripts.run_atlas_domain_registry
python -m scripts.run_final_meta_index
python -m scripts.run_universal_navigation_map
python -m scripts.run_cross_phase_lookup_engine
python -m scripts.run_offline_semantic_toc
python -m scripts.run_terminal_project_atlas
python -m scripts.run_atlas_quality_report
python -m scripts.run_atlas_status
```
"""
if "Local Project Atlas and Meta-Index" not in readme_content:
    with open(readme_path, "a", encoding="utf-8") as f:
        f.write(readme_add)

# ARCHITECTURE.md
arch_path = Path("commodity_fx_signal_bot/docs/ARCHITECTURE.md")
if arch_path.exists():
    with open(arch_path, "r", encoding="utf-8") as f:
        arch_content = f.read()
    arch_add = """
## Local Project Atlas Katmanı

Continuity Intelligence / Post-Completion Preservation / Project Completion / LongTerm Operations / Release Candidate / Incident Response / RedTeam / Governance Control / Usability / Performance / Simplification / Reuse / Closure / Archival / Delivery / Acceptance / Hardening / Synthesis / Docs / Reports / DataLake / Scripts / Tests / Safety
→ ProjectAtlasProfileRegistry
→ AtlasDomainRegistry
→ FinalLocalMetaIndex
→ UniversalNavigationMap
→ CrossPhaseLookupEngine
→ CrossPhaseLookupTables
→ OfflineSemanticTableOfContents
→ TerminalProjectAtlas
→ AtlasFamilyMaps
→ AtlasPhaseMaps
→ AtlasRouteMaps
→ AtlasGlossary
→ AtlasCrosswalks
→ AtlasNoGoSafeGo
→ AtlasExceptions
→ AtlasGaps
→ AtlasRisks
→ AtlasReadinessScoring
→ AtlasValidation
→ AtlasQuality
→ Local Project Atlas Outputs
"""
    if "ProjectAtlasProfileRegistry" not in arch_content:
        with open(arch_path, "a", encoding="utf-8") as f:
            f.write(arch_add)

# PHASE_LOG.md
phase_log_path = Path("commodity_fx_signal_bot/docs/PHASE_LOG.md")
if phase_log_path.exists():
    with open(phase_log_path, "r", encoding="utf-8") as f:
        phase_log_content = f.read()
    phase_add = """
## Phase 93
- Local project atlas profile sistemi eklendi.
- Atlas label registry eklendi.
- AtlasDomain, MetaIndexItem, NavigationItem, LookupItem, AtlasCrosswalkItem ve AtlasFinding modelleri eklendi.
- Atlas domain registry eklendi.
- Final local meta-index eklendi.
- Universal navigation map eklendi.
- Cross-phase lookup engine ve registry eklendi.
- Cross-phase output/script/docs/DataLake/report/generated-docs/safety-boundary lookup tables eklendi.
- Offline semantic table of contents eklendi.
- Terminal project atlas eklendi.
- Atlas family maps eklendi.
- Atlas phase dependency, phase-to-output, output-to-script ve command-to-output maps eklendi.
- Atlas role-based route maps eklendi.
- Atlas glossary index eklendi.
- Atlas concept/no-go/safety/maintenance/continuity/preservation/completion/longterm/release/incident/redteam-governance crosswalks eklendi.
- Meta-index no-go/safe-go summary eklendi.
- Meta-index exception/gap/risk registerları eklendi.
- Meta-index readiness score report eklendi.
- Meta-index validation ve quality report eklendi.
- LocalProjectAtlasPipeline eklendi.
- DataLake local project atlas kayıt desteği aldı.
- Local atlas scriptleri eklendi.
- Testler genişletildi.
"""
    if "Phase 93" not in phase_log_content:
        with open(phase_log_path, "a", encoding="utf-8") as f:
            f.write(phase_add)

docs_to_patch = [
    "OPERATOR_MANUAL.md", "ANALYST_HANDBOOK.md", "CODEX_AGENT_GUIDE.md",
    "SAFE_USAGE_GUIDE.md", "INSTALLATION.md", "CONFIGURATION.md"
]

doc_add = """
## Local Project Atlas (Phase 93)
- Meta-index, projenin okunabilir listesidir, official knowledge index değildir.
- Universal navigation map, başlangıç noktalarını gösterir, official SOP değildir.
- Cross-phase lookup engine, klasör içi anahtar kelime eşleştirmesidir, enterprise search değildir.
- Offline semantic table of contents, başlıkların statik hiyerarşisidir, vector/embedding search değildir.
- Terminal project atlas projenin haritasıdır.
- Gerçek cloud index, vector DB, embedding API, external LLM, package publish, deployment, canlı emir, broker execution ve yatırım tavsiyesi yoktur.
"""

for d in docs_to_patch:
    dp = Path(f"commodity_fx_signal_bot/docs/{d}")
    if dp.exists():
        with open(dp, "r", encoding="utf-8") as f:
            c = f.read()
        if "Local Project Atlas (Phase 93)" not in c:
            with open(dp, "a", encoding="utf-8") as f:
                f.write(doc_add)

print("Docs patched")
