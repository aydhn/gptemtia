import os
from pathlib import Path

ROOT = Path("commodity_fx_signal_bot")

# Update .env.example
env_path = ROOT / ".env.example"
env_example = ""
if env_path.exists():
    with open(env_path, "r", encoding="utf-8") as f:
        env_example = f.read()

if "LOCAL_GOVERNANCE_CONTROL_ENABLED" not in env_example:
    env_example += """
LOCAL_GOVERNANCE_CONTROL_ENABLED=true
DEFAULT_LOCAL_GOVERNANCE_CONTROL_PROFILE=balanced_local_governance_control
LOCAL_GOVERNANCE_CONTROL_DEFAULT_LANGUAGE=tr
LOCAL_GOVERNANCE_CONTROL_DRY_RUN_DEFAULT=true
LOCAL_GOVERNANCE_CONTROL_ALLOW_REAL_GOVERNANCE_DECISION=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_REAL_COMMITTEE_APPROVAL=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_LEGAL_SIGNOFF=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_COMPLIANCE_SIGNOFF=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_PRODUCTION_APPROVAL_CLAIM=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_LIVE_TRADING_APPROVAL_CLAIM=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_INVESTMENT_ADVICE=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_DASHBOARD_CREATION=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_GUI_CREATION=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_TUI_CREATION=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_TELEMETRY=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_CLOUD_UPLOAD=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_PACKAGE_PUBLISH=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_EXTERNAL_SERVICE=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_EXTERNAL_LLM=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_FILE_MODIFICATION=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_FILE_DELETION=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_FILE_MOVE=false
LOCAL_GOVERNANCE_CONTROL_ALLOW_OVERWRITE=false
LOCAL_GOVERNANCE_CONTROL_SCAN_DOCS=true
LOCAL_GOVERNANCE_CONTROL_SCAN_REPORTS=true
LOCAL_GOVERNANCE_CONTROL_SCAN_DATA_LAKE=true
LOCAL_GOVERNANCE_CONTROL_SCAN_SCRIPTS=true
LOCAL_GOVERNANCE_CONTROL_SCAN_TESTS=true
LOCAL_GOVERNANCE_CONTROL_SCAN_GENERATED_DOCS=true
LOCAL_GOVERNANCE_CONTROL_SCAN_USABILITY_OUTPUTS=true
LOCAL_GOVERNANCE_CONTROL_SCAN_PERFORMANCE_OUTPUTS=true
LOCAL_GOVERNANCE_CONTROL_SCAN_SAFETY_OUTPUTS=true
LOCAL_GOVERNANCE_CONTROL_MAX_ITEMS=500000
LOCAL_GOVERNANCE_CONTROL_MAX_LEDGER_ROWS=10000
LOCAL_GOVERNANCE_CONTROL_MIN_READINESS_SCORE=0.40
LOCAL_GOVERNANCE_CONTROL_MIN_QUALITY_SCORE=0.40
LOCAL_GOVERNANCE_CONTROL_SAVE_REPORTS=true
"""
    with open(env_path, "w", encoding="utf-8") as f:
        f.write(env_example)


# Update settings.py
settings_path = ROOT / "config" / "settings.py"
with open(settings_path, "r", encoding="utf-8") as f:
    settings_content = f.read()

if "local_governance_control_enabled" not in settings_content:
    new_settings = """    local_governance_control_enabled: bool = True
    default_local_governance_control_profile: str = "balanced_local_governance_control"
    local_governance_control_default_language: str = "tr"
    local_governance_control_dry_run_default: bool = True
    local_governance_control_allow_real_governance_decision: bool = False
    local_governance_control_allow_real_committee_approval: bool = False
    local_governance_control_allow_legal_signoff: bool = False
    local_governance_control_allow_compliance_signoff: bool = False
    local_governance_control_allow_production_approval_claim: bool = False
    local_governance_control_allow_live_trading_approval_claim: bool = False
    local_governance_control_allow_broker_readiness_claim: bool = False
    local_governance_control_allow_investment_advice: bool = False
    local_governance_control_allow_model_deployment_claim: bool = False
    local_governance_control_allow_dashboard_creation: bool = False
    local_governance_control_allow_gui_creation: bool = False
    local_governance_control_allow_tui_creation: bool = False
    local_governance_control_allow_telemetry: bool = False
    local_governance_control_allow_cloud_upload: bool = False
    local_governance_control_allow_package_publish: bool = False
    local_governance_control_allow_external_service: bool = False
    local_governance_control_allow_external_llm: bool = False
    local_governance_control_allow_file_modification: bool = False
    local_governance_control_allow_file_deletion: bool = False
    local_governance_control_allow_file_move: bool = False
    local_governance_control_allow_overwrite: bool = False
    local_governance_control_scan_docs: bool = True
    local_governance_control_scan_reports: bool = True
    local_governance_control_scan_data_lake: bool = True
    local_governance_control_scan_scripts: bool = True
    local_governance_control_scan_tests: bool = True
    local_governance_control_scan_generated_docs: bool = True
    local_governance_control_scan_usability_outputs: bool = True
    local_governance_control_scan_performance_outputs: bool = True
    local_governance_control_scan_safety_outputs: bool = True
    local_governance_control_max_items: int = 500000
    local_governance_control_max_ledger_rows: int = 10000
    local_governance_control_min_readiness_score: float = 0.40
    local_governance_control_min_quality_score: float = 0.40
    local_governance_control_save_reports: bool = True
"""
    settings_content = settings_content.replace(
        "    class Config:", 
        new_settings + "\n    class Config:"
    )
    with open(settings_path, "w", encoding="utf-8") as f:
        f.write(settings_content)


# Update paths.py
paths_path = ROOT / "config" / "paths.py"
with open(paths_path, "r", encoding="utf-8") as f:
    paths_content = f.read()

if "local_governance_control" not in paths_content:
    new_paths = """    local_governance_control = reports_output / "local_governance_control"
    local_governance_control_csv = local_governance_control / "csv"
    local_governance_control_markdown = local_governance_control / "markdown"
    local_governance_control_txt = local_governance_control / "txt"
    local_governance_control_json = local_governance_control / "json"

    docs_generated_local_governance_control = docs_generated / "local_governance_control"

    lake_local_governance_control = data_lake / "local_governance_control"
    lake_local_governance_control_profiles = lake_local_governance_control / "profiles"
    lake_local_governance_control_domains = lake_local_governance_control / "domains"
    lake_local_governance_control_control_room = lake_local_governance_control / "control_room"
    lake_local_governance_control_executive = lake_local_governance_control / "executive"
    lake_local_governance_control_manual_approval = lake_local_governance_control / "manual_approval"
    lake_local_governance_control_risk_committee = lake_local_governance_control / "risk_committee"
    lake_local_governance_control_operator_supervision = lake_local_governance_control / "operator_supervision"
    lake_local_governance_control_escalation = lake_local_governance_control / "escalation"
    lake_local_governance_control_roles = lake_local_governance_control / "roles"
    lake_local_governance_control_authority = lake_local_governance_control / "authority"
    lake_local_governance_control_boundaries = lake_local_governance_control / "boundaries"
    lake_local_governance_control_no_go_safe_go = lake_local_governance_control / "no_go_safe_go"
    lake_local_governance_control_evidence = lake_local_governance_control / "evidence"
    lake_local_governance_control_reading_order = lake_local_governance_control / "reading_order"
    lake_local_governance_control_metrics = lake_local_governance_control / "metrics"
    lake_local_governance_control_templates = lake_local_governance_control / "templates"
    lake_local_governance_control_signoff_forms = lake_local_governance_control / "signoff_forms"
    lake_local_governance_control_exceptions = lake_local_governance_control / "exceptions"
    lake_local_governance_control_unresolved = lake_local_governance_control / "unresolved"
    lake_local_governance_control_open_decisions = lake_local_governance_control / "open_decisions"
    lake_local_governance_control_risks = lake_local_governance_control / "risks"
    lake_local_governance_control_scoring = lake_local_governance_control / "scoring"
    lake_local_governance_control_validation = lake_local_governance_control / "validation"
    lake_local_governance_control_quality = lake_local_governance_control / "quality"
"""
    
    paths_content = paths_content.replace(
        "    return cls(project_root)",
        new_paths + "\n    return cls(project_root)"
    )

    ensure_dirs_str = """        cls.local_governance_control, cls.local_governance_control_csv, cls.local_governance_control_markdown,
        cls.local_governance_control_txt, cls.local_governance_control_json, cls.docs_generated_local_governance_control,
        cls.lake_local_governance_control, cls.lake_local_governance_control_profiles, cls.lake_local_governance_control_domains,
        cls.lake_local_governance_control_control_room, cls.lake_local_governance_control_executive, cls.lake_local_governance_control_manual_approval,
        cls.lake_local_governance_control_risk_committee, cls.lake_local_governance_control_operator_supervision, cls.lake_local_governance_control_escalation,
        cls.lake_local_governance_control_roles, cls.lake_local_governance_control_authority, cls.lake_local_governance_control_boundaries,
        cls.lake_local_governance_control_no_go_safe_go, cls.lake_local_governance_control_evidence, cls.lake_local_governance_control_reading_order,
        cls.lake_local_governance_control_metrics, cls.lake_local_governance_control_templates, cls.lake_local_governance_control_signoff_forms,
        cls.lake_local_governance_control_exceptions, cls.lake_local_governance_control_unresolved, cls.lake_local_governance_control_open_decisions,
        cls.lake_local_governance_control_risks, cls.lake_local_governance_control_scoring, cls.lake_local_governance_control_validation,
        cls.lake_local_governance_control_quality,"""
    
    paths_content = paths_content.replace(
        "cls.lake_local_usability,",
        ensure_dirs_str + "\n        cls.lake_local_usability,"
    )
    with open(paths_path, "w", encoding="utf-8") as f:
        f.write(paths_content)


# Update README.md
readme_path = ROOT / "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

if "Local Governance Control Room and Operator Supervision" not in readme_content:
    readme_ext = """
## Local Governance Control Room and Operator Supervision
Final local governance control room packet gerçek dashboard veya yönetim sistemi değildir.
Executive oversight packet resmi yönetim raporu değildir.
Manual approval ledger gerçek onay defteri değildir.
Risk committee rehearsal pack gerçek risk komitesi değildir.
Operator supervision guide canlı operasyon gözetimi değildir.
Approval boundaries resmi onay framework’ü değildir.
Governance readiness score production approval veya compliance sign-off değildir.
Çıktılar data/lake/local_governance_control ve reports/output/local_governance_control altında oluşur.

### Komutlar:
```bash
python -m scripts.run_governance_domain_registry
python -m scripts.run_final_governance_control_room
python -m scripts.run_executive_oversight_packet
python -m scripts.run_manual_approval_ledger
python -m scripts.run_risk_committee_rehearsal
python -m scripts.run_governance_quality_report
python -m scripts.run_governance_status
```
"""
    readme_content += readme_ext
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

# Update doc files
doc_files = [
    "ARCHITECTURE.md",
    "PHASE_LOG.md",
    "OPERATOR_MANUAL.md",
    "ANALYST_HANDBOOK.md",
    "CODEX_AGENT_GUIDE.md",
    "SAFE_USAGE_GUIDE.md",
    "INSTALLATION.md",
    "CONFIGURATION.md"
]

for doc_name in doc_files:
    doc = ROOT / "docs" / doc_name
    if not doc.exists():
        continue
    with open(doc, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Local Governance Control" not in content:
        if "ARCHITECTURE" in doc_name:
            content = content.replace("Safety\\n", "Safety\\n→ GovernanceControlProfileRegistry\\n→ GovernanceDomainRegistry\\n→ FinalLocalGovernanceControlRoomPacket\\n→ ExecutiveOversightPacket\\n→ ManualApprovalLedger\\n→ RiskCommitteeRehearsalPack\\n→ OperatorSupervision\\n→ EscalationMatrix\\n→ GovernanceRoles\\n→ DecisionAuthorityMap\\n→ ApprovalBoundaries\\n→ GovernanceNoGoSafeGo\\n→ OversightEvidence\\n→ OversightReadingOrder\\n→ GovernanceMetrics\\n→ MeetingNoteTemplates\\n→ SignoffRehearsalForms\\n→ ExceptionEscalation\\n→ UnresolvedOpenDecisions\\n→ GovernanceRisks\\n→ GovernanceReadinessScoring\\n→ GovernanceValidation\\n→ GovernanceQuality\\n→ Local Governance Control Outputs\\n")
        elif "PHASE_LOG" in doc_name:
            content += """
## Phase 85: Final Local Governance Control Room, Executive Oversight Packet, Manual Approval Ledger, Risk Committee Rehearsal ve Operator Supervision Layer
- Local governance control profile sistemi eklendi.
- Governance control label registry eklendi.
- GovernanceDomain, ManualApprovalItem, OversightItem, EscalationItem ve GovernanceFinding modelleri eklendi.
- Governance domain registry eklendi.
- Final local governance control room packet eklendi.
- Executive oversight packet eklendi.
- Manual approval ledger ve checklist registry eklendi.
- Risk committee rehearsal pack eklendi.
- Risk committee agenda template registry ve decision rehearsal ledger eklendi.
- Operator supervision guide ve checklist eklendi.
- Escalation matrix registry eklendi.
- Governance roles matrix ve decision authority map rehearsal eklendi.
- Approval/non-approval boundary registry eklendi.
- Governance no-go/safe-go summary eklendi.
- Oversight evidence index ve report reading order eklendi.
- Governance KPI rehearsal registry ve metric dictionary eklendi.
- Meeting note template library ve manual sign-off rehearsal form library eklendi.
- Exception escalation, unresolved item ve open decision register eklendi.
- Governance risk summary eklendi.
- Governance readiness score report eklendi.
- Governance validation ve quality report eklendi.
- LocalGovernanceControlPipeline eklendi.
- DataLake local governance control kayıt desteği aldı.
- Local governance scriptleri eklendi.
- Testler genişletildi.
"""
        else:
            content += """
## Local Governance Control Room and Operator Supervision

- **Governance control room packet nasıl okunur?** Control room packet gerçek dashboard veya yönetim sistemi değildir, offline/local provadır.
- **Executive oversight packet nasıl yorumlanır?** Resmi yönetim raporu değildir.
- **Manual approval ledger neden gerçek onay değildir?** Local/offline manuel review provasıdır, onay ve sign-off içermez.
- **Risk committee rehearsal neden gerçek komite değildir?** Formalite ve gözetim adımlarının provasıdır.
- **Operator supervision guide nasıl kullanılır?** Offline dokümantasyon olarak okunur ve uygulanır.
- **Approval/non-approval boundaries nasıl korunur?** Gerçek onay alınmadan ve non-approval boundaries ihlal edilmeden uygulanır.

**ÖNEMLİ:** Gerçek yönetim kararı, compliance sign-off, production approval, canlı emir, broker execution, deployment ve yatırım tavsiyesi olmadığı açık yazılsın.
"""
        with open(doc, "w", encoding="utf-8") as f:
            f.write(content)

print("Done updating settings, paths, env, and docs.")
