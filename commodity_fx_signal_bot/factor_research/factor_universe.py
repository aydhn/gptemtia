import pandas as pd
from config.symbols import SymbolSpec
import logging

logger = logging.getLogger(__name__)

def build_factor_universe(specs: list[SymbolSpec], min_symbols: int = 5) -> tuple[list[SymbolSpec], dict]:
    summary = {
        "provided_symbols": len(specs),
        "valid_symbols": 0,
        "warnings": []
    }

    valid_specs = [s for s in specs if s.symbol]
    summary["valid_symbols"] = len(valid_specs)

    if len(valid_specs) < min_symbols:
        summary["warnings"].append("insufficient_data: Universe size below minimum for factor research.")

    return valid_specs, summary

def build_factor_metadata_table(specs: list[SymbolSpec]) -> pd.DataFrame:
    records = []
    for spec in specs:
        records.append({
            "symbol": spec.symbol,
            "asset_class": spec.asset_class,
            "source": spec.source
        })
    return pd.DataFrame(records)

def filter_factor_universe_by_asset_class(specs: list[SymbolSpec], asset_class: str | None = None) -> list[SymbolSpec]:
    if not asset_class:
        return specs
    return [s for s in specs if s.asset_class == asset_class]

def check_factor_universe_coverage(specs: list[SymbolSpec], returns_df: pd.DataFrame | None = None) -> dict:
    summary = {"total_specs": len(specs), "missing_returns": [], "warnings": []}
    if returns_df is None:
        summary["warnings"].append("Returns dataframe is None.")
        return summary

    for spec in specs:
        if spec.symbol not in returns_df.columns:
            summary["missing_returns"].append(spec.symbol)

    if summary["missing_returns"]:
        summary["warnings"].append(f"Missing returns for {len(summary['missing_returns'])} symbols.")

    return summary
