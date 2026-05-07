import pandas as pd
from typing import Dict, Any

_FORBIDDEN_TRADE_TERMS = [
    "BUY",
    "SELL",
    "OPEN_LONG",
    "OPEN_SHORT",
    "CLOSE_POSITION",
    "MARKET_ORDER",
    "LIMIT_ORDER",
    "STOP_LOSS_ORDER",
    "TAKE_PROFIT_ORDER",
    "SEND_ORDER",
    "EXECUTE_TRADE",
    "REAL_POSITION_SIZE",
    "LIVE_POSITION",
    "BROKER_ORDER",
    "LEVERAGE_ORDER",
]


def check_sizing_candidate_dataframe(df: pd.DataFrame) -> Dict[str, Any]:
    if df is None or df.empty:
        return {"passed": False, "reason": "Empty dataframe"}
    return {"passed": True}


def check_sizing_score_ranges(df: pd.DataFrame) -> Dict[str, Any]:
    invalid_scores = 0
    cols = [
        "total_pretrade_risk_score",
        "risk_readiness_score",
        "sizing_readiness_score",
        "sizing_quality_score",
    ]

    for col in cols:
        if col in df.columns:
            invalid = df[(df[col] < 0.0) | (df[col] > 1.0)]
            invalid_scores += len(invalid)

    return {"invalid_score_count": invalid_scores, "passed": invalid_scores == 0}


def check_sizing_candidate_duplicates(df: pd.DataFrame) -> Dict[str, Any]:
    if "sizing_id" not in df.columns:
        return {"duplicate_sizing_count": 0, "passed": True}

    dupes = df.duplicated(subset=["sizing_id"]).sum()
    return {"duplicate_sizing_count": int(dupes), "passed": dupes == 0}


def check_missing_sizing_fields(df: pd.DataFrame) -> Dict[str, Any]:
    required = [
        "sizing_id",
        "symbol",
        "timeframe",
        "sizing_label",
        "adjusted_theoretical_units",
    ]
    missing = [c for c in required if c not in df.columns]
    return {"missing_required_fields": missing, "passed": len(missing) == 0}


def check_for_forbidden_trade_terms_in_sizing(df: pd.DataFrame) -> Dict[str, Any]:
    found = []
    # Check all object/string columns for forbidden terms
    obj_cols = df.select_dtypes(include=["object"]).columns
    for col in obj_cols:
        for term in _FORBIDDEN_TRADE_TERMS:
            # Check if any row contains the forbidden term
            if df[col].astype(str).str.contains(term, case=False, na=False).any():
                found.append(f"Term '{term}' found in column '{col}'")

    return {"forbidden_trade_terms_found": found, "passed": len(found) == 0}


def build_sizing_quality_report(
    df: pd.DataFrame, summary: Dict[str, Any]
) -> Dict[str, Any]:
    if df is None or df.empty:
        return {"passed": False, "rows": 0, "warning_count": 0}

    score_check = check_sizing_score_ranges(df)
    dupe_check = check_sizing_candidate_duplicates(df)
    missing_check = check_missing_sizing_fields(df)
    forbidden_check = check_for_forbidden_trade_terms_in_sizing(df)

    passed_ratio = 0.0
    if "sizing_label" in df.columns and len(df) > 0:
        passed_count = len(df[df["sizing_label"] == "sizing_approved_candidate"])
        passed_ratio = passed_count / len(df)

    all_passed = (
        score_check["passed"]
        and dupe_check["passed"]
        and missing_check["passed"]
        and forbidden_check["passed"]
    )

    return {
        "rows": len(df),
        "duplicate_sizing_count": dupe_check["duplicate_sizing_count"],
        "invalid_score_count": score_check["invalid_score_count"],
        "missing_required_fields": missing_check["missing_required_fields"],
        "forbidden_trade_terms_found": forbidden_check["forbidden_trade_terms_found"],
        "passed_sizing_ratio": passed_ratio,
        "warning_count": len(forbidden_check["forbidden_trade_terms_found"])
        + len(missing_check["missing_required_fields"]),
        "passed": all_passed,
    }
