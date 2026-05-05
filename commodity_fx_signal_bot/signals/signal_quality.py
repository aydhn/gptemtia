import pandas as pd


def check_score_ranges(df: pd.DataFrame) -> dict:
    if df is None or df.empty:
        return {"invalid_score_count": 0}

    invalid = 0
    score_cols = [c for c in df.columns if "score" in c]
    for col in score_cols:
        invalid += len(df[(df[col] < 0.0) | (df[col] > 1.0)])

    return {"invalid_score_count": invalid}


def check_candidate_duplicates(df: pd.DataFrame) -> dict:
    if df is None or df.empty:
        return {"duplicate_candidate_count": 0}

    if "candidate_id" in df.columns:
        dups = df.duplicated(subset=["candidate_id"]).sum()
        return {"duplicate_candidate_count": int(dups)}
    return {"duplicate_candidate_count": 0}


def check_missing_candidate_fields(df: pd.DataFrame) -> dict:
    required = ["symbol", "timeframe", "timestamp", "candidate_id", "candidate_score"]
    if df is None or df.empty:
        return {"missing_required_fields": required}

    missing = [c for c in required if c not in df.columns]
    return {"missing_required_fields": missing}


def check_signal_candidate_dataframe(df: pd.DataFrame) -> dict:
    res = {"rows": len(df) if df is not None else 0}
    res.update(check_score_ranges(df))
    res.update(check_candidate_duplicates(df))
    res.update(check_missing_candidate_fields(df))

    if df is not None and not df.empty and "passed_pre_filters" in df.columns:
        res["passed_candidate_ratio"] = df["passed_pre_filters"].mean()
    else:
        res["passed_candidate_ratio"] = 0.0

    if df is not None and not df.empty and "warnings" in df.columns:
        # Just count rows with non-empty warnings list/string
        res["warning_count"] = len(df[df["warnings"].astype(str) != "[]"])
    else:
        res["warning_count"] = 0

    return res


def build_signal_quality_report(df: pd.DataFrame, summary: dict) -> dict:
    q = check_signal_candidate_dataframe(df)

    # overall pass logic
    passed = (
        q["invalid_score_count"] == 0
        and q["duplicate_candidate_count"] == 0
        and len(q["missing_required_fields"]) == 0
    )

    q["passed"] = passed
    return q
