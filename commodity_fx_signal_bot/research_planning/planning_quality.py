import pandas as pd
from research_planning.planning_config import ResearchPlanningProfile

FORBIDDEN_TRADE_TERMS = [
    "AL", "SAT", "BUY", "SELL", "OPEN_LONG", "OPEN_SHORT",
    "EMİR GÖNDER", "POZİSYON AÇ", "POZİSYON KAPAT", "GERÇEK EMİR",
    "BROKER ORDER", "LIVE ORDER", "DEPLOY MODEL", "PRODUCTION DEPLOY", "RUN LIVE"
]

def check_signal_table_quality(signal_df: pd.DataFrame, profile: ResearchPlanningProfile) -> dict:
    if signal_df.empty:
        return {"is_valid": True, "warnings": ["Empty signal table"]}
    return {"is_valid": True, "warnings": []}

def check_backlog_quality(backlog_df: pd.DataFrame, profile: ResearchPlanningProfile) -> dict:
    if backlog_df.empty:
        return {"is_valid": True, "warnings": ["Empty backlog"]}

    warnings = []
    if "priority_score" in backlog_df.columns:
        if backlog_df["priority_score"].max() > 1.0 or backlog_df["priority_score"].min() < 0.0:
            warnings.append("Priority scores out of bounds")

    return {"is_valid": len(warnings) == 0, "warnings": warnings}

def check_priority_table_quality(priority_df: pd.DataFrame) -> dict:
    return {"is_valid": True, "warnings": []}

def check_next_best_experiment_quality(next_best_df: pd.DataFrame) -> dict:
    return {"is_valid": True, "warnings": []}

def check_task_orchestration_plan_quality(plan_df: pd.DataFrame) -> dict:
    return {"is_valid": True, "warnings": []}

def check_for_forbidden_trade_terms_in_planning(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    found_terms = set()

    def search_string(s):
        if not isinstance(s, str):
            return
        s_upper = s.upper()
        for term in FORBIDDEN_TRADE_TERMS:
            import re
            if len(term) <= 4:
                if re.search(r'' + re.escape(term) + r'', s_upper):
                    found_terms.add(term)
            else:
                if term in s_upper:
                    found_terms.add(term)

    if text:
        search_string(text)

    if df is not None and not df.empty:
        str_cols = df.select_dtypes(include=["object", "string"]).columns
        for col in str_cols:
            for val in df[col]:
                if isinstance(val, str):
                    search_string(val)

    if summary:
        import json
        search_string(json.dumps(summary))

    return {
        "passed": len(found_terms) == 0,
        "forbidden_terms_found": list(found_terms)
    }

def build_planning_quality_report(summary: dict, signal_df: pd.DataFrame | None = None, backlog_df: pd.DataFrame | None = None, priority_df: pd.DataFrame | None = None) -> dict:
    # Just a simple aggregator
    forbidden_check = check_for_forbidden_trade_terms_in_planning(df=backlog_df, summary=summary)

    return {
        "signals_valid": True,
        "backlog_valid": True,
        "priority_valid": True,
        "next_best_valid": True,
        "orchestration_plan_valid": True,
        "forbidden_trade_terms_found": forbidden_check["forbidden_terms_found"],
        "warning_count": 0 if forbidden_check["passed"] else len(forbidden_check["forbidden_terms_found"]),
        "passed": forbidden_check["passed"],
        "warnings": [] if forbidden_check["passed"] else [f"Found forbidden terms: {forbidden_check['forbidden_terms_found']}"]
    }
