import pandas as pd

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
]


def check_rule_candidate_dataframe(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"passed": True, "reason": "empty_dataframe"}

    res_ranges = check_rule_score_ranges(df)
    res_dup = check_rule_candidate_duplicates(df)
    res_miss = check_missing_rule_fields(df)
    res_forb = check_for_forbidden_order_terms_in_rules(df)

    passed = (
        res_ranges["passed"]
        and res_dup["passed"]
        and res_miss["passed"]
        and res_forb["passed"]
    )

    return {
        "passed": passed,
        "score_ranges": res_ranges,
        "duplicates": res_dup,
        "missing_fields": res_miss,
        "forbidden_terms": res_forb,
    }


def check_rule_score_ranges(df: pd.DataFrame) -> dict:
    invalid_count = 0
    cols_to_check = [
        "match_score",
        "confidence_score",
        "quality_score",
        "readiness_score",
        "conflict_score",
    ]

    for col in cols_to_check:
        if col in df.columns:
            invalid = df[(df[col] < 0.0) | (df[col] > 1.0)]
            invalid_count += len(invalid)

    return {"passed": invalid_count == 0, "invalid_score_count": invalid_count}


def check_rule_candidate_duplicates(df: pd.DataFrame) -> dict:
    dup_count = 0
    if "condition_id" in df.columns:
        dup_count = df.duplicated(subset=["condition_id"]).sum()

    return {"passed": dup_count == 0, "duplicate_condition_count": int(dup_count)}


def check_missing_rule_fields(df: pd.DataFrame) -> dict:
    required_cols = [
        "symbol",
        "timeframe",
        "condition_id",
        "rule_id",
        "rule_group",
        "condition_label",
        "rule_status",
        "match_score",
    ]
    missing = [col for col in required_cols if col not in df.columns]

    return {"passed": len(missing) == 0, "missing_required_fields": missing}


def check_for_forbidden_order_terms_in_rules(df: pd.DataFrame) -> dict:
    forbidden_found = []

    for col in df.columns:
        if df[col].dtype == object or pd.api.types.is_string_dtype(df[col]):
            text_series = df[col].astype(str).str.upper()
            for term in _FORBIDDEN_TERMS:
                if text_series.str.contains(term).any():
                    forbidden_found.append(f"{col}:{term}")

    return {
        "passed": len(forbidden_found) == 0,
        "forbidden_order_terms_found": forbidden_found,
    }


def build_rule_quality_report(df: pd.DataFrame, summary: dict) -> dict:
    quality_res = check_rule_candidate_dataframe(df)

    passed_ratio = 0.0
    if not df.empty and "passed_rule_filters" in df.columns:
        passed_ratio = df["passed_rule_filters"].mean()

    return {
        "rows": len(df),
        "passed": quality_res["passed"],
        "duplicate_condition_count": quality_res["duplicates"][
            "duplicate_condition_count"
        ],
        "invalid_score_count": quality_res["score_ranges"]["invalid_score_count"],
        "missing_required_fields": quality_res["missing_fields"][
            "missing_required_fields"
        ],
        "forbidden_order_terms_found": quality_res["forbidden_terms"][
            "forbidden_order_terms_found"
        ],
        "passed_rule_ratio": float(passed_ratio),
        "warning_count": len(summary.get("warnings", [])),
    }
