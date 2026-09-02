import os
from pathlib import Path

def patch_readme():
    print("Patching README.md")
    readme_path = Path("README.md")
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_section = """
## Local Audit-Memory and Knowledge Reuse Kit

- Final audit-memory pack resmi audit memory veya compliance knowledge base değildir.
- Reusable template catalog official engineering standard değildir.
- Local knowledge reuse kit implementation başlatmaz.
- v1.1 planning seed gerçek v1.1 sprint veya release değildir.
- Future project starter pack yeni proje oluşturmaz; yalnızca local/offline başlangıç şablonudur.
- Reuse readiness score production approval veya implementation approval değildir.
- Cloud upload, package publish, deployment ve canlı trading yoktur.
- Çıktılar data/lake/local_reuse ve reports/output/local_reuse altında oluşur.

Komutlar:
```bash
python -m scripts.run_reuse_domain_registry
python -m scripts.run_final_audit_memory_pack
python -m scripts.run_reusable_template_catalog
python -m scripts.run_local_knowledge_reuse_kit
python -m scripts.run_v1_1_planning_seed
python -m scripts.run_reuse_quality_report
python -m scripts.run_reuse_status
```
"""
    if "Local Audit-Memory and Knowledge Reuse Kit" not in content:
        content += new_section
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Successfully patched README.md")

def patch_architecture():
    print("Patching docs/ARCHITECTURE.md")
    arch_path = Path("docs/ARCHITECTURE.md")
    with open(arch_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_flow = """
Closure / Archival / Delivery / Acceptance / Hardening / Synthesis / Briefing / Training / Docs / Reports / DataLake / Scripts / Tests / Safety
→ ReuseProfileRegistry
→ ReuseDomainRegistry
→ FinalAuditMemoryPack
→ PhaseMemoryCapsules
→ ReusableTemplateCatalog
→ PromptTemplateLibrary
→ ModuleBlueprints
→ ScriptPatterns
→ TestPatterns
→ DataLakeContractPatterns
→ ReportPatterns
→ SafetyBoundaryPatterns
→ DocumentationPatterns
→ PatternExtractionReports
→ LocalKnowledgeReuseKit
→ V11PlanningSeed
→ V11BacklogSeed
→ V11SafetyBoundarySeed
→ FutureProjectStarter
→ ReuseNoGoSafeGo
→ ReuseExceptions
→ ReuseGaps
→ ReuseRisks
→ ReuseReadinessScoring
→ ReuseValidation
→ ReuseQuality
→ Local Reuse Outputs
"""
    if "Local Reuse Outputs" not in content:
        content += new_flow
        with open(arch_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Successfully patched ARCHITECTURE.md")

def patch_phase_log():
    print("Patching docs/PHASE_LOG.md")
    phase_log = Path("docs/PHASE_LOG.md")
    with open(phase_log, "r", encoding="utf-8") as f:
        content = f.read()

    new_phase = """
### Phase 81
- Local reuse profile sistemi eklendi.
- Reuse label registry eklendi.
- ReuseDomain, ReusableTemplate, PhaseMemoryCapsule, V11SeedItem ve ReuseFinding modelleri eklendi.
- Reuse domain registry eklendi.
- Final audit-memory pack eklendi.
- Phase memory capsule registry eklendi.
- Cross-project reusable template catalog eklendi.
- Reusable prompt template library eklendi.
- Reusable module/script/test blueprint catalog eklendi.
- Reusable DataLake/report/safety/documentation pattern catalog eklendi.
- Project/architecture/safety/validation-quality/handoff-delivery-closure pattern extraction raporları eklendi.
- Local knowledge reuse kit eklendi.
- v1.1 planning seed eklendi.
- v1.1 candidate backlog, safety boundary, research-only scope ve non-goals registry eklendi.
- Future project starter checklist ve prompt starter pack eklendi.
- Future project directory/test blueprint eklendi.
- Knowledge reuse no-go/safe-go summary eklendi.
- Reuse exception/gap/risk registerları eklendi.
- Reuse readiness score report eklendi.
- Reuse validation ve quality report eklendi.
- LocalReusePipeline eklendi.
- DataLake local reuse kayıt desteği aldı.
- Local reuse scriptleri eklendi.
- Testler genişletildi.
"""
    if "### Phase 81" not in content:
        content += new_phase
        with open(phase_log, "w", encoding="utf-8") as f:
            f.write(content)
        print("Successfully patched PHASE_LOG.md")

def patch_other_docs():
    docs = [
        "docs/OPERATOR_MANUAL.md",
        "docs/ANALYST_HANDBOOK.md",
        "docs/CODEX_AGENT_GUIDE.md",
        "docs/SAFE_USAGE_GUIDE.md",
        "docs/INSTALLATION.md",
        "docs/CONFIGURATION.md"
    ]
    
    new_section = """
### Local Reuse
- **Final audit-memory pack nasıl okunur?**: data/lake/local_reuse altından JSON/CSV veya reports/output/local_reuse/markdown altından okunur.
- **Reusable template catalog ne yapar/ne yapmaz?**: Geçmiş mimarileri modeller, kesinlikle official engineering standard değildir.
- **Local knowledge reuse kit nasıl kullanılır?**: Yeni projeler için offline referans olarak. Implementation başlatmaz.
- **v1.1 planning seed neden implementation approval değildir?**: Çünkü sadece fikir/tohumdur. Canlıya alınmaz.
- **Future project starter pack neden yeni proje oluşturmaz?**: Çünkü auto-generation kodu yoktur, sadece dokümantasyondur.
- **Reuse readiness score neden production approval değildir?**: Çünkü production ortamını test etmez.

*Bu sistemde gerçek v1.1 implementation, production release, official standard, compliance, package publish, cloud upload, deployment, canlı emir, broker execution ve yatırım tavsiyesi YOKTUR.*
"""
    for d in docs:
        p = Path(d)
        if not p.exists():
            with open(p, "w", encoding="utf-8") as f:
                f.write(f"# {p.stem}\n")
        
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "### Local Reuse" not in content:
            content += new_section
            with open(p, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Successfully patched {d}")

if __name__ == "__main__":
    patch_readme()
    patch_architecture()
    patch_phase_log()
    patch_other_docs()
