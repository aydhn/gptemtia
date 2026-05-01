import re

with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    content = f.read()

new_settings = """
    # Phase 16: Regime Classification Layer Settings
    regime_features_enabled: bool = field(
        default_factory=lambda: os.getenv("REGIME_FEATURES_ENABLED", "true").lower() == "true"
    )
    regime_events_enabled: bool = field(
        default_factory=lambda: os.getenv("REGIME_EVENTS_ENABLED", "true").lower() == "true"
    )
    default_regime_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_REGIME_PROFILE", "balanced_regime")
    )
    default_regime_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_REGIME_TIMEFRAME", "1d")
    )
    default_regime_feature_sets: tuple[str, ...] = field(
        default_factory=lambda: tuple(
            os.getenv("DEFAULT_REGIME_FEATURE_SETS", "trend,momentum,volatility,mean_reversion,price_action,mtf").split(",")
        )
    )
    default_adx_trend_threshold: float = field(
        default_factory=lambda: float(os.getenv("DEFAULT_ADX_TREND_THRESHOLD", "25.0"))
    )
    default_strong_trend_threshold: float = field(
        default_factory=lambda: float(os.getenv("DEFAULT_STRONG_TREND_THRESHOLD", "35.0"))
    )
    default_low_volatility_percentile: float = field(
        default_factory=lambda: float(os.getenv("DEFAULT_LOW_VOLATILITY_PERCENTILE", "0.20"))
    )
    default_high_volatility_percentile: float = field(
        default_factory=lambda: float(os.getenv("DEFAULT_HIGH_VOLATILITY_PERCENTILE", "0.80"))
    )
    default_range_adx_threshold: float = field(
        default_factory=lambda: float(os.getenv("DEFAULT_RANGE_ADX_THRESHOLD", "20.0"))
    )
    default_regime_transition_lookback: int = field(
        default_factory=lambda: int(os.getenv("DEFAULT_REGIME_TRANSITION_LOOKBACK", "5"))
    )
    save_regime_features: bool = field(
        default_factory=lambda: os.getenv("SAVE_REGIME_FEATURES", "true").lower() == "true"
    )
    save_regime_events: bool = field(
        default_factory=lambda: os.getenv("SAVE_REGIME_EVENTS", "true").lower() == "true"
    )

    paper_trading_enabled: bool = field(
"""

content = content.replace("    paper_trading_enabled: bool = field(", new_settings)

with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
    f.write(content)


with open("commodity_fx_signal_bot/.env.example", "r") as f:
    env_content = f.read()

new_env = """
MTF_STRICT_NO_LOOKAHEAD=true
SAVE_MTF_FEATURES=true
SAVE_MTF_EVENTS=true

# Phase 16: Regime Classification Layer
REGIME_FEATURES_ENABLED=true
REGIME_EVENTS_ENABLED=true
DEFAULT_REGIME_PROFILE=balanced_regime
DEFAULT_REGIME_TIMEFRAME=1d
DEFAULT_REGIME_FEATURE_SETS=trend,momentum,volatility,mean_reversion,price_action,mtf
DEFAULT_ADX_TREND_THRESHOLD=25.0
DEFAULT_STRONG_TREND_THRESHOLD=35.0
DEFAULT_LOW_VOLATILITY_PERCENTILE=0.20
DEFAULT_HIGH_VOLATILITY_PERCENTILE=0.80
DEFAULT_RANGE_ADX_THRESHOLD=20.0
DEFAULT_REGIME_TRANSITION_LOOKBACK=5
SAVE_REGIME_FEATURES=true
SAVE_REGIME_EVENTS=true

# Paper Trading / Strategy
PAPER_TRADING_ENABLED=true
"""

env_content = env_content.replace("""
MTF_STRICT_NO_LOOKAHEAD=true
SAVE_MTF_FEATURES=true
SAVE_MTF_EVENTS=true

# Paper Trading / Strategy
PAPER_TRADING_ENABLED=true
""", new_env)

with open("commodity_fx_signal_bot/.env.example", "w") as f:
    f.write(env_content)
