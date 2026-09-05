import os
import re

with open("commodity_fx_signal_bot/config/settings.py", "r", encoding="utf-8") as f:
    content = f.read()

settings_addition = """
    # Phase 93 - Local Project Atlas
    local_project_atlas_enabled: bool = True
    default_local_project_atlas_profile: str = "balanced_local_project_atlas"
    local_project_atlas_default_language: str = "tr"
    local_project_atlas_dry_run_default: bool = True
    local_project_atlas_allow_enterprise_search_claim: bool = False
    local_project_atlas_allow_cloud_index: bool = False
    local_project_atlas_allow_vector_db: bool = False
    local_project_atlas_allow_embedding_api: bool = False
    local_project_atlas_allow_external_search_service: bool = False
    local_project_atlas_allow_external_llm: bool = False
    local_project_atlas_allow_official_knowledge_index: bool = False
    local_project_atlas_allow_legal_evidence_claim: bool = False
    local_project_atlas_allow_compliance_evidence_claim: bool = False
    local_project_atlas_allow_production_approval_claim: bool = False
    local_project_atlas_allow_official_acceptance_claim: bool = False
    local_project_atlas_allow_package_publish: bool = False
    local_project_atlas_allow_docker_build_push: bool = False
    local_project_atlas_allow_git_tag: bool = False
    local_project_atlas_allow_cloud_upload: bool = False
    local_project_atlas_allow_deployment: bool = False
    local_project_atlas_allow_live_trading_claim: bool = False
    local_project_atlas_allow_broker_readiness_claim: bool = False
    local_project_atlas_allow_investment_advice: bool = False
    local_project_atlas_allow_model_deployment_claim: bool = False
    local_project_atlas_allow_telemetry: bool = False
    local_project_atlas_allow_dashboard_creation: bool = False
    local_project_atlas_allow_gui_creation: bool = False
    local_project_atlas_allow_tui_creation: bool = False
    local_project_atlas_allow_file_modification: bool = False
    local_project_atlas_allow_file_deletion: bool = False
    local_project_atlas_allow_file_move: bool = False
    local_project_atlas_allow_overwrite: bool = False
    local_project_atlas_scan_docs: bool = True
    local_project_atlas_scan_reports: bool = True
    local_project_atlas_scan_data_lake: bool = True
    local_project_atlas_scan_scripts: bool = True
    local_project_atlas_scan_tests: bool = True
    local_project_atlas_scan_generated_docs: bool = True
    local_project_atlas_scan_continuity_outputs: bool = True
    local_project_atlas_scan_preservation_outputs: bool = True
    local_project_atlas_scan_completion_outputs: bool = True
    local_project_atlas_scan_longterm_outputs: bool = True
    local_project_atlas_scan_release_outputs: bool = True
    local_project_atlas_scan_incident_outputs: bool = True
    local_project_atlas_scan_governance_outputs: bool = True
    local_project_atlas_scan_safety_outputs: bool = True
    local_project_atlas_max_items: int = 750000
    local_project_atlas_max_rows: int = 300000
    local_project_atlas_min_readiness_score: float = 0.40
    local_project_atlas_min_quality_score: float = 0.40
    local_project_atlas_save_reports: bool = True
"""

if "local_project_atlas_enabled" not in content:
    # insert before "def __post_init__"
    content = content.replace("    def __post_init__(self):", settings_addition + "\n    def __post_init__(self):")
    with open("commodity_fx_signal_bot/config/settings.py", "w", encoding="utf-8") as f:
        f.write(content)

with open("commodity_fx_signal_bot/.env.example", "r", encoding="utf-8") as f:
    env_content = f.read()

env_addition = """
# Phase 93
LOCAL_PROJECT_ATLAS_ENABLED=true
DEFAULT_LOCAL_PROJECT_ATLAS_PROFILE=balanced_local_project_atlas
LOCAL_PROJECT_ATLAS_DEFAULT_LANGUAGE=tr
LOCAL_PROJECT_ATLAS_DRY_RUN_DEFAULT=true
LOCAL_PROJECT_ATLAS_ALLOW_ENTERPRISE_SEARCH_CLAIM=false
LOCAL_PROJECT_ATLAS_ALLOW_CLOUD_INDEX=false
LOCAL_PROJECT_ATLAS_ALLOW_VECTOR_DB=false
LOCAL_PROJECT_ATLAS_ALLOW_EMBEDDING_API=false
LOCAL_PROJECT_ATLAS_ALLOW_EXTERNAL_SEARCH_SERVICE=false
LOCAL_PROJECT_ATLAS_ALLOW_EXTERNAL_LLM=false
LOCAL_PROJECT_ATLAS_ALLOW_OFFICIAL_KNOWLEDGE_INDEX=false
LOCAL_PROJECT_ATLAS_ALLOW_LEGAL_EVIDENCE_CLAIM=false
LOCAL_PROJECT_ATLAS_ALLOW_COMPLIANCE_EVIDENCE_CLAIM=false
LOCAL_PROJECT_ATLAS_ALLOW_PRODUCTION_APPROVAL_CLAIM=false
LOCAL_PROJECT_ATLAS_ALLOW_OFFICIAL_ACCEPTANCE_CLAIM=false
LOCAL_PROJECT_ATLAS_ALLOW_PACKAGE_PUBLISH=false
LOCAL_PROJECT_ATLAS_ALLOW_DOCKER_BUILD_PUSH=false
LOCAL_PROJECT_ATLAS_ALLOW_GIT_TAG=false
LOCAL_PROJECT_ATLAS_ALLOW_CLOUD_UPLOAD=false
LOCAL_PROJECT_ATLAS_ALLOW_DEPLOYMENT=false
LOCAL_PROJECT_ATLAS_ALLOW_LIVE_TRADING_CLAIM=false
LOCAL_PROJECT_ATLAS_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_PROJECT_ATLAS_ALLOW_INVESTMENT_ADVICE=false
LOCAL_PROJECT_ATLAS_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_PROJECT_ATLAS_ALLOW_TELEMETRY=false
LOCAL_PROJECT_ATLAS_ALLOW_DASHBOARD_CREATION=false
LOCAL_PROJECT_ATLAS_ALLOW_GUI_CREATION=false
LOCAL_PROJECT_ATLAS_ALLOW_TUI_CREATION=false
LOCAL_PROJECT_ATLAS_ALLOW_FILE_MODIFICATION=false
LOCAL_PROJECT_ATLAS_ALLOW_FILE_DELETION=false
LOCAL_PROJECT_ATLAS_ALLOW_FILE_MOVE=false
LOCAL_PROJECT_ATLAS_ALLOW_OVERWRITE=false
LOCAL_PROJECT_ATLAS_SCAN_DOCS=true
LOCAL_PROJECT_ATLAS_SCAN_REPORTS=true
LOCAL_PROJECT_ATLAS_SCAN_DATA_LAKE=true
LOCAL_PROJECT_ATLAS_SCAN_SCRIPTS=true
LOCAL_PROJECT_ATLAS_SCAN_TESTS=true
LOCAL_PROJECT_ATLAS_SCAN_GENERATED_DOCS=true
LOCAL_PROJECT_ATLAS_SCAN_CONTINUITY_OUTPUTS=true
LOCAL_PROJECT_ATLAS_SCAN_PRESERVATION_OUTPUTS=true
LOCAL_PROJECT_ATLAS_SCAN_COMPLETION_OUTPUTS=true
LOCAL_PROJECT_ATLAS_SCAN_LONGTERM_OUTPUTS=true
LOCAL_PROJECT_ATLAS_SCAN_RELEASE_OUTPUTS=true
LOCAL_PROJECT_ATLAS_SCAN_INCIDENT_OUTPUTS=true
LOCAL_PROJECT_ATLAS_SCAN_GOVERNANCE_OUTPUTS=true
LOCAL_PROJECT_ATLAS_SCAN_SAFETY_OUTPUTS=true
LOCAL_PROJECT_ATLAS_MAX_ITEMS=750000
LOCAL_PROJECT_ATLAS_MAX_ROWS=300000
LOCAL_PROJECT_ATLAS_MIN_READINESS_SCORE=0.40
LOCAL_PROJECT_ATLAS_MIN_QUALITY_SCORE=0.40
LOCAL_PROJECT_ATLAS_SAVE_REPORTS=true
"""

if "LOCAL_PROJECT_ATLAS_ENABLED" not in env_content:
    with open("commodity_fx_signal_bot/.env.example", "a", encoding="utf-8") as f:
        f.write(env_addition)
"""
print("Settings patched")
"""
