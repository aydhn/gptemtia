import os
from pathlib import Path

def patch_file(filepath, content_to_append):
    path = Path(filepath)
    if path.exists():
        content = path.read_text(encoding="utf-8")
        path.write_text(content + "\\n\\n" + content_to_append, encoding="utf-8")
        print(f"Patched {filepath}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content_to_append, encoding="utf-8")
        print(f"Created {filepath}")

def generate_docs():
    readme_content = """
## Local Continuity Intelligence and Operator Memory Rehearsal
- Final local operator memory book gerçek persistent memory sistemi değildir.
- Lessons-learned codex official lessons-learned report değildir.
- Decision rationale capsule official decision record değildir.
- Future-reader guide legal/compliance instruction değildir.
- Continuity intelligence binder official knowledge-management policy değildir.
- Continuity readiness score official approval değildir.
- Cloud memory sync, package publish, Docker push, Git tag, deployment, live trading, broker execution ve yatırım tavsiyesi yoktur.
- Çıktılar data/lake/local_continuity_intelligence ve reports/output/local_continuity_intelligence altında oluşur.

Komutlar:
python -m scripts.run_continuity_domain_registry
python -m scripts.run_operator_memory_book
python -m scripts.run_lessons_learned_codex
python -m scripts.run_decision_rationale_capsule
python -m scripts.run_future_reader_guide
python -m scripts.run_continuity_intelligence_binder
python -m scripts.run_continuity_quality_report
python -m scripts.run_continuity_status
"""
    patch_file("README.md", readme_content)

    phase_log = """
### Phase 92: Final Local Operator Memory Book & Continuity Intelligence Layer
- Local continuity intelligence profile sistemi eklendi.
- Continuity label registry eklendi.
- ContinuityDomain, OperatorMemoryItem, LessonLearnedItem, DecisionRationaleItem, FutureReaderItem ve ContinuityFinding modelleri eklendi.
- Continuity domain registry eklendi.
- Final local operator memory book eklendi.
- Operator memory index/topic map/reading route/quick-reference cards eklendi.
- Lessons-learned codex eklendi.
- Lessons-learned category/phase/risk/quality/safety maps eklendi.
- Decision rationale capsule eklendi.
- Decision rationale registry ve tradeoff matrix eklendi.
- Architecture/governance/safety/DataLake-reporting/testing-quality decision recaps eklendi.
- Future-reader guide eklendi.
- Future-reader onboarding/role/first-hour/first-day/first-week guides eklendi.
- Continuity intelligence binder eklendi.
- Continuity knowledge graph rehearsal, concept index ve glossary eklendi.
- Command/output interpretation guides eklendi.
- Anti-misuse ve maintenance reminder maps eklendi.
- Continuity no-go/safe-go summary eklendi.
- Continuity exception/gap/risk registerları eklendi.
- Continuity readiness score report eklendi.
- Continuity validation ve quality report eklendi.
- LocalContinuityIntelligencePipeline eklendi.
- DataLake local continuity intelligence kayıt desteği aldı.
- Local continuity scriptleri eklendi.
- Testler genişletildi.
"""
    patch_file("docs/PHASE_LOG.md", phase_log)

    arch_log = """
## Continuity Intelligence Architecture Flow (Phase 92)
Post-Completion Preservation / Project Completion / LongTerm Operations / Release Candidate / Incident Response / RedTeam / Governance Control / Usability / Performance / Simplification / Reuse / Closure / Archival / Delivery / Acceptance / Hardening / Synthesis / Docs / Reports / DataLake / Scripts / Tests / Safety
→ ContinuityProfileRegistry
→ ContinuityDomainRegistry
→ FinalLocalOperatorMemoryBook
→ OperatorMemoryMaps
→ OperatorMemoryCards
→ LessonsLearnedCodex
→ LessonsLearnedMaps
→ DecisionRationaleCapsule
→ DecisionTradeoffs
→ DecisionRecaps
→ FutureReaderGuide
→ FutureReaderMaps
→ ContinuityBinder
→ ContinuityKnowledgeGraphRehearsal
→ ContinuityConceptIndex
→ ContinuityGlossary
→ InterpretationGuides
→ ReminderMaps
→ ContinuityNoGoSafeGo
→ ContinuityExceptions
→ ContinuityGaps
→ ContinuityRisks
→ ContinuityReadinessScoring
→ ContinuityValidation
→ ContinuityQuality
→ Local Continuity Intelligence Outputs
"""
    patch_file("docs/ARCHITECTURE.md", arch_log)

    manuals_log = """
## Local Continuity Intelligence
- Operator memory book nasıl okunur? -> data/lake/local_continuity_intelligence ve reports altından.
- Lessons-learned codex nasıl yorumlanır? -> Bu sadece local bir prova olup official report değildir.
- Decision rationale capsule neden official decision record değildir? -> Sistem hiçbir recordı official olarak sunamaz, yatırım tavsiyesi veremez, cloud memory kullanamaz.
- Future-reader guide nasıl kullanılır? -> Onboarding map ve reading route ile projeye hizli giriş.
- Continuity binder nasıl okunur? -> Tüm bilgilerin indekslenmiş özetidir.
- Command/output interpretation guides neden komut çalıştırmaz? -> Bu fazda no-go durumundadır ve safe execution kuralları gereği komutlar otomatize edilmez.
- Gerçek memory system, cloud sync, official decision record, package publish, deployment, canlı emir, broker execution ve yatırım tavsiyesi YOKTUR.
"""
    manuals = [
        "docs/OPERATOR_MANUAL.md",
        "docs/ANALYST_HANDBOOK.md",
        "docs/CODEX_AGENT_GUIDE.md",
        "docs/SAFE_USAGE_GUIDE.md",
        "docs/INSTALLATION.md",
        "docs/CONFIGURATION.md"
    ]
    for m in manuals:
        patch_file(m, manuals_log)

if __name__ == "__main__":
    generate_docs()
    print("Docs generated")
