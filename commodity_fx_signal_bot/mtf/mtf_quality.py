import pandas as pd


def check_mtf_missing_timeframes(summary: dict) -> list[str]:
    # Extract missing timeframes or sets from summary dict
    return summary.get("missing_timeframes", [])


def check_mtf_nan_ratio(mtf_df: pd.DataFrame, max_nan_ratio: float = 0.50) -> dict:
    if mtf_df.empty:
        return {"total_nan_ratio": 0.0, "passed": False, "high_nan_cols": []}

    total_nan = mtf_df.isna().sum().sum()
    total_cells = mtf_df.size
    ratio = total_nan / total_cells if total_cells > 0 else 0.0

    col_ratios = mtf_df.isna().mean()
    high_nan_cols = col_ratios[col_ratios > max_nan_ratio].index.tolist()

    return {
        "total_nan_ratio": float(ratio),
        "passed": ratio <= max_nan_ratio,
        "high_nan_cols": high_nan_cols,
    }


def check_mtf_stale_context(
    mtf_df: pd.DataFrame, stale_col_pattern: str = "context_age"
) -> dict:
    stale_cols = [c for c in mtf_df.columns if stale_col_pattern in c]
    if not stale_cols:
        return {"stale_context_ratio": 0.0, "passed": True}

    stale_counts = (mtf_df[stale_cols] > 5).sum().sum()  # simplified check
    ratio = (
        stale_counts / mtf_df[stale_cols].size if mtf_df[stale_cols].size > 0 else 0.0
    )

    return {"stale_context_ratio": float(ratio), "passed": ratio < 0.30}


def check_mtf_duplicate_columns(mtf_df: pd.DataFrame) -> dict:
    duplicates = mtf_df.columns[mtf_df.columns.duplicated()].tolist()
    return {"duplicate_columns": duplicates, "passed": len(duplicates) == 0}


def check_mtf_index_integrity(mtf_df: pd.DataFrame) -> dict:
    if mtf_df.empty:
        return {"index_is_datetime": False, "duplicate_index_count": 0, "passed": False}

    is_datetime = isinstance(mtf_df.index, pd.DatetimeIndex)
    dupes = int(mtf_df.index.duplicated().sum())

    return {
        "index_is_datetime": is_datetime,
        "duplicate_index_count": dupes,
        "passed": is_datetime and dupes == 0,
    }


def build_mtf_quality_report(mtf_df: pd.DataFrame, summary: dict) -> dict:
    nan_check = check_mtf_nan_ratio(mtf_df)
    stale_check = check_mtf_stale_context(mtf_df)
    dup_check = check_mtf_duplicate_columns(mtf_df)
    idx_check = check_mtf_index_integrity(mtf_df)

    missing_tfs = summary.get("missing_timeframes", [])
    warnings = summary.get("warnings", [])

    passed = (
        nan_check["passed"]
        and stale_check["passed"]
        and dup_check["passed"]
        and idx_check["passed"]
    )

    return {
        "rows": len(mtf_df),
        "columns": len(mtf_df.columns),
        "total_nan_ratio": nan_check["total_nan_ratio"],
        "duplicate_columns": dup_check["duplicate_columns"],
        "index_is_datetime": idx_check["index_is_datetime"],
        "duplicate_index_count": idx_check["duplicate_index_count"],
        "stale_context_ratio": stale_check["stale_context_ratio"],
        "missing_timeframes": missing_tfs,
        "warnings": warnings + (["High NaN ratio"] if not nan_check["passed"] else []),
        "passed": passed,
    }
