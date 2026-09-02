import os

def patch_readme():
    file_path = "README.md"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_section = """
## Local Incident-Response Rehearsal and Resilience Supervision (Phase 87)

- **Final local incident-response rehearsal packet** gerçek incident report değildir.
- **Safety event register** gerçek incident kaydı değildir.
- **Rollback decision playbook** gerçek rollback yapmaz.
- **Containment/degraded-mode/recovery rehearsal** canlı sistemi değiştirmez.
- **Post-incident review templates** resmi olay raporu değildir.
- **Incident readiness score** production recovery approval değildir.
- Cloud upload, package publish, telemetry, dashboard, live trading, broker execution ve yatırım tavsiyesi yoktur.
- Çıktılar `data/lake/local_incident_response` ve `reports/output/local_incident_response` altında oluşur.

### Komutlar:
```bash
python -m scripts.run_incident_domain_registry
python -m scripts.run_final_local_incident_response
python -m scripts.run_safety_event_register
python -m scripts.run_rollback_decision_playbook
python -m scripts.run_post_incident_review_templates
python -m scripts.run_incident_quality_report
python -m scripts.run_incident_status
```
"""
    if "Local Incident-Response Rehearsal and Resilience Supervision" not in content:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(new_section)
        print("Updated README.md")

def patch_architecture():
    file_path = "docs/ARCHITECTURE.md"
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("""
### Phase 87 Pipeline
RedTeam / Governance Control / Usability / Performance / Simplification / Reuse / Closure / Archival / Delivery / Acceptance / Hardening / Synthesis / Docs / Reports / DataLake / Scripts / Tests / Safety
→ IncidentResponseProfileRegistry
→ IncidentDomainRegistry
→ FinalLocalIncidentResponseRehearsalPacket
→ SafetyEventRegister
→ SafetyEventTaxonomy
→ SeverityTriageClassification
→ SpecificEventRegistries
→ RollbackDecisionPlaybook
→ RollbackBoundaries
→ ContainmentRehearsal
→ DegradedModeRehearsal
→ RecoveryRehearsal
→ ResilienceSupervision
→ EvidenceSnapshotIndex
→ IncidentReadingOrder
→ TimelineTemplates
→ PostIncidentReviewTemplates
→ RootCauseCategories
→ CorrectiveActionRehearsal
→ CommunicationTemplates
→ EscalationDecisions
→ IncidentNoGoSafeGo
→ IncidentExceptions
→ IncidentGaps
→ IncidentRisks
→ IncidentReadinessScoring
→ IncidentValidation
→ IncidentQuality
→ Local Incident Response Outputs
""")
        print("Updated ARCHITECTURE.md")

def patch_phase_log():
    file_path = "docs/PHASE_LOG.md"
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("""
## Phase 87
- Local incident-response profile sistemi eklendi.
- Incident label registry eklendi.
- IncidentDomain, SafetyEvent, RollbackDecisionItem, PostIncidentTemplate ve IncidentFinding modelleri eklendi.
- Incident domain registry eklendi.
- Final local incident-response rehearsal packet eklendi.
- Safety event register eklendi.
- Safety event taxonomy, severity taxonomy, triage checklist ve classification registry eklendi.
- Specific event registry’leri eklendi.
- Rollback decision playbook eklendi.
- Rollback/non-rollback boundary registry eklendi.
- Containment, degraded-mode ve recovery rehearsal çıktıları eklendi.
- Offline resilience supervision guide eklendi.
- Safety event evidence snapshot index ve incident reading order eklendi.
- Incident timeline template registry ve post-incident review template library eklendi.
- Root-cause category registry, corrective-action rehearsal ve communication templates eklendi.
- Escalation decision registry eklendi.
- Incident no-go/safe-go summary eklendi.
- Incident exception/gap/risk registerları eklendi.
- Incident readiness score report eklendi.
- Incident validation ve quality report eklendi.
- LocalIncidentResponsePipeline eklendi.
- DataLake local incident response kayıt desteği aldı.
- Local incident response scriptleri eklendi.
- Testler genişletildi.
""")
        print("Updated PHASE_LOG.md")

def patch_other_docs():
    docs = [
        "docs/OPERATOR_MANUAL.md",
        "docs/ANALYST_HANDBOOK.md",
        "docs/CODEX_AGENT_GUIDE.md",
        "docs/SAFE_USAGE_GUIDE.md",
        "docs/INSTALLATION.md",
        "docs/CONFIGURATION.md"
    ]
    
    append_text = """
## Local Incident Response
- Incident-response rehearsal packet nasıl okunur: Sadece mock offline rehearsal raporudur.
- Safety event register nasıl yorumlanır: Offline event taxonomy ve classification'ı içerir.
- Rollback decision playbook neden gerçek rollback değildir: Sistem konfigürasyonunu veya durumunu geri almaz, sadece onay gerektiren kural listesidir.
- Containment/degraded-mode/recovery rehearsal neden canlı sistemi değiştirmez: Bu playbooklar tamamen dry-run olarak çalışır.
- Post-incident review template nasıl kullanılır: Sadece geçmişe yönelik taslak çıkarır.
- Incident no-go/safe-go sınırları nasıl korunur: Kalite kontrolleri tarafından hard limit olarak izlenir.
- Uyarı: Gerçek incident response, forensic analiz, production recovery, canlı emir, broker execution, deployment ve yatırım tavsiyesi YOKTUR.
"""
    for doc in docs:
        with open(doc, "a", encoding="utf-8") as f:
            f.write(append_text)
        print(f"Updated {doc}")

if __name__ == "__main__":
    patch_readme()
    patch_architecture()
    patch_phase_log()
    patch_other_docs()
