from dataclasses import dataclass
from typing import Dict, List, Optional
import os


class ConfigError(Exception):
    pass


@dataclass(frozen=True)
class SizingProfile:
    name: str
    description: str
    theoretical_account_equity: float
    base_currency: str
    risk_per_candidate: float
    max_risk_per_symbol: float
    max_risk_per_asset_class: float
    max_total_portfolio_risk: float
    min_risk_readiness_score: float = 0.50
    max_total_pretrade_risk: float = 0.70
    min_data_quality_score: float = 0.50
    use_atr_based_unit: bool = True
    use_volatility_adjustment: bool = True
    block_on_risk_rejection: bool = True
    allow_watchlist_for_borderline: bool = True
    enabled: bool = True
    notes: str = ""

    def __post_init__(self):
        if self.theoretical_account_equity <= 0:
            raise ConfigError("theoretical_account_equity must be strictly positive.")


_DEFAULT_SIZING_PROFILES: Dict[str, SizingProfile] = {
    "balanced_theoretical_sizing": SizingProfile(
        name="balanced_theoretical_sizing",
        description="Balanced theoretical position sizing",
        theoretical_account_equity=100000.0,
        base_currency="TRY",
        risk_per_candidate=0.005,
        max_risk_per_symbol=0.02,
        max_risk_per_asset_class=0.05,
        max_total_portfolio_risk=0.15,
        notes="Genel amaçlı teorik sizing simülasyon profili.",
    ),
    "conservative_theoretical_sizing": SizingProfile(
        name="conservative_theoretical_sizing",
        description="Conservative theoretical position sizing",
        theoretical_account_equity=100000.0,
        base_currency="TRY",
        risk_per_candidate=0.0025,
        max_risk_per_symbol=0.01,
        max_risk_per_asset_class=0.03,
        max_total_portfolio_risk=0.08,
        min_risk_readiness_score=0.60,
        max_total_pretrade_risk=0.55,
        notes="Daha temkinli teorik risk bütçesi.",
    ),
    "volatility_scaled_sizing": SizingProfile(
        name="volatility_scaled_sizing",
        description="Volatility scaled theoretical position sizing",
        theoretical_account_equity=100000.0,
        base_currency="TRY",
        risk_per_candidate=0.004,
        max_risk_per_symbol=0.02,
        max_risk_per_asset_class=0.05,
        max_total_portfolio_risk=0.15,
        use_atr_based_unit=True,
        use_volatility_adjustment=True,
        notes="Volatiliteye duyarlı teorik sizing.",
    ),
    "forex_try_sizing": SizingProfile(
        name="forex_try_sizing",
        description="Forex theoretical position sizing",
        theoretical_account_equity=100000.0,
        base_currency="TRY",
        risk_per_candidate=0.003,
        max_risk_per_symbol=0.015,
        max_risk_per_asset_class=0.04,
        max_total_portfolio_risk=0.10,
        notes="TL bazlı forex çiftleri için daha temkinli teorik sizing.",
    ),
    "metals_sizing": SizingProfile(
        name="metals_sizing",
        description="Metals theoretical position sizing",
        theoretical_account_equity=100000.0,
        base_currency="TRY",
        risk_per_candidate=0.004,
        max_risk_per_symbol=0.02,
        max_risk_per_asset_class=0.05,
        max_total_portfolio_risk=0.15,
        notes="Metaller için makro/volatilite duyarlı teorik sizing.",
    ),
}


def get_sizing_profile(name: str) -> SizingProfile:
    """Returns a sizing profile by name. Raises ConfigError if not found."""
    if name not in _DEFAULT_SIZING_PROFILES:
        raise ConfigError(f"Sizing profile '{name}' not found.")
    return _DEFAULT_SIZING_PROFILES[name]


def list_sizing_profiles(enabled_only: bool = True) -> List[SizingProfile]:
    """Lists available sizing profiles."""
    profiles = list(_DEFAULT_SIZING_PROFILES.values())
    if enabled_only:
        profiles = [p for p in profiles if p.enabled]
    return profiles


def validate_sizing_profiles() -> None:
    """Validates all sizing profiles."""
    for p in _DEFAULT_SIZING_PROFILES.values():
        if p.theoretical_account_equity <= 0:
            raise ConfigError(
                f"theoretical_account_equity must be positive for profile {p.name}"
            )
        for attr in [
            "risk_per_candidate",
            "max_risk_per_symbol",
            "max_risk_per_asset_class",
            "max_total_portfolio_risk",
        ]:
            val = getattr(p, attr)
            if not (0 <= val <= 1.0):
                raise ConfigError(
                    f"{attr} must be between 0 and 1 for profile {p.name}, got {val}"
                )


def get_default_sizing_profile() -> SizingProfile:
    """Gets the default sizing profile defined in settings."""
    profile_name = os.getenv("DEFAULT_SIZING_PROFILE", "balanced_theoretical_sizing")
    return get_sizing_profile(profile_name)
