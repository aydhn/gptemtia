"""
Central registry for regime labels.
"""

from core.exceptions import ConfigError

# Base regime labels
UNKNOWN = "unknown"
INSUFFICIENT_DATA = "insufficient_data"

# Trend labels
BULLISH_TREND = "bullish_trend"
BEARISH_TREND = "bearish_trend"
STRONG_BULLISH_TREND = "strong_bullish_trend"
STRONG_BEARISH_TREND = "strong_bearish_trend"
WEAK_TREND = "weak_trend"
FRAGILE_TREND = "fragile_trend"

# Range labels
RANGE_BOUND = "range_bound"
COMPRESSED_RANGE = "compressed_range"
VOLATILE_RANGE = "volatile_range"

# Volatility labels
HIGH_VOLATILITY = "high_volatility"
LOW_VOLATILITY = "low_volatility"
VOLATILITY_EXPANSION = "volatility_expansion"
VOLATILITY_COMPRESSION = "volatility_compression"

# Momentum labels
MOMENTUM_BULLISH = "momentum_bullish"
MOMENTUM_BEARISH = "momentum_bearish"
MOMENTUM_NEUTRAL = "momentum_neutral"

# Context labels
MEAN_REVERSION_FRIENDLY = "mean_reversion_friendly"
BREAKOUT_CANDIDATE_REGIME = "breakout_candidate_regime"
CONFLICTING_REGIME = "conflicting_regime"

# MTF labels
MTF_ALIGNED_TREND = "mtf_aligned_trend"
MTF_CONFLICT = "mtf_conflict"

_ALL_LABELS = {
    UNKNOWN, INSUFFICIENT_DATA,
    BULLISH_TREND, BEARISH_TREND, STRONG_BULLISH_TREND, STRONG_BEARISH_TREND, WEAK_TREND, FRAGILE_TREND,
    RANGE_BOUND, COMPRESSED_RANGE, VOLATILE_RANGE,
    HIGH_VOLATILITY, LOW_VOLATILITY, VOLATILITY_EXPANSION, VOLATILITY_COMPRESSION,
    MOMENTUM_BULLISH, MOMENTUM_BEARISH, MOMENTUM_NEUTRAL,
    MEAN_REVERSION_FRIENDLY, BREAKOUT_CANDIDATE_REGIME, CONFLICTING_REGIME,
    MTF_ALIGNED_TREND, MTF_CONFLICT
}

def list_regime_labels() -> list[str]:
    """Get list of all supported regime labels."""
    return sorted(list(_ALL_LABELS))

def validate_regime_label(label: str) -> None:
    """Validate a regime label."""
    if label not in _ALL_LABELS:
        raise ConfigError(f"Unknown regime label: {label}")

def is_trend_regime(label: str) -> bool:
    """Check if label is a trend regime."""
    return label in {BULLISH_TREND, BEARISH_TREND, STRONG_BULLISH_TREND, STRONG_BEARISH_TREND, WEAK_TREND, FRAGILE_TREND}

def is_range_regime(label: str) -> bool:
    """Check if label is a range regime."""
    return label in {RANGE_BOUND, COMPRESSED_RANGE, VOLATILE_RANGE}

def is_volatility_regime(label: str) -> bool:
    """Check if label is a volatility regime."""
    return label in {HIGH_VOLATILITY, LOW_VOLATILITY, VOLATILITY_EXPANSION, VOLATILITY_COMPRESSION}

def is_mtf_regime(label: str) -> bool:
    """Check if label is an MTF regime."""
    return label in {MTF_ALIGNED_TREND, MTF_CONFLICT}
