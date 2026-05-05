"""
Configuration and definitions for asset class behavioral profiles.
"""

from dataclasses import dataclass


class ConfigError(Exception):
    """Custom exception for configuration errors."""

    pass


@dataclass(frozen=True)
class AssetProfile:
    """Behavioral profile definition for an asset class."""

    asset_class: str
    name: str
    description: str
    preferred_timeframes: tuple[str, ...]
    core_feature_sets: tuple[str, ...]
    macro_sensitivity: str = "medium"
    volume_reliability: str = "medium"
    typical_volatility: str = "medium"
    liquidity_profile: str = "medium"
    gap_risk: str = "medium"
    seasonality_risk: str = "low"
    trend_following_suitability: str = "medium"
    mean_reversion_suitability: str = "medium"
    breakout_suitability: str = "medium"
    notes: str = ""


# Predefined Asset Profiles
_ASSET_PROFILES = {
    "metals": AssetProfile(
        asset_class="metals",
        name="Metals",
        description="Precious and industrial metals.",
        preferred_timeframes=("4h", "1d", "1wk"),
        core_feature_sets=(
            "trend",
            "momentum",
            "volatility",
            "mean_reversion",
            "macro",
            "regime",
        ),
        macro_sensitivity="high",
        volume_reliability="medium",
        gap_risk="medium",
        trend_following_suitability="high",
        mean_reversion_suitability="medium",
        breakout_suitability="medium",
        notes="Altın/gümüş gibi metaller USD, enflasyon, reel getiri ve risk algısına duyarlı olabilir.",
    ),
    "energy": AssetProfile(
        asset_class="energy",
        name="Energy",
        description="Energy commodities like oil and gas.",
        preferred_timeframes=("1d", "1wk"),
        core_feature_sets=(
            "trend",
            "momentum",
            "volatility",
            "mean_reversion",
            "regime",
        ),
        macro_sensitivity="high",
        typical_volatility="high",
        volume_reliability="medium",
        gap_risk="high",
        breakout_suitability="high",
        notes="Petrol/doğalgaz enerji haberlerine, arz-talep şoklarına ve volatilite genişlemesine hassastır.",
    ),
    "agriculture": AssetProfile(
        asset_class="agriculture",
        name="Agriculture",
        description="Agricultural products.",
        preferred_timeframes=("1d", "1wk"),
        core_feature_sets=(
            "trend",
            "momentum",
            "volatility",
            "mean_reversion",
            "regime",
        ),
        macro_sensitivity="medium",
        typical_volatility="medium",
        volume_reliability="medium",
        liquidity_profile="medium",
        seasonality_risk="high",
        notes="Tahıl ürünleri mevsimsellik, hava durumu ve arz şoklarına duyarlı olabilir.",
    ),
    "softs": AssetProfile(
        asset_class="softs",
        name="Soft Commodities",
        description="Soft commodities like coffee, cocoa, sugar.",
        preferred_timeframes=("1d", "1wk"),
        core_feature_sets=(
            "trend",
            "momentum",
            "volatility",
            "mean_reversion",
            "regime",
        ),
        macro_sensitivity="medium",
        typical_volatility="high",
        volume_reliability="medium",
        liquidity_profile="medium",
        seasonality_risk="high",
        notes="Kahve, kakao, şeker, pamuk gibi soft ürünlerde mevsimsellik ve arz şokları önemlidir.",
    ),
    "livestock": AssetProfile(
        asset_class="livestock",
        name="Livestock",
        description="Livestock futures.",
        preferred_timeframes=("1d", "1wk"),
        core_feature_sets=(
            "trend",
            "momentum",
            "volatility",
            "mean_reversion",
            "regime",
        ),
        macro_sensitivity="low",
        typical_volatility="medium",
        volume_reliability="medium",
        liquidity_profile="medium",
        seasonality_risk="medium",
        notes="Hayvancılık kontratlarında veri/likidite ve seans davranışları dikkatle ele alınmalıdır.",
    ),
    "forex_try": AssetProfile(
        asset_class="forex_try",
        name="TRY Forex",
        description="Turkish Lira based forex pairs.",
        preferred_timeframes=("1h", "4h", "1d"),
        core_feature_sets=("trend", "momentum", "volatility", "macro", "regime"),
        macro_sensitivity="very_high",
        volume_reliability="low",
        typical_volatility="high",
        liquidity_profile="medium",
        gap_risk="medium",
        trend_following_suitability="high",
        notes="TL bazlı döviz çiftleri yerel enflasyon, USDTRY trendi ve makro baskıya duyarlıdır.",
    ),
    "forex_major": AssetProfile(
        asset_class="forex_major",
        name="Major Forex",
        description="Major global currency pairs.",
        preferred_timeframes=("1h", "4h", "1d"),
        core_feature_sets=(
            "trend",
            "momentum",
            "volatility",
            "mean_reversion",
            "macro",
            "regime",
        ),
        macro_sensitivity="high",
        volume_reliability="low",
        typical_volatility="medium",
        liquidity_profile="high",
        gap_risk="low",
        notes="Majör forex çiftlerinde volume verisi sınırlı güvenilirliktedir.",
    ),
    "forex_cross": AssetProfile(
        asset_class="forex_cross",
        name="Cross Forex",
        description="Cross currency pairs.",
        preferred_timeframes=("1h", "4h", "1d"),
        core_feature_sets=(
            "trend",
            "momentum",
            "volatility",
            "mean_reversion",
            "regime",
        ),
        macro_sensitivity="high",
        volume_reliability="low",
        typical_volatility="medium",
        liquidity_profile="medium",
        gap_risk="low",
        notes="Çapraz forex çiftlerinde spread/likidite ve makro farklar önemlidir.",
    ),
    "benchmark": AssetProfile(
        asset_class="benchmark",
        name="Benchmark",
        description="Benchmark indices and assets.",
        preferred_timeframes=("1d", "1wk"),
        core_feature_sets=("benchmarks", "macro"),
        notes="Benchmark sembolleri trade edilebilir sinyal değil kıyaslama/bağlam içindir.",
    ),
}


def get_asset_profile(asset_class: str) -> AssetProfile:
    """Retrieve the asset profile for a given asset class."""
    if asset_class not in _ASSET_PROFILES:
        raise ConfigError(f"Unknown asset class: {asset_class}")
    return _ASSET_PROFILES[asset_class]


def list_asset_profiles() -> list[AssetProfile]:
    """List all available asset profiles."""
    return list(_ASSET_PROFILES.values())


def validate_asset_profiles() -> None:
    """Validate all asset profiles."""
    valid_macro_sensitivities = {"low", "medium", "high", "very_high"}
    valid_volume_reliabilities = {"low", "medium", "high"}

    for profile in _ASSET_PROFILES.values():
        if not profile.core_feature_sets:
            raise ConfigError(
                f"Asset profile {profile.asset_class} has empty core_feature_sets."
            )
        if profile.macro_sensitivity not in valid_macro_sensitivities:
            raise ConfigError(
                f"Invalid macro_sensitivity '{profile.macro_sensitivity}' in {profile.asset_class}"
            )
        if profile.volume_reliability not in valid_volume_reliabilities:
            raise ConfigError(
                f"Invalid volume_reliability '{profile.volume_reliability}' in {profile.asset_class}"
            )


def summarize_asset_profiles() -> dict:
    """Provide a summary of all asset profiles."""
    return {
        name: {
            "name": p.name,
            "core_features": p.core_feature_sets,
            "macro_sensitivity": p.macro_sensitivity,
            "volume_reliability": p.volume_reliability,
        }
        for name, p in _ASSET_PROFILES.items()
    }
