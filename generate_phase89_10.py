import os
from pathlib import Path
import re

def update_readme():
    path = "README.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    new_section = """
## Local Long-Term Operations and v1.x Roadmap Governance

Final local long-term operations binder gerçek production operations plan değildir. Yearly review calendar gerçek scheduler veya calendar entegrasyonu değildir. Lifecycle maintenance workbook official lifecycle policy değildir. Deprecation rehearsal gerçek deprecation veya otomatik migration değildir. v1.x roadmap governance packet official roadmap commitment değildir. Roadmap candidates implementation commitment değildir. Lifecycle readiness score production operations approval değildir.

Cloud upload, package publish, Docker push, Git tag, deployment, live trading, broker execution ve yatırım tavsiyesi yoktur. Çıktılar `data/lake/local_longterm_operations` ve `reports/output/local_longterm_operations` altında oluşur.

### Komutlar
```bash
python -m scripts.run_longterm_domain_registry
python -m scripts.run_final_longterm_operations_binder
python -m scripts.run_yearly_review_calendar
python -m scripts.run_lifecycle_maintenance_workbook
python -m scripts.run_deprecation_rehearsal
python -m scripts.run_v1x_roadmap_governance
python -m scripts.run_lifecycle_quality_report
python -m scripts.run_lifecycle_status
```
"""
    if "Local Long-Term Operations and v1.x Roadmap Governance" not in content:
        with open(path, "a", encoding="utf-8") as f:
            f.write(new_section)
        print("Updated README.md")

def update_architecture():
    path = "commodity_fx_signal_bot/docs/ARCHITECTURE.md"
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_flow = """
Release Candidate / Incident Response / RedTeam / Governance Control / Usability / Performance / Simplification / Reuse / Closure / Archival / Delivery / Acceptance / Hardening / Synthesis / Docs / Reports / DataLake / Scripts / Tests / Safety
→ LongTermOperationsProfileRegistry
→ LongTermDomainRegistry
→ FinalLocalLongTermOperationsBinder
→ ReviewCalendars
→ LifecycleMaintenanceWorkbook
→ MaintenanceCadence
→ MaintenanceOwnership
→ MaintenanceEvidence
→ RetentionDataLakeGeneratedDocsReview
→ QualitySafetyIncidentRedTeamGovernanceReview
→ DeprecationRehearsal
→ DeprecationCandidates
→ NonDeprecationBoundaries
→ MigrationReadiness
→ V1xRoadmapGovernance
→ RoadmapCandidates
→ RoadmapPriority
→ FeatureIntake
→ ChangeControl
→ RiskBenefitReview
→ RoadmapNoGoSafeGo
→ LifecycleExceptions
→ LifecycleGaps
→ LifecycleRisks
→ LifecycleReadinessScoring
→ LifecycleValidation
→ LifecycleQuality
→ Local Long-Term Operations Outputs
"""
    if "LongTermOperationsProfileRegistry" not in content:
        with open(path, "a", encoding="utf-8") as f:
            f.write(new_flow)
        print("Updated ARCHITECTURE.md")

def update_phase_log():
    path = "commodity_fx_signal_bot/docs/PHASE_LOG.md"
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    new_log = """
### Phase 89
- Local long-term operations profile sistemi eklendi.
- Long-term operations label registry eklendi.
- LongTermDomain, ReviewCalendarItem, LifecycleWorkbookItem, DeprecationCandidate, RoadmapCandidate ve LifecycleFinding modelleri eklendi.
- Long-term domain registry eklendi.
- Final local long-term operations binder eklendi.
- Yearly/quarterly/monthly/weekly review calendar registry eklendi.
- Lifecycle maintenance workbook eklendi.
- Maintenance cadence registry, ownership rehearsal matrix ve evidence checklist eklendi.
- Retention/DataLake/generated docs/quality/safety/incident-redteam-governance review workbook'leri eklendi.
- Deprecation rehearsal registry ve candidate registry eklendi.
- Non-deprecation boundary registry, decision checklist ve impact rehearsal matrix eklendi.
- Migration readiness rehearsal ve migration non-goals registry eklendi.
- v1.x roadmap governance packet eklendi.
- v1.x roadmap candidate registry, priority matrix, feature intake checklist, change-control ledger ve risk/benefit review matrix eklendi.
- v1.x roadmap no-go/safe-go summary eklendi.
- Lifecycle exception/gap/risk registerları eklendi.
- Lifecycle readiness score report eklendi.
- Lifecycle validation ve quality report eklendi.
- LocalLongTermOperationsPipeline eklendi.
- DataLake local long-term operations kayıt desteği aldı.
- Local long-term operations scriptleri eklendi.
- Testler genişletildi.
"""
    if "Phase 89" not in content:
        with open(path, "a", encoding="utf-8") as f:
            f.write(new_log)
        print("Updated PHASE_LOG.md")

def update_manuals():
    manuals = [
        "commodity_fx_signal_bot/docs/OPERATOR_MANUAL.md", 
        "commodity_fx_signal_bot/docs/ANALYST_HANDBOOK.md", 
        "commodity_fx_signal_bot/docs/CODEX_AGENT_GUIDE.md", 
        "commodity_fx_signal_bot/docs/SAFE_USAGE_GUIDE.md", 
        "commodity_fx_signal_bot/docs/INSTALLATION.md", 
        "commodity_fx_signal_bot/docs/CONFIGURATION.md"
    ]
    
    new_section = """
## Local Long-Term Operations
- **Long-term operations binder nasıl okunur?** Bu belge lokal bakım işlemlerinin bir provasıdır.
- **Review calendars nasıl yorumlanır?** Sadece manuel hatırlatma ve inceleme önerileridir, entegre takvim değildir.
- **Lifecycle maintenance workbook neden official lifecycle policy değildir?** Offline/local bir projedir ve regülatif bağlayıcılığı yoktur.
- **Deprecation rehearsal neden gerçek kaldırma/migration değildir?** Dosya silinmez, taşınmaz, değiştirilmez; sadece raporlanır.
- **v1.x roadmap governance neden official roadmap commitment değildir?** Planlama provasıdır, kesin sürüm garantisi sunmaz.
- **Feature intake ve change-control rehearsal nasıl kullanılır?** Sistemin gelişimini lokal bağlamda teorik olarak denetlemek için kullanılır.
- **ÖNEMLİ:** Gerçek operations plan, package publish, Docker push, Git tag, cloud upload, deployment, legal/compliance sign-off, canlı emir, broker execution ve yatırım tavsiyesi YOKTUR.
"""
    for m in manuals:
        if os.path.exists(m):
            with open(m, "r", encoding="utf-8") as f:
                content = f.read()
            if "Local Long-Term Operations" not in content:
                with open(m, "a", encoding="utf-8") as f:
                    f.write(new_section)
                print(f"Updated {m}")

if __name__ == "__main__":
    update_readme()
    update_architecture()
    update_phase_log()
    update_manuals()
