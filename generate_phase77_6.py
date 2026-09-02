import os
import re
from pathlib import Path

BASE_DIR = Path("commodity_fx_signal_bot")
DOCS_DIR = BASE_DIR / "docs"

# 1. Update README.md
readme_path = BASE_DIR / "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

readme_addition = """
## Local Final Acceptance Simulation and Reviewer Pack

- Final acceptance simulation resmi kabul değildir.
- Independent reviewer pack resmi audit veya compliance belgesi değildir.
- Evidence trail local/offline kanıt izi katalogudur; compliance sertifikası değildir.
- Sign-off rehearsal resmi imza/onay üretmez.
- Acceptance readiness score production release veya canlı trading izni değildir.
- No-go/safe-go summary yalnızca local/offline manual review bağlamındadır.
- Çıktılar data/lake/local_acceptance ve reports/output/local_acceptance altında oluşur.

Komutlar:
```bash
python -m scripts.run_acceptance_domain_registry
python -m scripts.run_final_acceptance_simulation
python -m scripts.run_independent_reviewer_pack
python -m scripts.run_acceptance_evidence_trail
python -m scripts.run_signoff_rehearsal
python -m scripts.run_acceptance_quality_report
python -m scripts.run_acceptance_status
```
"""
if "Local Final Acceptance Simulation" not in readme_content:
    with open(readme_path, "a", encoding="utf-8") as f:
        f.write(readme_addition)

# 2. Update docs/ARCHITECTURE.md
arch_path = DOCS_DIR / "ARCHITECTURE.md"
with open(arch_path, "r", encoding="utf-8") as f:
    arch_content = f.read()

arch_addition = """
Synthesis / Hardening / Docs / Reports / DataLake / Scripts / Tests / Safety / Evidence
→ AcceptanceProfileRegistry
→ AcceptanceDomainRegistry
→ AcceptanceCriteriaRegistry
→ FinalAcceptanceSimulationChecklist
→ ReviewerQuestionBank
→ ReviewerEvidenceRequestMatrix
→ AuditStyleLocalEvidenceTrail
→ EvidenceOutputTrace
→ EvidenceTestTrace
→ EvidenceDocTrace
→ EvidenceSafetyBoundaryTrace
→ IndependentReviewerPack
→ SignoffRehearsalChecklist
→ VerificationScenarioRegistry
→ VerificationRehearsalPlan
→ FinalVerificationEvidenceBinder
→ AcceptanceNoGoSafeGo
→ AcceptanceGaps
→ AcceptanceRisks
→ AcceptanceReadinessScoring
→ AcceptanceValidation
→ AcceptanceQuality
→ Local Acceptance Outputs
"""
if "AcceptanceProfileRegistry" not in arch_content:
    with open(arch_path, "a", encoding="utf-8") as f:
        f.write(arch_addition)

# 3. Update docs/PHASE_LOG.md
phase_path = DOCS_DIR / "PHASE_LOG.md"
with open(phase_path, "r", encoding="utf-8") as f:
    phase_content = f.read()

phase_addition = """
## Phase 77
- Local acceptance profile sistemi eklendi.
- Acceptance label registry eklendi.
- AcceptanceDomain, AcceptanceChecklistItem, ReviewerQuestion, EvidenceTraceItem ve AcceptanceFinding modelleri eklendi.
- Acceptance domain registry eklendi.
- Acceptance criteria registry eklendi.
- Final acceptance simulation checklist eklendi.
- Reviewer question bank eklendi.
- Reviewer evidence request matrix eklendi.
- Independent reviewer pack eklendi.
- Audit-style local evidence trail eklendi.
- Evidence-output/test/doc/safety trace matrix eklendi.
- Sign-off rehearsal checklist ve binder eklendi.
- Final verification scenario registry ve rehearsal plan eklendi.
- Final verification evidence binder eklendi.
- Acceptance exception/no-go/safe-go register eklendi.
- Acceptance gap register ve risk summary eklendi.
- Acceptance readiness score report eklendi.
- Acceptance validation ve quality report eklendi.
- LocalAcceptancePipeline eklendi.
- DataLake local acceptance kayıt desteği aldı.
- Local acceptance scriptleri eklendi.
- Testler genişletildi.
"""
if "Phase 77" not in phase_content:
    with open(phase_path, "a", encoding="utf-8") as f:
        f.write(phase_addition)

# 4. Update OPERATOR_MANUAL, ANALYST_HANDBOOK, CODEX_AGENT_GUIDE, SAFE_USAGE_GUIDE, INSTALLATION, CONFIGURATION
guides = [
    "OPERATOR_MANUAL.md", "ANALYST_HANDBOOK.md", "CODEX_AGENT_GUIDE.md", 
    "SAFE_USAGE_GUIDE.md", "INSTALLATION.md", "CONFIGURATION.md"
]

guide_addition = """
## Local Acceptance
- Final acceptance simulation nasıl okunur? Checklist olarak.
- Independent reviewer pack ne yapar/ne yapmaz? Prova yapar, sertifika vermez.
- Evidence trail nasıl yorumlanır? Local dosya listesi olarak.
- Sign-off rehearsal neden resmi sign-off değildir? Çünkü offline/lokal bir simülasyondur.
- Acceptance readiness score neden production release değildir? Sadece teknik hazırbulunuşluk ölçer.
- No-go/safe-go summary neden canlı işlem izni değildir? Yatırım kararı veya model onayı değildir.
- Resmi audit, compliance, production release, canlı emir, broker execution, deployment ve yatırım tavsiyesi OLMADIĞI AÇIKÇA BİLİNMELİDİR.
"""
for g in guides:
    p = DOCS_DIR / g
    if p.exists():
        with open(p, "r", encoding="utf-8") as f:
            c = f.read()
        if "Local Acceptance" not in c:
            with open(p, "a", encoding="utf-8") as f:
                f.write(guide_addition)
