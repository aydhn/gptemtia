import os
from pathlib import Path

def write_file(path: str, content: str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def append_file(path: str, content: str):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(content)

def read_file(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def insert_after_pattern(content: str, pattern: str, insertion: str) -> str:
    parts = content.split(pattern)
    if len(parts) > 1:
        return parts[0] + pattern + "\n" + insertion + parts[1]
    return content

# Update README.md
readme = read_file("README.md")
if "Local v1.0 Closure Rehearsal and Final Meta-Review" not in readme:
    readme_ext = """
## Local v1.0 Closure Rehearsal and Final Meta-Review

- v1.0 local closure gerçek v1.0 release değildir.
- Final meta-review production release veya resmi proje kapanışı değildir.
- Lessons-learned compendium denetim sertifikası değildir.
- Future roadmap backlog implementation approval değildir.
- Post-project governance rehearsal resmi yönetim prosedürü değildir.
- Closure readiness score production approval veya canlı trading izni değildir.
- Cloud upload, package publish, deployment ve canlı trading yoktur.
- Çıktılar data/lake/local_closure ve reports/output/local_closure altında oluşur.

### Komutlar
```bash
python -m scripts.run_closure_domain_registry
python -m scripts.run_final_meta_review
python -m scripts.run_lessons_learned_compendium
python -m scripts.run_future_roadmap_backlog
python -m scripts.run_v1_local_closure_dossier
python -m scripts.run_closure_quality_report
python -m scripts.run_closure_status
```
"""
    append_file("README.md", readme_ext)

# Update docs/ARCHITECTURE.md
arch = read_file("docs/ARCHITECTURE.md")
if "ClosureProfileRegistry" not in arch:
    arch_ext = """
## Phase 80: Local Closure Flow
Archival / Delivery / Acceptance / Hardening / Synthesis / Briefing / Training / Docs / Reports / DataLake / Scripts / Tests / Safety
→ ClosureProfileRegistry
→ ClosureDomainRegistry
→ FinalProjectMetaReview
→ LessonsLearnedCompendium
→ FutureRoadmapBacklog
→ FuturePhaseCandidateRegistry
→ PostProjectGovernanceRehearsal
→ ClosureRecaps
→ UnresolvedItems
→ OpenQuestions
→ ImprovementBacklog
→ MaintenanceCalendar
→ OwnershipMatrix
→ DecisionLog
→ AssumptionsRegister
→ LimitationsRegister
→ ClosureNoGoSafeGo
→ HandoffAftercare
→ ClosureFAQ
→ ClosureExceptions
→ ClosureGaps
→ ClosureRisks
→ ClosureReadinessScoring
→ V1LocalClosureDossier
→ ClosureValidation
→ ClosureQuality
→ Local Closure Outputs
"""
    append_file("docs/ARCHITECTURE.md", arch_ext)

# Update docs/PHASE_LOG.md
phase_log = read_file("docs/PHASE_LOG.md")
if "Phase 80:" not in phase_log:
    phase_log_ext = """
### Phase 80: Final Meta-Review, Lessons-Learned Compendium, Future Roadmap Backlog, Post-Project Governance Rehearsal ve v1.0 Local Closure Dossier
- Local closure profile sistemi eklendi.
- Closure label registry eklendi.
- ClosureDomain, ClosureItem, LessonLearnedItem, RoadmapItem ve ClosureFinding modelleri eklendi.
- Closure domain registry eklendi.
- Final project meta-review report eklendi.
- Lessons-learned compendium eklendi.
- Future roadmap backlog eklendi.
- Future phase candidate registry eklendi.
- Post-project governance rehearsal guide eklendi.
- v1.0 local closure dossier eklendi.
- Closure executive/technical/safety/architecture/evidence/archival/delivery recaps eklendi.
- Unresolved items ve open questions register eklendi.
- Future improvement backlog eklendi.
- Maintenance calendar ve ownership matrix rehearsal eklendi.
- Decision log, assumptions register ve known limitations register eklendi.
- Closure no-go/safe-go summary eklendi.
- Handoff-aftercare guide ve closure FAQ eklendi.
- Closure exception/gap/risk registerları eklendi.
- Closure readiness score report eklendi.
- Closure validation ve quality report eklendi.
- LocalClosurePipeline eklendi.
- DataLake local closure kayıt desteği aldı.
- Local closure scriptleri eklendi.
- Testler genişletildi.
"""
    append_file("docs/PHASE_LOG.md", phase_log_ext)

# Update other docs
docs_to_update = [
    "docs/OPERATOR_MANUAL.md",
    "docs/ANALYST_HANDBOOK.md",
    "docs/CODEX_AGENT_GUIDE.md",
    "docs/SAFE_USAGE_GUIDE.md",
    "docs/INSTALLATION.md",
    "docs/CONFIGURATION.md"
]

doc_ext = """
### Local Closure Notes (Phase 80)
- Final meta-review `local_closure` klasörü altından okunur.
- Lessons-learned compendium denetim sertifikası değildir.
- Future roadmap backlog implementasyon onayı değildir.
- v1.0 local closure dossier gerçek bir sürüm (release) değildir.
- Closure readiness score production onayı (approval) değildir.
- Handoff-aftercare guide canlı destek anlamına gelmez.
- Gerçek v1 release, production release, official closure, compliance, package publish, cloud upload, deployment, canlı emir, broker execution ve yatırım tavsiyesi YOKTUR.
"""

for d in docs_to_update:
    if Path(d).exists():
        content = read_file(d)
        if "Local Closure Notes (Phase 80)" not in content:
            append_file(d, doc_ext)

