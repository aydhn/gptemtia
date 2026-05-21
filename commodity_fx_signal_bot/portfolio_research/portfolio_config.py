from dataclasses import dataclass
from core.exceptions import ConfigError

@dataclass(frozen=True)
class PortfolioResearchProfile:
    name: str
    description: str
    return_method: str = "log"
    min_symbols: int = 3
    min_observations: int = 120
    correlation_window: int = 60
    max_basket_symbols: int = 10
    equal_weight_enabled: bool = True
    score_weight_enabled: bool = True
    risk_weight_enabled: bool = True
    paper_weight_enabled: bool = True
    max_single_symbol_weight: float = 0.25
    max_asset_class_weight: float = 0.50
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_portfolio_research": PortfolioResearchProfile(
        name="balanced_portfolio_research",
        description="Genel amaçlı portföy araştırması ve sanal sepet analizi profili.",
        return_method="log",
        min_symbols=3,
        min_observations=120,
        correlation_window=60,
        max_basket_symbols=10,
        max_single_symbol_weight=0.25,
        max_asset_class_weight=0.50,
        notes="Genel amaçlı portföy araştırması ve sanal sepet analizi profili."
    ),
    "conservative_portfolio_research": PortfolioResearchProfile(
        name="conservative_portfolio_research",
        description="Daha fazla gözlem ve daha düşük konsantrasyon isteyen profil.",
        min_symbols=5,
        min_observations=252,
        correlation_window=90,
        max_basket_symbols=8,
        max_single_symbol_weight=0.20,
        max_asset_class_weight=0.40,
        min_quality_score=0.55,
        notes="Daha fazla gözlem ve daha düşük konsantrasyon isteyen profil."
    ),
    "metals_basket_research": PortfolioResearchProfile(
        name="metals_basket_research",
        description="Değerli metaller odağında sanal basket araştırması.",
        min_symbols=3,
        max_basket_symbols=5,
        max_asset_class_weight=1.00,
        notes="Değerli metaller odağında sanal basket araştırması."
    ),
    "fx_try_basket_research": PortfolioResearchProfile(
        name="fx_try_basket_research",
        description="TL bazlı döviz evreni için sanal basket araştırması.",
        min_symbols=3,
        max_basket_symbols=6,
        max_asset_class_weight=1.00,
        notes="TL bazlı döviz evreni için sanal basket araştırması."
    ),
}

def get_portfolio_research_profile(name: str) -> PortfolioResearchProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown portfolio research profile: {name}")
    return _PROFILES[name]

def list_portfolio_research_profiles(enabled_only: bool = True) -> list[PortfolioResearchProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_portfolio_research_profiles() -> None:
    for name, profile in _PROFILES.items():
        if profile.return_method not in ["log", "simple"]:
            raise ConfigError(f"Invalid return_method in profile '{name}': {profile.return_method}")
        if profile.min_symbols <= 0:
            raise ConfigError(f"min_symbols must be positive in profile '{name}'")
        if profile.min_observations <= 0:
            raise ConfigError(f"min_observations must be positive in profile '{name}'")
        if profile.correlation_window <= 0:
            raise ConfigError(f"correlation_window must be positive in profile '{name}'")
        if profile.max_basket_symbols <= 0:
            raise ConfigError(f"max_basket_symbols must be positive in profile '{name}'")
        if not (0.0 <= profile.max_single_symbol_weight <= 1.0):
            raise ConfigError(f"max_single_symbol_weight must be between 0 and 1 in profile '{name}'")
        if not (0.0 <= profile.max_asset_class_weight <= 1.0):
            raise ConfigError(f"max_asset_class_weight must be between 0 and 1 in profile '{name}'")

def get_default_portfolio_research_profile() -> PortfolioResearchProfile:
    return _PROFILES["balanced_portfolio_research"]
