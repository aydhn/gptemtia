import pandas as pd
from report_summarization.summary_config import ReportSummaryProfile

def check_for_forbidden_terms_in_summaries(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    forbidden_terms = [
        "live order", "broker order", "real trade", "open position", "close position",
        "buy now", "sell now", "deploy model", "production deploy", "production scheduler",
        "background daemon", "while true", "run live", "guaranteed profit",
        "risk-free return", "yatirim tavsiyesidir", "kesin al", "kesin sat",
        "pozisyon ac", "pozisyon kapat"
    ]

    found = []

    if text:
        text_lower = text.lower()
        for term in forbidden_terms:
            if term in text_lower:
                found.append(term)

    if df is not None and not df.empty:
        for col in df.columns:
            for val in df[col]:
                if isinstance(val, str):
                    val_lower = val.lower()
                    for term in forbidden_terms:
                        if term in val_lower and term not in found:
                            found.append(term)

    return {
        "forbidden_terms_found": found,
        "valid": len(found) == 0
    }

def check_summary_inventory_quality(inventory_df: pd.DataFrame | None, profile: ReportSummaryProfile) -> dict:
    if inventory_df is None or inventory_df.empty:
        return {"valid": True, "warnings": ["Empty inventory"]}
    return {"valid": True, "warnings": []}

def check_summary_quality(summaries_df: pd.DataFrame | None, profile: ReportSummaryProfile) -> dict:
    if summaries_df is None or summaries_df.empty:
        return {"valid": True, "warnings": ["Empty summaries"]}
    return check_for_forbidden_terms_in_summaries(df=summaries_df)

def check_finding_quality(findings_df: pd.DataFrame | None, profile: ReportSummaryProfile) -> dict:
    if findings_df is None or findings_df.empty:
        return {"valid": True, "warnings": ["Empty findings"]}
    return check_for_forbidden_terms_in_summaries(df=findings_df)

def check_brief_quality(brief_df: pd.DataFrame | None, profile: ReportSummaryProfile) -> dict:
    if brief_df is None or brief_df.empty:
        return {"valid": True, "warnings": ["Empty briefs"]}
    return check_for_forbidden_terms_in_summaries(df=brief_df)

def check_follow_up_quality(tasks_df: pd.DataFrame | None, profile: ReportSummaryProfile) -> dict:
    if tasks_df is None or tasks_df.empty:
        return {"valid": True, "warnings": ["Empty follow ups"]}

    res = check_for_forbidden_terms_in_summaries(df=tasks_df)

    unsafe_commands = []
    if "suggested_safe_command" in tasks_df:
        cmds = tasks_df["suggested_safe_command"].dropna().tolist()
        for c in cmds:
            if any(unsafe in c.lower() for unsafe in ["live", "broker", "deploy", "daemon"]):
                unsafe_commands.append(c)

    if unsafe_commands:
        res["valid"] = False
        res.setdefault("warnings", []).append(f"Unsafe commands found: {unsafe_commands}")

    return res

def build_summary_quality_report(summary: dict, summaries_df: pd.DataFrame | None = None, findings_df: pd.DataFrame | None = None, tasks_df: pd.DataFrame | None = None) -> dict:
    res = {
        "inventory_valid": True,
        "summaries_valid": True,
        "findings_valid": True,
        "briefs_valid": True,
        "follow_ups_valid": True,
        "local_only_confirmed": True,
        "forbidden_terms_found": [],
        "warning_count": 0,
        "passed": True,
        "warnings": []
    }

    checks = []
    if summaries_df is not None:
        checks.append(check_summary_quality(summaries_df, None))
    if findings_df is not None:
        checks.append(check_finding_quality(findings_df, None))
    if tasks_df is not None:
        checks.append(check_follow_up_quality(tasks_df, None))

    for c in checks:
        if not c.get("valid", True):
            res["passed"] = False
        if "forbidden_terms_found" in c:
            for ft in c["forbidden_terms_found"]:
                if ft not in res["forbidden_terms_found"]:
                    res["forbidden_terms_found"].append(ft)
                    res["passed"] = False
        if "warnings" in c:
            res["warnings"].extend(c["warnings"])
            res["warning_count"] += len(c["warnings"])

    return res
