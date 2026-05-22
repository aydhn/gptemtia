import logging
from config.symbols import SymbolSpec

logger = logging.getLogger(__name__)

def filter_symbols_by_asset_class(specs: list[SymbolSpec], asset_class: str) -> list[SymbolSpec]:
    filtered = [s for s in specs if s.asset_class == asset_class]
    if not filtered:
        logger.warning(f"No symbols found for asset class: {asset_class}")
    return filtered

def build_metals_universe(specs: list[SymbolSpec]) -> list[SymbolSpec]:
    metals_group = ["PRECIOUS_METAL", "INDUSTRIAL_METAL", "METAL"]
    filtered = [s for s in specs if s.sub_class in metals_group]
    if not filtered:
        logger.warning("No symbols found for metals universe.")
    return filtered

def build_energy_universe(specs: list[SymbolSpec]) -> list[SymbolSpec]:
    energy_group = ["ENERGY"]
    filtered = [s for s in specs if s.sub_class in energy_group]
    if not filtered:
        logger.warning("No symbols found for energy universe.")
    return filtered

def build_agriculture_softs_universe(specs: list[SymbolSpec]) -> list[SymbolSpec]:
    agri_group = ["AGRICULTURE", "SOFTS"]
    filtered = [s for s in specs if s.sub_class in agri_group]
    if not filtered:
        logger.warning("No symbols found for agriculture/softs universe.")
    return filtered

def build_fx_try_universe(specs: list[SymbolSpec]) -> list[SymbolSpec]:
    fx_specs = filter_symbols_by_asset_class(specs, "FX")
    filtered = [s for s in fx_specs if "TRY" in s.symbol]
    if not filtered:
        logger.warning("No symbols found for FX TRY universe.")
    return filtered

def build_commodity_universe(specs: list[SymbolSpec]) -> list[SymbolSpec]:
    filtered = filter_symbols_by_asset_class(specs, "COMMODITY")
    if not filtered:
        logger.warning("No symbols found for commodity universe.")
    return filtered

def build_commodity_fx_universe(specs: list[SymbolSpec]) -> list[SymbolSpec]:
    commodity_specs = build_commodity_universe(specs)
    fx_try_specs = build_fx_try_universe(specs)
    filtered = commodity_specs + fx_try_specs
    if not filtered:
        logger.warning("No symbols found for commodity + FX universe.")
    return filtered

def build_index_universe_map(specs: list[SymbolSpec]) -> dict[str, list[SymbolSpec]]:
    return {
        "metals": build_metals_universe(specs),
        "energy": build_energy_universe(specs),
        "agriculture_softs": build_agriculture_softs_universe(specs),
        "fx_try": build_fx_try_universe(specs),
        "commodity": build_commodity_universe(specs),
        "commodity_fx": build_commodity_fx_universe(specs),
    }
