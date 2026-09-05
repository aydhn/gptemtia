import os
import re

def update_settings():
    settings_path = "commodity_fx_signal_bot/config/settings.py"
    with open(settings_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_settings = """
    # Local Long-Term Operations and v1.x Roadmap Governance
    local_longterm_operations_enabled: bool = True
    default_local_longterm_operations_profile: str = "balanced_local_longterm_operations"
    local_longterm_operations_default_language: str = "tr"
    local_longterm_operations_dry_run_default: bool = True
    local_longterm_operations_allow_real_operations_plan: bool = False
    local_longterm_operations_allow_official_lifecycle_policy: bool = False
    local_longterm_operations_allow_real_deprecation: bool = False
    local_longterm_operations_allow_auto_deprecation: bool = False
    local_longterm_operations_allow_auto_migration: bool = False
    local_longterm_operations_allow_production_roadmap_claim: bool = False
    local_longterm_operations_allow_official_release_commitment: bool = False
    local_longterm_operations_allow_package_publish: bool = False
    local_longterm_operations_allow_docker_build_push: bool = False
    local_longterm_operations_allow_git_tag: bool = False
    local_longterm_operations_allow_cloud_upload: bool = False
    local_longterm_operations_allow_deployment: bool = False
    local_longterm_operations_allow_legal_signoff: bool = False
    local_longterm_operations_allow_compliance_signoff: bool = False
    local_longterm_operations_allow_live_trading_claim: bool = False
    local_longterm_operations_allow_broker_readiness_claim: bool = False
    local_longterm_operations_allow_investment_advice: bool = False
    local_longterm_operations_allow_model_deployment_claim: bool = False
    local_longterm_operations_allow_telemetry: bool = False
    local_longterm_operations_allow_dashboard_creation: bool = False
    local_longterm_operations_allow_gui_creation: bool = False
    local_longterm_operations_allow_tui_creation: bool = False
    local_longterm_operations_allow_external_service: bool = False
    local_longterm_operations_allow_external_llm: bool = False
    local_longterm_operations_allow_file_modification: bool = False
    local_longterm_operations_allow_file_deletion: bool = False
    local_longterm_operations_allow_file_move: bool = False
    local_longterm_operations_allow_overwrite: bool = False
    local_longterm_operations_scan_docs: bool = True
    local_longterm_operations_scan_reports: bool = True
    local_longterm_operations_scan_data_lake: bool = True
    local_longterm_operations_scan_scripts: bool = True
    local_longterm_operations_scan_tests: bool = True
    local_longterm_operations_scan_generated_docs: bool = True
    local_longterm_operations_scan_release_candidate_outputs: bool = True
    local_longterm_operations_scan_incident_outputs: bool = True
    local_longterm_operations_scan_governance_outputs: bool = True
    local_longterm_operations_scan_safety_outputs: bool = True
    local_longterm_operations_max_items: int = 500000
    local_longterm_operations_max_calendar_rows: int = 10000
    local_longterm_operations_max_workbook_rows: int = 100000
    local_longterm_operations_min_readiness_score: float = 0.40
    local_longterm_operations_min_quality_score: float = 0.40
    local_longterm_operations_save_reports: bool = True
"""

    if "local_longterm_operations_enabled" not in content:
        # Find a good place to insert, like before model configuration
        insert_idx = content.find("    # Model Configuration")
        if insert_idx != -1:
            content = content[:insert_idx] + new_settings + "\n" + content[insert_idx:]
        else:
            print("Could not find insertion point in settings.py")
        
        with open(settings_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated settings.py")


def update_env_example():
    env_path = ".env.example"
    with open(env_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_env = """
LOCAL_LONGTERM_OPERATIONS_ENABLED=true
DEFAULT_LOCAL_LONGTERM_OPERATIONS_PROFILE=balanced_local_longterm_operations
LOCAL_LONGTERM_OPERATIONS_DEFAULT_LANGUAGE=tr
LOCAL_LONGTERM_OPERATIONS_DRY_RUN_DEFAULT=true
LOCAL_LONGTERM_OPERATIONS_ALLOW_REAL_OPERATIONS_PLAN=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_OFFICIAL_LIFECYCLE_POLICY=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_REAL_DEPRECATION=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_AUTO_DEPRECATION=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_AUTO_MIGRATION=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_PRODUCTION_ROADMAP_CLAIM=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_OFFICIAL_RELEASE_COMMITMENT=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_PACKAGE_PUBLISH=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_DOCKER_BUILD_PUSH=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_GIT_TAG=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_CLOUD_UPLOAD=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_DEPLOYMENT=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_LEGAL_SIGNOFF=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_COMPLIANCE_SIGNOFF=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_LIVE_TRADING_CLAIM=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_INVESTMENT_ADVICE=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_TELEMETRY=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_DASHBOARD_CREATION=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_GUI_CREATION=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_TUI_CREATION=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_EXTERNAL_SERVICE=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_EXTERNAL_LLM=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_FILE_MODIFICATION=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_FILE_DELETION=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_FILE_MOVE=false
LOCAL_LONGTERM_OPERATIONS_ALLOW_OVERWRITE=false
LOCAL_LONGTERM_OPERATIONS_SCAN_DOCS=true
LOCAL_LONGTERM_OPERATIONS_SCAN_REPORTS=true
LOCAL_LONGTERM_OPERATIONS_SCAN_DATA_LAKE=true
LOCAL_LONGTERM_OPERATIONS_SCAN_SCRIPTS=true
LOCAL_LONGTERM_OPERATIONS_SCAN_TESTS=true
LOCAL_LONGTERM_OPERATIONS_SCAN_GENERATED_DOCS=true
LOCAL_LONGTERM_OPERATIONS_SCAN_RELEASE_CANDIDATE_OUTPUTS=true
LOCAL_LONGTERM_OPERATIONS_SCAN_INCIDENT_OUTPUTS=true
LOCAL_LONGTERM_OPERATIONS_SCAN_GOVERNANCE_OUTPUTS=true
LOCAL_LONGTERM_OPERATIONS_SCAN_SAFETY_OUTPUTS=true
LOCAL_LONGTERM_OPERATIONS_MAX_ITEMS=500000
LOCAL_LONGTERM_OPERATIONS_MAX_CALENDAR_ROWS=10000
LOCAL_LONGTERM_OPERATIONS_MAX_WORKBOOK_ROWS=100000
LOCAL_LONGTERM_OPERATIONS_MIN_READINESS_SCORE=0.40
LOCAL_LONGTERM_OPERATIONS_MIN_QUALITY_SCORE=0.40
LOCAL_LONGTERM_OPERATIONS_SAVE_REPORTS=true
"""
    if "LOCAL_LONGTERM_OPERATIONS_ENABLED" not in content:
        with open(env_path, "a", encoding="utf-8") as f:
            f.write(new_env)
        print("Updated .env.example")


def update_paths():
    paths_path = "commodity_fx_signal_bot/config/paths.py"
    with open(paths_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_paths = """
        # Local Long-Term Operations
        "local_longterm_operations": self.data_lake_dir / "local_longterm_operations",
        "local_longterm_operations_profiles": self.data_lake_dir / "local_longterm_operations" / "profiles",
        "local_longterm_operations_domains": self.data_lake_dir / "local_longterm_operations" / "domains",
        "local_longterm_operations_binder": self.data_lake_dir / "local_longterm_operations" / "binder",
        "local_longterm_operations_calendars": self.data_lake_dir / "local_longterm_operations" / "calendars",
        "local_longterm_operations_workbooks": self.data_lake_dir / "local_longterm_operations" / "workbooks",
        "local_longterm_operations_maintenance": self.data_lake_dir / "local_longterm_operations" / "maintenance",
        "local_longterm_operations_ownership": self.data_lake_dir / "local_longterm_operations" / "ownership",
        "local_longterm_operations_evidence": self.data_lake_dir / "local_longterm_operations" / "evidence",
        "local_longterm_operations_retention": self.data_lake_dir / "local_longterm_operations" / "retention",
        "local_longterm_operations_datalake_review": self.data_lake_dir / "local_longterm_operations" / "datalake_review",
        "local_longterm_operations_generated_docs_review": self.data_lake_dir / "local_longterm_operations" / "generated_docs_review",
        "local_longterm_operations_quality_review": self.data_lake_dir / "local_longterm_operations" / "quality_review",
        "local_longterm_operations_safety_review": self.data_lake_dir / "local_longterm_operations" / "safety_review",
        "local_longterm_operations_inc_redteam_gov_review": self.data_lake_dir / "local_longterm_operations" / "inc_redteam_gov_review",
        "local_longterm_operations_deprecation": self.data_lake_dir / "local_longterm_operations" / "deprecation",
        "local_longterm_operations_migration": self.data_lake_dir / "local_longterm_operations" / "migration",
        "local_longterm_operations_roadmap": self.data_lake_dir / "local_longterm_operations" / "roadmap",
        "local_longterm_operations_feature_intake": self.data_lake_dir / "local_longterm_operations" / "feature_intake",
        "local_longterm_operations_change_control": self.data_lake_dir / "local_longterm_operations" / "change_control",
        "local_longterm_operations_risk_benefit": self.data_lake_dir / "local_longterm_operations" / "risk_benefit",
        "local_longterm_operations_no_go_safe_go": self.data_lake_dir / "local_longterm_operations" / "no_go_safe_go",
        "local_longterm_operations_exceptions": self.data_lake_dir / "local_longterm_operations" / "exceptions",
        "local_longterm_operations_gaps": self.data_lake_dir / "local_longterm_operations" / "gaps",
        "local_longterm_operations_risks": self.data_lake_dir / "local_longterm_operations" / "risks",
        "local_longterm_operations_scoring": self.data_lake_dir / "local_longterm_operations" / "scoring",
        "local_longterm_operations_validation": self.data_lake_dir / "local_longterm_operations" / "validation",
        "local_longterm_operations_quality": self.data_lake_dir / "local_longterm_operations" / "quality",
        "reports_output_local_longterm_operations": self.reports_output_dir / "local_longterm_operations",
        "reports_output_local_longterm_operations_csv": self.reports_output_dir / "local_longterm_operations" / "csv",
        "reports_output_local_longterm_operations_markdown": self.reports_output_dir / "local_longterm_operations" / "markdown",
        "reports_output_local_longterm_operations_txt": self.reports_output_dir / "local_longterm_operations" / "txt",
        "reports_output_local_longterm_operations_json": self.reports_output_dir / "local_longterm_operations" / "json",
        "docs_generated_local_longterm_operations": self.docs_generated_dir / "local_longterm_operations",
"""
    if "local_longterm_operations" not in content:
        insert_idx = content.find("        return dirs")
        if insert_idx != -1:
            content = content[:insert_idx] + new_paths + content[insert_idx:]
            with open(paths_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Updated paths.py")

if __name__ == "__main__":
    update_settings()
    update_env_example()
    update_paths()
