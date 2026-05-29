import re

def update_settings():
    with open('commodity_fx_signal_bot/config/settings.py', 'r') as f:
        content = f.read()

    if "scenario_regression_enabled" in content:
        print("Already updated settings")
        return

    insert_idx = content.find("def __post_init__(self):")

    new_settings = """
    # Phase 57: Scenario Regression
    scenario_regression_enabled: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_ENABLED", "true")).lower() == "true")
    default_scenario_regression_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_SCENARIO_REGRESSION_PROFILE", "balanced_scenario_regression"))
    scenario_regression_default_timeframe: str = field(default_factory=lambda: os.getenv("SCENARIO_REGRESSION_DEFAULT_TIMEFRAME", "1d"))
    scenario_regression_use_synthetic_only: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_USE_SYNTHETIC_ONLY", "true")).lower() == "true")
    scenario_regression_allow_real_market_download: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_ALLOW_REAL_MARKET_DOWNLOAD", "false")).lower() == "true")
    scenario_regression_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    scenario_regression_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    scenario_regression_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    scenario_regression_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    scenario_regression_generate_golden_outputs: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_GENERATE_GOLDEN_OUTPUTS", "true")).lower() == "true")
    scenario_regression_capture_snapshots: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_CAPTURE_SNAPSHOTS", "true")).lower() == "true")
    scenario_regression_compare_snapshots: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_COMPARE_SNAPSHOTS", "true")).lower() == "true")
    scenario_regression_run_deterministic_replay: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_RUN_DETERMINISTIC_REPLAY", "true")).lower() == "true")
    scenario_regression_validate_output_contracts: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_VALIDATE_OUTPUT_CONTRACTS", "true")).lower() == "true")
    scenario_regression_max_scenarios: int = field(default_factory=lambda: int(os.getenv("SCENARIO_REGRESSION_MAX_SCENARIOS", "50")))
    scenario_regression_max_snapshot_rows: int = field(default_factory=lambda: int(os.getenv("SCENARIO_REGRESSION_MAX_SNAPSHOT_ROWS", "1000")))
    scenario_regression_numeric_tolerance: float = field(default_factory=lambda: float(os.getenv("SCENARIO_REGRESSION_NUMERIC_TOLERANCE", "1e-8")))
    scenario_regression_text_similarity_threshold: float = field(default_factory=lambda: float(os.getenv("SCENARIO_REGRESSION_TEXT_SIMILARITY_THRESHOLD", "0.95")))
    scenario_regression_acceptance_threshold: float = field(default_factory=lambda: float(os.getenv("SCENARIO_REGRESSION_ACCEPTANCE_THRESHOLD", "0.85")))
    scenario_regression_random_seed: int = field(default_factory=lambda: int(os.getenv("SCENARIO_REGRESSION_RANDOM_SEED", "42")))
    scenario_regression_save_reports: bool = field(default_factory=lambda: str(os.getenv("SCENARIO_REGRESSION_SAVE_REPORTS", "true")).lower() == "true")
    scenario_regression_min_quality_score: float = field(default_factory=lambda: float(os.getenv("SCENARIO_REGRESSION_MIN_QUALITY_SCORE", "0.40")))

    """

    content = content[:insert_idx] + new_settings + content[insert_idx:]
    with open('commodity_fx_signal_bot/config/settings.py', 'w') as f:
        f.write(content)

def update_env():
    with open('commodity_fx_signal_bot/.env.example', 'r') as f:
        content = f.read()

    if "SCENARIO_REGRESSION_ENABLED" in content:
        print("Already updated env")
        return

    new_env = """
# Phase 57: Scenario Regression
SCENARIO_REGRESSION_ENABLED=true
DEFAULT_SCENARIO_REGRESSION_PROFILE=balanced_scenario_regression
SCENARIO_REGRESSION_DEFAULT_TIMEFRAME=1d
SCENARIO_REGRESSION_USE_SYNTHETIC_ONLY=true
SCENARIO_REGRESSION_ALLOW_REAL_MARKET_DOWNLOAD=false
SCENARIO_REGRESSION_ALLOW_LIVE_COMMANDS=false
SCENARIO_REGRESSION_ALLOW_BROKER_COMMANDS=false
SCENARIO_REGRESSION_ALLOW_DEPLOY_COMMANDS=false
SCENARIO_REGRESSION_ALLOW_BACKGROUND_DAEMONS=false
SCENARIO_REGRESSION_GENERATE_GOLDEN_OUTPUTS=true
SCENARIO_REGRESSION_CAPTURE_SNAPSHOTS=true
SCENARIO_REGRESSION_COMPARE_SNAPSHOTS=true
SCENARIO_REGRESSION_RUN_DETERMINISTIC_REPLAY=true
SCENARIO_REGRESSION_VALIDATE_OUTPUT_CONTRACTS=true
SCENARIO_REGRESSION_MAX_SCENARIOS=50
SCENARIO_REGRESSION_MAX_SNAPSHOT_ROWS=1000
SCENARIO_REGRESSION_NUMERIC_TOLERANCE=1e-8
SCENARIO_REGRESSION_TEXT_SIMILARITY_THRESHOLD=0.95
SCENARIO_REGRESSION_ACCEPTANCE_THRESHOLD=0.85
SCENARIO_REGRESSION_RANDOM_SEED=42
SCENARIO_REGRESSION_SAVE_REPORTS=true
SCENARIO_REGRESSION_MIN_QUALITY_SCORE=0.40
"""
    content += new_env
    with open('commodity_fx_signal_bot/.env.example', 'w') as f:
        f.write(content)

update_settings()
update_env()
