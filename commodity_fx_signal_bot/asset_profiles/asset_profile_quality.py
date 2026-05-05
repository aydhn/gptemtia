import pandas as pd


def check_asset_profile_missing_columns(df: pd.DataFrame) -> dict:
    """Check for commonly expected columns in asset profiles that might be missing."""
    expected = [
        "asset_behavior_score",
        "asset_behavior_regime_label",
        "asset_group_regime_label",
        "asset_relative_strength_regime_label",
    ]

    missing = [c for c in expected if c not in df.columns]
    return {"missing_columns": missing}


def check_group_member_coverage(
    asset_class: str, expected_members: int, available_members: int
) -> dict:
    """Check if group has enough members compared to expected."""
    ratio = available_members / expected_members if expected_members > 0 else 0
    passed = ratio >= 0.5 and available_members >= 3

    return {
        "asset_class": asset_class,
        "expected_members": expected_members,
        "available_members": available_members,
        "coverage_ratio": ratio,
        "passed_minimum_coverage": passed,
    }


def check_group_feature_nan_ratio(
    df: pd.DataFrame, max_nan_ratio: float = 0.50
) -> dict:
    """Check the NaN ratio of group features."""
    if df.empty:
        return {"total_nan_ratio": 1.0, "passed_nan_check": False}

    total_cells = df.size
    nan_cells = df.isna().sum().sum()
    ratio = nan_cells / total_cells if total_cells > 0 else 1.0

    return {"total_nan_ratio": ratio, "passed_nan_check": ratio <= max_nan_ratio}


def check_relative_strength_validity(df: pd.DataFrame) -> dict:
    """Check if relative strength calculation is available."""
    has_rs = any("rs_vs_group" in str(c) for c in df.columns)
    return {"relative_strength_available": has_rs}


def build_asset_profile_quality_report(df: pd.DataFrame, summary: dict) -> dict:
    """Build a comprehensive quality report for asset profiles."""
    report = {
        "rows": len(df),
        "columns": len(df.columns),
        "warnings": summary.get("warnings", []),
        "passed": True,
    }

    report.update(check_asset_profile_missing_columns(df))
    report.update(check_group_feature_nan_ratio(df))
    report.update(check_relative_strength_validity(df))

    report["correlation_available"] = any("corr_symbol" in str(c) for c in df.columns)
    report["dispersion_available"] = any("dispersion" in str(c) for c in df.columns)

    # Example logic to fail quality
    if not report["passed_nan_check"] or not report["relative_strength_available"]:
        report["passed"] = False
        report["warnings"].append(
            "Failed critical quality checks (NaN ratio or missing RS)."
        )

    return report
