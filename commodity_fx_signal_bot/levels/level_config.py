from dataclasses import dataclass
from core.exceptions import ConfigError


@dataclass(frozen=True)
class LevelProfile:
    name: str
    description: str
    atr_multipliers: tuple[float, ...]
    target_rr_multipliers: tuple[float, ...]
    min_reward_risk: float = 1.2
    preferred_reward_risk: float = 2.0
    max_stop_distance_pct: float = 0.08
    min_stop_distance_pct: float = 0.002
    min_sizing_readiness_score: float = 0.50
    max_total_pretrade_risk: float = 0.70
    use_atr_levels: bool = True
    use_structure_levels: bool = True
    use_volatility_adjustment: bool = True
    block_on_sizing_rejection: bool = True
    allow_watchlist_when_borderline: bool = True
    enabled: bool = True
    notes: str = ""


_LEVEL_PROFILES = {
    "balanced_theoretical_levels": LevelProfile(
        name="balanced_theoretical_levels",
        description="Genel amaçlı teorik stop/target seviye simülasyon profili.",
        atr_multipliers=(1.0, 1.5, 2.0, 3.0),
        target_rr_multipliers=(1.0, 1.5, 2.0, 3.0),
        min_reward_risk=1.2,
        preferred_reward_risk=2.0,
        max_stop_distance_pct=0.08,
        min_stop_distance_pct=0.002,
        notes="Genel amaçlı teorik stop/target seviye simülasyon profili.",
    ),
    "conservative_theoretical_levels": LevelProfile(
        name="conservative_theoretical_levels",
        description="Daha temkinli teorik stop/target profili.",
        atr_multipliers=(1.0, 1.5, 2.0),
        target_rr_multipliers=(1.5, 2.0, 2.5),
        min_reward_risk=1.5,
        preferred_reward_risk=2.0,
        max_stop_distance_pct=0.05,
        min_sizing_readiness_score=0.60,
        max_total_pretrade_risk=0.55,
        notes="Daha temkinli teorik stop/target profili.",
    ),
    "wide_volatility_levels": LevelProfile(
        name="wide_volatility_levels",
        description="Yüksek volatiliteye uyumlu geniş teorik seviye profili.",
        atr_multipliers=(1.5, 2.0, 3.0, 4.0),
        target_rr_multipliers=(1.5, 2.0, 3.0),
        max_stop_distance_pct=0.12,
        use_volatility_adjustment=True,
        notes="Yüksek volatiliteye uyumlu geniş teorik seviye profili.",
    ),
    "mean_reversion_levels": LevelProfile(
        name="mean_reversion_levels",
        description="Mean reversion adayları için daha yakın teorik hedef/stops.",
        atr_multipliers=(0.8, 1.0, 1.5, 2.0),
        target_rr_multipliers=(1.0, 1.3, 1.5, 2.0),
        min_reward_risk=1.0,
        preferred_reward_risk=1.5,
        notes="Mean reversion adayları için daha yakın teorik hedef/stops.",
    ),
    "breakout_levels": LevelProfile(
        name="breakout_levels",
        description="Breakout adayları için daha geniş hareket varsayımı.",
        atr_multipliers=(1.5, 2.0, 2.5, 3.0),
        target_rr_multipliers=(1.5, 2.0, 3.0, 4.0),
        min_reward_risk=1.5,
        preferred_reward_risk=2.5,
        notes="Breakout adayları için daha geniş hareket varsayımı.",
    ),
}


def get_level_profile(name: str) -> LevelProfile:
    if name not in _LEVEL_PROFILES:
        raise ConfigError(f"Bilinmeyen level profile: {name}")
    return _LEVEL_PROFILES[name]


def list_level_profiles(enabled_only: bool = True) -> list[LevelProfile]:
    if enabled_only:
        return [p for p in _LEVEL_PROFILES.values() if p.enabled]
    return list(_LEVEL_PROFILES.values())


def validate_level_profiles() -> None:
    for name, profile in _LEVEL_PROFILES.items():
        if any(m <= 0 for m in profile.atr_multipliers):
            raise ConfigError(f"[{name}] atr_multipliers pozitif olmali.")
        if any(m <= 0 for m in profile.target_rr_multipliers):
            raise ConfigError(f"[{name}] target_rr_multipliers pozitif olmali.")
        if profile.min_reward_risk <= 0:
            raise ConfigError(f"[{name}] min_reward_risk pozitif olmali.")
        if not (0 <= profile.max_stop_distance_pct <= 1):
            raise ConfigError(f"[{name}] max_stop_distance_pct 0-1 araliginda olmali.")
        if not (0 <= profile.min_stop_distance_pct <= 1):
            raise ConfigError(f"[{name}] min_stop_distance_pct 0-1 araliginda olmali.")
        if profile.max_stop_distance_pct <= profile.min_stop_distance_pct:
            raise ConfigError(
                f"[{name}] max_stop_distance_pct > min_stop_distance_pct olmali."
            )


def get_default_level_profile() -> LevelProfile:
    return get_level_profile("balanced_theoretical_levels")
