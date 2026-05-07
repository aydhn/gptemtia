from dataclasses import dataclass


class ConfigError(Exception):
    pass


@dataclass(frozen=True)
class BacktestProfile:
    name: str
    description: str
    initial_equity: float
    base_currency: str
    entry_delay_bars: int = 1
    exit_delay_bars: int = 1
    use_next_bar_open_for_entry: bool = True
    use_next_bar_open_for_exit: bool = True
    allow_same_bar_exit: bool = False
    include_transaction_costs: bool = True
    fee_bps: float = 5.0
    slippage_bps: float = 5.0
    max_holding_bars: int = 20
    single_position_per_symbol: bool = True
    block_overlapping_positions: bool = True
    require_level_candidate: bool = True
    require_sizing_candidate: bool = True
    enabled: bool = True
    notes: str = ""


_PROFILES: dict[str, BacktestProfile] = {
    "balanced_candidate_backtest": BacktestProfile(
        name="balanced_candidate_backtest",
        description="Balanced backtest configuration",
        initial_equity=100000.0,
        base_currency="TRY",
        entry_delay_bars=1,
        exit_delay_bars=1,
        use_next_bar_open_for_entry=True,
        use_next_bar_open_for_exit=True,
        allow_same_bar_exit=False,
        fee_bps=5.0,
        slippage_bps=5.0,
        max_holding_bars=20,
        notes="Genel amaçlı aday lifecycle backtest profili.",
    ),
    "conservative_candidate_backtest": BacktestProfile(
        name="conservative_candidate_backtest",
        description="Conservative backtest configuration",
        initial_equity=100000.0,
        base_currency="TRY",
        fee_bps=8.0,
        slippage_bps=10.0,
        max_holding_bars=15,
        require_level_candidate=True,
        require_sizing_candidate=True,
        notes="Daha yüksek maliyet ve daha sıkı simülasyon varsayımları.",
    ),
    "fast_swing_candidate_backtest": BacktestProfile(
        name="fast_swing_candidate_backtest",
        description="Fast swing backtest configuration",
        initial_equity=100000.0,
        base_currency="TRY",
        max_holding_bars=10,
        fee_bps=5.0,
        slippage_bps=8.0,
        notes="Daha kısa vadeli swing adayları için.",
    ),
    "wide_swing_candidate_backtest": BacktestProfile(
        name="wide_swing_candidate_backtest",
        description="Wide swing backtest configuration",
        initial_equity=100000.0,
        base_currency="TRY",
        max_holding_bars=40,
        allow_same_bar_exit=False,
        notes="Daha geniş stop/target ve uzun tutma süresi varsayımı.",
    ),
    "no_cost_debug_backtest": BacktestProfile(
        name="no_cost_debug_backtest",
        description="Debug backtest configuration",
        initial_equity=100000.0,
        base_currency="TRY",
        include_transaction_costs=False,
        fee_bps=0.0,
        slippage_bps=0.0,
        notes="Sadece debug ve karşılaştırma için maliyetsiz simülasyon.",
    ),
}


def get_backtest_profile(name: str) -> BacktestProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown backtest profile: {name}")
    return _PROFILES[name]


def list_backtest_profiles(enabled_only: bool = True) -> list[BacktestProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())


def validate_backtest_profiles() -> None:
    for name, profile in _PROFILES.items():
        if profile.initial_equity <= 0:
            raise ConfigError(f"Profile {name} initial_equity must be positive")
        if profile.entry_delay_bars < 0 or profile.exit_delay_bars < 0:
            raise ConfigError(f"Profile {name} delay bars must be non-negative")
        if profile.fee_bps < 0 or profile.slippage_bps < 0:
            raise ConfigError(f"Profile {name} fee and slippage must be non-negative")
        if profile.max_holding_bars <= 0:
            raise ConfigError(f"Profile {name} max_holding_bars must be positive")


def get_default_backtest_profile() -> BacktestProfile:
    from config.settings import settings

    return get_backtest_profile(settings.default_backtest_profile)
