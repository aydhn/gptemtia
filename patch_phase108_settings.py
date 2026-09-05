import re
from pathlib import Path

def patch_settings():
    path = Path("config/settings.py")
    if not path.exists(): return
    content = path.read_text(encoding="utf-8")
    
    if "advanced_commodity_providers_enabled" not in content:
        insert = """
    # Phase 108 Commodities Data Provider Layer Settings
    advanced_commodity_providers_enabled: bool = True
    default_commodity_provider_profile: str = "balanced_no_scraping_commodity_provider"
    commodity_provider_current_phase: int = 108
    commodity_provider_target_final_phase: int = 160
    commodity_provider_next_phase: int = 109
    commodity_provider_default_language: str = "tr"
    commodity_provider_dry_run_default: bool = True
    commodity_provider_local_only: bool = True
    commodity_provider_non_production: bool = True
    commodity_provider_research_only: bool = True
    commodity_provider_allow_live_trading: bool = False
    commodity_provider_allow_broker_integration: bool = False
    commodity_provider_allow_futures_broker_integration: bool = False
    commodity_provider_allow_real_order: bool = False
    commodity_provider_allow_investment_advice: bool = False
    commodity_provider_allow_futures_advice: bool = False
    commodity_provider_allow_model_deployment: bool = False
    commodity_provider_allow_production_deployment: bool = False
    commodity_provider_allow_web_server: bool = False
    commodity_provider_allow_dashboard: bool = False
    commodity_provider_allow_gui_tui: bool = False
    commodity_provider_allow_external_llm: bool = False
    commodity_provider_allow_vector_db: bool = False
    commodity_provider_allow_embedding_api: bool = False
    commodity_provider_allow_web_scraping: bool = False
    commodity_provider_allow_html_scraping: bool = False
    commodity_provider_allow_browser_automation_scraping: bool = False
    commodity_provider_allow_hidden_api_reverse_engineering: bool = False
    commodity_provider_allow_paywall_bypass: bool = False
    commodity_provider_allow_rate_limit_abuse: bool = False
    commodity_provider_allow_required_network_call: bool = False
    commodity_provider_allow_required_paid_api: bool = False
    commodity_provider_allow_credential_output: bool = False
    commodity_provider_allow_cloud_publish: bool = False
    commodity_provider_allow_docker_push: bool = False
    commodity_provider_allow_git_tag: bool = False
    commodity_provider_allow_archive_creation: bool = False
    commodity_provider_allow_file_deletion: bool = False
    commodity_provider_allow_file_move: bool = False
    commodity_provider_allow_overwrite: bool = False
    commodity_provider_enable_precious_metals: bool = True
    commodity_provider_enable_energy: bool = True
    commodity_provider_enable_industrial_metals: bool = True
    commodity_provider_enable_agriculture: bool = True
    commodity_provider_enable_spot_schema: bool = True
    commodity_provider_enable_futures_contract_metadata: bool = True
    commodity_provider_enable_continuous_contract_requirements: bool = True
    commodity_provider_enable_roll_adjustment_requirements: bool = True
    commodity_provider_enable_symbol_normalization: bool = True
    commodity_provider_enable_manual_file_provider: bool = True
    commodity_provider_enable_local_cache_provider: bool = True
    commodity_provider_enable_official_api_placeholder: bool = True
    commodity_provider_enable_licensed_provider_placeholder: bool = True
    commodity_provider_enable_dry_run_fixture_provider: bool = True
    commodity_provider_enable_capability_matching: bool = True
    commodity_provider_enable_preference_resolution: bool = True
    commodity_provider_enable_health_check: bool = True
    commodity_provider_min_readiness_score: float = 0.45
    commodity_provider_min_quality_score: float = 0.45
    commodity_provider_save_reports: bool = True
"""
        content = content.replace("class Settings(BaseSettings):", "class Settings(BaseSettings):\n" + insert)
        path.write_text(content, encoding="utf-8")

def patch_env_example():
    path = Path(".env.example")
    if not path.exists(): return
    content = path.read_text(encoding="utf-8")
    
    if "ADVANCED_COMMODITY_PROVIDERS_ENABLED" not in content:
        insert = """
# Phase 108 Commodities Data Provider Layer Settings
ADVANCED_COMMODITY_PROVIDERS_ENABLED=true
DEFAULT_COMMODITY_PROVIDER_PROFILE=balanced_no_scraping_commodity_provider
COMMODITY_PROVIDER_CURRENT_PHASE=108
COMMODITY_PROVIDER_TARGET_FINAL_PHASE=160
COMMODITY_PROVIDER_NEXT_PHASE=109
COMMODITY_PROVIDER_DEFAULT_LANGUAGE=tr
COMMODITY_PROVIDER_DRY_RUN_DEFAULT=true
COMMODITY_PROVIDER_LOCAL_ONLY=true
COMMODITY_PROVIDER_NON_PRODUCTION=true
COMMODITY_PROVIDER_RESEARCH_ONLY=true
COMMODITY_PROVIDER_ALLOW_LIVE_TRADING=false
COMMODITY_PROVIDER_ALLOW_BROKER_INTEGRATION=false
COMMODITY_PROVIDER_ALLOW_FUTURES_BROKER_INTEGRATION=false
COMMODITY_PROVIDER_ALLOW_REAL_ORDER=false
COMMODITY_PROVIDER_ALLOW_INVESTMENT_ADVICE=false
COMMODITY_PROVIDER_ALLOW_FUTURES_ADVICE=false
COMMODITY_PROVIDER_ALLOW_MODEL_DEPLOYMENT=false
COMMODITY_PROVIDER_ALLOW_PRODUCTION_DEPLOYMENT=false
COMMODITY_PROVIDER_ALLOW_WEB_SERVER=false
COMMODITY_PROVIDER_ALLOW_DASHBOARD=false
COMMODITY_PROVIDER_ALLOW_GUI_TUI=false
COMMODITY_PROVIDER_ALLOW_EXTERNAL_LLM=false
COMMODITY_PROVIDER_ALLOW_VECTOR_DB=false
COMMODITY_PROVIDER_ALLOW_EMBEDDING_API=false
COMMODITY_PROVIDER_ALLOW_WEB_SCRAPING=false
COMMODITY_PROVIDER_ALLOW_HTML_SCRAPING=false
COMMODITY_PROVIDER_ALLOW_BROWSER_AUTOMATION_SCRAPING=false
COMMODITY_PROVIDER_ALLOW_HIDDEN_API_REVERSE_ENGINEERING=false
COMMODITY_PROVIDER_ALLOW_PAYWALL_BYPASS=false
COMMODITY_PROVIDER_ALLOW_RATE_LIMIT_ABUSE=false
COMMODITY_PROVIDER_ALLOW_REQUIRED_NETWORK_CALL=false
COMMODITY_PROVIDER_ALLOW_REQUIRED_PAID_API=false
COMMODITY_PROVIDER_ALLOW_CREDENTIAL_OUTPUT=false
COMMODITY_PROVIDER_ALLOW_CLOUD_PUBLISH=false
COMMODITY_PROVIDER_ALLOW_DOCKER_PUSH=false
COMMODITY_PROVIDER_ALLOW_GIT_TAG=false
COMMODITY_PROVIDER_ALLOW_ARCHIVE_CREATION=false
COMMODITY_PROVIDER_ALLOW_FILE_DELETION=false
COMMODITY_PROVIDER_ALLOW_FILE_MOVE=false
COMMODITY_PROVIDER_ALLOW_OVERWRITE=false
COMMODITY_PROVIDER_ENABLE_PRECIOUS_METALS=true
COMMODITY_PROVIDER_ENABLE_ENERGY=true
COMMODITY_PROVIDER_ENABLE_INDUSTRIAL_METALS=true
COMMODITY_PROVIDER_ENABLE_AGRICULTURE=true
COMMODITY_PROVIDER_ENABLE_SPOT_SCHEMA=true
COMMODITY_PROVIDER_ENABLE_FUTURES_CONTRACT_METADATA=true
COMMODITY_PROVIDER_ENABLE_CONTINUOUS_CONTRACT_REQUIREMENTS=true
COMMODITY_PROVIDER_ENABLE_ROLL_ADJUSTMENT_REQUIREMENTS=true
COMMODITY_PROVIDER_ENABLE_SYMBOL_NORMALIZATION=true
COMMODITY_PROVIDER_ENABLE_MANUAL_FILE_PROVIDER=true
COMMODITY_PROVIDER_ENABLE_LOCAL_CACHE_PROVIDER=true
COMMODITY_PROVIDER_ENABLE_OFFICIAL_API_PLACEHOLDER=true
COMMODITY_PROVIDER_ENABLE_LICENSED_PROVIDER_PLACEHOLDER=true
COMMODITY_PROVIDER_ENABLE_DRY_RUN_FIXTURE_PROVIDER=true
COMMODITY_PROVIDER_ENABLE_CAPABILITY_MATCHING=true
COMMODITY_PROVIDER_ENABLE_PREFERENCE_RESOLUTION=true
COMMODITY_PROVIDER_ENABLE_HEALTH_CHECK=true
COMMODITY_PROVIDER_MIN_READINESS_SCORE=0.45
COMMODITY_PROVIDER_MIN_QUALITY_SCORE=0.45
COMMODITY_PROVIDER_SAVE_REPORTS=true
"""
        path.write_text(content + insert, encoding="utf-8")

def patch_paths():
    path = Path("config/paths.py")
    if not path.exists(): return
    content = path.read_text(encoding="utf-8")
    
    if "advanced_commodity_providers" not in content:
        insert = """
    "data/lake/advanced_commodity_providers/",
    "data/lake/advanced_commodity_providers/profiles/",
    "data/lake/advanced_commodity_providers/domains/",
    "data/lake/advanced_commodity_providers/universe/",
    "data/lake/advanced_commodity_providers/categories/",
    "data/lake/advanced_commodity_providers/metadata/",
    "data/lake/advanced_commodity_providers/symbols/",
    "data/lake/advanced_commodity_providers/schemas/",
    "data/lake/advanced_commodity_providers/futures_contracts/",
    "data/lake/advanced_commodity_providers/continuous_contracts/",
    "data/lake/advanced_commodity_providers/roll_adjustment/",
    "data/lake/advanced_commodity_providers/capabilities/",
    "data/lake/advanced_commodity_providers/request_response/",
    "data/lake/advanced_commodity_providers/contracts/",
    "data/lake/advanced_commodity_providers/registry/",
    "data/lake/advanced_commodity_providers/resolver/",
    "data/lake/advanced_commodity_providers/preferences/",
    "data/lake/advanced_commodity_providers/matcher/",
    "data/lake/advanced_commodity_providers/dry_run/",
    "data/lake/advanced_commodity_providers/placeholders/",
    "data/lake/advanced_commodity_providers/output_validation/",
    "data/lake/advanced_commodity_providers/safety/",
    "data/lake/advanced_commodity_providers/health/",
    "data/lake/advanced_commodity_providers/scoring/",
    "data/lake/advanced_commodity_providers/validation/",
    "data/lake/advanced_commodity_providers/quality/",
    "reports/output/advanced_commodity_providers/",
    "reports/output/advanced_commodity_providers/csv/",
    "reports/output/advanced_commodity_providers/markdown/",
    "reports/output/advanced_commodity_providers/txt/",
    "reports/output/advanced_commodity_providers/json/",
    "docs/generated/advanced_commodity_providers/",
    "docs/generated/advanced_commodity_providers/registry/",
    "docs/generated/advanced_commodity_providers/universe/",
    "docs/generated/advanced_commodity_providers/contracts/",
    "docs/generated/advanced_commodity_providers/dry_run/",
    "docs/generated/advanced_commodity_providers/health/",
    "docs/generated/advanced_commodity_providers/quality/",
    "docs/generated/advanced_commodity_providers/handoff/",
"""
        content = content.replace("PROJECT_DIRECTORIES = [", "PROJECT_DIRECTORIES = [" + insert)
        path.write_text(content, encoding="utf-8")

if __name__ == "__main__":
    patch_settings()
    patch_env_example()
    patch_paths()
    print("Settings, env.example, and paths patched.")
