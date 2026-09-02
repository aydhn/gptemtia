import os
from pathlib import Path
import re

def patch_readme():
    file_path = Path("commodity_fx_signal_bot/README.md")
    if not file_path.exists(): return
    content = file_path.read_text(encoding="utf-8")
    if "Local Modular Simplification and Maintainability Rehearsal" in content: return

    injection = """
## Local Modular Simplification and Maintainability Rehearsal

Phase 82 itibarıyla sistem, offline/local modular simplification ve maintainability rehearsal yetenekleri kazanmıştır.
Önemli uyarılar:
- Final modular complexity map resmi architecture assessment değildir.
- Optional slimming plan gerçek refactor veya cleanup uygulamaz.
- Consolidation candidates otomatik dosya birleştirme/silme/taşıma izni değildir.
- Repo ergonomics guide manual review ve okuma kolaylığı içindir.
- Maintainability readiness score production cleanup veya architecture approval değildir.
- Cloud upload, package publish, deployment ve canlı trading yoktur.
- Çıktılar `data/lake/local_simplification` ve `reports/output/local_simplification` altında oluşur.

### Local Simplification Komutları
```bash
python -m scripts.run_simplification_domain_registry
python -m scripts.run_final_modular_complexity_map
python -m scripts.run_optional_slimming_plan
python -m scripts.run_repo_ergonomics_rehearsal
python -m scripts.run_maintainability_seed
python -m scripts.run_simplification_quality_report
python -m scripts.run_simplification_status
```
"""
    content += injection
    file_path.write_text(content, encoding="utf-8")

def patch_architecture():
    file_path = Path("commodity_fx_signal_bot/docs/ARCHITECTURE.md")
    if not file_path.exists(): return
    content = file_path.read_text(encoding="utf-8")
    if "SimplificationProfileRegistry" in content: return

    injection = """
### Local Simplification Flow (Phase 82)
Reuse / Closure / Archival / Delivery / Acceptance / Hardening / Synthesis / Docs / Reports / DataLake / Scripts / Tests / Safety
→ SimplificationProfileRegistry
→ SimplificationDomainRegistry
→ FinalModularComplexityMap
→ ModuleFamilyComplexity
→ FolderDepthComplexity
→ FileCountComplexity
→ FunctionCountComplexity
→ Script/Test/Output/DocsSprawlReports
→ ConsolidationCandidates
→ SpecificSimplificationCandidates
→ OptionalSlimmingPlan
→ RepoErgonomicsGuide
→ MaintainerOnboardingGuide
→ MaintainabilityImprovementSeed
→ ComplexityNoGoSafeGo
→ SimplificationExceptions
→ SimplificationGaps
→ SimplificationRisks
→ MaintainabilityReadinessScoring
→ SimplificationValidation
→ SimplificationQuality
→ Local Simplification Outputs
"""
    content += injection
    file_path.write_text(content, encoding="utf-8")

def patch_phase_log():
    file_path = Path("commodity_fx_signal_bot/docs/PHASE_LOG.md")
    if not file_path.exists(): return
    content = file_path.read_text(encoding="utf-8")
    if "Phase 82" in content: return

    injection = """
## Phase 82: Final Modular Simplification, Complexity Reduction Map, Optional Slimming Plan, Local Maintainability Improvement Seed ve Repo Ergonomics Rehearsal Layer
- Local simplification profile sistemi eklendi.
- Simplification label registry eklendi.
- SimplificationDomain, ComplexityItem, SimplificationCandidate, SlimmingPlanItem ve SimplificationFinding modelleri eklendi.
- Simplification domain registry eklendi.
- Final modular complexity map eklendi.
- Module family/folder depth/file count/function count complexity raporları eklendi.
- Script/test/report-output/DataLake-output/documentation sprawl raporları eklendi.
- Optional slimming plan eklendi.
- Safe consolidation ve duplicate pattern candidate registry eklendi.
- Naming/config/DataLake/script CLI/test suite/docs navigation simplification candidate registry eklendi.
- Repo ergonomics rehearsal guide eklendi.
- Maintainer onboarding simplification guide eklendi.
- Local maintainability improvement seed eklendi.
- Complexity no-go/safe-go summary eklendi.
- Simplification exception/gap/risk registerları eklendi.
- Maintainability readiness score report eklendi.
- Simplification validation ve quality report eklendi.
- LocalSimplificationPipeline eklendi.
- DataLake local simplification kayıt desteği aldı.
- Local simplification scriptleri eklendi.
- Testler genişletildi.
"""
    content += injection
    file_path.write_text(content, encoding="utf-8")

def patch_other_docs():
    docs = [
        "commodity_fx_signal_bot/docs/OPERATOR_MANUAL.md",
        "commodity_fx_signal_bot/docs/ANALYST_HANDBOOK.md",
        "commodity_fx_signal_bot/docs/CODEX_AGENT_GUIDE.md",
        "commodity_fx_signal_bot/docs/SAFE_USAGE_GUIDE.md",
        "commodity_fx_signal_bot/docs/INSTALLATION.md",
        "commodity_fx_signal_bot/docs/CONFIGURATION.md"
    ]
    injection = """
## Local Simplification (Phase 82)
- Final modular complexity map bir architecture assessment değildir. Sadece fikir verir.
- Optional slimming plan dry-run bir rehearsal'dır. Gerçek refactor yapmaz.
- Consolidation candidates otomatik refactor demek değildir, manuel inceleme gerektirir.
- Repo ergonomics guide okuma kolaylığı sağlamak içindir.
- Maintainability readiness score bir architecture approval değildir.
- Gerçek refactor, dosya silme/taşıma, cleanup execution, package publish, cloud upload, deployment, canlı emir, broker execution ve yatırım tavsiyesi **yoktur**.
"""
    for doc in docs:
        p = Path(doc)
        if not p.exists(): continue
        c = p.read_text(encoding="utf-8")
        if "Local Simplification (Phase 82)" not in c:
            c += injection
            p.write_text(c, encoding="utf-8")

def main():
    patch_readme()
    patch_architecture()
    patch_phase_log()
    patch_other_docs()
    print("Patched docs for phase 82")

if __name__ == "__main__":
    main()
