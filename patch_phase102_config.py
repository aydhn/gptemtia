import os
import re

def append_to_file(filepath, content):
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(content)

def read_file(filepath):
    if not os.path.exists(filepath):
        return ""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    settings_content = """
# Phase 102 Advanced Runtime Settings
advanced_runtime_enabled: bool = True
default_advanced_runtime_profile: str = "balanced_advanced_runtime"
advanced_runtime_default_language: str = "tr"
advanced_runtime_current_phase: int = 102
advanced_runtime_target_final_phase: int = 160
advanced_runtime_dry_run_default: bool = True
advanced_runtime_local_only: bool = True
advanced_runtime_non_production: bool = True
advanced_runtime_research_only: bool = True
advanced_runtime_allow_live_trading: bool = False
advanced_runtime_allow_broker_integration: bool = False
advanced_runtime_allow_real_order: bool = False
advanced_runtime_allow_investment_advice: bool = False
advanced_runtime_allow_model_deployment: bool = False
advanced_runtime_allow_production_deployment: bool = False
advanced_runtime_allow_web_server: bool = False
advanced_runtime_allow_dashboard: bool = False
advanced_runtime_allow_gui_tui: bool = False
advanced_runtime_allow_external_llm: bool = False
advanced_runtime_allow_vector_db: bool = False
advanced_runtime_allow_embedding_api: bool = False
advanced_runtime_allow_web_scraping: bool = False
advanced_runtime_allow_cloud_publish: bool = False
advanced_runtime_allow_docker_push: bool = False
advanced_runtime_allow_git_tag: bool = False
advanced_runtime_allow_archive_creation: bool = False
advanced_runtime_allow_file_deletion: bool = False
advanced_runtime_allow_file_move: bool = False
advanced_runtime_allow_overwrite: bool = False
advanced_runtime_scan_settings: bool = True
advanced_runtime_scan_paths: bool = True
advanced_runtime_scan_datalake: bool = True
advanced_runtime_scan_featurestore: bool = True
advanced_runtime_scan_reports: bool = True
advanced_runtime_scan_scripts: bool = True
advanced_runtime_scan_tests: bool = True
advanced_runtime_scan_docs: bool = True
advanced_runtime_max_items: int = 1000000
advanced_runtime_max_rows: int = 500000
advanced_runtime_min_readiness_score: float = 0.45
advanced_runtime_min_quality_score: float = 0.45
advanced_runtime_save_reports: bool = True
"""
    if "advanced_runtime_enabled:" not in read_file("config/settings.py"):
        append_to_file("config/settings.py", settings_content)

    paths_content = """
# Phase 102 Advanced Runtime Paths
data/lake/advanced_runtime/
data/lake/advanced_runtime/profiles/
data/lake/advanced_runtime/context/
data/lake/advanced_runtime/capabilities/
data/lake/advanced_runtime/modules/
data/lake/advanced_runtime/dependencies/
data/lake/advanced_runtime/contracts/
data/lake/advanced_runtime/commands/
data/lake/advanced_runtime/outputs/
data/lake/advanced_runtime/datalake_contracts/
data/lake/advanced_runtime/featurestore_contracts/
data/lake/advanced_runtime/report_contracts/
data/lake/advanced_runtime/safety/
data/lake/advanced_runtime/health/
data/lake/advanced_runtime/scoring/
data/lake/advanced_runtime/validation/
data/lake/advanced_runtime/quality/

reports/output/advanced_runtime/
reports/output/advanced_runtime/csv/
reports/output/advanced_runtime/markdown/
reports/output/advanced_runtime/txt/
reports/output/advanced_runtime/json/

docs/generated/advanced_runtime/
docs/generated/advanced_runtime/context/
docs/generated/advanced_runtime/contracts/
docs/generated/advanced_runtime/health/
docs/generated/advanced_runtime/quality/
"""
    if "data/lake/advanced_runtime/" not in read_file("config/paths.py"):
        append_to_file("config/paths.py", paths_content)

    env_content = """
ADVANCED_RUNTIME_ENABLED=true
DEFAULT_ADVANCED_RUNTIME_PROFILE=balanced_advanced_runtime
ADVANCED_RUNTIME_DEFAULT_LANGUAGE=tr
ADVANCED_RUNTIME_CURRENT_PHASE=102
ADVANCED_RUNTIME_TARGET_FINAL_PHASE=160
ADVANCED_RUNTIME_DRY_RUN_DEFAULT=true
ADVANCED_RUNTIME_LOCAL_ONLY=true
ADVANCED_RUNTIME_NON_PRODUCTION=true
ADVANCED_RUNTIME_RESEARCH_ONLY=true
ADVANCED_RUNTIME_ALLOW_LIVE_TRADING=false
ADVANCED_RUNTIME_ALLOW_BROKER_INTEGRATION=false
ADVANCED_RUNTIME_ALLOW_REAL_ORDER=false
ADVANCED_RUNTIME_ALLOW_INVESTMENT_ADVICE=false
ADVANCED_RUNTIME_ALLOW_MODEL_DEPLOYMENT=false
ADVANCED_RUNTIME_ALLOW_PRODUCTION_DEPLOYMENT=false
ADVANCED_RUNTIME_ALLOW_WEB_SERVER=false
ADVANCED_RUNTIME_ALLOW_DASHBOARD=false
ADVANCED_RUNTIME_ALLOW_GUI_TUI=false
ADVANCED_RUNTIME_ALLOW_EXTERNAL_LLM=false
ADVANCED_RUNTIME_ALLOW_VECTOR_DB=false
ADVANCED_RUNTIME_ALLOW_EMBEDDING_API=false
ADVANCED_RUNTIME_ALLOW_WEB_SCRAPING=false
ADVANCED_RUNTIME_ALLOW_CLOUD_PUBLISH=false
ADVANCED_RUNTIME_ALLOW_DOCKER_PUSH=false
ADVANCED_RUNTIME_ALLOW_GIT_TAG=false
ADVANCED_RUNTIME_ALLOW_ARCHIVE_CREATION=false
ADVANCED_RUNTIME_ALLOW_FILE_DELETION=false
ADVANCED_RUNTIME_ALLOW_FILE_MOVE=false
ADVANCED_RUNTIME_ALLOW_OVERWRITE=false
ADVANCED_RUNTIME_SCAN_SETTINGS=true
ADVANCED_RUNTIME_SCAN_PATHS=true
ADVANCED_RUNTIME_SCAN_DATALAKE=true
ADVANCED_RUNTIME_SCAN_FEATURESTORE=true
ADVANCED_RUNTIME_SCAN_REPORTS=true
ADVANCED_RUNTIME_SCAN_SCRIPTS=true
ADVANCED_RUNTIME_SCAN_TESTS=true
ADVANCED_RUNTIME_SCAN_DOCS=true
ADVANCED_RUNTIME_MAX_ITEMS=1000000
ADVANCED_RUNTIME_MAX_ROWS=500000
ADVANCED_RUNTIME_MIN_READINESS_SCORE=0.45
ADVANCED_RUNTIME_MIN_QUALITY_SCORE=0.45
ADVANCED_RUNTIME_SAVE_REPORTS=true
"""
    if "ADVANCED_RUNTIME_ENABLED=" not in read_file(".env.example"):
        append_to_file(".env.example", env_content)

if __name__ == "__main__":
    main()
