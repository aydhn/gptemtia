"""
Quality and integrity checks for validation inputs and outputs.
"""

import logging
import pandas as pd
from typing import Optional

from validation.validation_models import TimeSplit

logger = logging.getLogger(__name__)

# Live trading terminology that should not appear in output dataframes
FORBIDDEN_LIVE_TERMS = [
    "LIVE_ORDER",
    "BROKER_ORDER",
    "SEND_ORDER",
    "EXECUTE_TRADE",
    "REAL_POSITION",
    "LIVE_POSITION",
    "MARKET_ORDER",
    "LIMIT_ORDER",
    "LIVE_STRATEGY_SELECTED"
]


def check_validation_input_integrity(
    price_df: Optional[pd.DataFrame] = None,
    trades_df: Optional[pd.DataFrame] = None,
    equity_curve: Optional[pd.DataFrame] = None
) -> dict:
    """Checks if validation inputs are valid."""
    warnings = []
    passed = True

    if price_df is None or price_df.empty:
        warnings.append("Price DataFrame is missing or empty")
        passed = False
    elif not isinstance(price_df.index, pd.DatetimeIndex):
         warnings.append("Price DataFrame index is not a DatetimeIndex")
         passed = False

    if trades_df is None or trades_df.empty:
        warnings.append("Trades DataFrame is missing or empty")
        passed = False

    if equity_curve is None or equity_curve.empty:
        warnings.append("Equity curve DataFrame is missing or empty")

    return {
        "passed": passed,
        "warnings": warnings
    }


def check_split_coverage(splits: list[TimeSplit]) -> dict:
    """Checks if time splits cover a reasonable period."""
    warnings = []
    passed = True

    if not splits:
        return {"passed": False, "warnings": ["No splits provided"]}

    if len(splits) < 2:
        warnings.append("Only 1 split generated. Walk-forward requires >= 2.")

    # Check if there are gaps (assuming sequential continuous splits)
    # This is optional based on expanding vs rolling window, but generally test start should >= previous test end

    return {
        "passed": passed,
        "warnings": warnings
    }


def check_walk_forward_result_quality(walk_forward_df: pd.DataFrame) -> dict:
    """Checks the quality of walk-forward evaluation results."""
    warnings = []
    passed = True

    if walk_forward_df.empty:
        return {"passed": False, "warnings": ["Empty walk-forward result"]}

    req_cols = ["split_id", "train_sharpe_ratio", "test_sharpe_ratio"]
    for col in req_cols:
        if col not in walk_forward_df.columns:
            warnings.append(f"Missing required column in walk-forward results: {col}")
            passed = False

    # Check for NaN values in key metrics
    if passed:
        if walk_forward_df["test_sharpe_ratio"].isna().any():
             warnings.append("NaN values found in test_sharpe_ratio")
             passed = False

    return {
        "passed": passed,
        "warnings": warnings
    }


def check_parameter_result_quality(result_table: pd.DataFrame) -> dict:
    """Checks parameter result table quality."""
    warnings = []
    passed = True

    if result_table.empty:
        return {"passed": False, "warnings": ["Empty parameter result table"]}

    param_cols = [c for c in result_table.columns if c.startswith('param_')]
    if not param_cols:
         warnings.append("No parameter columns found (missing 'param_' prefix)")
         passed = False

    return {
        "passed": passed,
        "warnings": warnings
    }


def check_for_forbidden_live_terms_in_validation(
    df: Optional[pd.DataFrame] = None,
    summary: Optional[dict] = None
) -> dict:
    """Ensures no live trading terms slipped into the validation results."""
    found_terms = []

    if df is not None and not df.empty:
        # Check column names
        for col in df.columns:
            for term in FORBIDDEN_LIVE_TERMS:
                if term in str(col).upper():
                    found_terms.append(f"Column name: {col} contains {term}")

        # Sample check string columns (doing full check might be slow)
        str_cols = df.select_dtypes(include=['object', 'string']).columns
        for col in str_cols:
            # Check unique values instead of every row for speed
            unique_vals = df[col].astype(str).unique()
            for val in unique_vals:
                for term in FORBIDDEN_LIVE_TERMS:
                    if term in str(val).upper():
                        found_terms.append(f"Value in {col}: {val} contains {term}")

    if summary is not None:
         # Serialize to string and check
         summary_str = str(summary).upper()
         for term in FORBIDDEN_LIVE_TERMS:
             if term in summary_str:
                 found_terms.append(f"Summary contains {term}")

    return {
        "passed": len(found_terms) == 0,
        "found_terms": found_terms,
        "warnings": [f"Forbidden live term found: {t}" for t in found_terms]
    }


def build_validation_quality_report(summary: dict) -> dict:
    """Compiles all quality checks into a single report."""

    passed = True
    warnings = []

    for key, result in summary.items():
        if isinstance(result, dict) and "passed" in result:
             if not result["passed"]:
                 passed = False
             if "warnings" in result:
                 warnings.extend(result["warnings"])

    # Deduplicate warnings
    warnings = list(dict.fromkeys(warnings))

    return {
        "input_integrity_passed": summary.get("input", {}).get("passed", False),
        "split_coverage_passed": summary.get("splits", {}).get("passed", False),
        "walk_forward_quality_passed": summary.get("walk_forward", {}).get("passed", False),
        "parameter_quality_passed": summary.get("parameters", {}).get("passed", False),
        "forbidden_live_terms_found": not summary.get("forbidden_terms", {}).get("passed", True),
        "warning_count": len(warnings),
        "passed": passed and summary.get("forbidden_terms", {}).get("passed", True),
        "warnings": warnings
    }
