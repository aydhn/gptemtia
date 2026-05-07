import pandas as pd
from levels.level_models import is_valid_level_for_direction

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
    "TRAILING_STOP_ORDER",
    "SEND_ORDER",
    "EXECUTE_TRADE",
    "LIVE_POSITION",
    "BROKER_ORDER",
]


def check_level_candidate_dataframe(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"error": "Empty dataframe"}
    return {"passed": True}


def check_level_score_ranges(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"invalid_score_count": 0}

    invalid_count = 0
    score_cols = ["stop_target_readiness_score", "stop_target_quality_score"]

    for col in score_cols:
        if col in df.columns:
            invalid = df[(df[col] < 0.0) | (df[col] > 1.0)]
            invalid_count += len(invalid)

    return {"invalid_score_count": invalid_count}


def check_level_candidate_duplicates(df: pd.DataFrame) -> dict:
    if df.empty or "level_id" not in df.columns:
        return {"duplicate_level_count": 0}

    dupes = df.duplicated(subset=["level_id"]).sum()
    return {"duplicate_level_count": int(dupes)}


def check_missing_level_fields(df: pd.DataFrame) -> dict:
    required = ["symbol", "timeframe", "level_id", "level_label"]
    missing = [c for c in required if c not in df.columns]
    return {"missing_required_fields": missing}


def check_invalid_level_geometry(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"invalid_geometry_count": 0}

    invalid_count = 0
    for _, row in df.iterrows():
        bias = row.get("directional_bias", "neutral")
        price = row.get("latest_close")
        stop = row.get("theoretical_stop_level")
        tgt = row.get("theoretical_target_level")

        if bias in ["neutral", "no_trade_candidate"]:
            continue

        if pd.notna(stop) and not is_valid_level_for_direction(
            price, stop, bias, "stop"
        ):
            invalid_count += 1
        elif pd.notna(tgt) and not is_valid_level_for_direction(
            price, tgt, bias, "target"
        ):
            invalid_count += 1

    return {"invalid_geometry_count": invalid_count}


def check_for_forbidden_trade_terms_in_levels(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"forbidden_trade_terms_found": False, "terms": []}

    found_terms = set()
    text_cols = df.select_dtypes(include=["object", "string"]).columns

    for col in text_cols:
        col_texts = df[col].dropna().astype(str).str.upper()
        for term in _FORBIDDEN_TRADE_TERMS:
            if col_texts.str.contains(term).any():
                found_terms.add(term)

    return {
        "forbidden_trade_terms_found": len(found_terms) > 0,
        "terms": list(found_terms),
    }


def build_level_quality_report(df: pd.DataFrame, summary: dict) -> dict:
    report = {
        "rows": len(df),
        "passed": True,
        "warning_count": 0,
        "passed_level_ratio": 0.0,
    }

    if df.empty:
        report["passed"] = False
        return report

    passed_count = len(
        df[df.get("passed_level_filters", pd.Series(False, index=df.index)) == True]
    )
    report["passed_level_ratio"] = passed_count / len(df) if len(df) > 0 else 0.0

    scores = check_level_score_ranges(df)
    report["invalid_score_count"] = scores["invalid_score_count"]

    dupes = check_level_candidate_duplicates(df)
    report["duplicate_level_count"] = dupes["duplicate_level_count"]

    missing = check_missing_level_fields(df)
    report["missing_required_fields"] = missing["missing_required_fields"]

    geom = check_invalid_level_geometry(df)
    report["invalid_geometry_count"] = geom["invalid_geometry_count"]

    forbidden = check_for_forbidden_trade_terms_in_levels(df)
    report["forbidden_trade_terms_found"] = forbidden["forbidden_trade_terms_found"]
    if forbidden["forbidden_trade_terms_found"]:
        report["passed"] = False

    warnings = 0
    if scores["invalid_score_count"] > 0:
        warnings += 1
    if dupes["duplicate_level_count"] > 0:
        warnings += 1
    if geom["invalid_geometry_count"] > 0:
        warnings += 1
    report["warning_count"] = warnings

    return report
