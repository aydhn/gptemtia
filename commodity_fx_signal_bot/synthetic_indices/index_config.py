from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class SyntheticIndexProfile:
    name: str
    description: str
    base_value: float = 100.0
    return_method: str = "log"
    rebalance_method: str = "static"
    rebalance_frequency: str = "monthly"
    min_symbols: int = 3
    min_observations: int = 120
    max_symbols_per_index: int = 20
    max_single_weight: float = 0.35
    relative_strength_windows: tuple[int, ...] = (20, 60, 120)
    rotation_lookback: int = 60
    rotation_top_n: int = 5
    rotation_bottom_n: int = 5
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_synthetic_index_research": SyntheticIndexProfile(
        name="balanced_synthetic_index_research",
        description="Balanced profile for synthetic index research",
        base_value=100.0,
        return_method="log",
        rebalance_method="static",
        rebalance_frequency="monthly",
        min_symbols=3,
        min_observations=120,
        max_symbols_per_index=20,
        max_single_weight=0.35,
        relative_strength_windows=(20, 60, 120),
        rotation_lookback=60,
        rotation_top_n=5,
        rotation_bottom_n=5,
        notes="Genel amaçlı sentetik benchmark/custom index ve relative strength araştırma profili.",
    ),
    "conservative_synthetic_index_research": SyntheticIndexProfile(
        name="conservative_synthetic_index_research",
        description="Conservative profile for synthetic index research",
        min_symbols=5,
        min_observations=252,
        max_single_weight=0.25,
        relative_strength_windows=(60, 120, 252),
        rotation_lookback=120,
        rotation_top_n=3,
        rotation_bottom_n=3,
        min_quality_score=0.55,
        notes="Daha uzun gözlem ve daha düşük konsantrasyonla sentetik index araştırması.",
    ),
    "short_term_rotation_research": SyntheticIndexProfile(
        name="short_term_rotation_research",
        description="Short term profile for synthetic index research",
        min_observations=90,
        relative_strength_windows=(10, 20, 60),
        rotation_lookback=20,
        rotation_top_n=5,
        rotation_bottom_n=5,
        notes="Kısa dönem relative strength ve rotation araştırması.",
    ),
    "commodity_fx_composite_research": SyntheticIndexProfile(
        name="commodity_fx_composite_research",
        description="Commodity and FX composite profile for synthetic index research",
        max_symbols_per_index=30,
        max_single_weight=0.20,
        notes="Emtia + TL bazlı FX karma composite index araştırması.",
    ),
}

def get_synthetic_index_profile(name: str) -> SyntheticIndexProfile:
    if name not in PROFILES:
        raise ConfigError(f"Unknown synthetic index profile: {name}")
    return PROFILES[name]

def list_synthetic_index_profiles(enabled_only: bool = True) -> list[SyntheticIndexProfile]:
    profiles = list(PROFILES.values())
    if enabled_only:
        return [p for p in profiles if p.enabled]
    return profiles

def validate_synthetic_index_profiles() -> None:
    for profile in PROFILES.values():
        if profile.base_value <= 0:
            raise ConfigError(f"Profile {profile.name} has invalid base_value: {profile.base_value}")
        if profile.return_method not in ["simple", "log"]:
            raise ConfigError(f"Profile {profile.name} has invalid return_method: {profile.return_method}")
        if profile.rebalance_method not in ["static", "periodic", "none"]:
            raise ConfigError(f"Profile {profile.name} has invalid rebalance_method: {profile.rebalance_method}")
        if profile.min_symbols <= 0:
            raise ConfigError(f"Profile {profile.name} has invalid min_symbols: {profile.min_symbols}")
        if profile.min_observations <= 0:
            raise ConfigError(f"Profile {profile.name} has invalid min_observations: {profile.min_observations}")
        if not 0 < profile.max_single_weight <= 1:
            raise ConfigError(f"Profile {profile.name} has invalid max_single_weight: {profile.max_single_weight}")
        if not all(isinstance(w, int) and w > 0 for w in profile.relative_strength_windows):
            raise ConfigError(f"Profile {profile.name} has invalid relative_strength_windows: {profile.relative_strength_windows}")
        if profile.rotation_top_n <= 0:
            raise ConfigError(f"Profile {profile.name} has invalid rotation_top_n: {profile.rotation_top_n}")
        if profile.rotation_bottom_n <= 0:
            raise ConfigError(f"Profile {profile.name} has invalid rotation_bottom_n: {profile.rotation_bottom_n}")

def get_default_synthetic_index_profile() -> SyntheticIndexProfile:
    return PROFILES["balanced_synthetic_index_research"]
