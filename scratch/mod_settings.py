import os
import re
from pathlib import Path

base_dir = Path(r"c:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia")

# 1. Update settings.py
settings_file = base_dir / "config" / "settings.py"
with open(settings_file, "r", encoding="utf-8") as f:
    settings_content = f.read()

macro_settings = """
    # Phase 109 Macro Data Provider Layer Settings
    advanced_macro_providers_enabled: bool = True
    default_macro_provider_profile: str = "balanced_no_scraping_macro_provider"
    macro_provider_current_phase: int = 109
    macro_provider_target_final_phase: int = 160
    macro_provider_next_phase: int = 110
    macro_provider_default_language: str = "tr"
    macro_provider_dry_run_default: bool = True
    macro_provider_local_only: bool = True
    macro_provider_non_production: bool = True
    macro_provider_research_only: bool = True
    macro_provider_allow_live_trading: bool = False
    macro_provider_allow_broker_integration: bool = False
    macro_provider_allow_real_order: bool = False
    macro_provider_allow_investment_advice: bool = False
    macro_provider_allow_directional_macro_claim: bool = False
    macro_provider_allow_model_deployment: bool = False
    macro_provider_allow_production_deployment: bool = False
    macro_provider_allow_web_server: bool = False
    macro_provider_allow_dashboard: bool = False
    macro_provider_allow_gui_tui: bool = False
    macro_provider_allow_external_llm: bool = False
    macro_provider_allow_vector_db: bool = False
    macro_provider_allow_embedding_api: bool = False
    macro_provider_allow_web_scraping: bool = False
    macro_provider_allow_html_scraping: bool = False
    macro_provider_allow_browser_automation_scraping: bool = False
    macro_provider_allow_hidden_api_reverse_engineering: bool = False
    macro_provider_allow_paywall_bypass: bool = False
    macro_provider_allow_rate_limit_abuse: bool = False
    macro_provider_allow_required_network_call: bool = False
    macro_provider_allow_required_paid_api: bool = False
    macro_provider_allow_credential_output: bool = False
    macro_provider_allow_cloud_publish: bool = False
    macro_provider_allow_docker_push: bool = False
    macro_provider_allow_git_tag: bool = False
    macro_provider_allow_archive_creation: bool = False
    macro_provider_allow_file_deletion: bool = False
    macro_provider_allow_file_move: bool = False
    macro_provider_allow_overwrite: bool = False
    macro_provider_enable_rates_and_yields: bool = True
    macro_provider_enable_inflation: bool = True
    macro_provider_enable_growth: bool = True
    macro_provider_enable_labor: bool = True
    macro_provider_enable_trade_balance: bool = True
    macro_provider_enable_central_bank_policy: bool = True
    macro_provider_enable_liquidity_indicators: bool = True
    macro_provider_enable_risk_sentiment: bool = True
    macro_provider_enable_yield_curve: bool = True
    macro_provider_enable_dxy_placeholder: bool = True
    macro_provider_enable_release_metadata: bool = True
    macro_provider_enable_revision_policy_requirements: bool = True
    macro_provider_enable_frequency_unit_normalization: bool = True
    macro_provider_enable_manual_file_provider: bool = True
    macro_provider_enable_local_cache_provider: bool = True
    macro_provider_enable_official_api_placeholder: bool = True
    macro_provider_enable_licensed_provider_placeholder: bool = True
    macro_provider_enable_public_dataset_placeholder: bool = True
    macro_provider_enable_dry_run_fixture_provider: bool = True
    macro_provider_enable_capability_matching: bool = True
    macro_provider_enable_preference_resolution: bool = True
    macro_provider_enable_health_check: bool = True
    macro_provider_min_readiness_score: float = 0.45
    macro_provider_min_quality_score: float = 0.45
    macro_provider_save_reports: bool = True
"""
if "advanced_macro_providers_enabled" not in settings_content:
    settings_content += "\n" + macro_settings
    with open(settings_file, "w", encoding="utf-8") as f:
        f.write(settings_content)

# 2. Update paths.py
paths_file = base_dir / "config" / "paths.py"
with open(paths_file, "r", encoding="utf-8") as f:
    paths_content = f.read()

macro_paths = """
    # Phase 109 Macro Provider Paths
    "advanced_macro_providers": DATA_LAKE_DIR / "advanced_macro_providers",
    "advanced_macro_providers_profiles": DATA_LAKE_DIR / "advanced_macro_providers/profiles",
    "advanced_macro_providers_domains": DATA_LAKE_DIR / "advanced_macro_providers/domains",
    "advanced_macro_providers_indicators": DATA_LAKE_DIR / "advanced_macro_providers/indicators",
    "advanced_macro_providers_categories": DATA_LAKE_DIR / "advanced_macro_providers/categories",
    "advanced_macro_providers_regions": DATA_LAKE_DIR / "advanced_macro_providers/regions",
    "advanced_macro_providers_symbols": DATA_LAKE_DIR / "advanced_macro_providers/symbols",
    "advanced_macro_providers_schemas": DATA_LAKE_DIR / "advanced_macro_providers/schemas",
    "advanced_macro_providers_release_metadata": DATA_LAKE_DIR / "advanced_macro_providers/release_metadata",
    "advanced_macro_providers_revision_policy": DATA_LAKE_DIR / "advanced_macro_providers/revision_policy",
    "advanced_macro_providers_frequency_unit": DATA_LAKE_DIR / "advanced_macro_providers/frequency_unit",
    "advanced_macro_providers_capabilities": DATA_LAKE_DIR / "advanced_macro_providers/capabilities",
    "advanced_macro_providers_metadata": DATA_LAKE_DIR / "advanced_macro_providers/metadata",
    "advanced_macro_providers_request_response": DATA_LAKE_DIR / "advanced_macro_providers/request_response",
    "advanced_macro_providers_contracts": DATA_LAKE_DIR / "advanced_macro_providers/contracts",
    "advanced_macro_providers_registry": DATA_LAKE_DIR / "advanced_macro_providers/registry",
    "advanced_macro_providers_resolver": DATA_LAKE_DIR / "advanced_macro_providers/resolver",
    "advanced_macro_providers_preferences": DATA_LAKE_DIR / "advanced_macro_providers/preferences",
    "advanced_macro_providers_matcher": DATA_LAKE_DIR / "advanced_macro_providers/matcher",
    "advanced_macro_providers_dry_run": DATA_LAKE_DIR / "advanced_macro_providers/dry_run",
    "advanced_macro_providers_placeholders": DATA_LAKE_DIR / "advanced_macro_providers/placeholders",
    "advanced_macro_providers_output_validation": DATA_LAKE_DIR / "advanced_macro_providers/output_validation",
    "advanced_macro_providers_safety": DATA_LAKE_DIR / "advanced_macro_providers/safety",
    "advanced_macro_providers_health": DATA_LAKE_DIR / "advanced_macro_providers/health",
    "advanced_macro_providers_scoring": DATA_LAKE_DIR / "advanced_macro_providers/scoring",
    "advanced_macro_providers_validation": DATA_LAKE_DIR / "advanced_macro_providers/validation",
    "advanced_macro_providers_quality": DATA_LAKE_DIR / "advanced_macro_providers/quality",
    
    "advanced_macro_providers_report_output": REPORTS_OUTPUT_DIR / "advanced_macro_providers",
    "advanced_macro_providers_csv_report": REPORTS_OUTPUT_DIR / "advanced_macro_providers/csv",
    "advanced_macro_providers_markdown_report": REPORTS_OUTPUT_DIR / "advanced_macro_providers/markdown",
    "advanced_macro_providers_txt_report": REPORTS_OUTPUT_DIR / "advanced_macro_providers/txt",
    "advanced_macro_providers_json_report": REPORTS_OUTPUT_DIR / "advanced_macro_providers/json",

    "advanced_macro_providers_docs": DOCS_GENERATED_DIR / "advanced_macro_providers",
    "advanced_macro_providers_docs_registry": DOCS_GENERATED_DIR / "advanced_macro_providers/registry",
    "advanced_macro_providers_docs_indicators": DOCS_GENERATED_DIR / "advanced_macro_providers/indicators",
    "advanced_macro_providers_docs_contracts": DOCS_GENERATED_DIR / "advanced_macro_providers/contracts",
    "advanced_macro_providers_docs_dry_run": DOCS_GENERATED_DIR / "advanced_macro_providers/dry_run",
    "advanced_macro_providers_docs_health": DOCS_GENERATED_DIR / "advanced_macro_providers/health",
    "advanced_macro_providers_docs_quality": DOCS_GENERATED_DIR / "advanced_macro_providers/quality",
    "advanced_macro_providers_docs_handoff": DOCS_GENERATED_DIR / "advanced_macro_providers/handoff",
"""
if "advanced_macro_providers" not in paths_content:
    # insert before "return PROJECT_DIRECTORIES" if it exists, or just append
    if "return PROJECT_DIRECTORIES" in paths_content:
        paths_content = paths_content.replace("return PROJECT_DIRECTORIES", macro_paths + "\n    return PROJECT_DIRECTORIES")
    else:
        # try to find the dictionary end
        idx = paths_content.rfind("}")
        if idx != -1:
            paths_content = paths_content[:idx] + ",\n" + macro_paths + "\n}" + paths_content[idx+1:]
    with open(paths_file, "w", encoding="utf-8") as f:
        f.write(paths_content)

print("Modified settings and paths")
