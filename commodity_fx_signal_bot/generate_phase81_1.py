import os
from pathlib import Path

def patch_settings():
    print("Patching config/settings.py")
    settings_path = Path("config/settings.py")
    with open(settings_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_settings = """
    # Local Reuse Settings
    local_reuse_enabled: bool = True
    default_local_reuse_profile: str = "balanced_local_reuse"
    local_reuse_default_language: str = "tr"
    local_reuse_dry_run_default: bool = True
    local_reuse_allow_real_v1_1_implementation: bool = False
    local_reuse_allow_implementation_approval: bool = False
    local_reuse_allow_production_release_claim: bool = False
    local_reuse_allow_official_standard_claim: bool = False
    local_reuse_allow_compliance_claim: bool = False
    local_reuse_allow_cloud_upload: bool = False
    local_reuse_allow_package_publish: bool = False
    local_reuse_allow_external_service: bool = False
    local_reuse_allow_external_llm: bool = False
    local_reuse_allow_file_modification: bool = False
    local_reuse_allow_file_deletion: bool = False
    local_reuse_allow_file_move: bool = False
    local_reuse_allow_overwrite: bool = False
    local_reuse_allow_live_trading_claim: bool = False
    local_reuse_allow_broker_readiness_claim: bool = False
    local_reuse_allow_investment_advice: bool = False
    local_reuse_allow_model_deployment_claim: bool = False
    
    local_reuse_scan_docs: bool = True
    local_reuse_scan_reports: bool = True
    local_reuse_scan_data_lake: bool = True
    local_reuse_scan_scripts: bool = True
    local_reuse_scan_tests: bool = True
    local_reuse_scan_generated_docs: bool = True
    local_reuse_scan_closure_outputs: bool = True
    local_reuse_scan_archival_outputs: bool = True
    local_reuse_scan_delivery_outputs: bool = True
    local_reuse_scan_acceptance_outputs: bool = True
    local_reuse_scan_safety_outputs: bool = True
    
    local_reuse_max_items: int = 500000
    local_reuse_max_templates: int = 10000
    local_reuse_min_readiness_score: float = 0.40
    local_reuse_min_quality_score: float = 0.40
    local_reuse_save_reports: bool = True
"""
    if "local_reuse_enabled" not in content:
        insert_idx = content.find("    model_config =")
        if insert_idx == -1:
            insert_idx = content.rfind("    @")
        
        if insert_idx != -1:
            content = content[:insert_idx] + new_settings + content[insert_idx:]
            with open(settings_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Successfully patched settings.py")
        else:
            print("Failed to find insertion point in settings.py")

def patch_env():
    print("Patching .env.example")
    env_path = Path(".env.example")
    if not env_path.exists():
        print(".env.example not found")
        return
    with open(env_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_env = """
# LOCAL REUSE
LOCAL_REUSE_ENABLED=true
DEFAULT_LOCAL_REUSE_PROFILE=balanced_local_reuse
LOCAL_REUSE_DEFAULT_LANGUAGE=tr
LOCAL_REUSE_DRY_RUN_DEFAULT=true
LOCAL_REUSE_ALLOW_REAL_V1_1_IMPLEMENTATION=false
LOCAL_REUSE_ALLOW_IMPLEMENTATION_APPROVAL=false
LOCAL_REUSE_ALLOW_PRODUCTION_RELEASE_CLAIM=false
LOCAL_REUSE_ALLOW_OFFICIAL_STANDARD_CLAIM=false
LOCAL_REUSE_ALLOW_COMPLIANCE_CLAIM=false
LOCAL_REUSE_ALLOW_CLOUD_UPLOAD=false
LOCAL_REUSE_ALLOW_PACKAGE_PUBLISH=false
LOCAL_REUSE_ALLOW_EXTERNAL_SERVICE=false
LOCAL_REUSE_ALLOW_EXTERNAL_LLM=false
LOCAL_REUSE_ALLOW_FILE_MODIFICATION=false
LOCAL_REUSE_ALLOW_FILE_DELETION=false
LOCAL_REUSE_ALLOW_FILE_MOVE=false
LOCAL_REUSE_ALLOW_OVERWRITE=false
LOCAL_REUSE_ALLOW_LIVE_TRADING_CLAIM=false
LOCAL_REUSE_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_REUSE_ALLOW_INVESTMENT_ADVICE=false
LOCAL_REUSE_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_REUSE_SCAN_DOCS=true
LOCAL_REUSE_SCAN_REPORTS=true
LOCAL_REUSE_SCAN_DATA_LAKE=true
LOCAL_REUSE_SCAN_SCRIPTS=true
LOCAL_REUSE_SCAN_TESTS=true
LOCAL_REUSE_SCAN_GENERATED_DOCS=true
LOCAL_REUSE_SCAN_CLOSURE_OUTPUTS=true
LOCAL_REUSE_SCAN_ARCHIVAL_OUTPUTS=true
LOCAL_REUSE_SCAN_DELIVERY_OUTPUTS=true
LOCAL_REUSE_SCAN_ACCEPTANCE_OUTPUTS=true
LOCAL_REUSE_SCAN_SAFETY_OUTPUTS=true
LOCAL_REUSE_MAX_ITEMS=500000
LOCAL_REUSE_MAX_TEMPLATES=10000
LOCAL_REUSE_MIN_READINESS_SCORE=0.40
LOCAL_REUSE_MIN_QUALITY_SCORE=0.40
LOCAL_REUSE_SAVE_REPORTS=true
"""
    if "LOCAL_REUSE_ENABLED" not in content:
        content += new_env
        with open(env_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Successfully patched .env.example")

def patch_paths():
    print("Patching config/paths.py")
    paths_path = Path("config/paths.py")
    with open(paths_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_paths = """
    # Local Reuse Paths
    LOCAL_REUSE_DIR = DATA_LAKE_DIR / "local_reuse"
    LOCAL_REUSE_PROFILES_DIR = LOCAL_REUSE_DIR / "profiles"
    LOCAL_REUSE_DOMAINS_DIR = LOCAL_REUSE_DIR / "domains"
    LOCAL_REUSE_AUDIT_MEMORY_DIR = LOCAL_REUSE_DIR / "audit_memory"
    LOCAL_REUSE_PHASE_CAPSULES_DIR = LOCAL_REUSE_DIR / "phase_capsules"
    LOCAL_REUSE_TEMPLATE_CATALOG_DIR = LOCAL_REUSE_DIR / "template_catalog"
    LOCAL_REUSE_PROMPT_TEMPLATES_DIR = LOCAL_REUSE_DIR / "prompt_templates"
    LOCAL_REUSE_MODULE_BLUEPRINTS_DIR = LOCAL_REUSE_DIR / "module_blueprints"
    LOCAL_REUSE_SCRIPT_PATTERNS_DIR = LOCAL_REUSE_DIR / "script_patterns"
    LOCAL_REUSE_TEST_PATTERNS_DIR = LOCAL_REUSE_DIR / "test_patterns"
    LOCAL_REUSE_DATALAKE_PATTERNS_DIR = LOCAL_REUSE_DIR / "datalake_patterns"
    LOCAL_REUSE_REPORT_PATTERNS_DIR = LOCAL_REUSE_DIR / "report_patterns"
    LOCAL_REUSE_SAFETY_PATTERNS_DIR = LOCAL_REUSE_DIR / "safety_patterns"
    LOCAL_REUSE_DOCUMENTATION_PATTERNS_DIR = LOCAL_REUSE_DIR / "documentation_patterns"
    LOCAL_REUSE_KNOWLEDGE_REUSE_KIT_DIR = LOCAL_REUSE_DIR / "knowledge_reuse_kit"
    LOCAL_REUSE_PATTERN_EXTRACTION_DIR = LOCAL_REUSE_DIR / "pattern_extraction"
    LOCAL_REUSE_V1_1_SEED_DIR = LOCAL_REUSE_DIR / "v1_1_seed"
    LOCAL_REUSE_FUTURE_PROJECT_DIR = LOCAL_REUSE_DIR / "future_project"
    LOCAL_REUSE_NO_GO_SAFE_GO_DIR = LOCAL_REUSE_DIR / "no_go_safe_go"
    LOCAL_REUSE_EXCEPTIONS_DIR = LOCAL_REUSE_DIR / "exceptions"
    LOCAL_REUSE_GAPS_DIR = LOCAL_REUSE_DIR / "gaps"
    LOCAL_REUSE_RISKS_DIR = LOCAL_REUSE_DIR / "risks"
    LOCAL_REUSE_SCORING_DIR = LOCAL_REUSE_DIR / "scoring"
    LOCAL_REUSE_VALIDATION_DIR = LOCAL_REUSE_DIR / "validation"
    LOCAL_REUSE_QUALITY_DIR = LOCAL_REUSE_DIR / "quality"
    
    LOCAL_REUSE_REPORTS_DIR = REPORTS_OUTPUT_DIR / "local_reuse"
    LOCAL_REUSE_REPORTS_CSV_DIR = LOCAL_REUSE_REPORTS_DIR / "csv"
    LOCAL_REUSE_REPORTS_MD_DIR = LOCAL_REUSE_REPORTS_DIR / "markdown"
    LOCAL_REUSE_REPORTS_TXT_DIR = LOCAL_REUSE_REPORTS_DIR / "txt"
    LOCAL_REUSE_REPORTS_JSON_DIR = LOCAL_REUSE_REPORTS_DIR / "json"
    
    LOCAL_REUSE_DOCS_DIR = GENERATED_DOCS_DIR / "local_reuse"
"""
    new_dirs_to_ensure = """
        cls.LOCAL_REUSE_DIR,
        cls.LOCAL_REUSE_PROFILES_DIR,
        cls.LOCAL_REUSE_DOMAINS_DIR,
        cls.LOCAL_REUSE_AUDIT_MEMORY_DIR,
        cls.LOCAL_REUSE_PHASE_CAPSULES_DIR,
        cls.LOCAL_REUSE_TEMPLATE_CATALOG_DIR,
        cls.LOCAL_REUSE_PROMPT_TEMPLATES_DIR,
        cls.LOCAL_REUSE_MODULE_BLUEPRINTS_DIR,
        cls.LOCAL_REUSE_SCRIPT_PATTERNS_DIR,
        cls.LOCAL_REUSE_TEST_PATTERNS_DIR,
        cls.LOCAL_REUSE_DATALAKE_PATTERNS_DIR,
        cls.LOCAL_REUSE_REPORT_PATTERNS_DIR,
        cls.LOCAL_REUSE_SAFETY_PATTERNS_DIR,
        cls.LOCAL_REUSE_DOCUMENTATION_PATTERNS_DIR,
        cls.LOCAL_REUSE_KNOWLEDGE_REUSE_KIT_DIR,
        cls.LOCAL_REUSE_PATTERN_EXTRACTION_DIR,
        cls.LOCAL_REUSE_V1_1_SEED_DIR,
        cls.LOCAL_REUSE_FUTURE_PROJECT_DIR,
        cls.LOCAL_REUSE_NO_GO_SAFE_GO_DIR,
        cls.LOCAL_REUSE_EXCEPTIONS_DIR,
        cls.LOCAL_REUSE_GAPS_DIR,
        cls.LOCAL_REUSE_RISKS_DIR,
        cls.LOCAL_REUSE_SCORING_DIR,
        cls.LOCAL_REUSE_VALIDATION_DIR,
        cls.LOCAL_REUSE_QUALITY_DIR,
        cls.LOCAL_REUSE_REPORTS_DIR,
        cls.LOCAL_REUSE_REPORTS_CSV_DIR,
        cls.LOCAL_REUSE_REPORTS_MD_DIR,
        cls.LOCAL_REUSE_REPORTS_TXT_DIR,
        cls.LOCAL_REUSE_REPORTS_JSON_DIR,
        cls.LOCAL_REUSE_DOCS_DIR,
"""
    if "LOCAL_REUSE_DIR" not in content:
        ensure_idx = content.find("    @classmethod\n    def ensure_project_directories")
        if ensure_idx != -1:
            content = content[:ensure_idx] + new_paths + "\n" + content[ensure_idx:]
            # Re-find the index after modification
            ensure_idx = content.find("    @classmethod\n    def ensure_project_directories")
            dirs_idx = content.find("]", ensure_idx)
            if dirs_idx != -1:
                content = content[:dirs_idx] + new_dirs_to_ensure + content[dirs_idx:]
            with open(paths_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Successfully patched paths.py")

if __name__ == "__main__":
    patch_settings()
    patch_env()
    patch_paths()
