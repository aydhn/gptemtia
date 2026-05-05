from dataclasses import dataclass, field
import logging

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class SignalScoringProfile:
    name: str
    description: str
    enabled_event_groups: tuple[str, ...]
    component_weights: dict[str, float]
    min_candidate_score: float = 0.40
    min_quality_score: float = 0.50
    min_context_score: float = 0.40
    max_conflict_score: float = 0.70
    event_lookback_bars: int = 5
    decay_half_life_bars: int = 3
    use_regime_filter: bool = True
    use_mtf_filter: bool = True
    use_macro_filter: bool = True
    use_asset_profile_filter: bool = True
    enabled: bool = True
    notes: str = ""


def normalize_component_weights(weights: dict[str, float]) -> dict[str, float]:
    total = sum(weights.values())
    if total <= 0:
        logger.warning("Component weights sum to <= 0, returning equal weights")
        count = len(weights)
        return {k: 1.0 / count for k in weights}
    return {k: v / total for k, v in weights.items()}


_PROFILES = {
    "balanced_candidate_scoring": SignalScoringProfile(
        name="balanced_candidate_scoring",
        description="Dengeli genel aday skorlama profili.",
        enabled_event_groups=(
            "momentum",
            "trend",
            "volatility",
            "volume",
            "mean_reversion",
            "price_action",
            "divergence",
            "mtf",
            "regime",
            "macro",
            "asset_profile",
        ),
        component_weights=normalize_component_weights(
            {
                "event_strength": 0.20,
                "category_confluence": 0.15,
                "trend_context": 0.15,
                "regime_context": 0.15,
                "mtf_context": 0.15,
                "macro_context": 0.05,
                "asset_profile_context": 0.05,
                "data_quality": 0.10,
            }
        ),
        notes="Dengeli genel aday skorlama profili.",
    ),
    "trend_following_candidate_scoring": SignalScoringProfile(
        name="trend_following_candidate_scoring",
        description="Trend takip setup adaylarını öne çıkarır.",
        enabled_event_groups=(
            "momentum",
            "trend",
            "volatility",
            "volume",
            "mean_reversion",
            "price_action",
            "divergence",
            "mtf",
            "regime",
            "macro",
            "asset_profile",
        ),
        component_weights=normalize_component_weights(
            {
                "event_strength": 0.15,
                "category_confluence": 0.10,
                "trend_context": 0.25,
                "regime_context": 0.20,
                "mtf_context": 0.15,
                "macro_context": 0.05,
                "asset_profile_context": 0.05,
                "data_quality": 0.05,
            }
        ),
        notes="Trend takip setup adaylarını öne çıkarır.",
    ),
    "mean_reversion_candidate_scoring": SignalScoringProfile(
        name="mean_reversion_candidate_scoring",
        description="Mean reversion dostu rejimleri öne çıkarır.",
        enabled_event_groups=(
            "momentum",
            "trend",
            "volatility",
            "volume",
            "mean_reversion",
            "price_action",
            "divergence",
            "mtf",
            "regime",
            "macro",
            "asset_profile",
        ),
        component_weights=normalize_component_weights(
            {
                "event_strength": 0.20,
                "category_confluence": 0.10,
                "trend_context": 0.05,
                "regime_context": 0.25,
                "mtf_context": 0.10,
                "macro_context": 0.05,
                "asset_profile_context": 0.05,
                "data_quality": 0.20,
            }
        ),
        notes="Mean reversion dostu rejimleri öne çıkarır.",
    ),
    "breakout_candidate_scoring": SignalScoringProfile(
        name="breakout_candidate_scoring",
        description="Sıkışma + expansion + breakout context adaylarını öne çıkarır.",
        enabled_event_groups=(
            "momentum",
            "trend",
            "volatility",
            "volume",
            "mean_reversion",
            "price_action",
            "divergence",
            "mtf",
            "regime",
            "macro",
            "asset_profile",
        ),
        component_weights=normalize_component_weights(
            {
                "event_strength": 0.25,
                "category_confluence": 0.15,
                "trend_context": 0.15,
                "regime_context": 0.10,
                "mtf_context": 0.10,
                "macro_context": 0.05,
                "asset_profile_context": 0.10,
                "data_quality": 0.10,
            }
        ),
        notes="Sıkışma + expansion + breakout context adaylarını öne çıkarır.",
    ),
    "macro_sensitive_candidate_scoring": SignalScoringProfile(
        name="macro_sensitive_candidate_scoring",
        description="Macro ve asset profile bağlamı daha yüksek ağırlıklı.",
        enabled_event_groups=(
            "momentum",
            "trend",
            "volatility",
            "volume",
            "mean_reversion",
            "price_action",
            "divergence",
            "mtf",
            "regime",
            "macro",
            "asset_profile",
        ),
        component_weights=normalize_component_weights(
            {
                "event_strength": 0.10,
                "category_confluence": 0.10,
                "trend_context": 0.15,
                "regime_context": 0.15,
                "mtf_context": 0.10,
                "macro_context": 0.20,
                "asset_profile_context": 0.15,
                "data_quality": 0.05,
            }
        ),
        notes="Özellikle metals ve forex_try tarafı için uygundur.",
    ),
}


def get_signal_scoring_profile(name: str) -> SignalScoringProfile:
    if name not in _PROFILES:
        raise ValueError(f"Unknown signal scoring profile: {name}")
    return _PROFILES[name]


def list_signal_scoring_profiles(
    enabled_only: bool = True,
) -> list[SignalScoringProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())


def validate_signal_scoring_profiles() -> None:
    from signals.signal_taxonomy import list_supported_event_groups

    supported_groups = set(list_supported_event_groups())

    for name, profile in _PROFILES.items():
        if not profile.enabled_event_groups:
            raise ValueError(f"Profile {name} has no enabled event groups.")
        for group in profile.enabled_event_groups:
            if group not in supported_groups:
                raise ValueError(f"Profile {name} has unknown event group: {group}")
        if not (0.0 <= profile.min_candidate_score <= 1.0):
            raise ValueError(f"Profile {name} min_candidate_score out of range.")
        if not (0.0 <= profile.min_quality_score <= 1.0):
            raise ValueError(f"Profile {name} min_quality_score out of range.")


def get_default_signal_scoring_profile() -> SignalScoringProfile:
    from config.settings import settings

    return get_signal_scoring_profile(settings.default_signal_profile)
