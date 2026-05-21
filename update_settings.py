import re

with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    content = f.read()

portfolio_regime_settings = """
    # Phase 42: Portfolio Regime Research
    portfolio_regime_research_enabled: bool = field(default_factory=lambda: str(os.getenv("PORTFOLIO_REGIME_RESEARCH_ENABLED", "true")).lower() == "true")
    default_portfolio_regime_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_PORTFOLIO_REGIME_PROFILE", "balanced_regime_portfolio_research"))
    portfolio_regime_default_timeframe: str = field(default_factory=lambda: os.getenv("PORTFOLIO_REGIME_DEFAULT_TIMEFRAME", "1d"))
    portfolio_regime_min_symbols: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_MIN_SYMBOLS", "3")))
    portfolio_regime_min_observations: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_MIN_OBSERVATIONS", "180")))
    portfolio_regime_volatility_window: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_VOLATILITY_WINDOW", "20")))
    portfolio_regime_trend_window: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_TREND_WINDOW", "50")))
    portfolio_regime_correlation_window: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_CORRELATION_WINDOW", "60")))
    portfolio_regime_drawdown_cluster_threshold: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_DRAWDOWN_CLUSTER_THRESHOLD", "-0.05")))
    portfolio_regime_stress_window_min_bars: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_STRESS_WINDOW_MIN_BARS", "20")))
    portfolio_regime_stress_window_max_bars: int = field(default_factory=lambda: int(os.getenv("PORTFOLIO_REGIME_STRESS_WINDOW_MAX_BARS", "90")))
    portfolio_regime_tail_quantile: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_TAIL_QUANTILE", "0.05")))
    portfolio_regime_scenario_shock_small: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_SCENARIO_SHOCK_SMALL", "0.03")))
    portfolio_regime_scenario_shock_medium: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_SCENARIO_SHOCK_MEDIUM", "0.07")))
    portfolio_regime_scenario_shock_large: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_SCENARIO_SHOCK_LARGE", "0.12")))
    portfolio_regime_save_reports: bool = field(default_factory=lambda: str(os.getenv("PORTFOLIO_REGIME_SAVE_REPORTS", "true")).lower() == "true")
    portfolio_regime_save_tables: bool = field(default_factory=lambda: str(os.getenv("PORTFOLIO_REGIME_SAVE_TABLES", "true")).lower() == "true")
    portfolio_regime_min_quality_score: float = field(default_factory=lambda: float(os.getenv("PORTFOLIO_REGIME_MIN_QUALITY_SCORE", "0.40")))
"""

content = content.replace("    def __post_init__(self):", portfolio_regime_settings + "\n    def __post_init__(self):")

with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
    f.write(content)

with open("commodity_fx_signal_bot/.env.example", "a") as f:
    f.write("""
PORTFOLIO_REGIME_RESEARCH_ENABLED=true
DEFAULT_PORTFOLIO_REGIME_PROFILE=balanced_regime_portfolio_research
PORTFOLIO_REGIME_DEFAULT_TIMEFRAME=1d
PORTFOLIO_REGIME_MIN_SYMBOLS=3
PORTFOLIO_REGIME_MIN_OBSERVATIONS=180
PORTFOLIO_REGIME_VOLATILITY_WINDOW=20
PORTFOLIO_REGIME_TREND_WINDOW=50
PORTFOLIO_REGIME_CORRELATION_WINDOW=60
PORTFOLIO_REGIME_DRAWDOWN_CLUSTER_THRESHOLD=-0.05
PORTFOLIO_REGIME_STRESS_WINDOW_MIN_BARS=20
PORTFOLIO_REGIME_STRESS_WINDOW_MAX_BARS=90
PORTFOLIO_REGIME_TAIL_QUANTILE=0.05
PORTFOLIO_REGIME_SCENARIO_SHOCK_SMALL=0.03
PORTFOLIO_REGIME_SCENARIO_SHOCK_MEDIUM=0.07
PORTFOLIO_REGIME_SCENARIO_SHOCK_LARGE=0.12
PORTFOLIO_REGIME_SAVE_REPORTS=true
PORTFOLIO_REGIME_SAVE_TABLES=true
PORTFOLIO_REGIME_MIN_QUALITY_SCORE=0.40
""")
