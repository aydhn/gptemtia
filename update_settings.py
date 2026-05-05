import re

with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    content = f.read()

insert_str = """
    # Decision Candidate Settings
    decision_candidates_enabled: bool = field(
        default_factory=lambda: os.getenv("DECISION_CANDIDATES_ENABLED", "true").lower() == "true"
    )
    directional_decision_enabled: bool = field(
        default_factory=lambda: os.getenv("DIRECTIONAL_DECISION_ENABLED", "true").lower() == "true"
    )
    default_decision_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_DECISION_PROFILE", "balanced_directional_decision")
    )
    default_decision_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_DECISION_TIMEFRAME", "1d")
    )
    decision_min_signal_score: float = field(
        default_factory=lambda: float(os.getenv("DECISION_MIN_SIGNAL_SCORE", "0.45"))
    )
    decision_min_confidence: float = field(
        default_factory=lambda: float(os.getenv("DECISION_MIN_CONFIDENCE", "0.50"))
    )
    decision_min_quality: float = field(
        default_factory=lambda: float(os.getenv("DECISION_MIN_QUALITY", "0.50"))
    )
    decision_max_conflict: float = field(
        default_factory=lambda: float(os.getenv("DECISION_MAX_CONFLICT", "0.65"))
    )
    decision_min_strategy_readiness: float = field(
        default_factory=lambda: float(os.getenv("DECISION_MIN_STRATEGY_READINESS", "0.45"))
    )
    decision_neutral_zone_threshold: float = field(
        default_factory=lambda: float(os.getenv("DECISION_NEUTRAL_ZONE_THRESHOLD", "0.15"))
    )
    decision_require_regime_confirmation: bool = field(
        default_factory=lambda: os.getenv("DECISION_REQUIRE_REGIME_CONFIRMATION", "true").lower() == "true"
    )
    decision_require_mtf_confirmation: bool = field(
        default_factory=lambda: os.getenv("DECISION_REQUIRE_MTF_CONFIRMATION", "true").lower() == "true"
    )
    decision_allow_macro_override: bool = field(
        default_factory=lambda: os.getenv("DECISION_ALLOW_MACRO_OVERRIDE", "false").lower() == "true"
    )
    save_decision_candidates: bool = field(
        default_factory=lambda: os.getenv("SAVE_DECISION_CANDIDATES", "true").lower() == "true"
    )
    save_decision_pool: bool = field(
        default_factory=lambda: os.getenv("SAVE_DECISION_POOL", "true").lower() == "true"
    )
"""

content = content.replace('save_signal_pool: bool = field(\n        default_factory=lambda: os.getenv("SAVE_SIGNAL_POOL", "true").lower() == "true"\n    )', 'save_signal_pool: bool = field(\n        default_factory=lambda: os.getenv("SAVE_SIGNAL_POOL", "true").lower() == "true"\n    )' + insert_str)

with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
    f.write(content)
