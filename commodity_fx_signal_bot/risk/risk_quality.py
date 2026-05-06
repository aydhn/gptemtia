import pandas as pd
from typing import Dict

_FORBIDDEN_TERMS = [
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
    "POSITION_SIZE",
    "LEVERAGE",
]


def check_risk_score_ranges(df: pd.DataFrame) -> Dict:
    if df.empty:
        return {"invalid_score_count": 0, "invalid_columns": []}
    score_cols = [c for c in df.columns if "score" in c]
    invalid_cols = []
    total_invalid = 0
    for c in score_cols:
        mask = (df[c] < 0.0) | (df[c] > 1.0)
        invalid_count = mask.sum()
        if invalid_count > 0:
            invalid_cols.append(c)
            total_invalid += invalid_count
    return {"invalid_score_count": int(total_invalid), "invalid_columns": invalid_cols}


def check_risk_candidate_duplicates(df: pd.DataFrame) -> Dict:
    if df.empty or "risk_id" not in df.columns:
        return {"duplicate_risk_count": 0}
    return {"duplicate_risk_count": int(df.duplicated(subset=["risk_id"]).sum())}


def check_missing_risk_fields(df: pd.DataFrame) -> Dict:
    if df.empty:
        return {"missing_required_fields": False, "missing_columns": []}
    required = [
        "symbol",
        "timeframe",
        "risk_id",
        "risk_label",
        "total_pretrade_risk_score",
    ]
    missing = [c for c in required if c not in df.columns]
    return {"missing_required_fields": len(missing) > 0, "missing_columns": missing}


def check_for_forbidden_order_terms_in_risk(df: pd.DataFrame) -> Dict:
    if df.empty:
        return {"forbidden_order_terms_found": False, "found_terms": []}
    found = set()
    str_cols = df.select_dtypes(include=["object", "string"]).columns
    for c in str_cols:
        text = " ".join(df[c].fillna("").astype(str).str.upper())
        for term in _FORBIDDEN_TERMS:
            if term in text:
                found.add(term)
    return {"forbidden_order_terms_found": len(found) > 0, "found_terms": list(found)}


def check_risk_candidate_dataframe(df: pd.DataFrame) -> Dict:
    return {
        **check_risk_score_ranges(df),
        **check_risk_candidate_duplicates(df),
        **check_missing_risk_fields(df),
        **check_for_forbidden_order_terms_in_risk(df),
    }


def build_risk_quality_report(df: pd.DataFrame, summary: Dict) -> Dict:
    checks = check_risk_candidate_dataframe(df)
    passed = not (
        checks.get("invalid_score_count", 0) > 0
        or checks.get("duplicate_risk_count", 0) > 0
        or checks.get("missing_required_fields", False)
        or checks.get("forbidden_order_terms_found", False)
    )
    return {
        "rows": len(df),
        "duplicate_risk_count": checks.get("duplicate_risk_count", 0),
        "invalid_score_count": checks.get("invalid_score_count", 0),
        "missing_required_fields": checks.get("missing_required_fields", False),
        "forbidden_order_terms_found": checks.get("forbidden_order_terms_found", False),
        "passed_risk_ratio": (
            (summary.get("passed_risk_candidates", 0) / len(df)) if len(df) > 0 else 0.0
        ),
        "warning_count": (
            df["warnings"].apply(len).sum() if not df.empty and "warnings" in df else 0
        ),
        "passed": passed,
    }
