import pandas as pd
from report_summarization.summary_config import ReportSummaryProfile
from report_summarization.summary_models import ExtractedFinding, build_finding_id
from report_summarization.text_summarizer import split_text_into_sentences, mask_sensitive_summary_text

def extract_risks_and_gaps(source_report_id: str, source_path: str, module_name: str, text: str, profile: ReportSummaryProfile) -> list[ExtractedFinding]:
    sentences = split_text_into_sentences(text)
    risks_gaps = []

    rg_patterns = [
        "risk", "gap", "missing", "bottleneck", "failure", "stale", "drift"
    ]

    for s in sentences:
        s_lower = s.lower()
        if any(pat in s_lower for pat in rg_patterns):
            cleaned = mask_sensitive_summary_text(s)

            rg = ExtractedFinding(
                finding_id=build_finding_id(source_report_id, cleaned),
                source_report_id=source_report_id,
                source_path=source_path,
                module_name=module_name,
                finding_type="gap_finding" if "gap" in s_lower or "missing" in s_lower else "risk_finding",
                priority=classify_risk_gap_priority(s_lower),
                text=cleaned,
                related_symbols=[],
                related_modules=[],
                warnings=[]
            )
            risks_gaps.append(rg)

    return risks_gaps

def classify_risk_gap_priority(text: str) -> str:
    if "critical" in text or "failure" in text:
        return "critical_priority"
    if "high" in text:
        return "high_priority"
    return "medium_priority"

def build_risk_gap_summary_table(findings_df: pd.DataFrame) -> pd.DataFrame:
    if findings_df.empty:
        return pd.DataFrame()
    mask = findings_df["finding_type"].isin(["risk_finding", "gap_finding"])
    return findings_df[mask][["module_name", "finding_type", "priority", "text", "source_path"]].copy()

def summarize_risks_and_gaps(risk_gap_df: pd.DataFrame) -> dict:
    if risk_gap_df.empty:
        return {"total_risks_gaps": 0}
    return {
        "total_risks_gaps": len(risk_gap_df),
        "risks": len(risk_gap_df[risk_gap_df["finding_type"] == "risk_finding"]),
        "gaps": len(risk_gap_df[risk_gap_df["finding_type"] == "gap_finding"])
    }
