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
    notes: str = ""


# Default symbol universe
DEFAULT_SYMBOL_UNIVERSE: List[SymbolSpec] = [
    # 1. Precious and Industrial Metals
    SymbolSpec("GC=F", "Gold", "Metals", "Precious", "USD", notes="Gold Futures"),
    SymbolSpec("MGC=F", "Micro Gold", "Metals", "Precious", "USD", notes="Micro Gold Futures"),
    SymbolSpec("SI=F", "Silver", "Metals", "Precious", "USD", notes="Silver Futures"),
    SymbolSpec("SIL=F", "Micro Silver", "Metals", "Precious", "USD", notes="Micro Silver Futures"),
    SymbolSpec("HG=F", "Copper", "Metals", "Industrial", "USD", notes="Copper Futures"),
    SymbolSpec("PL=F", "Platinum", "Metals", "Precious", "USD", notes="Platinum Futures"),
    SymbolSpec("PA=F", "Palladium", "Metals", "Precious", "USD", notes="Palladium Futures"),

    # 2. Energy
    SymbolSpec("CL=F", "WTI Crude Oil", "Energy", "Oil", "USD", notes="Crude Oil Futures"),
    SymbolSpec("BZ=F", "Brent Crude Oil", "Energy", "Oil", "USD", notes="Brent Crude Futures"),
    SymbolSpec("NG=F", "Natural Gas", "Energy", "Gas", "USD", notes="Natural Gas Futures"),
    SymbolSpec("HO=F", "Heating Oil", "Energy", "Oil", "USD", notes="Heating Oil Futures"),
    SymbolSpec("RB=F", "RBOB Gasoline", "Energy", "Gasoline", "USD", notes="RBOB Gasoline Futures"),

    # 3. Agriculture / Grains
    SymbolSpec("ZW=F", "Wheat", "Agriculture", "Grains", "USD", notes="Wheat Futures"),
    SymbolSpec("ZC=F", "Corn", "Agriculture", "Grains", "USD", notes="Corn Futures"),
    SymbolSpec("ZS=F", "Soybean", "Agriculture", "Grains", "USD", notes="Soybean Futures"),
    SymbolSpec("ZL=F", "Soybean Oil", "Agriculture", "Grains", "USD", notes="Soybean Oil Futures"),
    SymbolSpec("ZM=F", "Soybean Meal", "Agriculture", "Grains", "USD", notes="Soybean Meal Futures"),
    SymbolSpec("ZO=F", "Oat", "Agriculture", "Grains", "USD", notes="Oat Futures"),
    SymbolSpec("ZR=F", "Rough Rice", "Agriculture", "Grains", "USD", notes="Rough Rice Futures"),

    # 4. Soft Commodities
    SymbolSpec("KC=F", "Coffee", "Agriculture", "Softs", "USD", notes="Coffee Futures"),
    SymbolSpec("CC=F", "Cocoa", "Agriculture", "Softs", "USD", notes="Cocoa Futures"),
    SymbolSpec("SB=F", "Sugar", "Agriculture", "Softs", "USD", notes="Sugar Futures"),
    SymbolSpec("CT=F", "Cotton", "Agriculture", "Softs", "USD", notes="Cotton Futures"),
    SymbolSpec("OJ=F", "Orange Juice", "Agriculture", "Softs", "USD", notes="Orange Juice Futures"),

    # 5. Livestock
    SymbolSpec("LE=F", "Live Cattle", "Livestock", "Cattle", "USD", notes="Live Cattle Futures"),
    SymbolSpec("GF=F", "Feeder Cattle", "Livestock", "Cattle", "USD", notes="Feeder Cattle Futures"),
    SymbolSpec("HE=F", "Lean Hogs", "Livestock", "Hogs", "USD", notes="Lean Hogs Futures"),

    # 6. Forex — TL Based
    SymbolSpec("USDTRY=X", "USD/TRY", "Forex", "TRY_Cross", "TRY"),
    SymbolSpec("EURTRY=X", "EUR/TRY", "Forex", "TRY_Cross", "TRY"),
    SymbolSpec("GBPTRY=X", "GBP/TRY", "Forex", "TRY_Cross", "TRY"),
    SymbolSpec("JPYTRY=X", "JPY/TRY", "Forex", "TRY_Cross", "TRY"),
    SymbolSpec("CHFTRY=X", "CHF/TRY", "Forex", "TRY_Cross", "TRY"),
    SymbolSpec("AUDTRY=X", "AUD/TRY", "Forex", "TRY_Cross", "TRY"),
    SymbolSpec("CADTRY=X", "CAD/TRY", "Forex", "TRY_Cross", "TRY"),
    SymbolSpec("CNHTRY=X", "CNH/TRY", "Forex", "TRY_Cross", "TRY", aliases=("CNHY=X",)),

    # 7. Major Forex
    SymbolSpec("EURUSD=X", "EUR/USD", "Forex", "Major", "USD"),
    SymbolSpec("GBPUSD=X", "GBP/USD", "Forex", "Major", "USD"),
    SymbolSpec("JPY=X", "USD/JPY", "Forex", "Major", "JPY", aliases=("USDJPY=X",)),
    SymbolSpec("CHF=X", "USD/CHF", "Forex", "Major", "CHF", aliases=("USDCHF=X",)),
    SymbolSpec("AUDUSD=X", "AUD/USD", "Forex", "Major", "USD"),
    SymbolSpec("CAD=X", "USD/CAD", "Forex", "Major", "CAD", aliases=("USDCAD=X",)),
    SymbolSpec("NZDUSD=X", "NZD/USD", "Forex", "Major", "USD"),

    # 8. Cross Forex
    SymbolSpec("EURGBP=X", "EUR/GBP", "Forex", "Cross", "GBP"),
    SymbolSpec("EURJPY=X", "EUR/JPY", "Forex", "Cross", "JPY"),
    SymbolSpec("GBPJPY=X", "GBP/JPY", "Forex", "Cross", "JPY"),
    SymbolSpec("EURCHF=X", "EUR/CHF", "Forex", "Cross", "CHF"),
    SymbolSpec("AUDJPY=X", "AUD/JPY", "Forex", "Cross", "JPY"),
    SymbolSpec("CADJPY=X", "CAD/JPY", "Forex", "Cross", "JPY"),

    # 9. Benchmark & Macro References
    SymbolSpec("BENCH_USDTRY", "USD/TRY Benchmark", "Benchmark", "Currency", "TRY", data_source="synthetic", notes="Sadece USD/TRY tutma benchmark"),
    SymbolSpec("BENCH_GOLD", "Gold Benchmark", "Benchmark", "Metals", "USD", data_source="synthetic", notes="Sadece altin tutma benchmark"),
    SymbolSpec("BENCH_CASH", "Cash Benchmark", "Benchmark", "Cash", "TRY", data_source="synthetic", notes="Nakit/sifir getiri benchmark"),
    SymbolSpec("BENCH_EQ_WEIGHT", "Equal Weight Benchmark", "Benchmark", "Portfolio", "TRY", data_source="synthetic", notes="Esit agirlikli sembol sepeti benchmark"),
    SymbolSpec("MACRO_TR_CPI", "Türkiye CPI", "Macro", "Inflation", "TRY", data_source="evds", notes="TUIK/EVDS enflasyon verisi"),
    SymbolSpec("MACRO_US_CPI", "US CPI", "Macro", "Inflation", "USD", data_source="fred", notes="FRED US CPI verisi"),
]


def get_enabled_symbols() -> List[SymbolSpec]:
    """Return a list of all enabled symbols in the universe."""
    return [s for s in DEFAULT_SYMBOL_UNIVERSE if s.enabled]


def get_symbols_by_asset_class(asset_class: str) -> List[SymbolSpec]:
    """Return all enabled symbols belonging to a specific asset class."""
    return [s for s in DEFAULT_SYMBOL_UNIVERSE if s.enabled and s.asset_class == asset_class]


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


def validate_symbol_universe() -> Tuple[bool, List[str]]:
    """
    Validate the default symbol universe.
    Checks for:
    - Empty symbols
    - Duplicate symbols
    - Duplicate aliases mapping to different symbols

    Returns:
        (is_valid, list_of_errors)
    """
    errors = []
    seen_symbols = set()

    for spec in DEFAULT_SYMBOL_UNIVERSE:
        if not spec.symbol:
            errors.append(f"Empty symbol found in universe. Name: {spec.name}")
            continue

        if spec.symbol in seen_symbols:
            errors.append(f"Duplicate symbol found: {spec.symbol}")

        seen_symbols.add(spec.symbol)

        # Check aliases
        for alias in spec.aliases:
            if alias in seen_symbols and alias != spec.symbol:
                errors.append(f"Alias {alias} for {spec.symbol} is already defined as a symbol")
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
