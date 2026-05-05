import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


class ConfigError(Exception):
    pass


@dataclass(frozen=True)
class StrategySelectionProfile:
    name: str
    description: str
    enabled_strategy_families: tuple[str, ...]
    family_weights: dict[str, float]
    component_weights: dict[str, float]
    min_selection_score: float = 0.45
    min_fit_score: float = 0.45
    min_decision_confidence: float = 0.50
    min_decision_quality: float = 0.50
    max_conflict_score: float = 0.65
    allow_no_trade_family: bool = True
    allow_watchlist_family: bool = True
    enabled: bool = True
    notes: str = ""


def normalize_strategy_weights(weights: dict[str, float]) -> dict[str, float]:
    total = sum(weights.values())
    if total == 0:
        return {k: 0.0 for k in weights}
    return {k: v / total for k, v in weights.items()}


_PROFILES = {
    "balanced_strategy_selection": StrategySelectionProfile(
        name="balanced_strategy_selection",
        description="Dengeli strateji seçimi.",
        enabled_strategy_families=(
            "trend_following",
            "mean_reversion",
            "breakout",
            "pullback",
            "divergence_reversal",
            "momentum_continuation",
            "range_reversion",
            "no_trade",
            "watchlist",
        ),
        family_weights={
            "trend_following": 1.0,
            "mean_reversion": 1.0,
            "breakout": 1.0,
            "pullback": 1.0,
            "divergence_reversal": 1.0,
            "momentum_continuation": 1.0,
            "range_reversion": 1.0,
            "no_trade": 1.0,
            "watchlist": 1.0,
        },
        component_weights={
            "decision_score": 0.20,
            "decision_confidence": 0.15,
            "decision_quality": 0.15,
            "regime_fit": 0.15,
            "mtf_fit": 0.10,
            "asset_profile_fit": 0.10,
            "macro_fit": 0.05,
            "conflict_penalty": 0.10,
        },
        notes="Dengeli strateji ailesi seçici profil.",
    )
}


def get_strategy_selection_profile(name: str) -> StrategySelectionProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown strategy selection profile: {name}")
    return _PROFILES[name]


def list_strategy_selection_profiles(
    enabled_only: bool = True,
) -> list[StrategySelectionProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())


def validate_strategy_selection_profiles() -> None:
    for name, profile in _PROFILES.items():
        if not profile.enabled_strategy_families:
            raise ConfigError(f"Profile {name} has no enabled_strategy_families")


def get_default_strategy_selection_profile() -> StrategySelectionProfile:
    from config.settings import settings

    return get_strategy_selection_profile(settings.default_strategy_profile)
