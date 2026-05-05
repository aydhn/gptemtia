"""
Registry and grouping utilities for symbol universes based on asset class.
"""

from typing import Dict, List
from config.symbols import SymbolSpec


def group_symbols_by_asset_class(
    symbols: List[SymbolSpec],
) -> Dict[str, List[SymbolSpec]]:
    """Group symbols by their asset_class."""
    grouped = {}
    for spec in symbols:
        if spec.asset_class not in grouped:
            grouped[spec.asset_class] = []
        grouped[spec.asset_class].append(spec)
    return grouped


def group_symbols_by_sub_class(
    symbols: List[SymbolSpec],
) -> Dict[str, List[SymbolSpec]]:
    """Group symbols by their sub_class."""
    grouped = {}
    for spec in symbols:
        if spec.sub_class not in grouped:
            grouped[spec.sub_class] = []
        grouped[spec.sub_class].append(spec)
    return grouped


def get_tradeable_asset_classes(symbols: List[SymbolSpec]) -> List[str]:
    """Get a unique list of tradeable asset classes."""
    classes = set()
    for spec in symbols:
        if (
            spec.enabled
            and spec.analysis_enabled
            and not spec.benchmark_enabled
            and spec.asset_class not in ("macro", "synthetic")
        ):
            classes.add(spec.asset_class)
    return list(classes)


def get_group_members(symbols: List[SymbolSpec], asset_class: str) -> List[SymbolSpec]:
    """Get all enabled members of a specific asset class group."""
    return [
        spec
        for spec in symbols
        if spec.asset_class == asset_class
        and spec.enabled
        and spec.analysis_enabled
        and not spec.benchmark_enabled
    ]


def get_group_symbol_codes(symbols: List[SymbolSpec], asset_class: str) -> List[str]:
    """Get symbol codes for members of a specific asset class group."""
    return [spec.symbol for spec in get_group_members(symbols, asset_class)]


def filter_symbols_for_group_analysis(
    symbols: List[SymbolSpec], min_members: int = 3
) -> Dict[str, List[SymbolSpec]]:
    """Filter symbols into groups suitable for group-level analysis."""
    grouped = group_symbols_by_asset_class(symbols)
    tradeable_groups = {}

    for ac, group_symbols in grouped.items():
        if ac in ("macro", "synthetic", "benchmark"):
            continue

        tradeable_members = [
            s
            for s in group_symbols
            if s.enabled and s.analysis_enabled and not s.benchmark_enabled
        ]

        if len(tradeable_members) >= min_members:
            tradeable_groups[ac] = tradeable_members

    return tradeable_groups


def summarize_asset_class_universe(symbols: List[SymbolSpec]) -> dict:
    """Summarize the symbol universe by asset classes."""
    grouped = group_symbols_by_asset_class(symbols)
    summary = {
        "total_symbols": len(symbols),
        "total_asset_classes": len(grouped),
        "asset_classes": {},
        "warnings": [],
    }

    from asset_profiles.asset_profile_config import list_asset_profiles

    known_asset_classes = {p.asset_class for p in list_asset_profiles()}
    known_asset_classes.add("macro")
    known_asset_classes.add("synthetic")

    for ac, group_symbols in grouped.items():
        tradeable = [
            s
            for s in group_symbols
            if s.enabled and s.analysis_enabled and not s.benchmark_enabled
        ]

        summary["asset_classes"][ac] = {
            "total_count": len(group_symbols),
            "tradeable_count": len(tradeable),
            "is_known": ac in known_asset_classes,
        }

        if ac not in known_asset_classes:
            summary["warnings"].append(f"Unknown asset class found: {ac}")

    return summary
