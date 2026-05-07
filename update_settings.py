import re

with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    content = f.read()

settings_fields = """
    # Phase 24: Theoretical Sizing Candidate Layer
    sizing_candidates_enabled: bool = field(
        default_factory=lambda: str(os.getenv("SIZING_CANDIDATES_ENABLED", "true")).lower() == "true"
    )
    theoretical_position_sizing_enabled: bool = field(
        default_factory=lambda: str(os.getenv("THEORETICAL_POSITION_SIZING_ENABLED", "true")).lower() == "true"
    )
    default_sizing_profile: str = field(
        default_factory=lambda: os.getenv("DEFAULT_SIZING_PROFILE", "balanced_theoretical_sizing")
    )
    default_sizing_timeframe: str = field(
        default_factory=lambda: os.getenv("DEFAULT_SIZING_TIMEFRAME", "1d")
    )
    theoretical_account_equity: float = field(
        default_factory=lambda: float(os.getenv("THEORETICAL_ACCOUNT_EQUITY", "100000.0"))
    )
    theoretical_base_currency: str = field(
        default_factory=lambda: os.getenv("THEORETICAL_BASE_CURRENCY", "TRY")
    )
    theoretical_risk_per_candidate: float = field(
        default_factory=lambda: float(os.getenv("THEORETICAL_RISK_PER_CANDIDATE", "0.005"))
    )
    theoretical_max_risk_per_symbol: float = field(
        default_factory=lambda: float(os.getenv("THEORETICAL_MAX_RISK_PER_SYMBOL", "0.02"))
    )
    theoretical_max_risk_per_asset_class: float = field(
        default_factory=lambda: float(os.getenv("THEORETICAL_MAX_RISK_PER_ASSET_CLASS", "0.05"))
    )
    theoretical_max_total_portfolio_risk: float = field(
        default_factory=lambda: float(os.getenv("THEORETICAL_MAX_TOTAL_PORTFOLIO_RISK", "0.15"))
    )
    sizing_min_risk_readiness_score: float = field(
        default_factory=lambda: float(os.getenv("SIZING_MIN_RISK_READINESS_SCORE", "0.50"))
    )
    sizing_max_total_pretrade_risk: float = field(
        default_factory=lambda: float(os.getenv("SIZING_MAX_TOTAL_PRETRADE_RISK", "0.70"))
    )
    sizing_min_data_quality_score: float = field(
        default_factory=lambda: float(os.getenv("SIZING_MIN_DATA_QUALITY_SCORE", "0.50"))
    )
    sizing_use_atr_based_unit: bool = field(
        default_factory=lambda: str(os.getenv("SIZING_USE_ATR_BASED_UNIT", "true")).lower() == "true"
    )
    sizing_use_volatility_adjustment: bool = field(
        default_factory=lambda: str(os.getenv("SIZING_USE_VOLATILITY_ADJUSTMENT", "true")).lower() == "true"
    )
    sizing_block_on_risk_rejection: bool = field(
        default_factory=lambda: str(os.getenv("SIZING_BLOCK_ON_RISK_REJECTION", "true")).lower() == "true"
    )
    sizing_allow_watchlist_for_borderline: bool = field(
        default_factory=lambda: str(os.getenv("SIZING_ALLOW_WATCHLIST_FOR_BORDERLINE", "true")).lower() == "true"
    )
    save_sizing_candidates: bool = field(
        default_factory=lambda: str(os.getenv("SAVE_SIZING_CANDIDATES", "true")).lower() == "true"
    )
    save_sizing_pool: bool = field(
        default_factory=lambda: str(os.getenv("SAVE_SIZING_POOL", "true")).lower() == "true"
    )

    # Force live trading off
"""

content = re.sub(r'    # Force live trading off', settings_fields, content)

with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
    f.write(content)

with open("commodity_fx_signal_bot/.env.example", "r") as f:
    env_content = f.read()

env_fields = """
# Phase 24: Theoretical Sizing Candidate Layer
SIZING_CANDIDATES_ENABLED=true
THEORETICAL_POSITION_SIZING_ENABLED=true
DEFAULT_SIZING_PROFILE=balanced_theoretical_sizing
DEFAULT_SIZING_TIMEFRAME=1d
THEORETICAL_ACCOUNT_EQUITY=100000
THEORETICAL_BASE_CURRENCY=TRY
THEORETICAL_RISK_PER_CANDIDATE=0.005
THEORETICAL_MAX_RISK_PER_SYMBOL=0.02
THEORETICAL_MAX_RISK_PER_ASSET_CLASS=0.05
THEORETICAL_MAX_TOTAL_PORTFOLIO_RISK=0.15
SIZING_MIN_RISK_READINESS_SCORE=0.50
SIZING_MAX_TOTAL_PRETRADE_RISK=0.70
SIZING_MIN_DATA_QUALITY_SCORE=0.50
SIZING_USE_ATR_BASED_UNIT=true
SIZING_USE_VOLATILITY_ADJUSTMENT=true
SIZING_BLOCK_ON_RISK_REJECTION=true
SIZING_ALLOW_WATCHLIST_FOR_BORDERLINE=true
SAVE_SIZING_CANDIDATES=true
SAVE_SIZING_POOL=true
"""

with open("commodity_fx_signal_bot/.env.example", "w") as f:
    f.write(env_content + "\n" + env_fields)
