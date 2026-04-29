import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

from core.logger import get_logger

logger = get_logger(__name__)


@dataclass
class CleaningReport:
    symbol: str
    timeframe: str
    raw_rows: int
    cleaned_rows: int
    quality_before: str
    quality_after: str
    score_before: float
    score_after: float
    duplicate_rows_removed: int
    missing_summary: Dict[str, Any]
    gap_summary: Dict[str, Any]
    outlier_summary: Dict[str, Any]
    integrity_before: Dict[str, Any]
    integrity_after: Dict[str, Any]
    warnings: List[str]
    created_at_utc: str


def build_cleaning_report(
    symbol: str,
    timeframe: str,
    raw_df: pd.DataFrame,
    cleaned_df: pd.DataFrame,
    cleaning_summary: Dict[str, Any],
    quality_score_before: Any,  # DataQualityScore
    quality_score_after: Any,  # DataQualityScore
    gap_summary: Dict[str, Any],
    outlier_summary: Dict[str, Any],
    integrity_before: Dict[str, Any],
    integrity_after: Dict[str, Any],
) -> CleaningReport:
    """Build a comprehensive report of the cleaning process."""

    # Extract missing data stats
    missing_stats = {}
    if cleaned_df is not None and not cleaned_df.empty:
        for col in cleaned_df.columns:
            missing_stats[col] = int(cleaned_df[col].isna().sum())

    return CleaningReport(
        symbol=symbol,
        timeframe=timeframe,
        raw_rows=len(raw_df) if raw_df is not None else 0,
        cleaned_rows=len(cleaned_df) if cleaned_df is not None else 0,
        quality_before=quality_score_before.grade if quality_score_before else "N/A",
        quality_after=quality_score_after.grade if quality_score_after else "N/A",
        score_before=quality_score_before.score if quality_score_before else 0.0,
        score_after=quality_score_after.score if quality_score_after else 0.0,
        duplicate_rows_removed=cleaning_summary.get("duplicate_rows_removed", 0),
        missing_summary=missing_stats,
        gap_summary=gap_summary,
        outlier_summary=outlier_summary,
        integrity_before=integrity_before,
        integrity_after=integrity_after,
        warnings=cleaning_summary.get("warnings", []),
        created_at_utc=datetime.now(timezone.utc).isoformat(),
    )


def cleaning_report_to_dict(report: CleaningReport) -> Dict[str, Any]:
    """Convert a CleaningReport dataclass to a dictionary."""
    return asdict(report)


def save_cleaning_report_json(report: CleaningReport, path: Path) -> None:
    """Save the cleaning report as a JSON file."""
    data = cleaning_report_to_dict(report)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    logger.debug(f"Saved cleaning report JSON to {path}")


def save_cleaning_report_text(report: CleaningReport, path: Path) -> None:
    """Save the cleaning report as a human-readable text file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"CLEANING REPORT: {report.symbol} ({report.timeframe})\n")
        f.write(f"Generated At: {report.created_at_utc}\n")
        f.write("=" * 50 + "\n\n")

        f.write("1. SUMMARY\n")
        f.write("-" * 20 + "\n")
        f.write(f"Raw Rows: {report.raw_rows}\n")
        f.write(f"Cleaned Rows: {report.cleaned_rows}\n")
        f.write(
            f"Quality Before: {report.quality_before} ({report.score_before:.1f}/100)\n"
        )
        f.write(
            f"Quality After: {report.quality_after} ({report.score_after:.1f}/100)\n"
        )
        f.write(f"Duplicate Rows Removed: {report.duplicate_rows_removed}\n\n")

        f.write("2. INTEGRITY\n")
        f.write("-" * 20 + "\n")
        f.write(f"Errors Before: {len(report.integrity_before.get('errors', []))}\n")
        f.write(f"Errors After: {len(report.integrity_after.get('errors', []))}\n")
        if report.integrity_after.get("errors"):
            f.write("Remaining Errors:\n")
            for err in report.integrity_after["errors"]:
                f.write(f"  - {err}\n")
        f.write("\n")

        f.write("3. MISSING DATA\n")
        f.write("-" * 20 + "\n")
        for col, count in report.missing_summary.items():
            if count > 0:
                f.write(f"{col}: {count} missing\n")
        if not any(count > 0 for count in report.missing_summary.values()):
            f.write("No missing data remaining.\n")
        f.write("\n")

        f.write("4. GAPS & OUTLIERS\n")
        f.write("-" * 20 + "\n")
        f.write(f"Total Gaps Found: {report.gap_summary.get('total_gaps', 0)}\n")
        if report.gap_summary.get("total_gaps", 0) > 0:
            f.write(f"Max Gap: {report.gap_summary.get('max_gap')}\n")

        f.write(
            f"Total Outliers Flagged: {report.outlier_summary.get('total_outliers', 0)}\n"
        )
        f.write("\n")

        if report.warnings:
            f.write("5. WARNINGS\n")
            f.write("-" * 20 + "\n")
            for w in report.warnings:
                f.write(f"  - {w}\n")

    logger.debug(f"Saved cleaning report TXT to {path}")
