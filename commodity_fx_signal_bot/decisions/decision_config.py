from dataclasses import dataclass, field
from typing import Dict, List, Tuple


class ConfigError(Exception):
    pass


@dataclass(frozen=True)
class DecisionProfile:
    name: str
    description: str
    candidate_types: Tuple[str, ...]
    component_weights: Dict[str, float]
    min_signal_score: float = 0.45
    min_confidence: float = 0.50
    min_quality: float = 0.50
    max_conflict: float = 0.65
    min_strategy_readiness: float = 0.45
    neutral_zone_threshold: float = 0.15
    require_regime_confirmation: bool = True
    require_mtf_confirmation: bool = True
    allow_macro_override: bool = False
    enabled: bool = True
    notes: str = ""


def normalize_decision_weights(weights: Dict[str, float]) -> Dict[str, float]:
    total = sum(weights.values())
    if total == 0:
        return {k: 1.0 / len(weights) for k in weights}
    return {k: v / total for k, v in weights.items()}


_PROFILES = {
    "balanced_directional_decision": DecisionProfile(
        name="balanced_directional_decision",
        description="Dengeli yönsel ön karar profili.",
        candidate_types=(
            "trend_following",
            "mean_reversion",
            "breakout",
            "pullback",
            "divergence",
        ),
        component_weights=normalize_decision_weights(
            {
                "signal_score": 0.20,
                "directional_consensus": 0.20,
                "regime_confirmation": 0.15,
                "mtf_confirmation": 0.15,
                "macro_context": 0.05,
                "asset_profile_fit": 0.10,
                "quality_score": 0.10,
                "risk_precheck": 0.05,
            }
        ),
        notes="Dengeli yönsel ön karar profili.",
    ),
    "trend_following_directional_decision": DecisionProfile(
        name="trend_following_directional_decision",
        description="Trend, momentum, MTF, regime ve asset profile fit ağırlıkları daha yüksek.",
        candidate_types=("trend_following", "pullback"),
        component_weights=normalize_decision_weights(
            {
                "signal_score": 0.15,
                "directional_consensus": 0.15,
                "regime_confirmation": 0.20,
                "mtf_confirmation": 0.20,
                "macro_context": 0.05,
                "asset_profile_fit": 0.15,
                "quality_score": 0.05,
                "risk_precheck": 0.05,
            }
        ),
        notes="Trend following odaklı profil.",
    ),
    "mean_reversion_directional_decision": DecisionProfile(
        name="mean_reversion_directional_decision",
        description="Mean reversion odaklı profil.",
        candidate_types=("mean_reversion", "divergence"),
        component_weights=normalize_decision_weights(
            {
                "signal_score": 0.25,
                "directional_consensus": 0.10,
                "regime_confirmation": 0.20,
                "mtf_confirmation": 0.10,
                "macro_context": 0.05,
                "asset_profile_fit": 0.10,
                "quality_score": 0.10,
                "risk_precheck": 0.10,
            }
        ),
        notes="Mean reversion, volatility, range regime odaklı.",
    ),
    "breakout_directional_decision": DecisionProfile(
        name="breakout_directional_decision",
        description="Breakout odaklı profil.",
        candidate_types=("breakout",),
        component_weights=normalize_decision_weights(
            {
                "signal_score": 0.25,
                "directional_consensus": 0.20,
                "regime_confirmation": 0.15,
                "mtf_confirmation": 0.10,
                "macro_context": 0.05,
                "asset_profile_fit": 0.15,
                "quality_score": 0.05,
                "risk_precheck": 0.05,
            }
        ),
        notes="Breakout candidate ayrıştırmasına odaklanır.",
    ),
    "conservative_directional_decision": DecisionProfile(
        name="conservative_directional_decision",
        description="Muhafazakar profil.",
        candidate_types=(
            "trend_following",
            "mean_reversion",
            "breakout",
            "pullback",
            "divergence",
        ),
        component_weights=normalize_decision_weights(
            {
                "signal_score": 0.20,
                "directional_consensus": 0.20,
                "regime_confirmation": 0.15,
                "mtf_confirmation": 0.15,
                "macro_context": 0.05,
                "asset_profile_fit": 0.10,
                "quality_score": 0.10,
                "risk_precheck": 0.05,
            }
        ),
        min_confidence=0.60,
        min_quality=0.60,
        max_conflict=0.50,
        min_strategy_readiness=0.60,
        notes="Daha yüksek min_confidence, min_quality ve min_strategy_readiness ister.",
    ),
}


def get_decision_profile(name: str) -> DecisionProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown decision profile: {name}")
    return _PROFILES[name]


def list_decision_profiles(enabled_only: bool = True) -> List[DecisionProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())


def validate_decision_profiles() -> None:
    for name, profile in _PROFILES.items():
        if not profile.candidate_types:
            raise ConfigError(f"Profile {name} has no candidate_types")
        for threshold in [
            profile.min_signal_score,
            profile.min_confidence,
            profile.min_quality,
            profile.max_conflict,
            profile.min_strategy_readiness,
            profile.neutral_zone_threshold,
        ]:
            if not 0.0 <= threshold <= 1.0:
                raise ConfigError(f"Profile {name} has threshold out of bounds [0,1]")


def get_default_decision_profile() -> DecisionProfile:
    from config.settings import settings

    return get_decision_profile(settings.default_decision_profile)
