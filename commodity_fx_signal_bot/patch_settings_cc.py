import re

with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    content = f.read()

cc_settings = """
    # Phase 50: Command Center
    command_center_enabled: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_ENABLED", "true")).lower() == "true")
    default_command_center_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_COMMAND_CENTER_PROFILE", "balanced_offline_command_center"))
    command_center_default_timeframe: str = field(default_factory=lambda: os.getenv("COMMAND_CENTER_DEFAULT_TIMEFRAME", "1d"))
    command_center_dry_run_default: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_DRY_RUN_DEFAULT", "true")).lower() == "true")
    command_center_require_safe_commands: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_REQUIRE_SAFE_COMMANDS", "true")).lower() == "true")
    command_center_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    command_center_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    command_center_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    command_center_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    command_center_max_suggested_commands: int = field(default_factory=lambda: int(os.getenv("COMMAND_CENTER_MAX_SUGGESTED_COMMANDS", "50")))
    command_center_include_research_reports: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_RESEARCH_REPORTS", "true")).lower() == "true")
    command_center_include_portfolio_reports: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_PORTFOLIO_REPORTS", "true")).lower() == "true")
    command_center_include_regime_reports: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_REGIME_REPORTS", "true")).lower() == "true")
    command_center_include_synthetic_indices: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_SYNTHETIC_INDICES", "true")).lower() == "true")
    command_center_include_factor_research: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_FACTOR_RESEARCH", "true")).lower() == "true")
    command_center_include_meta_research: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_META_RESEARCH", "true")).lower() == "true")
    command_center_include_experiments: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_EXPERIMENTS", "true")).lower() == "true")
    command_center_include_governance: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_GOVERNANCE", "true")).lower() == "true")
    command_center_include_planning: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_PLANNING", "true")).lower() == "true")
    command_center_include_knowledge_base: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_INCLUDE_KNOWLEDGE_BASE", "true")).lower() == "true")
    command_center_save_reports: bool = field(default_factory=lambda: str(os.getenv("COMMAND_CENTER_SAVE_REPORTS", "true")).lower() == "true")
    command_center_min_quality_score: float = field(default_factory=lambda: float(os.getenv("COMMAND_CENTER_MIN_QUALITY_SCORE", "0.40")))

    def __post_init__(self):"""

content = re.sub(r'    def __post_init__\(self\):', cc_settings, content)

with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
    f.write(content)
