import os
from pathlib import Path

def patch_settings():
    settings_path = Path("commodity_fx_signal_bot/config/settings.py")
    if not settings_path.exists():
        return
    content = settings_path.read_text(encoding="utf-8")
    
    # Check if already patched
    if "local_simplification_enabled: bool" in content:
        return

    # Add variables to Settings class
    injection = """    # Phase 82
    local_simplification_enabled: bool = True
    default_local_simplification_profile: str = "balanced_local_simplification"
    local_simplification_default_language: str = "tr"
    local_simplification_dry_run_default: bool = True
    local_simplification_allow_auto_refactor: bool = False
    local_simplification_allow_file_modification: bool = False
    local_simplification_allow_file_deletion: bool = False
    local_simplification_allow_file_move: bool = False
    local_simplification_allow_overwrite: bool = False
    local_simplification_allow_cleanup_execution: bool = False
    local_simplification_allow_package_publish: bool = False
    local_simplification_allow_cloud_upload: bool = False
    local_simplification_allow_external_service: bool = False
    local_simplification_allow_external_llm: bool = False
    local_simplification_allow_production_cleanup_claim: bool = False
    local_simplification_allow_architecture_approval_claim: bool = False
    local_simplification_allow_compliance_claim: bool = False
    local_simplification_allow_live_trading_claim: bool = False
    local_simplification_allow_broker_readiness_claim: bool = False
    local_simplification_allow_investment_advice: bool = False
    local_simplification_allow_model_deployment_claim: bool = False
    local_simplification_scan_source: bool = True
    local_simplification_scan_docs: bool = True
    local_simplification_scan_reports: bool = True
    local_simplification_scan_data_lake: bool = True
    local_simplification_scan_scripts: bool = True
    local_simplification_scan_tests: bool = True
    local_simplification_scan_generated_docs: bool = True
    local_simplification_scan_reuse_outputs: bool = True
    local_simplification_scan_closure_outputs: bool = True
    local_simplification_scan_safety_outputs: bool = True
    local_simplification_max_items: int = 500000
    local_simplification_max_candidate_items: int = 100000
    local_simplification_min_readiness_score: float = 0.40
    local_simplification_min_quality_score: float = 0.40
    local_simplification_save_reports: bool = True
"""
    # Insert just before the end of class Settings or before def validate
    if "def validate" in content:
        content = content.replace("    def validate", injection + "\\n    def validate")
    else:
        content += "\\n" + injection
    
    settings_path.write_text(content, encoding="utf-8")

def patch_paths():
    paths_path = Path("commodity_fx_signal_bot/config/paths.py")
    if not paths_path.exists():
        return
    content = paths_path.read_text(encoding="utf-8")
    if "local_simplification" in content:
        return
        
    dirs = [
        "data/lake/local_simplification",
        "data/lake/local_simplification/profiles",
        "data/lake/local_simplification/domains",
        "data/lake/local_simplification/complexity",
        "data/lake/local_simplification/sprawl",
        "data/lake/local_simplification/slimming_plan",
        "data/lake/local_simplification/consolidation",
        "data/lake/local_simplification/naming",
        "data/lake/local_simplification/config",
        "data/lake/local_simplification/datalake",
        "data/lake/local_simplification/scripts",
        "data/lake/local_simplification/tests",
        "data/lake/local_simplification/docs_navigation",
        "data/lake/local_simplification/ergonomics",
        "data/lake/local_simplification/onboarding",
        "data/lake/local_simplification/maintainability_seed",
        "data/lake/local_simplification/no_go_safe_go",
        "data/lake/local_simplification/exceptions",
        "data/lake/local_simplification/gaps",
        "data/lake/local_simplification/risks",
        "data/lake/local_simplification/scoring",
        "data/lake/local_simplification/validation",
        "data/lake/local_simplification/quality",
        "reports/output/local_simplification",
        "reports/output/local_simplification/csv",
        "reports/output/local_simplification/markdown",
        "reports/output/local_simplification/txt",
        "reports/output/local_simplification/json",
        "docs/generated/local_simplification"
    ]
    
    # insert inside get_project_directories
    injection = ""
    for d in dirs:
        injection += f'        base_dir / "{d}",\\n'
    
    target = '        base_dir / "reports/output",'
    if target in content:
        content = content.replace(target, target + '\\n' + injection)
    
    paths_path.write_text(content, encoding="utf-8")

def patch_env():
    env_path = Path("commodity_fx_signal_bot/.env.example")
    if not env_path.exists():
        return
    content = env_path.read_text(encoding="utf-8")
    if "LOCAL_SIMPLIFICATION_ENABLED" in content:
        return
        
    injection = """
LOCAL_SIMPLIFICATION_ENABLED=true
DEFAULT_LOCAL_SIMPLIFICATION_PROFILE=balanced_local_simplification
LOCAL_SIMPLIFICATION_DEFAULT_LANGUAGE=tr
LOCAL_SIMPLIFICATION_DRY_RUN_DEFAULT=true
LOCAL_SIMPLIFICATION_ALLOW_AUTO_REFACTOR=false
LOCAL_SIMPLIFICATION_ALLOW_FILE_MODIFICATION=false
LOCAL_SIMPLIFICATION_ALLOW_FILE_DELETION=false
LOCAL_SIMPLIFICATION_ALLOW_FILE_MOVE=false
LOCAL_SIMPLIFICATION_ALLOW_OVERWRITE=false
LOCAL_SIMPLIFICATION_ALLOW_CLEANUP_EXECUTION=false
LOCAL_SIMPLIFICATION_ALLOW_PACKAGE_PUBLISH=false
LOCAL_SIMPLIFICATION_ALLOW_CLOUD_UPLOAD=false
LOCAL_SIMPLIFICATION_ALLOW_EXTERNAL_SERVICE=false
LOCAL_SIMPLIFICATION_ALLOW_EXTERNAL_LLM=false
LOCAL_SIMPLIFICATION_ALLOW_PRODUCTION_CLEANUP_CLAIM=false
LOCAL_SIMPLIFICATION_ALLOW_ARCHITECTURE_APPROVAL_CLAIM=false
LOCAL_SIMPLIFICATION_ALLOW_COMPLIANCE_CLAIM=false
LOCAL_SIMPLIFICATION_ALLOW_LIVE_TRADING_CLAIM=false
LOCAL_SIMPLIFICATION_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_SIMPLIFICATION_ALLOW_INVESTMENT_ADVICE=false
LOCAL_SIMPLIFICATION_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_SIMPLIFICATION_SCAN_SOURCE=true
LOCAL_SIMPLIFICATION_SCAN_DOCS=true
LOCAL_SIMPLIFICATION_SCAN_REPORTS=true
LOCAL_SIMPLIFICATION_SCAN_DATA_LAKE=true
LOCAL_SIMPLIFICATION_SCAN_SCRIPTS=true
LOCAL_SIMPLIFICATION_SCAN_TESTS=true
LOCAL_SIMPLIFICATION_SCAN_GENERATED_DOCS=true
LOCAL_SIMPLIFICATION_SCAN_REUSE_OUTPUTS=true
LOCAL_SIMPLIFICATION_SCAN_CLOSURE_OUTPUTS=true
LOCAL_SIMPLIFICATION_SCAN_SAFETY_OUTPUTS=true
LOCAL_SIMPLIFICATION_MAX_ITEMS=500000
LOCAL_SIMPLIFICATION_MAX_CANDIDATE_ITEMS=100000
LOCAL_SIMPLIFICATION_MIN_READINESS_SCORE=0.40
LOCAL_SIMPLIFICATION_MIN_QUALITY_SCORE=0.40
LOCAL_SIMPLIFICATION_SAVE_REPORTS=true
"""
    content += injection
    env_path.write_text(content, encoding="utf-8")

def main():
    patch_settings()
    patch_paths()
    patch_env()
    print("Patched configs for phase 82")

if __name__ == "__main__":
    main()
