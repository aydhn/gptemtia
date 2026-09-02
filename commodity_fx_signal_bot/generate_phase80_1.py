import os
from pathlib import Path

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def write_file(path: str, content: str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def read_file(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def insert_after_pattern(content: str, pattern: str, insertion: str) -> str:
    parts = content.split(pattern)
    if len(parts) > 1:
        return parts[0] + pattern + "\n" + insertion + parts[1]
    return content

print("Starting Phase 80 Generation - Part 1...")

# 1. Update config/settings.py
settings_content = read_file("config/settings.py")
if "local_closure_enabled" not in settings_content:
    closure_settings = """
    # Phase 80: Local Closure Settings
    local_closure_enabled: bool = True
    default_local_closure_profile: str = "balanced_local_closure"
    local_closure_default_language: str = "tr"
    local_closure_dry_run_default: bool = True
    local_closure_allow_real_v1_release: bool = False
    local_closure_allow_production_release_claim: bool = False
    local_closure_allow_official_project_closure_claim: bool = False
    local_closure_allow_legal_signoff_claim: bool = False
    local_closure_allow_compliance_claim: bool = False
    local_closure_allow_cloud_upload: bool = False
    local_closure_allow_package_publish: bool = False
    local_closure_allow_external_service: bool = False
    local_closure_allow_external_llm: bool = False
    local_closure_allow_file_modification: bool = False
    local_closure_allow_file_deletion: bool = False
    local_closure_allow_file_move: bool = False
    local_closure_allow_overwrite: bool = False
    local_closure_allow_live_trading_claim: bool = False
    local_closure_allow_broker_readiness_claim: bool = False
    local_closure_allow_investment_advice: bool = False
    local_closure_allow_model_deployment_claim: bool = False
    local_closure_scan_docs: bool = True
    local_closure_scan_reports: bool = True
    local_closure_scan_data_lake: bool = True
    local_closure_scan_scripts: bool = True
    local_closure_scan_tests: bool = True
    local_closure_scan_generated_docs: bool = True
    local_closure_scan_archival_outputs: bool = True
    local_closure_scan_delivery_outputs: bool = True
    local_closure_scan_acceptance_outputs: bool = True
    local_closure_scan_safety_outputs: bool = True
    local_closure_max_items: int = 500000
    local_closure_min_readiness_score: float = 0.40
    local_closure_min_quality_score: float = 0.40
    local_closure_save_reports: bool = True
"""
    settings_content = insert_after_pattern(settings_content, "class Settings(BaseSettings):", closure_settings)
    write_file("config/settings.py", settings_content)

# 2. Update .env.example
env_content = read_file(".env.example")
if "LOCAL_CLOSURE_ENABLED" not in env_content:
    closure_env = """
# Phase 80: Local Closure Settings
LOCAL_CLOSURE_ENABLED=true
DEFAULT_LOCAL_CLOSURE_PROFILE=balanced_local_closure
LOCAL_CLOSURE_DEFAULT_LANGUAGE=tr
LOCAL_CLOSURE_DRY_RUN_DEFAULT=true
LOCAL_CLOSURE_ALLOW_REAL_V1_RELEASE=false
LOCAL_CLOSURE_ALLOW_PRODUCTION_RELEASE_CLAIM=false
LOCAL_CLOSURE_ALLOW_OFFICIAL_PROJECT_CLOSURE_CLAIM=false
LOCAL_CLOSURE_ALLOW_LEGAL_SIGNOFF_CLAIM=false
LOCAL_CLOSURE_ALLOW_COMPLIANCE_CLAIM=false
LOCAL_CLOSURE_ALLOW_CLOUD_UPLOAD=false
LOCAL_CLOSURE_ALLOW_PACKAGE_PUBLISH=false
LOCAL_CLOSURE_ALLOW_EXTERNAL_SERVICE=false
LOCAL_CLOSURE_ALLOW_EXTERNAL_LLM=false
LOCAL_CLOSURE_ALLOW_FILE_MODIFICATION=false
LOCAL_CLOSURE_ALLOW_FILE_DELETION=false
LOCAL_CLOSURE_ALLOW_FILE_MOVE=false
LOCAL_CLOSURE_ALLOW_OVERWRITE=false
LOCAL_CLOSURE_ALLOW_LIVE_TRADING_CLAIM=false
LOCAL_CLOSURE_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_CLOSURE_ALLOW_INVESTMENT_ADVICE=false
LOCAL_CLOSURE_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_CLOSURE_SCAN_DOCS=true
LOCAL_CLOSURE_SCAN_REPORTS=true
LOCAL_CLOSURE_SCAN_DATA_LAKE=true
LOCAL_CLOSURE_SCAN_SCRIPTS=true
LOCAL_CLOSURE_SCAN_TESTS=true
LOCAL_CLOSURE_SCAN_GENERATED_DOCS=true
LOCAL_CLOSURE_SCAN_ARCHIVAL_OUTPUTS=true
LOCAL_CLOSURE_SCAN_DELIVERY_OUTPUTS=true
LOCAL_CLOSURE_SCAN_ACCEPTANCE_OUTPUTS=true
LOCAL_CLOSURE_SCAN_SAFETY_OUTPUTS=true
LOCAL_CLOSURE_MAX_ITEMS=500000
LOCAL_CLOSURE_MIN_READINESS_SCORE=0.40
LOCAL_CLOSURE_MIN_QUALITY_SCORE=0.40
LOCAL_CLOSURE_SAVE_REPORTS=true
"""
    with open(".env.example", "a", encoding="utf-8") as f:
        f.write(closure_env)

# 3. Update config/paths.py
paths_content = read_file("config/paths.py")
if "local_closure" not in paths_content:
    paths_attrs = """
    # Phase 80: Local Closure Paths
    LAKE_LOCAL_CLOSURE: Path = LAKE_DIR / "local_closure"
    LAKE_CLOSURE_PROFILES: Path = LAKE_LOCAL_CLOSURE / "profiles"
    LAKE_CLOSURE_DOMAINS: Path = LAKE_LOCAL_CLOSURE / "domains"
    LAKE_CLOSURE_META_REVIEW: Path = LAKE_LOCAL_CLOSURE / "meta_review"
    LAKE_CLOSURE_LESSONS_LEARNED: Path = LAKE_LOCAL_CLOSURE / "lessons_learned"
    LAKE_CLOSURE_ROADMAP: Path = LAKE_LOCAL_CLOSURE / "roadmap"
    LAKE_CLOSURE_FUTURE_PHASES: Path = LAKE_LOCAL_CLOSURE / "future_phases"
    LAKE_CLOSURE_GOVERNANCE: Path = LAKE_LOCAL_CLOSURE / "governance"
    LAKE_CLOSURE_DOSSIER: Path = LAKE_LOCAL_CLOSURE / "dossier"
    LAKE_CLOSURE_RECAPS: Path = LAKE_LOCAL_CLOSURE / "recaps"
    LAKE_CLOSURE_UNRESOLVED: Path = LAKE_LOCAL_CLOSURE / "unresolved"
    LAKE_CLOSURE_OPEN_QUESTIONS: Path = LAKE_LOCAL_CLOSURE / "open_questions"
    LAKE_CLOSURE_IMPROVEMENTS: Path = LAKE_LOCAL_CLOSURE / "improvements"
    LAKE_CLOSURE_MAINTENANCE: Path = LAKE_LOCAL_CLOSURE / "maintenance"
    LAKE_CLOSURE_OWNERSHIP: Path = LAKE_LOCAL_CLOSURE / "ownership"
    LAKE_CLOSURE_DECISIONS: Path = LAKE_LOCAL_CLOSURE / "decisions"
    LAKE_CLOSURE_ASSUMPTIONS: Path = LAKE_LOCAL_CLOSURE / "assumptions"
    LAKE_CLOSURE_LIMITATIONS: Path = LAKE_LOCAL_CLOSURE / "limitations"
    LAKE_CLOSURE_NO_GO_SAFE_GO: Path = LAKE_LOCAL_CLOSURE / "no_go_safe_go"
    LAKE_CLOSURE_AFTERCARE: Path = LAKE_LOCAL_CLOSURE / "aftercare"
    LAKE_CLOSURE_FAQ: Path = LAKE_LOCAL_CLOSURE / "faq"
    LAKE_CLOSURE_EXCEPTIONS: Path = LAKE_LOCAL_CLOSURE / "exceptions"
    LAKE_CLOSURE_GAPS: Path = LAKE_LOCAL_CLOSURE / "gaps"
    LAKE_CLOSURE_RISKS: Path = LAKE_LOCAL_CLOSURE / "risks"
    LAKE_CLOSURE_SCORING: Path = LAKE_LOCAL_CLOSURE / "scoring"
    LAKE_CLOSURE_VALIDATION: Path = LAKE_LOCAL_CLOSURE / "validation"
    LAKE_CLOSURE_QUALITY: Path = LAKE_LOCAL_CLOSURE / "quality"

    OUTPUT_LOCAL_CLOSURE: Path = REPORTS_OUTPUT_DIR / "local_closure"
    OUTPUT_CLOSURE_CSV: Path = OUTPUT_LOCAL_CLOSURE / "csv"
    OUTPUT_CLOSURE_MARKDOWN: Path = OUTPUT_LOCAL_CLOSURE / "markdown"
    OUTPUT_CLOSURE_TXT: Path = OUTPUT_LOCAL_CLOSURE / "txt"
    OUTPUT_CLOSURE_JSON: Path = OUTPUT_LOCAL_CLOSURE / "json"

    DOCS_LOCAL_CLOSURE: Path = DOCS_GENERATED_DIR / "local_closure"
"""
    paths_content = insert_after_pattern(paths_content, "DOCS_GENERATED_DIR: Path = DOCS_DIR / \"generated\"", paths_attrs)
    
    ensure_dirs = """
        cls.LAKE_LOCAL_CLOSURE,
        cls.LAKE_CLOSURE_PROFILES,
        cls.LAKE_CLOSURE_DOMAINS,
        cls.LAKE_CLOSURE_META_REVIEW,
        cls.LAKE_CLOSURE_LESSONS_LEARNED,
        cls.LAKE_CLOSURE_ROADMAP,
        cls.LAKE_CLOSURE_FUTURE_PHASES,
        cls.LAKE_CLOSURE_GOVERNANCE,
        cls.LAKE_CLOSURE_DOSSIER,
        cls.LAKE_CLOSURE_RECAPS,
        cls.LAKE_CLOSURE_UNRESOLVED,
        cls.LAKE_CLOSURE_OPEN_QUESTIONS,
        cls.LAKE_CLOSURE_IMPROVEMENTS,
        cls.LAKE_CLOSURE_MAINTENANCE,
        cls.LAKE_CLOSURE_OWNERSHIP,
        cls.LAKE_CLOSURE_DECISIONS,
        cls.LAKE_CLOSURE_ASSUMPTIONS,
        cls.LAKE_CLOSURE_LIMITATIONS,
        cls.LAKE_CLOSURE_NO_GO_SAFE_GO,
        cls.LAKE_CLOSURE_AFTERCARE,
        cls.LAKE_CLOSURE_FAQ,
        cls.LAKE_CLOSURE_EXCEPTIONS,
        cls.LAKE_CLOSURE_GAPS,
        cls.LAKE_CLOSURE_RISKS,
        cls.LAKE_CLOSURE_SCORING,
        cls.LAKE_CLOSURE_VALIDATION,
        cls.LAKE_CLOSURE_QUALITY,
        cls.OUTPUT_LOCAL_CLOSURE,
        cls.OUTPUT_CLOSURE_CSV,
        cls.OUTPUT_CLOSURE_MARKDOWN,
        cls.OUTPUT_CLOSURE_TXT,
        cls.OUTPUT_CLOSURE_JSON,
        cls.DOCS_LOCAL_CLOSURE,
"""
    paths_content = insert_after_pattern(paths_content, "cls.DOCS_GENERATED_DIR,", ensure_dirs)
    write_file("config/paths.py", paths_content)

print("Part 1 completed.")
