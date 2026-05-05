import pandas as pd
from typing import Dict

_FORBIDDEN_TERMS = {
    "buy",
    "sell",
    "open_long",
    "open_short",
    "close_position",
    "market_order",
    "limit_order",
    "AL",
    "SAT",
    "al",
    "sat",
}


def check_decision_score_ranges(df: pd.DataFrame) -> Dict:
    invalid_count = 0
    if df is not None and not df.empty:
        cols_to_check = [
            "signal_score_component",
            "directional_consensus_component",
            "regime_confirmation_component",
            "mtf_confirmation_component",
            "macro_context_component",
            "asset_profile_fit_component",
            "quality_component",
            "risk_precheck_component",
            "conflict_score",
            "decision_score",
            "decision_confidence",
            "decision_quality_score",
            "strategy_readiness_score",
        ]

        for col in cols_to_check:
            if col in df.columns:
                invalid = df[(df[col] < 0.0) | (df[col] > 1.0)]
                invalid_count += len(invalid)

    return {"invalid_score_count": invalid_count}


def check_decision_duplicates(df: pd.DataFrame) -> Dict:
    dup_count = 0
    if df is not None and not df.empty and "decision_id" in df.columns:
        dup_count = df.duplicated(subset=["decision_id"]).sum()
    return {"duplicate_decision_count": int(dup_count)}


def check_missing_decision_fields(df: pd.DataFrame) -> Dict:
    missing = []
    if df is not None and not df.empty:
        required = [
            "symbol",
            "timeframe",
            "decision_id",
            "decision_label",
            "directional_bias",
            "decision_score",
        ]
        missing = [c for c in required if c not in df.columns]
    return {"missing_required_fields": missing}


def check_for_forbidden_trade_terms(df: pd.DataFrame) -> Dict:
    found = []
    if df is not None and not df.empty:
        for col in df.select_dtypes(include=["object"]):
            for term in _FORBIDDEN_TERMS:
                if df[col].astype(str).str.lower().str.contains(term).any():
                    found.append(f"{term} in {col}")
    return {"forbidden_trade_terms_found": found}


def check_decision_dataframe(df: pd.DataFrame) -> Dict:
    res = {}
    res.update(check_decision_score_ranges(df))
    res.update(check_decision_duplicates(df))
    res.update(check_missing_decision_fields(df))
    res.update(check_for_forbidden_trade_terms(df))
    return res


def build_decision_quality_report(df: pd.DataFrame, summary: Dict) -> Dict:
    checks = check_decision_dataframe(df)

    rows = len(df) if df is not None else 0
    passed_ratio = summary.get("passed_decisions", 0) / rows if rows > 0 else 0.0

    passed = (
        checks["invalid_score_count"] == 0
        and checks["duplicate_decision_count"] == 0
        and len(checks["missing_required_fields"]) == 0
        and len(checks["forbidden_trade_terms_found"]) == 0
    )

    report = {
        "rows": rows,
        "duplicate_decision_count": checks["duplicate_decision_count"],
        "invalid_score_count": checks["invalid_score_count"],
        "missing_required_fields": checks["missing_required_fields"],
        "forbidden_trade_terms_found": checks["forbidden_trade_terms_found"],
        "passed_decision_ratio": passed_ratio,
        "warning_count": checks["invalid_score_count"]
        + len(checks["missing_required_fields"])
        + len(checks["forbidden_trade_terms_found"]),
        "passed": passed,
    }

    return report
