from dataclasses import dataclass

from core.exceptions import ConfigError


@dataclass(frozen=True)
class MTFProfile:
    name: str
    base_timeframe: str
    context_timeframes: tuple[str, ...]
    feature_sets: tuple[str, ...]
    forward_fill_context: bool = True
    max_context_age_bars: int = 5
    strict_no_lookahead: bool = True
    enabled: bool = True
    notes: str = ""


SUPPORTED_FEATURE_SETS = {
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
}

_MTF_PROFILES = {
    "daily_swing": MTFProfile(
        name="daily_swing",
        base_timeframe="1d",
        context_timeframes=("4h", "1d", "1wk"),
        feature_sets=(
            "momentum",
            "trend",
            "volatility",
            "mean_reversion",
            "price_action",
            "divergence",
        ),
        notes="Günlük swing analiz için ana profil.",
    ),
    "four_hour_swing": MTFProfile(
        name="four_hour_swing",
        base_timeframe="4h",
        context_timeframes=("1h", "4h", "1d"),
        feature_sets=(
            "momentum",
            "trend",
            "volatility",
            "mean_reversion",
            "price_action",
        ),
        notes="4h tabanlı daha aktif swing analiz.",
    ),
    "weekly_context": MTFProfile(
        name="weekly_context",
        base_timeframe="1d",
        context_timeframes=("1d", "1wk"),
        feature_sets=("trend", "volatility", "mean_reversion"),
        notes="Üst zaman dilimi makro/swing bağlamı.",
    ),
    "intraday_light_mtf": MTFProfile(
        name="intraday_light_mtf",
        base_timeframe="1h",
        context_timeframes=("1h", "4h", "1d"),
        feature_sets=("momentum", "trend", "volatility", "price_action"),
        enabled=False,
        notes="Daha sık veri gerektirir; ücretsiz veri sınırları açısından dikkatli kullanılmalı.",
    ),
}


def get_mtf_profile(name: str) -> MTFProfile:
    if name not in _MTF_PROFILES:
        raise ConfigError(f"Unknown MTF profile: {name}")
    return _MTF_PROFILES[name]


def list_mtf_profiles(enabled_only: bool = True) -> list[MTFProfile]:
    if enabled_only:
        return [p for p in _MTF_PROFILES.values() if p.enabled]
    return list(_MTF_PROFILES.values())


def get_default_mtf_profile() -> MTFProfile:
    return _MTF_PROFILES["daily_swing"]


def validate_mtf_feature_sets(feature_sets: tuple[str, ...]) -> None:
    for fset in feature_sets:
        if fset not in SUPPORTED_FEATURE_SETS:
            raise ConfigError(
                f"Validation failed: Unsupported feature set '{fset}' in MTF profile"
            )


def validate_mtf_profiles() -> None:
    for name, profile in _MTF_PROFILES.items():
        if not profile.base_timeframe:
            raise ConfigError(
                f"Validation failed: Missing base_timeframe for MTF profile: {name}"
            )
        if not profile.context_timeframes:
            raise ConfigError(
                f"Validation failed: Missing context_timeframes for MTF profile: {name}"
            )
        validate_mtf_feature_sets(profile.feature_sets)
