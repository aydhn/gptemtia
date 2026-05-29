import re

with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    content = f.read()

new_settings = """
    # Phase 58: Analyst UX & Operator Productivity
    analyst_ux_enabled: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ENABLED", "true")).lower() == "true")
    default_analyst_ux_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_ANALYST_UX_PROFILE", "balanced_analyst_productivity"))
    analyst_ux_default_language: str = field(default_factory=lambda: os.getenv("ANALYST_UX_DEFAULT_LANGUAGE", "tr"))
    analyst_ux_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    analyst_ux_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    analyst_ux_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    analyst_ux_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    analyst_ux_allow_real_market_download: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_ALLOW_REAL_MARKET_DOWNLOAD", "false")).lower() == "true")
    analyst_ux_generate_aliases: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_GENERATE_ALIASES", "true")).lower() == "true")
    analyst_ux_generate_prompt_packs: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_GENERATE_PROMPT_PACKS", "true")).lower() == "true")
    analyst_ux_generate_cheat_sheets: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_GENERATE_CHEAT_SHEETS", "true")).lower() == "true")
    analyst_ux_generate_task_board: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_GENERATE_TASK_BOARD", "true")).lower() == "true")
    analyst_ux_max_command_suggestions: int = field(default_factory=lambda: int(os.getenv("ANALYST_UX_MAX_COMMAND_SUGGESTIONS", "10")))
    analyst_ux_min_intent_confidence: float = field(default_factory=lambda: float(os.getenv("ANALYST_UX_MIN_INTENT_CONFIDENCE", "0.40")))
    analyst_ux_save_reports: bool = field(default_factory=lambda: str(os.getenv("ANALYST_UX_SAVE_REPORTS", "true")).lower() == "true")
    analyst_ux_min_quality_score: float = field(default_factory=lambda: float(os.getenv("ANALYST_UX_MIN_QUALITY_SCORE", "0.40")))

    def __post_init__(self):"""

content = content.replace("    def __post_init__(self):", new_settings)

with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
    f.write(content)

with open("commodity_fx_signal_bot/.env.example", "r") as f:
    env_content = f.read()

new_env = """
ANALYST_UX_ENABLED=true
DEFAULT_ANALYST_UX_PROFILE=balanced_analyst_productivity
ANALYST_UX_DEFAULT_LANGUAGE=tr
ANALYST_UX_ALLOW_LIVE_COMMANDS=false
ANALYST_UX_ALLOW_BROKER_COMMANDS=false
ANALYST_UX_ALLOW_DEPLOY_COMMANDS=false
ANALYST_UX_ALLOW_BACKGROUND_DAEMONS=false
ANALYST_UX_ALLOW_REAL_MARKET_DOWNLOAD=false
ANALYST_UX_GENERATE_ALIASES=true
ANALYST_UX_GENERATE_PROMPT_PACKS=true
ANALYST_UX_GENERATE_CHEAT_SHEETS=true
ANALYST_UX_GENERATE_TASK_BOARD=true
ANALYST_UX_MAX_COMMAND_SUGGESTIONS=10
ANALYST_UX_MIN_INTENT_CONFIDENCE=0.40
ANALYST_UX_SAVE_REPORTS=true
ANALYST_UX_MIN_QUALITY_SCORE=0.40
"""
env_content += new_env

with open("commodity_fx_signal_bot/.env.example", "w") as f:
    f.write(env_content)
