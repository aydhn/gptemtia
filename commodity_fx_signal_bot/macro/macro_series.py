import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class MacroSeriesSpec:
    code: str
    name: str
    source: str
    frequency: str
    currency: str = ""
    unit: str = ""
    transform: str = "level"
    enabled: bool = True
    aliases: tuple[str, ...] = ()
    notes: str = ""


_MACRO_SERIES = [
    MacroSeriesSpec(
        code="TR_CPI",
        name="Türkiye TÜFE / CPI",
        source="evds",
        frequency="monthly",
        currency="TRY",
        unit="index",
        notes="EVDS üzerinden resmi seri kodu yapılandırılmalıdır. Kod scraping yapmamalıdır.",
    ),
    MacroSeriesSpec(
        code="US_CPI",
        name="ABD CPI",
        source="fred",
        frequency="monthly",
        currency="USD",
        unit="index",
        aliases=("CPIAUCSL",),
        notes="FRED CPI serisi için kullanılabilir.",
    ),
    MacroSeriesSpec(
        code="USDTRY",
        name="USDTRY",
        source="yahoo",
        frequency="daily",
        currency="TRY",
        unit="fx_rate",
        aliases=("USDTRY=X",),
    ),
    MacroSeriesSpec(
        code="GOLD_USD",
        name="Gold Futures",
        source="yahoo",
        frequency="daily",
        currency="USD",
        unit="price",
        aliases=("GC=F",),
    ),
    MacroSeriesSpec(
        code="OIL_WTI",
        name="WTI Crude Oil",
        source="yahoo",
        frequency="daily",
        currency="USD",
        unit="price",
        aliases=("CL=F",),
    ),
]

_SERIES_MAP = {s.code: s for s in _MACRO_SERIES}


def get_macro_series_spec(code: str) -> MacroSeriesSpec:
    if code not in _SERIES_MAP:
        raise ValueError(f"Unknown macro series: {code}")
    return _SERIES_MAP[code]


def list_macro_series(enabled_only: bool = True) -> list[MacroSeriesSpec]:
    if enabled_only:
        return [s for s in _MACRO_SERIES if s.enabled]
    return list(_MACRO_SERIES)


def validate_macro_series_specs() -> None:
    valid_sources = {"evds", "fred", "yahoo", "synthetic"}
    valid_frequencies = {"daily", "weekly", "monthly", "quarterly", "yearly"}
    seen_codes = set()

    for s in _MACRO_SERIES:
        if not s.code:
            raise ValueError("Macro series must have a code")
        if s.code in seen_codes:
            raise ValueError(f"Duplicate macro series code: {s.code}")
        seen_codes.add(s.code)

        if s.source not in valid_sources:
            raise ValueError(f"Invalid source '{s.source}' for series {s.code}")
        if s.frequency not in valid_frequencies:
            raise ValueError(f"Invalid frequency '{s.frequency}' for series {s.code}")


def get_macro_series_by_source(source: str) -> list[MacroSeriesSpec]:
    return [s for s in _MACRO_SERIES if s.source == source and s.enabled]
