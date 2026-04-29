from dataclasses import dataclass
from typing import List

import pandas as pd

from core.logger import get_logger
from data.cleaning.integrity_checks import run_integrity_checks
from data.cleaning.missing_data import calculate_missing_ratios, detect_timestamp_gaps
from data.cleaning.outlier_detector import build_outlier_report

logger = get_logger(__name__)


@dataclass
class DataQualityScore:
    symbol: str
    timeframe: str
    rows: int
    score: float
    grade: str
    passed: bool
    errors: List[str]
    warnings: List[str]
    missing_ratio: float
    outlier_count: int
    duplicate_count: int
    gap_count: int
    notes: str = ""


def grade_from_score(score: float) -> str:
    """Convert a numeric score to a letter grade."""
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


def calculate_quality_score(
    symbol: str, timeframe: str, df: pd.DataFrame, min_rows: int = 50
) -> DataQualityScore:
    """
    Calculate a comprehensive quality score (0-100) and grade for a DataFrame.
    """
    if df is None or df.empty:
        return DataQualityScore(
            symbol=symbol,
            timeframe=timeframe,
            rows=0,
            score=0.0,
            grade="F",
            passed=False,
            errors=["DataFrame is empty or None"],
            warnings=[],
            missing_ratio=1.0,
            outlier_count=0,
            duplicate_count=0,
            gap_count=0,
            notes="Empty data",
        )

    score = 100.0
    notes_list = []

    # 1. Integrity Checks
    integrity = run_integrity_checks(df, min_rows)
    errors = integrity["errors"]
    warnings = integrity["warnings"]

    # Penalize for integrity errors
    if len(errors) > 0:
        score -= min(50.0, len(errors) * 15.0)
        notes_list.append(f"Integrity errors found ({len(errors)})")

        # Specific severe penalties
        error_text = " ".join(errors).lower()
        if "high < low" in error_text:
            score -= 25.0
            notes_list.append("Critical: high < low")
        if "duplicate" in error_text:
            score -= 10.0
        if "minimum required" in error_text:
            score -= 20.0

    # Penalize for integrity warnings
    if len(warnings) > 0:
        score -= min(15.0, len(warnings) * 5.0)
        warning_text = " ".join(warnings).lower()
        if "negative" in warning_text:
            score -= 30.0
            notes_list.append("Negative prices found")

    # 2. Missing Data
    ratios = calculate_missing_ratios(df)
    close_missing = ratios.get("close", 0.0)

    if close_missing > 0.10:
        score -= 40.0
        notes_list.append(f"High missing close ratio: {close_missing:.1%}")
    elif close_missing > 0.05:
        score -= 20.0
        notes_list.append(f"Moderate missing close ratio: {close_missing:.1%}")
    elif close_missing > 0.01:
        score -= 10.0

    # Check other OHLC missing
    ohlc_cols = [c for c in ["open", "high", "low"] if c in df.columns]
    if ohlc_cols:
        avg_ohlc_missing = sum(ratios.get(c, 0.0) for c in ohlc_cols) / len(ohlc_cols)
        if avg_ohlc_missing > 0.05:
            score -= 10.0

    # 3. Gaps
    gaps_df = detect_timestamp_gaps(df, timeframe)
    gap_count = len(gaps_df) if not gaps_df.empty else 0
    if gap_count > 10:
        score -= 25.0
        notes_list.append(f"Too many gaps ({gap_count})")
    elif gap_count > 3:
        score -= 10.0

    # 4. Outliers
    # Note: Outliers aren't necessarily bad data, but too many might indicate bad prints
    outlier_report = build_outlier_report(df)
    outlier_count = outlier_report.get("total_outliers", 0)
    total_rows = len(df)
    outlier_ratio = outlier_count / total_rows if total_rows > 0 else 0

    if outlier_ratio > 0.05:
        score -= 25.0
        notes_list.append(f"High outlier ratio ({outlier_ratio:.1%})")
    elif outlier_ratio > 0.01:
        score -= 10.0

    # Clamp score
    score = max(0.0, min(100.0, score))
    grade = grade_from_score(score)
    passed = grade in ["A", "B", "C"]

    return DataQualityScore(
        symbol=symbol,
        timeframe=timeframe,
        rows=total_rows,
        score=score,
        grade=grade,
        passed=passed,
        errors=errors,
        warnings=warnings,
        missing_ratio=close_missing,
        outlier_count=outlier_count,
        duplicate_count=df.index.duplicated().sum(),
        gap_count=gap_count,
        notes="; ".join(notes_list) if notes_list else "Data looks good",
    )
