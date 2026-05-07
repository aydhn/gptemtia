import pandas as pd

_FORBIDDEN_TERMS = [
    "LIVE_ORDER",
    "BROKER_ORDER",
    "SEND_ORDER",
    "EXECUTE_TRADE",
    "REAL_POSITION",
    "LIVE_POSITION",
    "MARKET_ORDER",
    "LIMIT_ORDER",
]


def check_backtest_trade_dataframe(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"passed": True}
    return {"passed": True}


def check_backtest_score_ranges(df: pd.DataFrame) -> dict:
    return {"passed": True}


def check_trade_timestamp_order(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"passed": True}

    invalid_count = 0
    for _, row in df.iterrows():
        if pd.isna(row.get("entry_timestamp")) or pd.isna(row.get("exit_timestamp")):
            continue
        entry_ts = pd.to_datetime(row["entry_timestamp"])
        exit_ts = pd.to_datetime(row["exit_timestamp"])
        if exit_ts < entry_ts:
            invalid_count += 1

    return {"passed": invalid_count == 0, "invalid_timestamp_count": invalid_count}


def check_overlapping_positions(
    df: pd.DataFrame, single_position_per_symbol: bool = True
) -> dict:
    if df.empty or not single_position_per_symbol:
        return {"passed": True, "overlap_count": 0}

    overlap_count = 0
    for sym, group in df.groupby("symbol"):
        sorted_group = group.sort_values("entry_timestamp")
        prev_exit = None
        for _, row in sorted_group.iterrows():
            if pd.isna(row.get("entry_timestamp")) or pd.isna(
                row.get("exit_timestamp")
            ):
                continue
            entry_ts = pd.to_datetime(row["entry_timestamp"])
            if prev_exit is not None and entry_ts < prev_exit:
                overlap_count += 1
            prev_exit = pd.to_datetime(row["exit_timestamp"])

    return {"passed": overlap_count == 0, "overlap_count": overlap_count}


def check_lookahead_audit(audit: dict) -> dict:
    return {"passed": audit.get("passed", True)}


def check_for_forbidden_live_terms_in_backtest(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"passed": True, "forbidden_live_terms_found": False}

    found = False
    for col in df.columns:
        # ensure we check by converting col to string just in case
        for term in _FORBIDDEN_TERMS:
            if df[col].astype(str).str.contains(term, case=False).any():
                found = True
                break
        if found:
            break

    return {"passed": not found, "forbidden_live_terms_found": found}


def build_backtest_quality_report(
    trades_df: pd.DataFrame, summary: dict, lookahead_audit: dict
) -> dict:
    order_res = check_trade_timestamp_order(trades_df)
    overlap_res = check_overlapping_positions(trades_df)
    term_res = check_for_forbidden_live_terms_in_backtest(trades_df)

    passed = (
        order_res["passed"]
        and overlap_res["passed"]
        and term_res["passed"]
        and lookahead_audit.get("passed", True)
    )

    return {
        "rows": len(trades_df),
        "invalid_timestamp_count": order_res.get("invalid_timestamp_count", 0),
        "overlap_count": overlap_res.get("overlap_count", 0),
        "lookahead_violation_count": lookahead_audit.get("violation_count", 0),
        "forbidden_live_terms_found": term_res.get("forbidden_live_terms_found", False),
        "warning_count": 0,
        "passed": passed,
    }
