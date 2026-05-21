from dataclasses import dataclass
from typing import List

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class PortfolioRegimeProfile:
    name: str
    description: str
    min_symbols: int = 3
    min_observations: int = 180
    volatility_window: int = 20
    trend_window: int = 50
    correlation_window: int = 60
    drawdown_cluster_threshold: float = -0.05
    stress_window_min_bars: int = 20
    stress_window_max_bars: int = 90
    tail_quantile: float = 0.05
    scenario_shock_small: float = 0.03
    scenario_shock_medium: float = 0.07
    scenario_shock_large: float = 0.12
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_REGIME_PROFILES = {
    "balanced_regime_portfolio_research": PortfolioRegimeProfile(
        name="balanced_regime_portfolio_research",
        description="Balanced regime portfolio research profile",
        min_symbols=3,
        min_observations=180,
        volatility_window=20,
        trend_window=50,
        correlation_window=60,
        drawdown_cluster_threshold=-0.05,
        stress_window_min_bars=20,
        stress_window_max_bars=90,
        tail_quantile=0.05,
        notes="Genel amaçlı rejim bazlı portföy ve stres testi araştırma profili."
    ),
    "conservative_regime_portfolio_research": PortfolioRegimeProfile(
        name="conservative_regime_portfolio_research",
        description="Conservative regime portfolio research profile",
        min_symbols=5,
        min_observations=252,
        volatility_window=30,
        trend_window=100,
        correlation_window=90,
        drawdown_cluster_threshold=-0.04,
        stress_window_min_bars=30,
        stress_window_max_bars=120,
        tail_quantile=0.03,
        min_quality_score=0.55,
        notes="Daha fazla veri ve daha sıkı risk rejimi varsayımları kullanan profil."
    ),
    "crisis_stress_research": PortfolioRegimeProfile(
        name="crisis_stress_research",
        description="Crisis stress research profile",
        drawdown_cluster_threshold=-0.08,
        stress_window_min_bars=20,
        stress_window_max_bars=180,
        scenario_shock_small=0.05,
        scenario_shock_medium=0.10,
        scenario_shock_large=0.20,
        tail_quantile=0.01,
        notes="Daha sert stres ve kriz penceresi araştırmaları için."
    ),
    "short_window_regime_research": PortfolioRegimeProfile(
        name="short_window_regime_research",
        description="Short window regime research profile",
        min_observations=90,
        volatility_window=10,
        trend_window=30,
        correlation_window=30,
        stress_window_min_bars=10,
        stress_window_max_bars=45,
        notes="Daha kısa veri geçmişi olan evrenlerde debug/araştırma için."
    )
}

def get_portfolio_regime_profile(name: str) -> PortfolioRegimeProfile:
    if name not in _REGIME_PROFILES:
        raise ConfigError(f"Unknown portfolio regime profile: {name}")
    return _REGIME_PROFILES[name]

def list_portfolio_regime_profiles(enabled_only: bool = True) -> List[PortfolioRegimeProfile]:
    if enabled_only:
        return [p for p in _REGIME_PROFILES.values() if p.enabled]
    return list(_REGIME_PROFILES.values())

def validate_portfolio_regime_profiles() -> None:
    for name, profile in _REGIME_PROFILES.items():
        if profile.min_symbols <= 0:
            raise ValueError(f"Profile {name}: min_symbols must be positive")
        if profile.min_observations <= 0:
            raise ValueError(f"Profile {name}: min_observations must be positive")
        if profile.volatility_window <= 0 or profile.trend_window <= 0 or profile.correlation_window <= 0:
            raise ValueError(f"Profile {name}: window values must be positive")
        if profile.stress_window_max_bars < profile.stress_window_min_bars:
            raise ValueError(f"Profile {name}: stress_window_max_bars must be >= stress_window_min_bars")
        if not (0 <= profile.tail_quantile <= 0.5):
            raise ValueError(f"Profile {name}: tail_quantile must be between 0 and 0.5")
        if profile.scenario_shock_small <= 0 or profile.scenario_shock_medium <= 0 or profile.scenario_shock_large <= 0:
            raise ValueError(f"Profile {name}: scenario shock values must be positive")
        if not (0 <= profile.min_quality_score <= 1.0):
            raise ValueError(f"Profile {name}: min_quality_score must be between 0 and 1")

def get_default_portfolio_regime_profile() -> PortfolioRegimeProfile:
    from config.settings import settings
    return get_portfolio_regime_profile(settings.default_portfolio_regime_profile)
