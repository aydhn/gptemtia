import pandas as pd

_FORBIDDEN_TERMS = {
    "buy",
    "sell",
    "open_long",
    "open_short",
    "close_position",
    "market_order",
    "limit_order",
    "stop_loss_order",
    "take_profit_order",
}


def check_strategy_score_ranges(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"invalid_score_count": 0, "issues": []}

    score_cols = [
        "decision_score",
        "decision_confidence",
        "decision_quality_score",
        "strategy_selection_score",
        "strategy_fit_score",
        "regime_fit_score",
        "mtf_fit_score",
        "macro_fit_score",
        "asset_profile_fit_score",
        "conflict_penalty",
        "strategy_readiness_score",
    ]

    invalid_count = 0
    issues = []

    for col in score_cols:
        if col in df.columns:
            out_of_bounds = df[(df[col] < 0.0) | (df[col] > 1.0)]
            if not out_of_bounds.empty:
                invalid_count += len(out_of_bounds)
                issues.append(
                    f"{col} has {len(out_of_bounds)} rows out of bounds [0,1]"
                )

    return {"invalid_score_count": invalid_count, "issues": issues}


def check_strategy_duplicates(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"duplicate_strategy_count": 0}

    if "strategy_id" in df.columns:
        dups = df.duplicated(subset=["strategy_id"]).sum()
        return {"duplicate_strategy_count": int(dups)}

    return {"duplicate_strategy_count": 0}


def check_missing_strategy_fields(df: pd.DataFrame) -> dict:
    required_cols = [
        "symbol",
        "timeframe",
        "strategy_id",
        "strategy_family",
        "strategy_status",
        "directional_bias",
    ]

    missing = []
    for col in required_cols:
        if col not in df.columns:
            missing.append(col)

    return {"missing_required_fields": missing}


def check_for_forbidden_order_terms(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"forbidden_order_terms_found": False, "terms_found": []}

    found_terms = set()

    str_cols = df.select_dtypes(include=["object", "string"]).columns

    for col in str_cols:
        unique_vals = df[col].astype(str).str.lower().unique()
        for val in unique_vals:
            for term in _FORBIDDEN_TERMS:
                if term in val:
                    found_terms.add(term)

    return {
        "forbidden_order_terms_found": len(found_terms) > 0,
        "terms_found": list(found_terms),
    }


def build_strategy_quality_report(df: pd.DataFrame, summary: dict) -> dict:
    if df.empty:
        return {
            "rows": 0,
            "duplicate_strategy_count": 0,
            "invalid_score_count": 0,
            "missing_required_fields": [],
            "forbidden_order_terms_found": False,
            "passed_strategy_ratio": 0.0,
            "warning_count": 0,
            "passed": False,
        }

    score_check = check_strategy_score_ranges(df)
    dup_check = check_strategy_duplicates(df)
    fields_check = check_missing_strategy_fields(df)
    forbidden_check = check_for_forbidden_order_terms(df)

    total = len(df)
    passed_ratio = (
        summary.get("passed_strategy_candidates", 0) / total if total > 0 else 0.0
    )

    passed = (
        score_check["invalid_score_count"] == 0
        and dup_check["duplicate_strategy_count"] == 0
        and len(fields_check["missing_required_fields"]) == 0
        and not forbidden_check["forbidden_order_terms_found"]
    )

    return {
        "rows": total,
        "duplicate_strategy_count": dup_check["duplicate_strategy_count"],
        "invalid_score_count": score_check["invalid_score_count"],
        "missing_required_fields": fields_check["missing_required_fields"],
        "forbidden_order_terms_found": forbidden_check["forbidden_order_terms_found"],
        "forbidden_terms": forbidden_check["terms_found"],
        "passed_strategy_ratio": passed_ratio,
        "warning_count": len(score_check["issues"]),
        "passed": passed,
    }
