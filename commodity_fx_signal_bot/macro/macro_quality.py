import pandas as pd


def check_macro_series_staleness(
    df: pd.DataFrame, max_staleness_days: int = 45
) -> dict:
    """Check how stale the latest data point is."""
    if df.empty:
        return {"stale_series": []}

    latest_date = df.index.max()
    now = pd.Timestamp.now(tz=latest_date.tz)

    stale_series = []

    for col in df.columns:
        valid_idx = df[col].last_valid_index()
        if valid_idx is not None:
            days_diff = (now - valid_idx).days
            if days_diff > max_staleness_days:
                stale_series.append(
                    {
                        "column": col,
                        "last_date": valid_idx.strftime("%Y-%m-%d"),
                        "days_stale": days_diff,
                    }
                )
        else:
            stale_series.append(
                {"column": col, "last_date": "never", "days_stale": float("inf")}
            )

    return {"stale_series": stale_series}


def check_macro_missing_values(df: pd.DataFrame) -> dict:
    """Check for missing values ratio in the dataframe."""
    if df.empty:
        return {"missing_ratio_by_column": {}}

    missing_ratio = (df.isna().sum() / len(df)).to_dict()
    return {"missing_ratio_by_column": missing_ratio}


def check_macro_frequency(df: pd.DataFrame) -> dict:
    """Check if the frequency of the index is consistent."""
    if df.empty or len(df) < 2:
        return {"frequency_warnings": ["Not enough data to check frequency"]}

    freq = pd.infer_freq(df.index)
    warnings = []
    if freq is None:
        warnings.append("Could not infer a regular frequency from index.")

    return {"frequency_warnings": warnings}


def build_macro_quality_report(macro_df: pd.DataFrame, summary: dict) -> dict:
    """Build the final quality report dictionary."""
    report = {
        "rows": len(macro_df),
        "columns": list(macro_df.columns) if not macro_df.empty else [],
        "latest_date": (
            macro_df.index.max().strftime("%Y-%m-%d") if not macro_df.empty else None
        ),
        "passed": True,
        "warnings": [],
    }

    if macro_df.empty:
        report["passed"] = False
        report["warnings"].append("Macro dataframe is empty.")
        return report

    staleness = check_macro_series_staleness(macro_df)
    report["stale_series"] = staleness["stale_series"]
    if staleness["stale_series"]:
        report["warnings"].append(
            f"Found {len(staleness['stale_series'])} stale series."
        )
        report["passed"] = False

    missing = check_macro_missing_values(macro_df)
    report["missing_ratio_by_column"] = missing["missing_ratio_by_column"]

    high_missing = [k for k, v in missing["missing_ratio_by_column"].items() if v > 0.2]
    if high_missing:
        report["warnings"].append(
            f"High missing values (>20%) in: {', '.join(high_missing)}"
        )

    freq_check = check_macro_frequency(macro_df)
    report["frequency_warnings"] = freq_check["frequency_warnings"]
    if freq_check["frequency_warnings"]:
        report["warnings"].extend(freq_check["frequency_warnings"])

    # incorporate existing summary info
    report.update(summary)

    return report
