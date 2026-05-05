import re
with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    content = f.read()

insert_str = """
    # Strategy settings
    strategy_candidates_enabled: bool = field(
        default_factory=lambda: os.getenv("STRATEGY_CANDIDATES_ENABLED", "true").lower() == "true"
    )
    strategy_selection_enabled: bool = field(
        default_factory=lambda: os.getenv("STRATEGY_SELECTION_ENABLED", "true").lower() == "true"
    )
    default_strategy_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_STRATEGY_PROFILE", "balanced_strategy_selection")
    )
    default_strategy_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_STRATEGY_TIMEFRAME", "1d")
    )
    strategy_min_selection_score: float = field(
        default_factory=lambda: float(os.getenv("STRATEGY_MIN_SELECTION_SCORE", "0.45"))
    )
    strategy_min_fit_score: float = field(
        default_factory=lambda: float(os.getenv("STRATEGY_MIN_FIT_SCORE", "0.45"))
    )
    strategy_min_decision_confidence: float = field(
        default_factory=lambda: float(os.getenv("STRATEGY_MIN_DECISION_CONFIDENCE", "0.50"))
    )
    strategy_min_decision_quality: float = field(
        default_factory=lambda: float(os.getenv("STRATEGY_MIN_DECISION_QUALITY", "0.50"))
    )
    strategy_max_conflict_score: float = field(
        default_factory=lambda: float(os.getenv("STRATEGY_MAX_CONFLICT_SCORE", "0.65"))
    )
    strategy_allow_no_trade_family: bool = field(
        default_factory=lambda: os.getenv("STRATEGY_ALLOW_NO_TRADE_FAMILY", "true").lower() == "true"
    )
    strategy_allow_watchlist_family: bool = field(
        default_factory=lambda: os.getenv("STRATEGY_ALLOW_WATCHLIST_FAMILY", "true").lower() == "true"
    )
    save_strategy_candidates: bool = field(
        default_factory=lambda: os.getenv("SAVE_STRATEGY_CANDIDATES", "true").lower() == "true"
    )
    save_strategy_pool: bool = field(
        default_factory=lambda: os.getenv("SAVE_STRATEGY_POOL", "true").lower() == "true"
    )
"""

if "strategy_candidates_enabled" not in content:
    content = content.replace('    def __post_init__(self):', insert_str + '\n    def __post_init__(self):')
    with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
        f.write(content)
