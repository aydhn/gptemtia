import re

env_example_content = """
# Phase 9: Trend Features & Events Settings
TREND_FEATURES_ENABLED=true
TREND_EVENTS_ENABLED=true
DEFAULT_TREND_MA_WINDOWS=10,20,50,100,200
DEFAULT_TREND_FAST_WINDOWS=10,20
DEFAULT_TREND_SLOW_WINDOWS=50,100,200
DEFAULT_ADX_THRESHOLD=25
DEFAULT_STRONG_ADX_THRESHOLD=35
DEFAULT_MACD_FAST=12
DEFAULT_MACD_SLOW=26
DEFAULT_MACD_SIGNAL=9
SAVE_TREND_FEATURES=true
SAVE_TREND_EVENTS=true
"""

with open("commodity_fx_signal_bot/.env.example", "r") as f:
    env_content = f.read()

if "TREND_FEATURES_ENABLED" not in env_content:
    with open("commodity_fx_signal_bot/.env.example", "a") as f:
        f.write(env_example_content)

settings_content = """
    # Phase 9: Trend Features & Events Settings
    trend_features_enabled: bool = field(
        default_factory=lambda: os.getenv("TREND_FEATURES_ENABLED", "true").lower()
        == "true"
    )
    trend_events_enabled: bool = field(
        default_factory=lambda: os.getenv("TREND_EVENTS_ENABLED", "true").lower()
        == "true"
    )
    default_trend_ma_windows: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x)
            for x in os.getenv("DEFAULT_TREND_MA_WINDOWS", "10,20,50,100,200").split(",")
        )
    )
    default_trend_fast_windows: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x)
            for x in os.getenv("DEFAULT_TREND_FAST_WINDOWS", "10,20").split(",")
        )
    )
    default_trend_slow_windows: tuple[int, ...] = field(
        default_factory=lambda: tuple(
            int(x)
            for x in os.getenv("DEFAULT_TREND_SLOW_WINDOWS", "50,100,200").split(",")
        )
    )
    default_adx_threshold: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_ADX_THRESHOLD", "25.0")
        )
    )
    default_strong_adx_threshold: float = field(
        default_factory=lambda: float(
            os.getenv("DEFAULT_STRONG_ADX_THRESHOLD", "35.0")
        )
    )
    default_macd_fast: int = field(
        default_factory=lambda: int(
            os.getenv("DEFAULT_MACD_FAST", "12")
        )
    )
    default_macd_slow: int = field(
        default_factory=lambda: int(
            os.getenv("DEFAULT_MACD_SLOW", "26")
        )
    )
    default_macd_signal: int = field(
        default_factory=lambda: int(
            os.getenv("DEFAULT_MACD_SIGNAL", "9")
        )
    )
    save_trend_features: bool = field(
        default_factory=lambda: os.getenv("SAVE_TREND_FEATURES", "true").lower()
        == "true"
    )
    save_trend_events: bool = field(
        default_factory=lambda: os.getenv("SAVE_TREND_EVENTS", "true").lower()
        == "true"
    )
"""

with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    content = f.read()

if "trend_features_enabled" not in content:
    # Insert before paper_trading_enabled
    content = content.replace("    paper_trading_enabled: bool =", settings_content + "\n    paper_trading_enabled: bool =")
    with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
        f.write(content)
