import os
from pathlib import Path

base_dir = Path("c:/Users/immor/OneDrive/Belgeler/Projelerim/gptemtia/commodity_fx_signal_bot")

# README.md
readme = base_dir / "README.md"
content = readme.read_text(encoding="utf-8")
if "Local Final Synthesis and End-State Documentation" not in content:
    content += """
## Local Final Synthesis and End-State Documentation (Phase 75)
Local synthesis layer production release veya resmi proje kapanış sertifikası değildir.
Master index dosya taşımaz, silmez veya değiştirmez.
Cross-phase final map canlı sistem onayı değildir.
Project completion dossier resmi compliance veya investment committee çıktısı değildir.
Final no-go/safe-go summary canlı trading izni vermez.
Navigation guides read-only/manual kullanım içindir.
Çıktılar `data/lake/local_synthesis` ve `reports/output/local_synthesis` altında oluşur.

Komutlar:
```bash
python -m scripts.run_synthesis_profile_registry
python -m scripts.run_master_index_unification
python -m scripts.run_cross_phase_final_map
python -m scripts.run_project_completion_dossier
python -m scripts.run_end_state_documentation
python -m scripts.run_synthesis_quality_report
python -m scripts.run_synthesis_status
```
"""
    readme.write_text(content, encoding="utf-8")

# ARCHITECTURE.md
arch = base_dir / "docs" / "ARCHITECTURE.md"
content = arch.read_text(encoding="utf-8")
if "SynthesisProfileRegistry" not in content:
    content += """
### Phase 75: Local Synthesis Layer
Docs / Reports / DataLake / Scripts / Tests / Evidence / Metadata / Graph / Timeline / Consistency / Readiness / Maintenance / Archive / DR / Training / Briefing
→ SynthesisProfileRegistry
→ PhaseFamilyRegistry
→ MasterArtifactIndex
→ MasterReportIndex
→ MasterDataLakeIndex
→ MasterDocsIndex
→ MasterScriptIndex
→ MasterTestIndex
→ CrossPhaseFinalMap
→ EndStateCapabilityMap
→ EndStateBoundaryMap
→ EndStateModuleDependencyMap
→ EndStateOutputCatalog
→ FinalCatalogs
→ FinalNonUsePolicyBinder
→ FinalSafetyBoundaryBinder
→ FinalLocalOnlyStatement
→ FinalLimitationRegister
→ FinalManualReviewRegister
→ FinalNoGoSafeGoSummary
→ NavigationGuides
→ ProjectCompletionDossier
→ ProjectClosureChecklist
→ FinalSynthesisValidation
→ FinalSynthesisQuality
→ Local Synthesis Outputs
"""
    arch.write_text(content, encoding="utf-8")

# PHASE_LOG.md
phase_log = base_dir / "docs" / "PHASE_LOG.md"
content = phase_log.read_text(encoding="utf-8")
if "Phase 75" not in content:
    content += """
## Phase 75: Local Final Synthesis and End-State Documentation
- Local synthesis profile sistemi eklendi.
- Synthesis label registry eklendi.
- PhaseFamily, MasterIndexItem, FinalMapNode, FinalBinderSection ve SynthesisFinding modelleri eklendi.
- Phase family registry eklendi.
- Master artifact/report/DataLake/docs/script/test indexleri eklendi.
- Cross-phase final map eklendi.
- End-state capability map eklendi.
- End-state boundary map eklendi.
- End-state module dependency map eklendi.
- End-state output catalog eklendi.
- Final generated-docs/command/report-family/DataLake-domain/cross-layer catalog eklendi.
- Final non-use policy binder eklendi.
- Final safety boundary binder eklendi.
- Final local-only statement eklendi.
- Final limitation register eklendi.
- Final manual review register eklendi.
- Final no-go/safe-go summary eklendi.
- Operator/stakeholder/developer navigation guide eklendi.
- Final project closure checklist eklendi.
- Project completion dossier eklendi.
- Final synthesis validation ve quality report eklendi.
- LocalSynthesisPipeline eklendi.
- DataLake local synthesis kayıt desteği aldı.
- Local synthesis scriptleri eklendi.
- Testler genişletildi.
"""
    phase_log.write_text(content, encoding="utf-8")

# Other docs
docs_to_patch = ["OPERATOR_MANUAL.md", "ANALYST_HANDBOOK.md", "CODEX_AGENT_GUIDE.md", "SAFE_USAGE_GUIDE.md", "INSTALLATION.md", "CONFIGURATION.md"]
for d in docs_to_patch:
    p = base_dir / "docs" / d
    if p.exists():
        content = p.read_text(encoding="utf-8")
        if "Local Synthesis" not in content:
            content += """
## Local Synthesis (Phase 75)
- **Master index nasıl okunur?** Sadece readonly dosya indeksleridir.
- **Cross-phase final map ne yapar/ne yapmaz?** Bağımlılıkları gösterir, canlı sistem onayı değildir.
- **Project completion dossier nasıl kullanılmalı?** Çevrimdışı ve dokümantasyon amaçlıdır.
- **Final navigation guides nasıl okunmalı?** Sadece yönlendirme sağlar, çalıştırılabilir işlem içermez.
- **Final no-go/safe-go summary neden canlı işlem izni değildir?** Offline kontrol sağlar, canlı işlem izni veremez.
- **Final synthesis quality report nasıl yorumlanır?** Proje kalitesini gösterir, yatırım tavsiyesi değildir.
*Not: Bu sistemde yatırım tavsiyesi, canlı emir, broker execution, deployment, production release, resmi completion ve compliance yoktur.*
"""
            p.write_text(content, encoding="utf-8")
