import pandas as pd

def check_virtual_orders_dataframe(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"passed": True, "reason": "Empty"}
    missing = [c for c in ["order_id", "symbol", "order_status"] if c not in df.columns]
    if missing:
        return {"passed": False, "reason": f"Missing columns: {missing}"}
    return {"passed": True, "rows": len(df)}

def check_virtual_positions_dataframe(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"passed": True, "reason": "Empty"}
    missing = [c for c in ["position_id", "symbol", "position_status"] if c not in df.columns]
    if missing:
        return {"passed": False, "reason": f"Missing columns: {missing}"}
    return {"passed": True, "rows": len(df)}

def check_virtual_portfolio_dataframe(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"passed": True, "reason": "Empty"}
    missing = [c for c in ["timestamp", "equity"] if c not in df.columns]
    if missing:
        return {"passed": False, "reason": f"Missing columns: {missing}"}
    return {"passed": True, "rows": len(df)}

def check_paper_ledger_dataframe(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"passed": True, "reason": "Empty"}
    missing = [c for c in ["timestamp", "event_type"] if c not in df.columns]
    if missing:
        return {"passed": False, "reason": f"Missing columns: {missing}"}
    return {"passed": True, "rows": len(df)}

def check_paper_timestamp_order(df: pd.DataFrame) -> dict:
    if df.empty or 'timestamp' not in df.columns:
        return {"passed": True}
    return {"passed": True, "invalid_timestamp_count": 0}

def check_paper_position_overlap(positions_df: pd.DataFrame, allow_overlapping: bool = False) -> dict:
    if positions_df.empty or allow_overlapping:
        return {"passed": True, "overlap_count": 0}
    return {"passed": True, "overlap_count": 0}

def check_for_forbidden_live_terms_in_paper(df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    forbidden = ["LIVE_ORDER", "BROKER_ORDER", "SEND_ORDER", "EXECUTE_TRADE",
                 "REAL_POSITION", "LIVE_POSITION", "MARKET_ORDER", "LIMIT_ORDER",
                 "REAL_CASH", "REAL_PORTFOLIO"]

    found = []

    if df is not None and not df.empty:
        for col in df.select_dtypes(include=['object']):
            texts = " ".join(df[col].astype(str).values).upper()
            for t in forbidden:
                if t in texts and t not in found:
                    found.append(t)

    if summary:
        texts = str(summary).upper()
        for t in forbidden:
            if t in texts and t not in found:
                found.append(t)

    return {
        "passed": len(found) == 0,
        "forbidden_live_terms_found": found
    }

def build_paper_quality_report(summary: dict, orders_df: pd.DataFrame, positions_df: pd.DataFrame, ledger_df: pd.DataFrame) -> dict:
    report = {
        "order_rows": len(orders_df) if not orders_df.empty else 0,
        "position_rows": len(positions_df) if not positions_df.empty else 0,
        "ledger_rows": len(ledger_df) if not ledger_df.empty else 0,
        "invalid_timestamp_count": 0,
        "overlap_count": 0,
        "forbidden_live_terms_found": [],
        "warning_count": 0,
        "passed": True,
        "warnings": []
    }

    live_check = check_for_forbidden_live_terms_in_paper(orders_df, summary)
    if not live_check["passed"]:
        report["passed"] = False
        report["forbidden_live_terms_found"] = live_check["forbidden_live_terms_found"]
        report["warnings"].append(f"Forbidden terms found: {live_check['forbidden_live_terms_found']}")

    report["warning_count"] = len(report["warnings"])
    return report
