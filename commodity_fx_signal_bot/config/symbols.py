"""
Symbol universe definition and management.
"""

from dataclasses import dataclass
from typing import List, Dict, Tuple


@dataclass(frozen=True)
class SymbolSpec:
    """Specification for a trading symbol in the universe."""

    symbol: str
    name: str
    asset_class: str
    sub_class: str
    currency: str
    data_source: str = "yahoo"
    aliases: tuple[str, ...] = ()
    enabled: bool = True
    priority: int = 1
    exchange: str = ""
    contract_type: str = ""
    point_value: float | None = None
    tick_size: float | None = None
    typical_session: str = ""
    quote_currency: str = "USD"
    base_currency: str = ""
    region: str = "global"
    liquidity_tier: int = 2
    analysis_enabled: bool = True
    paper_trade_enabled: bool = True
    benchmark_enabled: bool = False
    tags: tuple[str, ...] = ()
    min_recommended_interval: str = "1d"
    preferred_timeframes: tuple[str, ...] = ()
    excluded_timeframes: tuple[str, ...] = ()
    notes: str = ""


# Default symbol universe
DEFAULT_SYMBOL_UNIVERSE: List[SymbolSpec] = [
    # 1. Precious and Industrial Metals
    SymbolSpec("GC=F", "Gold", "metals", "precious", "USD", notes="Gold Futures"),
    SymbolSpec(
        "MGC=F", "Micro Gold", "metals", "precious", "USD", notes="Micro Gold Futures"
    ),
    SymbolSpec("SI=F", "Silver", "metals", "precious", "USD", notes="Silver Futures"),
    SymbolSpec(
        "SIL=F",
        "Micro Silver",
        "metals",
        "precious",
        "USD",
        notes="Micro Silver Futures",
    ),
    SymbolSpec("HG=F", "Copper", "metals", "industrial", "USD", notes="Copper Futures"),
    SymbolSpec(
        "PL=F", "Platinum", "metals", "precious", "USD", notes="Platinum Futures"
    ),
    SymbolSpec(
        "PA=F", "Palladium", "metals", "precious", "USD", notes="Palladium Futures"
    ),
    # 2. Energy
    SymbolSpec(
        "CL=F", "WTI Crude Oil", "energy", "oil", "USD", notes="Crude Oil Futures"
    ),
    SymbolSpec(
        "BZ=F", "Brent Crude Oil", "energy", "oil", "USD", notes="Brent Crude Futures"
    ),
    SymbolSpec(
        "NG=F", "Natural Gas", "energy", "gas", "USD", notes="Natural Gas Futures"
    ),
    SymbolSpec(
        "HO=F", "Heating Oil", "energy", "oil", "USD", notes="Heating Oil Futures"
    ),
    SymbolSpec(
        "RB=F",
        "RBOB Gasoline",
        "energy",
        "gasoline",
        "USD",
        notes="RBOB Gasoline Futures",
    ),
    # 3. Agriculture / Grains
    SymbolSpec("ZW=F", "Wheat", "agriculture", "grains", "USD", notes="Wheat Futures"),
    SymbolSpec("ZC=F", "Corn", "agriculture", "grains", "USD", notes="Corn Futures"),
    SymbolSpec(
        "ZS=F", "Soybean", "agriculture", "grains", "USD", notes="Soybean Futures"
    ),
    SymbolSpec(
        "ZL=F",
        "Soybean Oil",
        "agriculture",
        "grains",
        "USD",
        notes="Soybean Oil Futures",
    ),
    SymbolSpec(
        "ZM=F",
        "Soybean Meal",
        "agriculture",
        "grains",
        "USD",
        notes="Soybean Meal Futures",
    ),
    SymbolSpec("ZO=F", "Oat", "agriculture", "grains", "USD", notes="Oat Futures"),
    SymbolSpec(
        "ZR=F", "Rough Rice", "agriculture", "grains", "USD", notes="Rough Rice Futures"
    ),
    # 4. Soft Commodities
    SymbolSpec("KC=F", "Coffee", "softs", "agriculture", "USD", notes="Coffee Futures"),
    SymbolSpec("CC=F", "Cocoa", "softs", "agriculture", "USD", notes="Cocoa Futures"),
    SymbolSpec("SB=F", "Sugar", "softs", "agriculture", "USD", notes="Sugar Futures"),
    SymbolSpec("CT=F", "Cotton", "softs", "agriculture", "USD", notes="Cotton Futures"),
    SymbolSpec(
        "OJ=F",
        "Orange Juice",
        "softs",
        "agriculture",
        "USD",
        notes="Orange Juice Futures",
    ),
    # 5. Livestock
    SymbolSpec(
        "LE=F", "Live Cattle", "livestock", "cattle", "USD", notes="Live Cattle Futures"
    ),
    SymbolSpec(
        "GF=F",
        "Feeder Cattle",
        "livestock",
        "cattle",
        "USD",
        notes="Feeder Cattle Futures",
    ),
    SymbolSpec(
        "HE=F", "Lean Hogs", "livestock", "hogs", "USD", notes="Lean Hogs Futures"
    ),
    # 6. Forex — TL Based
    SymbolSpec("USDTRY=X", "USD/TRY", "forex_try", "cross", "TRY"),
    SymbolSpec("EURTRY=X", "EUR/TRY", "forex_try", "cross", "TRY"),
    SymbolSpec("GBPTRY=X", "GBP/TRY", "forex_try", "cross", "TRY"),
    SymbolSpec("JPYTRY=X", "JPY/TRY", "forex_try", "cross", "TRY"),
    SymbolSpec("CHFTRY=X", "CHF/TRY", "forex_try", "cross", "TRY"),
    SymbolSpec("AUDTRY=X", "AUD/TRY", "forex_try", "cross", "TRY"),
    SymbolSpec("CADTRY=X", "CAD/TRY", "forex_try", "cross", "TRY"),
    SymbolSpec("CNHTRY=X", "CNH/TRY", "forex_try", "cross", "TRY", aliases=("CNHY=X",)),
    # 7. Major Forex
    SymbolSpec("EURUSD=X", "EUR/USD", "forex_major", "major", "USD"),
    SymbolSpec("GBPUSD=X", "GBP/USD", "forex_major", "major", "USD"),
    SymbolSpec(
        "JPY=X", "USD/JPY", "forex_major", "major", "JPY", aliases=("USDJPY=X",)
    ),
    SymbolSpec(
        "CHF=X", "USD/CHF", "forex_major", "major", "CHF", aliases=("USDCHF=X",)
    ),
    SymbolSpec("AUDUSD=X", "AUD/USD", "forex_major", "major", "USD"),
    SymbolSpec(
        "CAD=X", "USD/CAD", "forex_major", "major", "CAD", aliases=("USDCAD=X",)
    ),
    SymbolSpec("NZDUSD=X", "NZD/USD", "forex_major", "major", "USD"),
    # 8. Cross Forex
    SymbolSpec("EURGBP=X", "EUR/GBP", "forex_cross", "cross", "GBP"),
    SymbolSpec("EURJPY=X", "EUR/JPY", "forex_cross", "cross", "JPY"),
    SymbolSpec("GBPJPY=X", "GBP/JPY", "forex_cross", "cross", "JPY"),
    SymbolSpec("EURCHF=X", "EUR/CHF", "forex_cross", "cross", "CHF"),
    SymbolSpec("AUDJPY=X", "AUD/JPY", "forex_cross", "cross", "JPY"),
    SymbolSpec("CADJPY=X", "CAD/JPY", "forex_cross", "cross", "JPY"),
    SymbolSpec("CHFJPY=X", "CHF/JPY", "forex_cross", "cross", "JPY"),
    SymbolSpec("NZDJPY=X", "NZD/JPY", "forex_cross", "cross", "JPY"),
    SymbolSpec("EURAUD=X", "EUR/AUD", "forex_cross", "cross", "AUD"),
    SymbolSpec("GBPAUD=X", "GBP/AUD", "forex_cross", "cross", "AUD"),
    # 9. Benchmark & Macro References
    SymbolSpec(
        "USDTRY=X",
        "USD/TRY benchmark",
        "benchmark",
        "currency",
        "TRY",
        data_source="synthetic",
        notes="Sadece USD/TRY tutma benchmark",
        benchmark_enabled=True,
    ),
    SymbolSpec(
        "GC=F",
        "Gold benchmark",
        "benchmark",
        "metals",
        "USD",
        data_source="synthetic",
        notes="Sadece altin tutma benchmark",
        benchmark_enabled=True,
    ),
    SymbolSpec(
        "CASH_TRY",
        "Cash TRY benchmark",
        "benchmark",
        "cash",
        "TRY",
        data_source="synthetic",
        notes="Nakit/sifir getiri benchmark",
        benchmark_enabled=True,
    ),
    SymbolSpec(
        "CASH_USD",
        "Cash USD benchmark",
        "benchmark",
        "cash",
        "USD",
        data_source="synthetic",
        notes="Nakit/sifir getiri benchmark",
        benchmark_enabled=True,
    ),
    SymbolSpec(
        "EQ_COMM_BASKET",
        "Equal Weighted Commodity Basket",
        "benchmark",
        "portfolio",
        "USD",
        data_source="synthetic",
        notes="Esit agirlikli emtia sepeti benchmark",
        benchmark_enabled=True,
    ),
    SymbolSpec(
        "EQ_FX_BASKET",
        "Equal Weighted FX Basket",
        "benchmark",
        "portfolio",
        "TRY",
        data_source="synthetic",
        notes="Esit agirlikli fx sepeti benchmark",
        benchmark_enabled=True,
    ),
    SymbolSpec(
        "MACRO_TR_CPI",
        "Türkiye CPI",
        "macro",
        "inflation",
        "TRY",
        data_source="evds",
        notes="TUIK/EVDS enflasyon verisi",
    ),
    SymbolSpec(
        "MACRO_US_CPI",
        "US CPI",
        "macro",
        "inflation",
        "USD",
        data_source="fred",
        notes="FRED US CPI verisi",
    ),
]


def get_enabled_symbols() -> List[SymbolSpec]:
    """Return a list of all enabled symbols in the universe."""
    return [s for s in DEFAULT_SYMBOL_UNIVERSE if s.enabled]


def get_symbols_by_asset_class(asset_class: str) -> List[SymbolSpec]:
    """Return all enabled symbols belonging to a specific asset class."""
    return [
        s for s in DEFAULT_SYMBOL_UNIVERSE if s.enabled and s.asset_class == asset_class
    ]


def get_symbol_map() -> Dict[str, SymbolSpec]:
    """
    Return a mapping from symbol string to SymbolSpec for all enabled symbols.
    Includes aliases mapping to the primary SymbolSpec.
    """
    mapping = {}
    for spec in get_enabled_symbols():
        mapping[spec.symbol] = spec
        for alias in spec.aliases:
            if alias not in mapping:
                mapping[alias] = spec
    return mapping


def get_analysis_symbols() -> List[SymbolSpec]:
    return [s for s in DEFAULT_SYMBOL_UNIVERSE if s.analysis_enabled and s.enabled]


def get_paper_trade_symbols() -> List[SymbolSpec]:
    return [s for s in DEFAULT_SYMBOL_UNIVERSE if s.paper_trade_enabled and s.enabled]


def get_benchmark_symbols() -> List[SymbolSpec]:
    return [s for s in DEFAULT_SYMBOL_UNIVERSE if s.benchmark_enabled and s.enabled]


def get_symbols_by_data_source(data_source: str) -> List[SymbolSpec]:
    return [
        s for s in DEFAULT_SYMBOL_UNIVERSE if s.data_source == data_source and s.enabled
    ]


def group_symbols_by_asset_class() -> Dict[str, List[SymbolSpec]]:
    groups = {}
    for spec in get_enabled_symbols():
        if spec.asset_class not in groups:
            groups[spec.asset_class] = []
        groups[spec.asset_class].append(spec)
    return groups


def summarize_universe() -> dict:
    total = len(DEFAULT_SYMBOL_UNIVERSE)
    enabled = sum(1 for s in DEFAULT_SYMBOL_UNIVERSE if s.enabled)
    analysis = sum(
        1 for s in DEFAULT_SYMBOL_UNIVERSE if s.analysis_enabled and s.enabled
    )
    paper_trade = sum(
        1 for s in DEFAULT_SYMBOL_UNIVERSE if s.paper_trade_enabled and s.enabled
    )
    benchmark = sum(
        1 for s in DEFAULT_SYMBOL_UNIVERSE if s.benchmark_enabled and s.enabled
    )

    by_asset_class = {}
    by_data_source = {}
    by_liquidity_tier = {}

    for s in DEFAULT_SYMBOL_UNIVERSE:
        if s.enabled:
            by_asset_class[s.asset_class] = by_asset_class.get(s.asset_class, 0) + 1
            by_data_source[s.data_source] = by_data_source.get(s.data_source, 0) + 1
            by_liquidity_tier[s.liquidity_tier] = (
                by_liquidity_tier.get(s.liquidity_tier, 0) + 1
            )

    return {
        "total": total,
        "enabled": enabled,
        "analysis_enabled": analysis,
        "paper_trade_enabled": paper_trade,
        "benchmark_enabled": benchmark,
        "by_asset_class": by_asset_class,
        "by_data_source": by_data_source,
        "by_liquidity_tier": by_liquidity_tier,
    }


def validate_symbol_universe() -> Tuple[bool, List[str]]:
    """
    Validate the default symbol universe.
    Checks for:
    - Empty symbols
    - Duplicate symbols
    - Duplicate aliases mapping to different symbols
    - Asset classes, Data sources, and more

    Returns:
        (is_valid, list_of_errors)
    """
    errors = []
    seen_symbols = set()

    if not DEFAULT_SYMBOL_UNIVERSE:
        return False, ["Universe is empty."]

    VALID_DATA_SOURCES = {"yahoo", "evds", "fred", "synthetic"}
    VALID_ASSET_CLASSES = {
        "metals",
        "energy",
        "agriculture",
        "softs",
        "livestock",
        "forex_try",
        "forex_major",
        "forex_cross",
        "benchmark",
        "macro",
    }

    for spec in DEFAULT_SYMBOL_UNIVERSE:
        if not spec.symbol:
            errors.append(f"Empty symbol found in universe. Name: {spec.name}")
            continue

        if not spec.name:
            errors.append(f"Empty name found for symbol: {spec.symbol}")

        if not spec.asset_class:
            errors.append(f"Empty asset_class found for symbol: {spec.symbol}")

        if not spec.sub_class:
            errors.append(f"Empty sub_class found for symbol: {spec.symbol}")

        if not spec.data_source:
            errors.append(f"Empty data_source found for symbol: {spec.symbol}")

        if not isinstance(spec.priority, int) or spec.priority <= 0:
            errors.append(
                f"Priority must be a positive integer for symbol: {spec.symbol}"
            )

        if spec.liquidity_tier not in (1, 2, 3):
            errors.append(
                f"liquidity_tier must be 1, 2, or 3 for symbol: {spec.symbol}"
            )

        if not isinstance(spec.enabled, bool):
            errors.append(f"enabled must be a boolean for symbol: {spec.symbol}")

        if not isinstance(spec.analysis_enabled, bool):
            errors.append(
                f"analysis_enabled must be a boolean for symbol: {spec.symbol}"
            )

        if not isinstance(spec.aliases, tuple):
            errors.append(f"aliases must be a tuple for symbol: {spec.symbol}")

        if not isinstance(spec.tags, tuple):
            errors.append(f"tags must be a tuple for symbol: {spec.symbol}")

        if spec.data_source not in VALID_DATA_SOURCES:
            errors.append(
                f"Invalid data_source '{spec.data_source}' for symbol: {spec.symbol}"
            )

        if spec.asset_class not in VALID_ASSET_CLASSES:
            errors.append(
                f"Invalid asset_class '{spec.asset_class}' for symbol: {spec.symbol}"
            )

        if spec.symbol in seen_symbols:
            # allow duplicate benchmark if it's synthetic
            if not (
                spec.asset_class == "benchmark" and spec.data_source == "synthetic"
            ):
                errors.append(f"Duplicate active primary symbol found: {spec.symbol}")
        else:
            seen_symbols.add(spec.symbol)

        # Check aliases
        for alias in spec.aliases:
            if alias in seen_symbols and alias != spec.symbol:
                errors.append(
                    f"Alias {alias} for {spec.symbol} is already defined as a symbol"
                )
            seen_symbols.add(alias)

    return len(errors) == 0, errors


def get_symbol_spec(symbol: str) -> SymbolSpec | None:
    """Get the SymbolSpec for a given symbol or alias."""
    mapping = get_symbol_map()
    return mapping.get(symbol)


def get_all_candidate_symbols(spec: SymbolSpec) -> list[str]:
    """Get all candidate symbols to try fetching, primary first, then aliases."""
    candidates = [spec.symbol]
    candidates.extend(spec.aliases)
    return candidates


def get_default_timeframes_for_asset_class(asset_class: str) -> tuple[str, ...]:
    defaults = {
        "metals": ("4h", "1d", "1wk"),
        "energy": ("4h", "1d", "1wk"),
        "agriculture": ("1d", "1wk"),
        "softs": ("1d", "1wk"),
        "livestock": ("1d", "1wk"),
        "forex_try": ("1h", "4h", "1d"),
        "forex_major": ("1h", "4h", "1d"),
        "forex_cross": ("1h", "4h", "1d"),
        "benchmark": ("1d", "1wk"),
        "macro": ("1mo",),
    }
    return defaults.get(asset_class, ("1d",))


def get_allowed_timeframes_for_symbol(spec: SymbolSpec) -> tuple[str, ...]:
    if spec.preferred_timeframes:
        tfs = list(spec.preferred_timeframes)
    else:
        tfs = list(get_default_timeframes_for_asset_class(spec.asset_class))

    # Remove excluded
    if spec.excluded_timeframes:
        tfs = [tf for tf in tfs if tf not in spec.excluded_timeframes]

    return tuple(tfs)
