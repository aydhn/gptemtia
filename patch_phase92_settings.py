import re
from pathlib import Path

def patch_settings():
    path = Path("commodity_fx_signal_bot/config/settings.py")
    content = path.read_text(encoding="utf-8")
    
    if "local_continuity_intelligence_enabled" not in content:
        fields = """
    # Local Continuity Intelligence
    local_continuity_intelligence_enabled: bool = True
    default_local_continuity_intelligence_profile: str = "balanced_local_continuity"
    local_continuity_intelligence_default_language: str = "tr"
    local_continuity_intelligence_dry_run_default: bool = True
    local_continuity_intelligence_allow_real_memory_system: bool = False
    local_continuity_intelligence_allow_cloud_memory_sync: bool = False
    local_continuity_intelligence_allow_official_lessons_report: bool = False
    local_continuity_intelligence_allow_official_decision_record: bool = False
    local_continuity_intelligence_allow_legal_evidence_claim: bool = False
    local_continuity_intelligence_allow_compliance_evidence_claim: bool = False
    local_continuity_intelligence_allow_production_approval_claim: bool = False
    local_continuity_intelligence_allow_official_acceptance_claim: bool = False
    local_continuity_intelligence_allow_package_publish: bool = False
    local_continuity_intelligence_allow_docker_build_push: bool = False
    local_continuity_intelligence_allow_git_tag: bool = False
    local_continuity_intelligence_allow_cloud_upload: bool = False
    local_continuity_intelligence_allow_deployment: bool = False
    local_continuity_intelligence_allow_live_trading_claim: bool = False
    local_continuity_intelligence_allow_broker_readiness_claim: bool = False
    local_continuity_intelligence_allow_investment_advice: bool = False
    local_continuity_intelligence_allow_model_deployment_claim: bool = False
    local_continuity_intelligence_allow_telemetry: bool = False
    local_continuity_intelligence_allow_dashboard_creation: bool = False
    local_continuity_intelligence_allow_gui_creation: bool = False
    local_continuity_intelligence_allow_tui_creation: bool = False
    local_continuity_intelligence_allow_external_service: bool = False
    local_continuity_intelligence_allow_external_llm: bool = False
    local_continuity_intelligence_allow_file_modification: bool = False
    local_continuity_intelligence_allow_file_deletion: bool = False
    local_continuity_intelligence_allow_file_move: bool = False
    local_continuity_intelligence_allow_overwrite: bool = False
    local_continuity_intelligence_scan_docs: bool = True
    local_continuity_intelligence_scan_reports: bool = True
    local_continuity_intelligence_scan_data_lake: bool = True
    local_continuity_intelligence_scan_scripts: bool = True
    local_continuity_intelligence_scan_tests: bool = True
    local_continuity_intelligence_scan_generated_docs: bool = True
    local_continuity_intelligence_scan_preservation_outputs: bool = True
    local_continuity_intelligence_scan_completion_outputs: bool = True
    local_continuity_intelligence_scan_longterm_outputs: bool = True
    local_continuity_intelligence_scan_governance_outputs: bool = True
    local_continuity_intelligence_scan_safety_outputs: bool = True
    local_continuity_intelligence_max_items: int = 500000
    local_continuity_intelligence_max_rows: int = 250000
    local_continuity_intelligence_min_readiness_score: float = 0.40
    local_continuity_intelligence_min_quality_score: float = 0.40
    local_continuity_intelligence_save_reports: bool = True
"""
        # Find the end of dataclass fields. Let's just put it before __post_init__ or at the end of class fields.
        if "def __post_init__(self):" in content:
            content = content.replace("def __post_init__(self):", fields + "\n    def __post_init__(self):")
        else:
            # If no post_init, just append before the end of the file, assuming methods are at the bottom.
            # Or use regex to find the last class definition
            pass
            
        path.write_text(content, encoding="utf-8")
        print("Patched settings.py")

def patch_env():
    path = Path(".env.example")
    content = path.read_text(encoding="utf-8")
    if "LOCAL_CONTINUITY_INTELLIGENCE_ENABLED" not in content:
        env_vars = """
# Local Continuity Intelligence
LOCAL_CONTINUITY_INTELLIGENCE_ENABLED=true
DEFAULT_LOCAL_CONTINUITY_INTELLIGENCE_PROFILE=balanced_local_continuity
LOCAL_CONTINUITY_INTELLIGENCE_DEFAULT_LANGUAGE=tr
LOCAL_CONTINUITY_INTELLIGENCE_DRY_RUN_DEFAULT=true
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_REAL_MEMORY_SYSTEM=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_CLOUD_MEMORY_SYNC=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_OFFICIAL_LESSONS_REPORT=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_OFFICIAL_DECISION_RECORD=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_LEGAL_EVIDENCE_CLAIM=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_COMPLIANCE_EVIDENCE_CLAIM=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_PRODUCTION_APPROVAL_CLAIM=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_OFFICIAL_ACCEPTANCE_CLAIM=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_PACKAGE_PUBLISH=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_DOCKER_BUILD_PUSH=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_GIT_TAG=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_CLOUD_UPLOAD=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_DEPLOYMENT=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_LIVE_TRADING_CLAIM=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_INVESTMENT_ADVICE=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_TELEMETRY=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_DASHBOARD_CREATION=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_GUI_CREATION=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_TUI_CREATION=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_EXTERNAL_SERVICE=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_EXTERNAL_LLM=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_FILE_MODIFICATION=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_FILE_DELETION=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_FILE_MOVE=false
LOCAL_CONTINUITY_INTELLIGENCE_ALLOW_OVERWRITE=false
LOCAL_CONTINUITY_INTELLIGENCE_SCAN_DOCS=true
LOCAL_CONTINUITY_INTELLIGENCE_SCAN_REPORTS=true
LOCAL_CONTINUITY_INTELLIGENCE_SCAN_DATA_LAKE=true
LOCAL_CONTINUITY_INTELLIGENCE_SCAN_SCRIPTS=true
LOCAL_CONTINUITY_INTELLIGENCE_SCAN_TESTS=true
LOCAL_CONTINUITY_INTELLIGENCE_SCAN_GENERATED_DOCS=true
LOCAL_CONTINUITY_INTELLIGENCE_SCAN_PRESERVATION_OUTPUTS=true
LOCAL_CONTINUITY_INTELLIGENCE_SCAN_COMPLETION_OUTPUTS=true
LOCAL_CONTINUITY_INTELLIGENCE_SCAN_LONGTERM_OUTPUTS=true
LOCAL_CONTINUITY_INTELLIGENCE_SCAN_GOVERNANCE_OUTPUTS=true
LOCAL_CONTINUITY_INTELLIGENCE_SCAN_SAFETY_OUTPUTS=true
LOCAL_CONTINUITY_INTELLIGENCE_MAX_ITEMS=500000
LOCAL_CONTINUITY_INTELLIGENCE_MAX_ROWS=250000
LOCAL_CONTINUITY_INTELLIGENCE_MIN_READINESS_SCORE=0.40
LOCAL_CONTINUITY_INTELLIGENCE_MIN_QUALITY_SCORE=0.40
LOCAL_CONTINUITY_INTELLIGENCE_SAVE_REPORTS=true
"""
        with open(path, "a", encoding="utf-8") as f:
            f.write(env_vars)
        print("Patched .env.example")

def patch_paths():
    path = Path("commodity_fx_signal_bot/config/paths.py")
    content = path.read_text(encoding="utf-8")
    if "local_continuity_intelligence" not in content:
        # Simple string replacement for data lake and reports directories
        content = content.replace(
            "def ensure_project_directories():",
            """
    # Local Continuity Intelligence Paths
    LOCAL_CONTINUITY_LAKE_DIR = DATA_LAKE_DIR / "local_continuity_intelligence"
    LOCAL_CONTINUITY_PROFILES_DIR = LOCAL_CONTINUITY_LAKE_DIR / "profiles"
    LOCAL_CONTINUITY_DOMAINS_DIR = LOCAL_CONTINUITY_LAKE_DIR / "domains"
    LOCAL_CONTINUITY_OPERATOR_MEMORY_DIR = LOCAL_CONTINUITY_LAKE_DIR / "operator_memory"
    LOCAL_CONTINUITY_LESSONS_LEARNED_DIR = LOCAL_CONTINUITY_LAKE_DIR / "lessons_learned"
    LOCAL_CONTINUITY_DECISION_RATIONALE_DIR = LOCAL_CONTINUITY_LAKE_DIR / "decision_rationale"
    LOCAL_CONTINUITY_FUTURE_READER_DIR = LOCAL_CONTINUITY_LAKE_DIR / "future_reader"
    LOCAL_CONTINUITY_BINDER_DIR = LOCAL_CONTINUITY_LAKE_DIR / "binder"
    LOCAL_CONTINUITY_KNOWLEDGE_GRAPH_DIR = LOCAL_CONTINUITY_LAKE_DIR / "knowledge_graph"
    LOCAL_CONTINUITY_CONCEPTS_DIR = LOCAL_CONTINUITY_LAKE_DIR / "concepts"
    LOCAL_CONTINUITY_GLOSSARY_DIR = LOCAL_CONTINUITY_LAKE_DIR / "glossary"
    LOCAL_CONTINUITY_INTERPRETATION_GUIDES_DIR = LOCAL_CONTINUITY_LAKE_DIR / "interpretation_guides"
    LOCAL_CONTINUITY_REMINDERS_DIR = LOCAL_CONTINUITY_LAKE_DIR / "reminders"
    LOCAL_CONTINUITY_NO_GO_SAFE_GO_DIR = LOCAL_CONTINUITY_LAKE_DIR / "no_go_safe_go"
    LOCAL_CONTINUITY_EXCEPTIONS_DIR = LOCAL_CONTINUITY_LAKE_DIR / "exceptions"
    LOCAL_CONTINUITY_GAPS_DIR = LOCAL_CONTINUITY_LAKE_DIR / "gaps"
    LOCAL_CONTINUITY_RISKS_DIR = LOCAL_CONTINUITY_LAKE_DIR / "risks"
    LOCAL_CONTINUITY_SCORING_DIR = LOCAL_CONTINUITY_LAKE_DIR / "scoring"
    LOCAL_CONTINUITY_VALIDATION_DIR = LOCAL_CONTINUITY_LAKE_DIR / "validation"
    LOCAL_CONTINUITY_QUALITY_DIR = LOCAL_CONTINUITY_LAKE_DIR / "quality"
    
    LOCAL_CONTINUITY_REPORTS_DIR = OUTPUT_REPORTS_DIR / "local_continuity_intelligence"
    LOCAL_CONTINUITY_REPORTS_CSV_DIR = LOCAL_CONTINUITY_REPORTS_DIR / "csv"
    LOCAL_CONTINUITY_REPORTS_MARKDOWN_DIR = LOCAL_CONTINUITY_REPORTS_DIR / "markdown"
    LOCAL_CONTINUITY_REPORTS_TXT_DIR = LOCAL_CONTINUITY_REPORTS_DIR / "txt"
    LOCAL_CONTINUITY_REPORTS_JSON_DIR = LOCAL_CONTINUITY_REPORTS_DIR / "json"
    
    LOCAL_CONTINUITY_DOCS_DIR = GENERATED_DOCS_DIR / "local_continuity_intelligence"

def ensure_project_directories():"""
        )
        
        # Now add them to ensure_project_directories
        ensure_dirs = """        LOCAL_CONTINUITY_LAKE_DIR,
        LOCAL_CONTINUITY_PROFILES_DIR,
        LOCAL_CONTINUITY_DOMAINS_DIR,
        LOCAL_CONTINUITY_OPERATOR_MEMORY_DIR,
        LOCAL_CONTINUITY_LESSONS_LEARNED_DIR,
        LOCAL_CONTINUITY_DECISION_RATIONALE_DIR,
        LOCAL_CONTINUITY_FUTURE_READER_DIR,
        LOCAL_CONTINUITY_BINDER_DIR,
        LOCAL_CONTINUITY_KNOWLEDGE_GRAPH_DIR,
        LOCAL_CONTINUITY_CONCEPTS_DIR,
        LOCAL_CONTINUITY_GLOSSARY_DIR,
        LOCAL_CONTINUITY_INTERPRETATION_GUIDES_DIR,
        LOCAL_CONTINUITY_REMINDERS_DIR,
        LOCAL_CONTINUITY_NO_GO_SAFE_GO_DIR,
        LOCAL_CONTINUITY_EXCEPTIONS_DIR,
        LOCAL_CONTINUITY_GAPS_DIR,
        LOCAL_CONTINUITY_RISKS_DIR,
        LOCAL_CONTINUITY_SCORING_DIR,
        LOCAL_CONTINUITY_VALIDATION_DIR,
        LOCAL_CONTINUITY_QUALITY_DIR,
        LOCAL_CONTINUITY_REPORTS_DIR,
        LOCAL_CONTINUITY_REPORTS_CSV_DIR,
        LOCAL_CONTINUITY_REPORTS_MARKDOWN_DIR,
        LOCAL_CONTINUITY_REPORTS_TXT_DIR,
        LOCAL_CONTINUITY_REPORTS_JSON_DIR,
        LOCAL_CONTINUITY_DOCS_DIR,
"""
        content = content.replace("        GENERATED_DOCS_DIR,", ensure_dirs + "        GENERATED_DOCS_DIR,")
        
        path.write_text(content, encoding="utf-8")
        print("Patched paths.py")

if __name__ == "__main__":
    patch_settings()
    patch_env()
    patch_paths()
