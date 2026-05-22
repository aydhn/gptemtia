from dataclasses import dataclass

@dataclass(frozen=True)
class FactorResearchProfile:
    name: str
    description: str
    return_method: str = "log"
    min_symbols: int = 5
    min_observations: int = 180
    forward_return_horizon: int = 20
    rank_top_quantile: float = 0.30
    rank_bottom_quantile: float = 0.30
    trend_windows: tuple[int, ...] = (20, 60, 120)
    momentum_windows: tuple[int, ...] = (20, 60, 120)
    volatility_windows: tuple[int, ...] = (20, 60)
    decay_windows: tuple[int, ...] = (5, 10, 20, 60)
    neutralize_asset_class: bool = True
    neutralize_volatility: bool = True
    max_single_symbol_weight: float = 0.20
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_factor_research": FactorResearchProfile(
        name="balanced_factor_research",
        description="Genel amaçlı cross-sectional factor research profili.",
        return_method="log",
        min_symbols=5,
        min_observations=180,
        forward_return_horizon=20,
        rank_top_quantile=0.30,
        rank_bottom_quantile=0.30,
        trend_windows=(20, 60, 120),
        momentum_windows=(20, 60, 120),
        volatility_windows=(20, 60),
        decay_windows=(5, 10, 20, 60),
        neutralize_asset_class=True,
        neutralize_volatility=True,
        max_single_symbol_weight=0.20,
        min_quality_score=0.40,
        notes="Genel amaçlı cross-sectional factor research profili."
    ),
    "conservative_factor_research": FactorResearchProfile(
        name="conservative_factor_research",
        description="Daha uzun veri ve daha sıkı faktör araştırması profili.",
        min_symbols=8,
        min_observations=252,
        forward_return_horizon=20,
        rank_top_quantile=0.25,
        rank_bottom_quantile=0.25,
        trend_windows=(60, 120, 252),
        momentum_windows=(60, 120, 252),
        volatility_windows=(60, 120),
        decay_windows=(20, 60, 120),
        max_single_symbol_weight=0.15,
        min_quality_score=0.55,
        notes="Daha uzun veri ve daha sıkı faktör araştırması profili."
    ),
    "short_term_factor_research": FactorResearchProfile(
        name="short_term_factor_research",
        description="Kısa dönem faktör ayrıştırması ve rotasyon araştırması için.",
        min_symbols=5,
        min_observations=90,
        forward_return_horizon=10,
        trend_windows=(10, 20, 60),
        momentum_windows=(10, 20, 60),
        volatility_windows=(10, 20),
        decay_windows=(3, 5, 10, 20),
        notes="Kısa dönem faktör ayrıştırması ve rotasyon araştırması için."
    ),
    "macro_sensitive_factor_research": FactorResearchProfile(
        name="macro_sensitive_factor_research",
        description="USDTRY, altın, petrol ve enflasyon proxy duyarlılık faktörlerine odaklanan profil.",
        min_symbols=5,
        forward_return_horizon=20,
        neutralize_asset_class=True,
        neutralize_volatility=True,
        notes="USDTRY, altın, petrol ve enflasyon proxy duyarlılık faktörlerine odaklanan profil."
    )
}

class ConfigError(Exception):
    pass

def get_factor_research_profile(name: str) -> FactorResearchProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Profile {name} not found.")
    return _PROFILES[name]

def list_factor_research_profiles(enabled_only: bool = True) -> list[FactorResearchProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def get_default_factor_research_profile() -> FactorResearchProfile:
    from config.settings import settings
    return get_factor_research_profile(settings.default_factor_research_profile)

def validate_factor_research_profiles() -> None:
    for profile in _PROFILES.values():
        if profile.return_method not in ("simple", "log"):
            raise ValueError("return_method must be simple or log")
        if profile.min_symbols <= 0:
            raise ValueError("min_symbols must be positive")
        if profile.min_observations <= 0:
            raise ValueError("min_observations must be positive")
        if profile.forward_return_horizon <= 0:
            raise ValueError("forward_return_horizon must be positive")
        if not (0.0 < profile.rank_top_quantile < 0.5):
            raise ValueError("rank_top_quantile must be between 0 and 0.5")
        if not (0.0 < profile.rank_bottom_quantile < 0.5):
            raise ValueError("rank_bottom_quantile must be between 0 and 0.5")
        if not all(isinstance(w, int) and w > 0 for w in profile.trend_windows):
            raise ValueError("trend_windows must be positive integer tuple")
        if not all(isinstance(w, int) and w > 0 for w in profile.momentum_windows):
            raise ValueError("momentum_windows must be positive integer tuple")
        if not all(isinstance(w, int) and w > 0 for w in profile.volatility_windows):
            raise ValueError("volatility_windows must be positive integer tuple")
        if not all(isinstance(w, int) and w > 0 for w in profile.decay_windows):
             raise ValueError("decay_windows must be positive integer tuple")
        if not (0.0 < profile.max_single_symbol_weight <= 1.0):
            raise ValueError("max_single_symbol_weight must be between 0 and 1")
        if not (0.0 <= profile.min_quality_score <= 1.0):
            raise ValueError("min_quality_score must be between 0 and 1")
