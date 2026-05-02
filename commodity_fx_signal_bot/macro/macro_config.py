import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class MacroProfile:
    name: str
    description: str
    macro_series: tuple[str, ...]
    benchmark_symbols: tuple[str, ...]
    base_currency: str = "TRY"
    frequency: str = "monthly"
    forward_fill_to_daily: bool = True
    max_staleness_days: int = 45
    enabled: bool = True
    notes: str = ""


_MACRO_PROFILES = [
    MacroProfile(
        name="turkey_inflation_fx",
        description="Türkiye enflasyonu, ABD CPI ve USDTRY merkezli makro bağlam",
        macro_series=("TR_CPI", "US_CPI", "USDTRY"),
        benchmark_symbols=("USDTRY=X", "GC=F", "EQ_COMM_BASKET", "EQ_FX_BASKET"),
        base_currency="TRY",
        frequency="monthly",
        notes="Türkiye enflasyonu, ABD CPI ve USDTRY merkezli makro bağlam.",
    ),
    MacroProfile(
        name="global_commodity_macro",
        description="Emtia odaklı global makro bağlam",
        macro_series=("US_CPI", "USDTRY", "GOLD_USD", "OIL_WTI"),
        benchmark_symbols=("GC=F", "CL=F", "EQ_COMM_BASKET"),
        base_currency="USD",
        frequency="monthly",
        notes="Emtia odaklı global makro bağlam.",
    ),
    MacroProfile(
        name="inflation_benchmark",
        description="Performans kıyaslama ve reel getiri analizi",
        macro_series=("TR_CPI", "US_CPI", "USDTRY"),
        benchmark_symbols=("USDTRY=X", "GC=F", "CASH_TRY", "CASH_USD"),
        base_currency="TRY",
        frequency="monthly",
        notes="Performans kıyaslama ve reel getiri analizi.",
    ),
]

_PROFILE_MAP = {p.name: p for p in _MACRO_PROFILES}


def get_macro_profile(name: str) -> MacroProfile:
    if name not in _PROFILE_MAP:
        raise ValueError(f"Unknown macro profile: {name}")
    return _PROFILE_MAP[name]


def list_macro_profiles(enabled_only: bool = True) -> list[MacroProfile]:
    if enabled_only:
        return [p for p in _MACRO_PROFILES if p.enabled]
    return list(_MACRO_PROFILES)


def validate_macro_profiles() -> None:
    for profile in _MACRO_PROFILES:
        if not profile.name:
            raise ValueError("Macro profile must have a name")
        if not profile.macro_series:
            raise ValueError(
                f"Macro profile '{profile.name}' must have at least one macro_series"
            )
        if not profile.benchmark_symbols:
            raise ValueError(
                f"Macro profile '{profile.name}' must have at least one benchmark_symbols"
            )


def get_default_macro_profile() -> MacroProfile:
    from config.settings import settings

    # Normally read from settings but default to turkey_inflation_fx
    try:
        if hasattr(settings, "default_macro_profile"):
            return get_macro_profile(settings.default_macro_profile)
    except Exception:
        pass

    return get_macro_profile("turkey_inflation_fx")
