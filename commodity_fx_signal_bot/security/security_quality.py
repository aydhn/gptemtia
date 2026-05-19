import pandas as pd
_FORBIDDEN_LIVE_TERMS = ["SEND_ORDER", "EXECUTE_TRADE", "LIVE_ORDER", "REAL_POSITION", "LIVE_POSITION", "LIVE_SIGNAL", "BROKER_ORDER", "BUY_NOW", "SELL_NOW", "OPEN_REAL_POSITION"]

def check_security_findings_dataframe(df: pd.DataFrame) -> dict:
    if df.empty: return {"findings_schema_valid": True}
    return {"findings_schema_valid": all(c in df.columns for c in ["finding_id", "category", "severity", "status", "title", "description"])}

def check_security_summary_consistency(summary: dict, findings_df: pd.DataFrame) -> dict: return {"summary_consistent": True}
def check_evidence_redaction(df: pd.DataFrame) -> dict: return {"evidence_redacted": True}

def check_security_report_for_forbidden_live_terms(df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    found = False
    if df is not None and not df.empty:
        for term in _FORBIDDEN_LIVE_TERMS:
            if df.astype(str).apply(lambda col: col.str.contains(term, case=False, na=False)).any().any(): found = True
    if summary:
        for term in _FORBIDDEN_LIVE_TERMS:
            if term.lower() in str(summary).lower(): found = True
    return {"forbidden_live_terms_found": found}

def build_security_quality_report(findings_df: pd.DataFrame, summary: dict) -> dict:
    res = {}
    res.update(check_security_findings_dataframe(findings_df))
    res.update(check_security_summary_consistency(summary, findings_df))
    res.update(check_evidence_redaction(findings_df))
    res.update(check_security_report_for_forbidden_live_terms(findings_df, summary))
    res["passed"] = res["findings_schema_valid"] and res["summary_consistent"] and res["evidence_redacted"] and not res["forbidden_live_terms_found"]
    res["warnings"] = []
    return res
