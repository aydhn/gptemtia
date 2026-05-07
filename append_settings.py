import re

with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    content = f.read()

settings_str = """
    # Level Candidates Settings
    level_candidates_enabled: bool = True
    theoretical_stop_target_enabled: bool = True
    default_level_profile: str = "balanced_theoretical_levels"
    default_level_timeframe: str = "1d"
    level_default_atr_multipliers: tuple[float, ...] = (1.0, 1.5, 2.0, 3.0)
    level_default_target_rr_multipliers: tuple[float, ...] = (1.0, 1.5, 2.0, 3.0)
    level_min_reward_risk: float = 1.2
    level_preferred_reward_risk: float = 2.0
    level_max_stop_distance_pct: float = 0.08
    level_min_stop_distance_pct: float = 0.002
    level_min_sizing_readiness_score: float = 0.50
    level_max_total_pretrade_risk: float = 0.70
    level_use_atr_levels: bool = True
    level_use_structure_levels: bool = True
    level_use_volatility_adjustment: bool = True
    level_block_on_sizing_rejection: bool = True
    level_allow_watchlist_when_borderline: bool = True
    save_level_candidates: bool = True
    save_level_pool: bool = True
"""

# Insert before the end of the Settings class (before the last method if any, or just append)
content = content.replace("    save_sizing_pool: bool = True", "    save_sizing_pool: bool = True" + settings_str)

with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
    f.write(content)

with open("commodity_fx_signal_bot/.env.example", "r") as f:
    env_content = f.read()

env_str = """
LEVEL_CANDIDATES_ENABLED=true
THEORETICAL_STOP_TARGET_ENABLED=true
DEFAULT_LEVEL_PROFILE=balanced_theoretical_levels
DEFAULT_LEVEL_TIMEFRAME=1d
LEVEL_DEFAULT_ATR_MULTIPLIERS=1.0,1.5,2.0,3.0
LEVEL_DEFAULT_TARGET_RR_MULTIPLIERS=1.0,1.5,2.0,3.0
LEVEL_MIN_REWARD_RISK=1.2
LEVEL_PREFERRED_REWARD_RISK=2.0
LEVEL_MAX_STOP_DISTANCE_PCT=0.08
LEVEL_MIN_STOP_DISTANCE_PCT=0.002
LEVEL_MIN_SIZING_READINESS_SCORE=0.50
LEVEL_MAX_TOTAL_PRETRADE_RISK=0.70
LEVEL_USE_ATR_LEVELS=true
LEVEL_USE_STRUCTURE_LEVELS=true
LEVEL_USE_VOLATILITY_ADJUSTMENT=true
LEVEL_BLOCK_ON_SIZING_REJECTION=true
LEVEL_ALLOW_WATCHLIST_WHEN_BORDERLINE=true
SAVE_LEVEL_CANDIDATES=true
SAVE_LEVEL_POOL=true
"""

with open("commodity_fx_signal_bot/.env.example", "w") as f:
    f.write(env_content + "\n" + env_str)
