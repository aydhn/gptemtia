from dataclasses import dataclass
from core.exceptions import ConfigError

@dataclass(frozen=True)
class PaperTradingProfile:
    name: str
    description: str
    initial_equity: float
    base_currency: str = "TRY"
    max_open_positions: int = 5
    max_open_positions_per_symbol: int = 1
    allow_overlapping_positions: bool = False
    allow_short_bias_simulation: bool = True
    require_risk_approval_candidate: bool = True
    require_sizing_approved_candidate: bool = True
    require_level_approved_candidate: bool = True
    allow_watchlist_candidates: bool = False
    default_order_expiry_bars: int = 3
    max_holding_bars: int = 20
    fee_bps: float = 5.0
    slippage_bps: float = 5.0
    use_next_bar_open_for_fill: bool = True
    allow_same_bar_exit: bool = False
    mark_to_market_enabled: bool = True
    enabled: bool = True
    notes: str = ""

_PAPER_TRADING_PROFILES = {
    "balanced_virtual_paper": PaperTradingProfile(
        name="balanced_virtual_paper",
        description="Genel amaçlı sanal paper trading simülasyon profili.",
        initial_equity=100000.0,
        max_open_positions=5,
        max_open_positions_per_symbol=1,
        allow_overlapping_positions=False,
        fee_bps=5.0,
        slippage_bps=5.0,
        max_holding_bars=20,
        notes="Genel amaçlı sanal paper trading simülasyon profili."
    ),
    "conservative_virtual_paper": PaperTradingProfile(
        name="conservative_virtual_paper",
        description="Daha temkinli sanal portföy ve maliyet varsayımları.",
        initial_equity=100000.0,
        max_open_positions=3,
        max_open_positions_per_symbol=1,
        allow_watchlist_candidates=False,
        fee_bps=8.0,
        slippage_bps=10.0,
        max_holding_bars=15,
        notes="Daha temkinli sanal portföy ve maliyet varsayımları."
    ),
    "research_virtual_paper": PaperTradingProfile(
        name="research_virtual_paper",
        description="Araştırma ve debug için daha gevşek sanal simülasyon profili.",
        initial_equity=100000.0,
        require_risk_approval_candidate=False,
        require_sizing_approved_candidate=False,
        require_level_approved_candidate=False,
        allow_watchlist_candidates=True,
        max_open_positions=10,
        notes="Araştırma ve debug için daha gevşek sanal simülasyon profili."
    ),
    "no_cost_virtual_paper": PaperTradingProfile(
        name="no_cost_virtual_paper",
        description="Maliyet etkisini ayrıştırmak için sanal maliyetsiz profil.",
        initial_equity=100000.0,
        fee_bps=0.0,
        slippage_bps=0.0,
        notes="Maliyet etkisini ayrıştırmak için sanal maliyetsiz profil."
    )
}

def get_paper_trading_profile(name: str) -> PaperTradingProfile:
    profile = _PAPER_TRADING_PROFILES.get(name)
    if not profile:
        raise ConfigError(f"Bilinmeyen profile: {name}")
    return profile

def list_paper_trading_profiles(enabled_only: bool = True) -> list[PaperTradingProfile]:
    if enabled_only:
        return [p for p in _PAPER_TRADING_PROFILES.values() if p.enabled]
    return list(_PAPER_TRADING_PROFILES.values())

def get_default_paper_trading_profile() -> PaperTradingProfile:
    return get_paper_trading_profile("balanced_virtual_paper")

def validate_paper_trading_profiles() -> None:
    for name, profile in _PAPER_TRADING_PROFILES.items():
        if profile.initial_equity <= 0:
            raise ConfigError(f"Profile {name} initial equity must be positive.")
        if profile.max_open_positions <= 0:
            raise ConfigError(f"Profile {name} max_open_positions must be positive.")
        if profile.fee_bps < 0 or profile.slippage_bps < 0:
            raise ConfigError(f"Profile {name} fee and slippage cannot be negative.")
        if profile.default_order_expiry_bars <= 0 or profile.max_holding_bars <= 0:
            raise ConfigError(f"Profile {name} expiry and holding bars must be positive.")
