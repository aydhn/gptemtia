import datetime
from config.symbols import SymbolSpec
from synthetic_indices.index_config import SyntheticIndexProfile
from synthetic_indices.index_models import SyntheticIndexDefinition, build_synthetic_index_id
from synthetic_indices.index_universe import (
    build_metals_universe,
    build_energy_universe,
    build_agriculture_softs_universe,
    build_fx_try_universe,
    build_commodity_universe,
    build_commodity_fx_universe
)
from synthetic_indices.weighting_schemes import calculate_equal_weights

def build_metals_composite_definition(specs: list[SymbolSpec], timeframe: str, profile: SyntheticIndexProfile, weighting_scheme: str = "equal_weight") -> SyntheticIndexDefinition:
    universe = build_metals_universe(specs)
    symbols = [s.symbol for s in universe]
    warnings = []

    if len(symbols) < profile.min_symbols:
        warnings.append(f"Metals universe has {len(symbols)} symbols, less than minimum {profile.min_symbols}.")

    weights = calculate_equal_weights(symbols)
    index_id = build_synthetic_index_id("metals_composite_index", timeframe, symbols, weighting_scheme)

    return SyntheticIndexDefinition(
        index_id=index_id,
        index_name="Metals Composite Index (Synthetic)",
        index_type="metals_composite_index",
        timeframe=timeframe,
        symbols=symbols,
        weights=weights,
        weighting_scheme=weighting_scheme,
        base_value=profile.base_value,
        created_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        methodology="Equal weighted synthetic benchmark for metals.",
        warnings=warnings
    )

def build_energy_composite_definition(specs: list[SymbolSpec], timeframe: str, profile: SyntheticIndexProfile, weighting_scheme: str = "equal_weight") -> SyntheticIndexDefinition:
    universe = build_energy_universe(specs)
    symbols = [s.symbol for s in universe]
    warnings = []

    if len(symbols) < profile.min_symbols:
        warnings.append(f"Energy universe has {len(symbols)} symbols, less than minimum {profile.min_symbols}.")

    weights = calculate_equal_weights(symbols)
    index_id = build_synthetic_index_id("energy_composite_index", timeframe, symbols, weighting_scheme)

    return SyntheticIndexDefinition(
        index_id=index_id,
        index_name="Energy Composite Index (Synthetic)",
        index_type="energy_composite_index",
        timeframe=timeframe,
        symbols=symbols,
        weights=weights,
        weighting_scheme=weighting_scheme,
        base_value=profile.base_value,
        created_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        methodology="Equal weighted synthetic benchmark for energy.",
        warnings=warnings
    )

def build_agriculture_softs_composite_definition(specs: list[SymbolSpec], timeframe: str, profile: SyntheticIndexProfile, weighting_scheme: str = "equal_weight") -> SyntheticIndexDefinition:
    universe = build_agriculture_softs_universe(specs)
    symbols = [s.symbol for s in universe]
    warnings = []

    if len(symbols) < profile.min_symbols:
        warnings.append(f"Agriculture/Softs universe has {len(symbols)} symbols, less than minimum {profile.min_symbols}.")

    weights = calculate_equal_weights(symbols)
    index_id = build_synthetic_index_id("agriculture_softs_composite_index", timeframe, symbols, weighting_scheme)

    return SyntheticIndexDefinition(
        index_id=index_id,
        index_name="Agriculture/Softs Composite Index (Synthetic)",
        index_type="agriculture_softs_composite_index",
        timeframe=timeframe,
        symbols=symbols,
        weights=weights,
        weighting_scheme=weighting_scheme,
        base_value=profile.base_value,
        created_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        methodology="Equal weighted synthetic benchmark for agriculture and softs.",
        warnings=warnings
    )

def build_fx_try_composite_definition(specs: list[SymbolSpec], timeframe: str, profile: SyntheticIndexProfile, weighting_scheme: str = "equal_weight") -> SyntheticIndexDefinition:
    universe = build_fx_try_universe(specs)
    symbols = [s.symbol for s in universe]
    warnings = []

    if len(symbols) < profile.min_symbols:
        warnings.append(f"FX TRY universe has {len(symbols)} symbols, less than minimum {profile.min_symbols}.")

    weights = calculate_equal_weights(symbols)
    index_id = build_synthetic_index_id("fx_try_composite_index", timeframe, symbols, weighting_scheme)

    return SyntheticIndexDefinition(
        index_id=index_id,
        index_name="FX TRY Composite Index (Synthetic)",
        index_type="fx_try_composite_index",
        timeframe=timeframe,
        symbols=symbols,
        weights=weights,
        weighting_scheme=weighting_scheme,
        base_value=profile.base_value,
        created_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        methodology="Equal weighted synthetic benchmark for FX TRY pairs.",
        warnings=warnings
    )

def build_commodity_composite_definition(specs: list[SymbolSpec], timeframe: str, profile: SyntheticIndexProfile, weighting_scheme: str = "equal_weight") -> SyntheticIndexDefinition:
    universe = build_commodity_universe(specs)
    symbols = [s.symbol for s in universe]
    warnings = []

    if len(symbols) < profile.min_symbols:
        warnings.append(f"Commodity universe has {len(symbols)} symbols, less than minimum {profile.min_symbols}.")

    weights = calculate_equal_weights(symbols)
    index_id = build_synthetic_index_id("commodity_composite_index", timeframe, symbols, weighting_scheme)

    return SyntheticIndexDefinition(
        index_id=index_id,
        index_name="Commodity Composite Index (Synthetic)",
        index_type="commodity_composite_index",
        timeframe=timeframe,
        symbols=symbols,
        weights=weights,
        weighting_scheme=weighting_scheme,
        base_value=profile.base_value,
        created_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        methodology="Equal weighted synthetic benchmark for broad commodities.",
        warnings=warnings
    )

def build_commodity_fx_composite_definition(specs: list[SymbolSpec], timeframe: str, profile: SyntheticIndexProfile, weighting_scheme: str = "equal_weight") -> SyntheticIndexDefinition:
    universe = build_commodity_fx_universe(specs)
    symbols = [s.symbol for s in universe]
    warnings = []

    if len(symbols) < profile.min_symbols:
        warnings.append(f"Commodity/FX universe has {len(symbols)} symbols, less than minimum {profile.min_symbols}.")

    weights = calculate_equal_weights(symbols)
    index_id = build_synthetic_index_id("commodity_fx_composite_index", timeframe, symbols, weighting_scheme)

    return SyntheticIndexDefinition(
        index_id=index_id,
        index_name="Commodity/FX Composite Index (Synthetic)",
        index_type="commodity_fx_composite_index",
        timeframe=timeframe,
        symbols=symbols,
        weights=weights,
        weighting_scheme=weighting_scheme,
        base_value=profile.base_value,
        created_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        methodology="Equal weighted synthetic benchmark for commodities and FX.",
        warnings=warnings
    )

def build_default_synthetic_benchmark_definitions(specs: list[SymbolSpec], timeframe: str, profile: SyntheticIndexProfile) -> tuple[list[SyntheticIndexDefinition], dict]:
    definitions = []
    summary = {"warnings": [], "definitions_created": 0}

    try:
        definitions.append(build_metals_composite_definition(specs, timeframe, profile))
        definitions.append(build_energy_composite_definition(specs, timeframe, profile))
        definitions.append(build_agriculture_softs_composite_definition(specs, timeframe, profile))
        definitions.append(build_fx_try_composite_definition(specs, timeframe, profile))
        definitions.append(build_commodity_composite_definition(specs, timeframe, profile))
        definitions.append(build_commodity_fx_composite_definition(specs, timeframe, profile))

        summary["definitions_created"] = len(definitions)
    except Exception as e:
        summary["warnings"].append(f"Error building definitions: {e}")

    return definitions, summary
