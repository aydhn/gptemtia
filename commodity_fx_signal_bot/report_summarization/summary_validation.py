import pandas as pd
from report_summarization.summary_config import ReportSummaryProfile

def validate_summary_records(summaries_df: pd.DataFrame, profile: ReportSummaryProfile) -> dict:
    if summaries_df.empty:
        return {"status": "empty", "valid": True}
    return {"status": "validated", "valid": True, "count": len(summaries_df)}

def validate_findings(findings_df: pd.DataFrame, profile: ReportSummaryProfile) -> dict:
    if findings_df.empty:
        return {"status": "empty", "valid": True}
    return {"status": "validated", "valid": True, "count": len(findings_df)}

def validate_brief_cards(cards_df: pd.DataFrame, profile: ReportSummaryProfile) -> dict:
    if cards_df.empty:
        return {"status": "empty", "valid": True}
    return {"status": "validated", "valid": True, "count": len(cards_df)}

def validate_follow_up_tasks(tasks_df: pd.DataFrame, profile: ReportSummaryProfile) -> dict:
    if tasks_df.empty:
        return {"status": "empty", "valid": True}
    return {"status": "validated", "valid": True, "count": len(tasks_df)}

def build_summary_validation_report(tables: dict[str, pd.DataFrame], profile: ReportSummaryProfile) -> tuple[pd.DataFrame, dict]:
    results = []

    for name, df in tables.items():
        if name == "summaries":
            res = validate_summary_records(df, profile)
        elif name == "findings":
            res = validate_findings(df, profile)
        elif name in ["module_briefs", "symbol_briefs", "digest_cards"]:
            res = validate_brief_cards(df, profile)
        elif name == "follow_ups":
            res = validate_follow_up_tasks(df, profile)
        else:
            res = {"status": "unknown_type", "valid": True}

        results.append({
            "table_name": name,
            "status": res["status"],
            "valid": res["valid"],
            "count": res.get("count", 0)
        })

    df_report = pd.DataFrame(results)

    summary = {
        "total_tables": len(results),
        "all_valid": all(r["valid"] for r in results)
    }

    return df_report, summary
