import os
import re

# Update Settings
settings_path = "commodity_fx_signal_bot/config/settings.py"
with open(settings_path, "r") as f:
    settings_content = f.read()

settings_addition = """
    # Artifact Metadata Settings
    artifact_metadata_enabled: bool = True
    default_artifact_metadata_profile: str = "balanced_local_metadata"
    artifact_metadata_default_language: str = "tr"
    artifact_metadata_dry_run_default: bool = True
    artifact_metadata_allow_model_deployment_claims: bool = False
    artifact_metadata_allow_official_certification_claims: bool = False
    artifact_metadata_allow_investment_advice_claims: bool = False
    artifact_metadata_allow_cloud_registry: bool = False
    artifact_metadata_allow_file_modification: bool = False
    artifact_metadata_allow_file_deletion: bool = False
    artifact_metadata_allow_live_commands: bool = False
    artifact_metadata_allow_broker_commands: bool = False
    artifact_metadata_allow_deploy_commands: bool = False
    artifact_metadata_allow_background_daemons: bool = False
    artifact_metadata_allow_real_market_download: bool = False
    artifact_metadata_allow_external_llm: bool = False
    artifact_metadata_scan_models: bool = True
    artifact_metadata_scan_datasets: bool = True
    artifact_metadata_scan_experiments: bool = True
    artifact_metadata_scan_backtests: bool = True
    artifact_metadata_scan_scenarios: bool = True
    artifact_metadata_scan_reports: bool = True
    artifact_metadata_scan_evidence: bool = True
    artifact_metadata_max_artifacts: int = 200000
    artifact_metadata_max_artifact_mb: int = 50
    artifact_metadata_freshness_days_warning: int = 45
    artifact_metadata_save_reports: bool = True
    artifact_metadata_min_quality_score: float = 0.40
"""
if "artifact_metadata_enabled" not in settings_content:
    # insert before the end of the class
    settings_content = settings_content + settings_addition

with open(settings_path, "w") as f:
    f.write(settings_content)

# Update Env
env_path = "commodity_fx_signal_bot/.env.example"
with open(env_path, "r") as f:
    env_content = f.read()

env_addition = """
# Artifact Metadata Config
ARTIFACT_METADATA_ENABLED=true
DEFAULT_ARTIFACT_METADATA_PROFILE=balanced_local_metadata
ARTIFACT_METADATA_DEFAULT_LANGUAGE=tr
ARTIFACT_METADATA_DRY_RUN_DEFAULT=true
ARTIFACT_METADATA_ALLOW_MODEL_DEPLOYMENT_CLAIMS=false
ARTIFACT_METADATA_ALLOW_OFFICIAL_CERTIFICATION_CLAIMS=false
ARTIFACT_METADATA_ALLOW_INVESTMENT_ADVICE_CLAIMS=false
ARTIFACT_METADATA_ALLOW_CLOUD_REGISTRY=false
ARTIFACT_METADATA_ALLOW_FILE_MODIFICATION=false
ARTIFACT_METADATA_ALLOW_FILE_DELETION=false
ARTIFACT_METADATA_ALLOW_LIVE_COMMANDS=false
ARTIFACT_METADATA_ALLOW_BROKER_COMMANDS=false
ARTIFACT_METADATA_ALLOW_DEPLOY_COMMANDS=false
ARTIFACT_METADATA_ALLOW_BACKGROUND_DAEMONS=false
ARTIFACT_METADATA_ALLOW_REAL_MARKET_DOWNLOAD=false
ARTIFACT_METADATA_ALLOW_EXTERNAL_LLM=false
ARTIFACT_METADATA_SCAN_MODELS=true
ARTIFACT_METADATA_SCAN_DATASETS=true
ARTIFACT_METADATA_SCAN_EXPERIMENTS=true
ARTIFACT_METADATA_SCAN_BACKTESTS=true
ARTIFACT_METADATA_SCAN_SCENARIOS=true
ARTIFACT_METADATA_SCAN_REPORTS=true
ARTIFACT_METADATA_SCAN_EVIDENCE=true
ARTIFACT_METADATA_MAX_ARTIFACTS=200000
ARTIFACT_METADATA_MAX_ARTIFACT_MB=50
ARTIFACT_METADATA_FRESHNESS_DAYS_WARNING=45
ARTIFACT_METADATA_SAVE_REPORTS=true
ARTIFACT_METADATA_MIN_QUALITY_SCORE=0.40
"""
if "ARTIFACT_METADATA_ENABLED" not in env_content:
    env_content = env_content + "\n" + env_addition

with open(env_path, "w") as f:
    f.write(env_content)


# Update paths
paths_path = "commodity_fx_signal_bot/config/paths.py"
with open(paths_path, "r") as f:
    paths_content = f.read()

paths_addition = """
# Artifact Metadata Paths
DATA_LAKE_ARTIFACT_METADATA_DIR = DATA_LAKE_DIR / "artifact_metadata"
DATA_LAKE_ARTIFACT_METADATA_INVENTORY_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "inventory"
DATA_LAKE_ARTIFACT_METADATA_REGISTRY_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "metadata_registry"
DATA_LAKE_ARTIFACT_METADATA_MODEL_CARDS_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "model_cards"
DATA_LAKE_ARTIFACT_METADATA_DATASET_CARDS_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "dataset_cards"
DATA_LAKE_ARTIFACT_METADATA_EXPERIMENT_CARDS_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "experiment_cards"
DATA_LAKE_ARTIFACT_METADATA_REPRODUCIBILITY_CARDS_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "reproducibility_cards"
DATA_LAKE_ARTIFACT_METADATA_BACKTEST_CARDS_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "backtest_cards"
DATA_LAKE_ARTIFACT_METADATA_SCENARIO_CARDS_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "scenario_cards"
DATA_LAKE_ARTIFACT_METADATA_REGRESSION_CARDS_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "regression_cards"
DATA_LAKE_ARTIFACT_METADATA_FEATURE_SET_CARDS_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "feature_set_cards"
DATA_LAKE_ARTIFACT_METADATA_SYNTHETIC_DATA_CARDS_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "synthetic_data_cards"
DATA_LAKE_ARTIFACT_METADATA_RESEARCH_REPORT_CARDS_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "research_report_cards"
DATA_LAKE_ARTIFACT_METADATA_LINEAGE_CARDS_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "lineage_cards"
DATA_LAKE_ARTIFACT_METADATA_LIMITATION_CARDS_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "limitation_cards"
DATA_LAKE_ARTIFACT_METADATA_INTENDED_USE_CARDS_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "intended_use_cards"
DATA_LAKE_ARTIFACT_METADATA_NON_USE_POLICY_CARDS_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "non_use_policy_cards"
DATA_LAKE_ARTIFACT_METADATA_SCORING_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "scoring"
DATA_LAKE_ARTIFACT_METADATA_VALIDATION_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "validation"
DATA_LAKE_ARTIFACT_METADATA_QUALITY_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "quality"
DATA_LAKE_ARTIFACT_METADATA_EXPORTS_DIR = DATA_LAKE_ARTIFACT_METADATA_DIR / "exports"

REPORTS_ARTIFACT_METADATA_DIR = REPORTS_OUTPUT_DIR / "artifact_metadata"
REPORTS_ARTIFACT_METADATA_CSV_DIR = REPORTS_ARTIFACT_METADATA_DIR / "csv"
REPORTS_ARTIFACT_METADATA_MD_DIR = REPORTS_ARTIFACT_METADATA_DIR / "markdown"
REPORTS_ARTIFACT_METADATA_TXT_DIR = REPORTS_ARTIFACT_METADATA_DIR / "txt"
REPORTS_ARTIFACT_METADATA_JSON_DIR = REPORTS_ARTIFACT_METADATA_DIR / "json"

DOCS_GENERATED_ARTIFACT_METADATA_DIR = DOCS_GENERATED_DIR / "artifact_metadata"
"""

if "DATA_LAKE_ARTIFACT_METADATA_DIR" not in paths_content:
    # find def ensure_project_directories(): and insert before
    paths_content = paths_content.replace(
        "def ensure_project_directories():",
        paths_addition + "\ndef ensure_project_directories():"
    )

dirs_to_create = [
    "DATA_LAKE_ARTIFACT_METADATA_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_INVENTORY_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_REGISTRY_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_MODEL_CARDS_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_DATASET_CARDS_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_EXPERIMENT_CARDS_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_REPRODUCIBILITY_CARDS_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_BACKTEST_CARDS_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_SCENARIO_CARDS_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_REGRESSION_CARDS_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_FEATURE_SET_CARDS_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_SYNTHETIC_DATA_CARDS_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_RESEARCH_REPORT_CARDS_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_LINEAGE_CARDS_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_LIMITATION_CARDS_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_INTENDED_USE_CARDS_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_NON_USE_POLICY_CARDS_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_SCORING_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_VALIDATION_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_QUALITY_DIR",
    "DATA_LAKE_ARTIFACT_METADATA_EXPORTS_DIR",
    "REPORTS_ARTIFACT_METADATA_DIR",
    "REPORTS_ARTIFACT_METADATA_CSV_DIR",
    "REPORTS_ARTIFACT_METADATA_MD_DIR",
    "REPORTS_ARTIFACT_METADATA_TXT_DIR",
    "REPORTS_ARTIFACT_METADATA_JSON_DIR",
    "DOCS_GENERATED_ARTIFACT_METADATA_DIR"
]

for d in dirs_to_create:
    if f"{d}.mkdir(parents=True, exist_ok=True)" not in paths_content:
        paths_content = paths_content.replace(
            "        CACHE_DIR.mkdir(parents=True, exist_ok=True)",
            f"        {d}.mkdir(parents=True, exist_ok=True)\n        CACHE_DIR.mkdir(parents=True, exist_ok=True)"
        )

with open(paths_path, "w") as f:
    f.write(paths_content)

print("Settings and Paths updated")
