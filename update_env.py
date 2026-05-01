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
"""

env_content = env_content.replace("""
MTF_STRICT_NO_LOOKAHEAD=true
SAVE_MTF_FEATURES=true
SAVE_MTF_EVENTS=true

# Paper Trading / Strategy
""", new_env)

with open("commodity_fx_signal_bot/.env.example", "w") as f:
    f.write(env_content)
