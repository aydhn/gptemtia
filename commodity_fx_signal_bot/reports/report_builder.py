"""
Report generation utilities.
"""

from typing import List
from pathlib import Path
import pandas as pd
from config.symbols import SymbolSpec
from data.universe_analyzer import SymbolReliabilityResult, UniverseAnalyzer


def build_universe_report(symbols: List[SymbolSpec]) -> str:
    """
    Build a text summary report of the symbol universe.
    """
    total = len(symbols)
    enabled = sum(1 for s in symbols if s.enabled)
    analysis = sum(1 for s in symbols if s.enabled and s.analysis_enabled)
    paper_trade = sum(1 for s in symbols if s.enabled and s.paper_trade_enabled)

    # Count by asset class
    classes = {}
    data_sources = {}
    for s in symbols:
        if s.enabled:
            classes[s.asset_class] = classes.get(s.asset_class, 0) + 1
            data_sources[s.data_source] = data_sources.get(s.data_source, 0) + 1

    lines = [
        "=== Symbol Universe Summary ===",
        f"Total Symbols: {total}",
        f"Enabled Symbols: {enabled}",
        f"Analysis Enabled: {analysis}",
        f"Paper Trade Enabled: {paper_trade}",
        "",
        "Breakdown by Asset Class:",
    ]
    for ac, count in sorted(classes.items()):
        lines.append(f"  - {ac}: {count}")

    lines.append("")
    lines.append("Breakdown by Data Source:")
    for ds, count in sorted(data_sources.items()):
        lines.append(f"  - {ds}: {count}")

    lines.append("=============================")
    return "\n".join(lines)


def build_reliability_report(results: List[SymbolReliabilityResult]) -> str:
    """
    Build a text report summarizing the reliability scan results.
    """
    summary = UniverseAnalyzer.summarize_results(results)
    if not summary:
        return "No reliability results available."

    lines = [
        "=== Symbol Reliability Report ===",
        f"Total Analyzed: {summary['total_analyzed']}",
        f"Success: {summary['success_count']}",
        f"Failed: {summary['fail_count']}",
        f"Average Score: {summary['avg_score']:.2f}",
        "",
        "Grade Distribution:",
    ]
    for grade, count in sorted(summary["grade_distribution"].items()):
        lines.append(f"  - {grade}: {count}")

    lines.append("")
    lines.append("Asset Class Success Rate:")
    for ac, rate in sorted(summary["asset_class_success_rate"].items()):
        lines.append(f"  - {ac}: {rate*100:.1f}%")

    lines.append("")
    lines.append("Top 10 Most Reliable:")
    for b in summary["best_10"]:
        lines.append(
            f"  - {b['symbol']}: {b['reliability_score']:.1f} ({b['reliability_grade']})"
        )

    lines.append("")
    lines.append("Bottom 10 Least Reliable:")
    for w in summary["worst_10"]:
        err_msg = f" - {w['error'][:50]}..." if w["error"] else ""
        lines.append(
            f"  - {w['symbol']}: {w['reliability_score']:.1f} ({w['reliability_grade']}){err_msg}"
        )

    lines.append("")
    lines.append(f"Alias Used: {len(summary['used_alias_symbols'])}")
    if summary["used_alias_symbols"]:
        lines.append(f"  Symbols: {', '.join(summary['used_alias_symbols'])}")

    lines.append("")
    lines.append(f"Errors Found: {len(summary['error_symbols'])}")
    for e in summary["error_symbols"][:10]:  # print first 10
        lines.append(f"  - {e['symbol']}: {e['error'][:80]}...")
    if len(summary["error_symbols"]) > 10:
        lines.append(f"  ... and {len(summary['error_symbols']) - 10} more")

    lines.append("=================================")
    return "\n".join(lines)


def build_asset_class_summary(results: List[SymbolReliabilityResult]) -> str:
    """
    Build a brief summary of results by asset class.
    """
    summary = UniverseAnalyzer.summarize_results(results)
    if not summary:
        return "No data"

    lines = ["Asset Class Success Rates:"]
    for ac, rate in sorted(summary["asset_class_success_rate"].items()):
        lines.append(f"{ac}: {rate*100:.1f}%")
    return "\n".join(lines)


def save_text_report(text: str, path: Path) -> None:
    """Save text report to file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(text)


def save_dataframe_report(df: pd.DataFrame, path: Path) -> None:
    """Save dataframe to CSV."""
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def build_timeframe_compatibility_report(
    symbols: List[SymbolSpec], scan_plan: dict
) -> str:
    from config.symbols import (
        get_default_timeframes_for_asset_class,
        get_allowed_timeframes_for_symbol,
    )

    lines = [
        "=== Timeframe Compatibility Audit ===",
        f"Total Symbols: {scan_plan['total_symbols']}",
        "",
        "Asset Class Breakdowns (Eligible Symbols):",
    ]
    for ac, count in scan_plan.get("by_asset_class", {}).items():
        lines.append(f"  - {ac}: {count}")

    lines.append("")
    lines.append("Excluded Timeframes (Found in Symbols):")
    for s in symbols:
        if s.excluded_timeframes:
            lines.append(f"  - {s.symbol}: {s.excluded_timeframes}")

    lines.append("")
    lines.append("Preferred Timeframes (Found in Symbols):")
    for s in symbols:
        if s.preferred_timeframes:
            lines.append(f"  - {s.symbol}: {s.preferred_timeframes}")

    lines.append("")
    lines.append("Scan Plan Info:")
    lines.append(f"  - Profile: {scan_plan['profile']}")
    lines.append(f"  - Eligible Symbols: {len(scan_plan['eligible_symbols'])}")
    lines.append(f"  - Skipped Symbols: {len(scan_plan['skipped_symbols'])}")

    return "\n".join(lines)


def build_scan_plan_report(scan_plan: dict) -> str:
    lines = [
        "=== Scan Plan ===",
        f"Profile: {scan_plan['profile']}",
        f"Time: {scan_plan['now']}",
        f"Interval: {scan_plan['scan_interval_minutes']}m",
        f"Eligible: {len(scan_plan['eligible_symbols'])}",
        f"Skipped: {len(scan_plan['skipped_symbols'])}",
        "=================",
    ]
    return "\n".join(lines)
