from dataclasses import dataclass, field


class ConfigError(Exception):
    pass


@dataclass(frozen=True)
class RiskPrecheckProfile:
    name: str
    description: str
    enabled_risk_components: tuple[str, ...]
    component_weights: dict[str, float]
    max_total_pretrade_risk: float = 0.70
    min_readiness_score: float = 0.45
    max_volatility_risk: float = 0.75
    max_gap_risk: float = 0.75
    max_liquidity_risk: float = 0.75
    max_data_quality_risk: float = 0.60
    max_regime_risk: float = 0.70
    max_mtf_risk: float = 0.70
    max_macro_risk: float = 0.80
    block_on_invalid_data_quality: bool = True
    block_on_extreme_volatility: bool = True
    block_on_high_conflict: bool = True
    allow_watchlist_when_borderline: bool = True
    enabled: bool = True
    notes: str = ""


_PROFILES = {
    "balanced_pretrade_risk": RiskPrecheckProfile(
        name="balanced_pretrade_risk",
        description="Balanced pre-trade risk profile",
        enabled_risk_components=(
            "volatility",
            "gap",
            "liquidity",
            "data_quality",
            "regime",
            "mtf",
            "macro",
            "asset_profile",
            "conflict",
        ),
        component_weights={
            "volatility": 0.18,
            "gap": 0.10,
            "liquidity": 0.10,
            "data_quality": 0.15,
            "regime": 0.12,
            "mtf": 0.12,
            "macro": 0.08,
            "asset_profile": 0.10,
            "conflict": 0.15,
        },
    )
}


def get_risk_precheck_profile(name: str) -> RiskPrecheckProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown risk profile: {name}")
    return _PROFILES[name]


def list_risk_precheck_profiles(enabled_only: bool = True) -> list[RiskPrecheckProfile]:
    return [p for p in _PROFILES.values() if not enabled_only or p.enabled]


def validate_risk_precheck_profiles() -> None:
    for name, profile in _PROFILES.items():
        if not profile.enabled_risk_components:
            raise ConfigError(f"Profile {name} has no enabled risk components")
        if not profile.component_weights:
            raise ConfigError(f"Profile {name} has no component weights")


def get_default_risk_precheck_profile() -> RiskPrecheckProfile:
    return _PROFILES["balanced_pretrade_risk"]


def normalize_risk_component_weights(weights: dict[str, float]) -> dict[str, float]:
    total = sum(weights.values())
    if total == 0:
        return {k: 1.0 / len(weights) for k in weights}
    return {k: v / total for k, v in weights.items()}
