"""
Configuration for regime classification.
"""

from dataclasses import dataclass
from typing import Dict, List

from core.exceptions import ConfigError


@dataclass(frozen=True)
class RegimeProfile:
    name: str
    description: str
    feature_sets: tuple[str, ...]
    adx_trend_threshold: float = 25.0
    strong_trend_threshold: float = 35.0
    low_volatility_percentile: float = 0.20
    high_volatility_percentile: float = 0.80
    range_adx_threshold: float = 20.0
    momentum_threshold: float = 0.0
    mean_reversion_zscore_threshold: float = 2.0
    transition_lookback: int = 5
    enabled: bool = True
    notes: str = ""


# Default built-in profiles
_PROFILES: Dict[str, RegimeProfile] = {
    "balanced_regime": RegimeProfile(
        name="balanced_regime",
        description="Balanced regime profile",
        feature_sets=("trend", "momentum", "volatility", "mean_reversion", "price_action", "mtf"),
        adx_trend_threshold=25.0,
        strong_trend_threshold=35.0,
        low_volatility_percentile=0.20,
        high_volatility_percentile=0.80,
        range_adx_threshold=20.0,
        notes="Varsayılan dengeli rejim profili."
    ),
    "trend_sensitive": RegimeProfile(
        name="trend_sensitive",
        description="Trend sensitive regime profile",
        feature_sets=("trend", "momentum", "volatility", "mtf"),
        adx_trend_threshold=22.0,
        strong_trend_threshold=32.0,
        notes="Trend rejimlerini daha erken yakalamaya çalışır."
    ),
    "range_sensitive": RegimeProfile(
        name="range_sensitive",
        description="Range sensitive regime profile",
        feature_sets=("trend", "volatility", "mean_reversion", "price_action"),
        range_adx_threshold=22.0,
        low_volatility_percentile=0.25,
        notes="Range ve mean-reversion dostu ortamları daha hassas yakalar."
    ),
    "volatility_sensitive": RegimeProfile(
        name="volatility_sensitive",
        description="Volatility sensitive regime profile",
        feature_sets=("volatility", "price_action", "trend", "mtf"),
        high_volatility_percentile=0.70,
        low_volatility_percentile=0.30,
        notes="Volatilite geçişlerine daha duyarlıdır."
    )
}

ALLOWED_FEATURE_SETS = {
    "technical",
    "momentum",
    "momentum_events",
    "trend",
    "trend_events",
    "volatility",
    "volatility_events",
    "volume",
    "volume_events",
    "mean_reversion",
    "mean_reversion_events",
    "price_action",
    "price_action_events",
    "divergence",
    "divergence_events",
    "mtf",
    "mtf_events"
}

def get_regime_profile(name: str) -> RegimeProfile:
    """Get a specific regime profile by name."""
    if name not in _PROFILES:
        raise ConfigError(f"Unknown regime profile: {name}")
    return _PROFILES[name]

def list_regime_profiles(enabled_only: bool = True) -> list[RegimeProfile]:
    """List available regime profiles."""
    profiles = list(_PROFILES.values())
    if enabled_only:
        profiles = [p for p in profiles if p.enabled]
    return profiles

def get_default_regime_profile() -> RegimeProfile:
    """Get the default regime profile (balanced_regime)."""
    return get_regime_profile("balanced_regime")

def validate_regime_feature_sets(feature_sets: tuple[str, ...]) -> None:
    """Validate that feature sets are recognized."""
    if not feature_sets:
        raise ConfigError("feature_sets cannot be empty.")

    for fs in feature_sets:
        if fs not in ALLOWED_FEATURE_SETS:
            raise ConfigError(f"Unsupported feature set: {fs}")

def validate_regime_profiles() -> None:
    """Validate all configured regime profiles."""
    for p in _PROFILES.values():
        if not p.feature_sets:
            raise ConfigError(f"Profile {p.name} has empty feature_sets.")

        validate_regime_feature_sets(p.feature_sets)

        if p.low_volatility_percentile >= p.high_volatility_percentile:
            raise ConfigError(f"Profile {p.name}: low_volatility_percentile must be < high_volatility_percentile.")

        if p.adx_trend_threshold >= p.strong_trend_threshold:
            raise ConfigError(f"Profile {p.name}: adx_trend_threshold must be < strong_trend_threshold.")
