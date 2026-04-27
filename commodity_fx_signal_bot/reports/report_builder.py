"""
Report generation utilities.
"""
from typing import List
from config.symbols import SymbolSpec

def build_universe_report(symbols: List[SymbolSpec]) -> str:
    """
    Build a text summary report of the symbol universe.
    """
    total = len(symbols)
    enabled = sum(1 for s in symbols if s.enabled)

    # Count by asset class
    classes = {}
    for s in symbols:
        if s.enabled:
            classes[s.asset_class] = classes.get(s.asset_class, 0) + 1

    lines = [
        "=== Symbol Universe Summary ===",
        f"Total Symbols: {total}",
        f"Enabled Symbols: {enabled}",
        "",
        "Breakdown by Asset Class:"
    ]

    for ac, count in sorted(classes.items()):
        lines.append(f"  - {ac}: {count}")

    lines.append("=============================")
    return "\n".join(lines)
