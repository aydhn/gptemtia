import os
from pathlib import Path

def w(path: str, content: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# config/settings.py update logic
settings_update = """
    # Phase 107 FX Provider Settings
    advanced_fx_providers_enabled: bool = True
    default_fx_provider_profile: str = "balanced_no_scraping_fx_provider"
    fx_provider_current_phase: int = 107
    fx_provider_target_final_phase: int = 160
    fx_provider_next_phase: int = 108
    fx_provider_default_language: str = "tr"
    fx_provider_dry_run_default: bool = True
    fx_provider_local_only: bool = True
    fx_provider_non_production: bool = True
    fx_provider_research_only: bool = True
    fx_provider_allow_live_trading: bool = False
    fx_provider_allow_broker_integration: bool = False
    fx_provider_allow_real_order: bool = False
    fx_provider_allow_investment_advice: bool = False
    fx_provider_allow_model_deployment: bool = False
    fx_provider_allow_production_deployment: bool = False
    fx_provider_allow_web_server: bool = False
    fx_provider_allow_dashboard: bool = False
    fx_provider_allow_gui_tui: bool = False
    fx_provider_allow_external_llm: bool = False
    fx_provider_allow_vector_db: bool = False
    fx_provider_allow_embedding_api: bool = False
    fx_provider_allow_web_scraping: bool = False
    fx_provider_allow_html_scraping: bool = False
    fx_provider_allow_browser_automation_scraping: bool = False
    fx_provider_allow_hidden_api_reverse_engineering: bool = False
    fx_provider_allow_paywall_bypass: bool = False
    fx_provider_allow_rate_limit_abuse: bool = False
    fx_provider_allow_required_network_call: bool = False
    fx_provider_allow_required_paid_api: bool = False
    fx_provider_allow_credential_output: bool = False
    fx_provider_allow_cloud_publish: bool = False
    fx_provider_allow_docker_push: bool = False
    fx_provider_allow_git_tag: bool = False
    fx_provider_allow_archive_creation: bool = False
    fx_provider_allow_file_deletion: bool = False
    fx_provider_allow_file_move: bool = False
    fx_provider_allow_overwrite: bool = False
    fx_provider_enable_major_pairs: bool = True
    fx_provider_enable_minor_pairs: bool = True
    fx_provider_enable_exotic_pairs: bool = True
    fx_provider_enable_cross_rate_requirements: bool = True
    fx_provider_enable_symbol_normalization: bool = True
    fx_provider_enable_manual_file_provider: bool = True
    fx_provider_enable_local_cache_provider: bool = True
    fx_provider_enable_official_api_placeholder: bool = True
    fx_provider_enable_licensed_provider_placeholder: bool = True
    fx_provider_enable_dry_run_fixture_provider: bool = True
    fx_provider_enable_capability_matching: bool = True
    fx_provider_enable_preference_resolution: bool = True
    fx_provider_enable_health_check: bool = True
    fx_provider_min_readiness_score: float = 0.45
    fx_provider_min_quality_score: float = 0.45
    fx_provider_save_reports: bool = True
"""

def update_settings():
    path = "config/settings.py"
    if not os.path.exists(path): return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if "advanced_fx_providers_enabled" not in content:
        # find class Settings(BaseSettings):
        if "class Settings(BaseSettings):" in content:
            parts = content.split("class Settings(BaseSettings):")
            new_content = parts[0] + "class Settings(BaseSettings):\n" + settings_update + parts[1]
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)

update_settings()

env_example_update = """
ADVANCED_FX_PROVIDERS_ENABLED=true
DEFAULT_FX_PROVIDER_PROFILE=balanced_no_scraping_fx_provider
FX_PROVIDER_CURRENT_PHASE=107
FX_PROVIDER_TARGET_FINAL_PHASE=160
FX_PROVIDER_NEXT_PHASE=108
FX_PROVIDER_DEFAULT_LANGUAGE=tr
FX_PROVIDER_DRY_RUN_DEFAULT=true
FX_PROVIDER_LOCAL_ONLY=true
FX_PROVIDER_NON_PRODUCTION=true
FX_PROVIDER_RESEARCH_ONLY=true
FX_PROVIDER_ALLOW_LIVE_TRADING=false
FX_PROVIDER_ALLOW_BROKER_INTEGRATION=false
FX_PROVIDER_ALLOW_REAL_ORDER=false
FX_PROVIDER_ALLOW_INVESTMENT_ADVICE=false
FX_PROVIDER_ALLOW_MODEL_DEPLOYMENT=false
FX_PROVIDER_ALLOW_PRODUCTION_DEPLOYMENT=false
FX_PROVIDER_ALLOW_WEB_SERVER=false
FX_PROVIDER_ALLOW_DASHBOARD=false
FX_PROVIDER_ALLOW_GUI_TUI=false
FX_PROVIDER_ALLOW_EXTERNAL_LLM=false
FX_PROVIDER_ALLOW_VECTOR_DB=false
FX_PROVIDER_ALLOW_EMBEDDING_API=false
FX_PROVIDER_ALLOW_WEB_SCRAPING=false
FX_PROVIDER_ALLOW_HTML_SCRAPING=false
FX_PROVIDER_ALLOW_BROWSER_AUTOMATION_SCRAPING=false
FX_PROVIDER_ALLOW_HIDDEN_API_REVERSE_ENGINEERING=false
FX_PROVIDER_ALLOW_PAYWALL_BYPASS=false
FX_PROVIDER_ALLOW_RATE_LIMIT_ABUSE=false
FX_PROVIDER_ALLOW_REQUIRED_NETWORK_CALL=false
FX_PROVIDER_ALLOW_REQUIRED_PAID_API=false
FX_PROVIDER_ALLOW_CREDENTIAL_OUTPUT=false
FX_PROVIDER_ALLOW_CLOUD_PUBLISH=false
FX_PROVIDER_ALLOW_DOCKER_PUSH=false
FX_PROVIDER_ALLOW_GIT_TAG=false
FX_PROVIDER_ALLOW_ARCHIVE_CREATION=false
FX_PROVIDER_ALLOW_FILE_DELETION=false
FX_PROVIDER_ALLOW_FILE_MOVE=false
FX_PROVIDER_ALLOW_OVERWRITE=false
FX_PROVIDER_ENABLE_MAJOR_PAIRS=true
FX_PROVIDER_ENABLE_MINOR_PAIRS=true
FX_PROVIDER_ENABLE_EXOTIC_PAIRS=true
FX_PROVIDER_ENABLE_CROSS_RATE_REQUIREMENTS=true
FX_PROVIDER_ENABLE_SYMBOL_NORMALIZATION=true
FX_PROVIDER_ENABLE_MANUAL_FILE_PROVIDER=true
FX_PROVIDER_ENABLE_LOCAL_CACHE_PROVIDER=true
FX_PROVIDER_ENABLE_OFFICIAL_API_PLACEHOLDER=true
FX_PROVIDER_ENABLE_LICENSED_PROVIDER_PLACEHOLDER=true
FX_PROVIDER_ENABLE_DRY_RUN_FIXTURE_PROVIDER=true
FX_PROVIDER_ENABLE_CAPABILITY_MATCHING=true
FX_PROVIDER_ENABLE_PREFERENCE_RESOLUTION=true
FX_PROVIDER_ENABLE_HEALTH_CHECK=true
FX_PROVIDER_MIN_READINESS_SCORE=0.45
FX_PROVIDER_MIN_QUALITY_SCORE=0.45
FX_PROVIDER_SAVE_REPORTS=true
"""

def update_env_example():
    path = ".env.example"
    if not os.path.exists(path): return
    with open(path, "a", encoding="utf-8") as f:
        f.write("\n" + env_example_update.strip() + "\n")

update_env_example()

def update_paths():
    path = "config/paths.py"
    if not os.path.exists(path): return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    paths_addition = """
    # Advanced FX Providers
    "data/lake/advanced_fx_providers",
    "data/lake/advanced_fx_providers/profiles",
    "data/lake/advanced_fx_providers/domains",
    "data/lake/advanced_fx_providers/pairs",
    "data/lake/advanced_fx_providers/currencies",
    "data/lake/advanced_fx_providers/symbols",
    "data/lake/advanced_fx_providers/schemas",
    "data/lake/advanced_fx_providers/cross_rates",
    "data/lake/advanced_fx_providers/capabilities",
    "data/lake/advanced_fx_providers/metadata",
    "data/lake/advanced_fx_providers/request_response",
    "data/lake/advanced_fx_providers/contracts",
    "data/lake/advanced_fx_providers/registry",
    "data/lake/advanced_fx_providers/resolver",
    "data/lake/advanced_fx_providers/preferences",
    "data/lake/advanced_fx_providers/matcher",
    "data/lake/advanced_fx_providers/dry_run",
    "data/lake/advanced_fx_providers/placeholders",
    "data/lake/advanced_fx_providers/output_validation",
    "data/lake/advanced_fx_providers/safety",
    "data/lake/advanced_fx_providers/health",
    "data/lake/advanced_fx_providers/scoring",
    "data/lake/advanced_fx_providers/validation",
    "data/lake/advanced_fx_providers/quality",
    "reports/output/advanced_fx_providers",
    "reports/output/advanced_fx_providers/csv",
    "reports/output/advanced_fx_providers/markdown",
    "reports/output/advanced_fx_providers/txt",
    "reports/output/advanced_fx_providers/json",
    "docs/generated/advanced_fx_providers",
    "docs/generated/advanced_fx_providers/registry",
    "docs/generated/advanced_fx_providers/pairs",
    "docs/generated/advanced_fx_providers/contracts",
    "docs/generated/advanced_fx_providers/dry_run",
    "docs/generated/advanced_fx_providers/health",
    "docs/generated/advanced_fx_providers/quality",
    "docs/generated/advanced_fx_providers/handoff",
"""
    if "data/lake/advanced_fx_providers" not in content:
        content = content.replace('PROJECT_DIRECTORIES = [', 'PROJECT_DIRECTORIES = [' + paths_addition)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

update_paths()
print("Base configs updated")
