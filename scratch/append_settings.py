import os
from pathlib import Path

ROOT_DIR = Path("C:/Users/immor/OneDrive/Belgeler/Projelerim/gptemtia")

def append_to_file(filepath, content):
    with open(filepath, "a", encoding="utf-8") as f:
        f.write("\n" + content + "\n")

settings_content = """
# Phase 105 Advanced Gap Closure System
advanced_gap_closure_enabled: bool = True
default_advanced_gap_closure_profile: str = "balanced_functional_gap_closure"
advanced_gap_closure_current_phase: int = 105
advanced_gap_closure_target_final_phase: int = 160
advanced_gap_closure_next_phase: int = 106
advanced_gap_closure_default_language: str = "tr"
advanced_gap_closure_dry_run_default: bool = True
advanced_gap_closure_local_only: bool = True
advanced_gap_closure_non_production: bool = True
advanced_gap_closure_research_only: bool = True
advanced_gap_closure_allow_live_trading: bool = False
advanced_gap_closure_allow_broker_integration: bool = False
advanced_gap_closure_allow_real_order: bool = False
advanced_gap_closure_allow_investment_advice: bool = False
advanced_gap_closure_allow_model_deployment: bool = False
advanced_gap_closure_allow_production_deployment: bool = False
advanced_gap_closure_allow_web_server: bool = False
advanced_gap_closure_allow_dashboard: bool = False
advanced_gap_closure_allow_gui_tui: bool = False
advanced_gap_closure_allow_external_llm: bool = False
advanced_gap_closure_allow_vector_db: bool = False
advanced_gap_closure_allow_embedding_api: bool = False
advanced_gap_closure_allow_web_scraping: bool = False
advanced_gap_closure_allow_cloud_publish: bool = False
advanced_gap_closure_allow_docker_push: bool = False
advanced_gap_closure_allow_git_tag: bool = False
advanced_gap_closure_allow_archive_creation: bool = False
advanced_gap_closure_allow_file_deletion: bool = False
advanced_gap_closure_allow_file_move: bool = False
advanced_gap_closure_allow_overwrite: bool = False
advanced_gap_closure_enable_phase_106_handoff: bool = True
advanced_gap_closure_enable_provider_requirements: bool = True
advanced_gap_closure_enable_no_scraping_boundary: bool = True
advanced_gap_closure_enable_readiness_reconciliation: bool = True
advanced_gap_closure_min_readiness_score: float = 0.45
advanced_gap_closure_min_quality_score: float = 0.45
advanced_gap_closure_save_reports: bool = True
"""

append_to_file(ROOT_DIR / "config/settings.py", settings_content)

env_content = """
ADVANCED_GAP_CLOSURE_ENABLED=true
DEFAULT_ADVANCED_GAP_CLOSURE_PROFILE=balanced_functional_gap_closure
ADVANCED_GAP_CLOSURE_CURRENT_PHASE=105
ADVANCED_GAP_CLOSURE_TARGET_FINAL_PHASE=160
ADVANCED_GAP_CLOSURE_NEXT_PHASE=106
ADVANCED_GAP_CLOSURE_DEFAULT_LANGUAGE=tr
ADVANCED_GAP_CLOSURE_DRY_RUN_DEFAULT=true
ADVANCED_GAP_CLOSURE_LOCAL_ONLY=true
ADVANCED_GAP_CLOSURE_NON_PRODUCTION=true
ADVANCED_GAP_CLOSURE_RESEARCH_ONLY=true
ADVANCED_GAP_CLOSURE_ALLOW_LIVE_TRADING=false
ADVANCED_GAP_CLOSURE_ALLOW_BROKER_INTEGRATION=false
ADVANCED_GAP_CLOSURE_ALLOW_REAL_ORDER=false
ADVANCED_GAP_CLOSURE_ALLOW_INVESTMENT_ADVICE=false
ADVANCED_GAP_CLOSURE_ALLOW_MODEL_DEPLOYMENT=false
ADVANCED_GAP_CLOSURE_ALLOW_PRODUCTION_DEPLOYMENT=false
ADVANCED_GAP_CLOSURE_ALLOW_WEB_SERVER=false
ADVANCED_GAP_CLOSURE_ALLOW_DASHBOARD=false
ADVANCED_GAP_CLOSURE_ALLOW_GUI_TUI=false
ADVANCED_GAP_CLOSURE_ALLOW_EXTERNAL_LLM=false
ADVANCED_GAP_CLOSURE_ALLOW_VECTOR_DB=false
ADVANCED_GAP_CLOSURE_ALLOW_EMBEDDING_API=false
ADVANCED_GAP_CLOSURE_ALLOW_WEB_SCRAPING=false
ADVANCED_GAP_CLOSURE_ALLOW_CLOUD_PUBLISH=false
ADVANCED_GAP_CLOSURE_ALLOW_DOCKER_PUSH=false
ADVANCED_GAP_CLOSURE_ALLOW_GIT_TAG=false
ADVANCED_GAP_CLOSURE_ALLOW_ARCHIVE_CREATION=false
ADVANCED_GAP_CLOSURE_ALLOW_FILE_DELETION=false
ADVANCED_GAP_CLOSURE_ALLOW_FILE_MOVE=false
ADVANCED_GAP_CLOSURE_ALLOW_OVERWRITE=false
ADVANCED_GAP_CLOSURE_ENABLE_PHASE_106_HANDOFF=true
ADVANCED_GAP_CLOSURE_ENABLE_PROVIDER_REQUIREMENTS=true
ADVANCED_GAP_CLOSURE_ENABLE_NO_SCRAPING_BOUNDARY=true
ADVANCED_GAP_CLOSURE_ENABLE_READINESS_RECONCILIATION=true
ADVANCED_GAP_CLOSURE_MIN_READINESS_SCORE=0.45
ADVANCED_GAP_CLOSURE_MIN_QUALITY_SCORE=0.45
ADVANCED_GAP_CLOSURE_SAVE_REPORTS=true
"""

append_to_file(ROOT_DIR / ".env.example", env_content)

print("Appended settings to settings.py and .env.example")
