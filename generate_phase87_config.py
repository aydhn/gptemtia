import os
import re

def update_settings():
    settings_file = "config/settings.py"
    with open(settings_file, "r", encoding="utf-8") as f:
        content = f.read()

    new_settings = """
    local_incident_response_enabled: bool = True
    default_local_incident_response_profile: str = "balanced_local_incident_response"
    local_incident_response_default_language: str = "tr"
    local_incident_response_dry_run_default: bool = True
    local_incident_response_allow_real_incident_response: bool = False
    local_incident_response_allow_real_rollback: bool = False
    local_incident_response_allow_forensic_analysis: bool = False
    local_incident_response_allow_production_recovery: bool = False
    local_incident_response_allow_live_system_halt: bool = False
    local_incident_response_allow_broker_halt_instruction: bool = False
    local_incident_response_allow_compliance_signoff: bool = False
    local_incident_response_allow_legal_signoff: bool = False
    local_incident_response_allow_production_recovery_claim: bool = False
    local_incident_response_allow_live_trading_claim: bool = False
    local_incident_response_allow_broker_readiness_claim: bool = False
    local_incident_response_allow_investment_advice: bool = False
    local_incident_response_allow_model_deployment_claim: bool = False
    local_incident_response_allow_telemetry: bool = False
    local_incident_response_allow_dashboard_creation: bool = False
    local_incident_response_allow_gui_creation: bool = False
    local_incident_response_allow_tui_creation: bool = False
    local_incident_response_allow_cloud_upload: bool = False
    local_incident_response_allow_package_publish: bool = False
    local_incident_response_allow_external_service: bool = False
    local_incident_response_allow_external_llm: bool = False
    local_incident_response_allow_file_modification: bool = False
    local_incident_response_allow_file_deletion: bool = False
    local_incident_response_allow_file_move: bool = False
    local_incident_response_allow_overwrite: bool = False
    local_incident_response_scan_docs: bool = True
    local_incident_response_scan_reports: bool = True
    local_incident_response_scan_data_lake: bool = True
    local_incident_response_scan_scripts: bool = True
    local_incident_response_scan_tests: bool = True
    local_incident_response_scan_generated_docs: bool = True
    local_incident_response_scan_redteam_outputs: bool = True
    local_incident_response_scan_governance_outputs: bool = True
    local_incident_response_scan_safety_outputs: bool = True
    local_incident_response_max_items: int = 500000
    local_incident_response_max_events: int = 10000
    local_incident_response_min_readiness_score: float = 0.40
    local_incident_response_min_quality_score: float = 0.40
    local_incident_response_save_reports: bool = True
"""
    if "local_incident_response_enabled" not in content:
        content = content.replace("class Settings(BaseSettings):", f"class Settings(BaseSettings):\n{new_settings}")
        with open(settings_file, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated settings.py")

def update_env():
    env_file = ".env.example"
    with open(env_file, "r", encoding="utf-8") as f:
        content = f.read()

    new_env = """
LOCAL_INCIDENT_RESPONSE_ENABLED=true
DEFAULT_LOCAL_INCIDENT_RESPONSE_PROFILE=balanced_local_incident_response
LOCAL_INCIDENT_RESPONSE_DEFAULT_LANGUAGE=tr
LOCAL_INCIDENT_RESPONSE_DRY_RUN_DEFAULT=true
LOCAL_INCIDENT_RESPONSE_ALLOW_REAL_INCIDENT_RESPONSE=false
LOCAL_INCIDENT_RESPONSE_ALLOW_REAL_ROLLBACK=false
LOCAL_INCIDENT_RESPONSE_ALLOW_FORENSIC_ANALYSIS=false
LOCAL_INCIDENT_RESPONSE_ALLOW_PRODUCTION_RECOVERY=false
LOCAL_INCIDENT_RESPONSE_ALLOW_LIVE_SYSTEM_HALT=false
LOCAL_INCIDENT_RESPONSE_ALLOW_BROKER_HALT_INSTRUCTION=false
LOCAL_INCIDENT_RESPONSE_ALLOW_COMPLIANCE_SIGNOFF=false
LOCAL_INCIDENT_RESPONSE_ALLOW_LEGAL_SIGNOFF=false
LOCAL_INCIDENT_RESPONSE_ALLOW_PRODUCTION_RECOVERY_CLAIM=false
LOCAL_INCIDENT_RESPONSE_ALLOW_LIVE_TRADING_CLAIM=false
LOCAL_INCIDENT_RESPONSE_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_INCIDENT_RESPONSE_ALLOW_INVESTMENT_ADVICE=false
LOCAL_INCIDENT_RESPONSE_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_INCIDENT_RESPONSE_ALLOW_TELEMETRY=false
LOCAL_INCIDENT_RESPONSE_ALLOW_DASHBOARD_CREATION=false
LOCAL_INCIDENT_RESPONSE_ALLOW_GUI_CREATION=false
LOCAL_INCIDENT_RESPONSE_ALLOW_TUI_CREATION=false
LOCAL_INCIDENT_RESPONSE_ALLOW_CLOUD_UPLOAD=false
LOCAL_INCIDENT_RESPONSE_ALLOW_PACKAGE_PUBLISH=false
LOCAL_INCIDENT_RESPONSE_ALLOW_EXTERNAL_SERVICE=false
LOCAL_INCIDENT_RESPONSE_ALLOW_EXTERNAL_LLM=false
LOCAL_INCIDENT_RESPONSE_ALLOW_FILE_MODIFICATION=false
LOCAL_INCIDENT_RESPONSE_ALLOW_FILE_DELETION=false
LOCAL_INCIDENT_RESPONSE_ALLOW_FILE_MOVE=false
LOCAL_INCIDENT_RESPONSE_ALLOW_OVERWRITE=false
LOCAL_INCIDENT_RESPONSE_SCAN_DOCS=true
LOCAL_INCIDENT_RESPONSE_SCAN_REPORTS=true
LOCAL_INCIDENT_RESPONSE_SCAN_DATA_LAKE=true
LOCAL_INCIDENT_RESPONSE_SCAN_SCRIPTS=true
LOCAL_INCIDENT_RESPONSE_SCAN_TESTS=true
LOCAL_INCIDENT_RESPONSE_SCAN_GENERATED_DOCS=true
LOCAL_INCIDENT_RESPONSE_SCAN_REDTEAM_OUTPUTS=true
LOCAL_INCIDENT_RESPONSE_SCAN_GOVERNANCE_OUTPUTS=true
LOCAL_INCIDENT_RESPONSE_SCAN_SAFETY_OUTPUTS=true
LOCAL_INCIDENT_RESPONSE_MAX_ITEMS=500000
LOCAL_INCIDENT_RESPONSE_MAX_EVENTS=10000
LOCAL_INCIDENT_RESPONSE_MIN_READINESS_SCORE=0.40
LOCAL_INCIDENT_RESPONSE_MIN_QUALITY_SCORE=0.40
LOCAL_INCIDENT_RESPONSE_SAVE_REPORTS=true
"""
    if "LOCAL_INCIDENT_RESPONSE_ENABLED" not in content:
        with open(env_file, "a", encoding="utf-8") as f:
            f.write(new_env)
        print("Updated .env.example")

def update_paths():
    paths_file = "config/paths.py"
    with open(paths_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_paths = """
    # Local Incident Response
    LOCAL_INCIDENT_RESPONSE_DIR = LAKE_DIR / "local_incident_response"
    LOCAL_INCIDENT_RESPONSE_PROFILES_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "profiles"
    LOCAL_INCIDENT_RESPONSE_DOMAINS_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "domains"
    LOCAL_INCIDENT_RESPONSE_REHEARSAL_PACKET_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "rehearsal_packet"
    LOCAL_INCIDENT_RESPONSE_EVENTS_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "events"
    LOCAL_INCIDENT_RESPONSE_TAXONOMY_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "taxonomy"
    LOCAL_INCIDENT_RESPONSE_SEVERITY_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "severity"
    LOCAL_INCIDENT_RESPONSE_TRIAGE_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "triage"
    LOCAL_INCIDENT_RESPONSE_CLASSIFICATION_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "classification"
    LOCAL_INCIDENT_RESPONSE_BOUNDARY_BREACH_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "boundary_breach"
    LOCAL_INCIDENT_RESPONSE_UNSAFE_OUTPUTS_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "unsafe_outputs"
    LOCAL_INCIDENT_RESPONSE_FORBIDDEN_CAPABILITIES_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "forbidden_capabilities"
    LOCAL_INCIDENT_RESPONSE_SECRET_EXPOSURE_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "secret_exposure"
    LOCAL_INCIDENT_RESPONSE_FILE_ACTIONS_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "file_actions"
    LOCAL_INCIDENT_RESPONSE_CLOUD_PUBLISH_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "cloud_publish"
    LOCAL_INCIDENT_RESPONSE_LIVE_BROKER_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "live_broker"
    LOCAL_INCIDENT_RESPONSE_MODEL_DEPLOYMENT_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "model_deployment"
    LOCAL_INCIDENT_RESPONSE_EXTERNAL_LLM_API_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "external_llm_api"
    LOCAL_INCIDENT_RESPONSE_ROLLBACK_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "rollback"
    LOCAL_INCIDENT_RESPONSE_CONTAINMENT_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "containment"
    LOCAL_INCIDENT_RESPONSE_DEGRADED_MODE_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "degraded_mode"
    LOCAL_INCIDENT_RESPONSE_RECOVERY_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "recovery"
    LOCAL_INCIDENT_RESPONSE_RESILIENCE_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "resilience"
    LOCAL_INCIDENT_RESPONSE_EVIDENCE_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "evidence"
    LOCAL_INCIDENT_RESPONSE_READING_ORDER_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "reading_order"
    LOCAL_INCIDENT_RESPONSE_TIMELINE_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "timeline"
    LOCAL_INCIDENT_RESPONSE_POST_INCIDENT_REVIEW_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "post_incident_review"
    LOCAL_INCIDENT_RESPONSE_ROOT_CAUSE_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "root_cause"
    LOCAL_INCIDENT_RESPONSE_CORRECTIVE_ACTIONS_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "corrective_actions"
    LOCAL_INCIDENT_RESPONSE_COMMUNICATION_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "communication"
    LOCAL_INCIDENT_RESPONSE_ESCALATION_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "escalation"
    LOCAL_INCIDENT_RESPONSE_NO_GO_SAFE_GO_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "no_go_safe_go"
    LOCAL_INCIDENT_RESPONSE_EXCEPTIONS_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "exceptions"
    LOCAL_INCIDENT_RESPONSE_GAPS_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "gaps"
    LOCAL_INCIDENT_RESPONSE_RISKS_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "risks"
    LOCAL_INCIDENT_RESPONSE_SCORING_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "scoring"
    LOCAL_INCIDENT_RESPONSE_VALIDATION_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "validation"
    LOCAL_INCIDENT_RESPONSE_QUALITY_DIR = LOCAL_INCIDENT_RESPONSE_DIR / "quality"
    
    OUTPUT_LOCAL_INCIDENT_RESPONSE_DIR = OUTPUT_DIR / "local_incident_response"
    OUTPUT_LOCAL_INCIDENT_RESPONSE_CSV_DIR = OUTPUT_LOCAL_INCIDENT_RESPONSE_DIR / "csv"
    OUTPUT_LOCAL_INCIDENT_RESPONSE_MARKDOWN_DIR = OUTPUT_LOCAL_INCIDENT_RESPONSE_DIR / "markdown"
    OUTPUT_LOCAL_INCIDENT_RESPONSE_TXT_DIR = OUTPUT_LOCAL_INCIDENT_RESPONSE_DIR / "txt"
    OUTPUT_LOCAL_INCIDENT_RESPONSE_JSON_DIR = OUTPUT_LOCAL_INCIDENT_RESPONSE_DIR / "json"

    DOCS_GENERATED_LOCAL_INCIDENT_RESPONSE_DIR = DOCS_GENERATED_DIR / "local_incident_response"
"""
    if "LOCAL_INCIDENT_RESPONSE_DIR" not in content:
        content = content.replace('    # Docs Generated', new_paths + '\n    # Docs Generated')
        
        # update ensure_project_directories
        dirs_to_add = """        LOCAL_INCIDENT_RESPONSE_DIR,
        LOCAL_INCIDENT_RESPONSE_PROFILES_DIR,
        LOCAL_INCIDENT_RESPONSE_DOMAINS_DIR,
        LOCAL_INCIDENT_RESPONSE_REHEARSAL_PACKET_DIR,
        LOCAL_INCIDENT_RESPONSE_EVENTS_DIR,
        LOCAL_INCIDENT_RESPONSE_TAXONOMY_DIR,
        LOCAL_INCIDENT_RESPONSE_SEVERITY_DIR,
        LOCAL_INCIDENT_RESPONSE_TRIAGE_DIR,
        LOCAL_INCIDENT_RESPONSE_CLASSIFICATION_DIR,
        LOCAL_INCIDENT_RESPONSE_BOUNDARY_BREACH_DIR,
        LOCAL_INCIDENT_RESPONSE_UNSAFE_OUTPUTS_DIR,
        LOCAL_INCIDENT_RESPONSE_FORBIDDEN_CAPABILITIES_DIR,
        LOCAL_INCIDENT_RESPONSE_SECRET_EXPOSURE_DIR,
        LOCAL_INCIDENT_RESPONSE_FILE_ACTIONS_DIR,
        LOCAL_INCIDENT_RESPONSE_CLOUD_PUBLISH_DIR,
        LOCAL_INCIDENT_RESPONSE_LIVE_BROKER_DIR,
        LOCAL_INCIDENT_RESPONSE_MODEL_DEPLOYMENT_DIR,
        LOCAL_INCIDENT_RESPONSE_EXTERNAL_LLM_API_DIR,
        LOCAL_INCIDENT_RESPONSE_ROLLBACK_DIR,
        LOCAL_INCIDENT_RESPONSE_CONTAINMENT_DIR,
        LOCAL_INCIDENT_RESPONSE_DEGRADED_MODE_DIR,
        LOCAL_INCIDENT_RESPONSE_RECOVERY_DIR,
        LOCAL_INCIDENT_RESPONSE_RESILIENCE_DIR,
        LOCAL_INCIDENT_RESPONSE_EVIDENCE_DIR,
        LOCAL_INCIDENT_RESPONSE_READING_ORDER_DIR,
        LOCAL_INCIDENT_RESPONSE_TIMELINE_DIR,
        LOCAL_INCIDENT_RESPONSE_POST_INCIDENT_REVIEW_DIR,
        LOCAL_INCIDENT_RESPONSE_ROOT_CAUSE_DIR,
        LOCAL_INCIDENT_RESPONSE_CORRECTIVE_ACTIONS_DIR,
        LOCAL_INCIDENT_RESPONSE_COMMUNICATION_DIR,
        LOCAL_INCIDENT_RESPONSE_ESCALATION_DIR,
        LOCAL_INCIDENT_RESPONSE_NO_GO_SAFE_GO_DIR,
        LOCAL_INCIDENT_RESPONSE_EXCEPTIONS_DIR,
        LOCAL_INCIDENT_RESPONSE_GAPS_DIR,
        LOCAL_INCIDENT_RESPONSE_RISKS_DIR,
        LOCAL_INCIDENT_RESPONSE_SCORING_DIR,
        LOCAL_INCIDENT_RESPONSE_VALIDATION_DIR,
        LOCAL_INCIDENT_RESPONSE_QUALITY_DIR,
        OUTPUT_LOCAL_INCIDENT_RESPONSE_DIR,
        OUTPUT_LOCAL_INCIDENT_RESPONSE_CSV_DIR,
        OUTPUT_LOCAL_INCIDENT_RESPONSE_MARKDOWN_DIR,
        OUTPUT_LOCAL_INCIDENT_RESPONSE_TXT_DIR,
        OUTPUT_LOCAL_INCIDENT_RESPONSE_JSON_DIR,
        DOCS_GENERATED_LOCAL_INCIDENT_RESPONSE_DIR,"""
        
        content = content.replace("        OUTPUT_LOCAL_KNOWLEDGE_GRAPH_JSON_DIR,", f"        OUTPUT_LOCAL_KNOWLEDGE_GRAPH_JSON_DIR,\n{dirs_to_add}")
        with open(paths_file, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated paths.py")

if __name__ == "__main__":
    update_settings()
    update_env()
    update_paths()
