import pandas as pd
import re
from report_summarization.summary_config import ReportSummaryProfile
from report_summarization.summary_models import ExtractedFinding, build_finding_id
from report_summarization.text_summarizer import split_text_into_sentences, mask_sensitive_summary_text

def extract_findings_from_text(source_report_id: str, source_path: str, module_name: str, text: str, profile: ReportSummaryProfile) -> list[ExtractedFinding]:
    sentences = split_text_into_sentences(text)
    findings = []

    finding_keywords = [
        "missing", "failed", "warning", "blocked", "gap", "risk", "drift", "stale",
        "over_budget", "safety", "quality", "regression", "acceptance", "maintenance",
        "documentation", "final review", "governance", "experiment", "planning"
    ]

    for s in sentences:
        s_lower = s.lower()
        if any(kw in s_lower for kw in finding_keywords):
            cleaned = mask_sensitive_summary_text(s)
            finding_type = classify_finding_type(cleaned)
            priority = infer_finding_priority(cleaned)
            related_symbols = extract_related_symbols(cleaned)
            related_modules = extract_related_modules(cleaned)

            f = ExtractedFinding(
                finding_id=build_finding_id(source_report_id, cleaned),
                source_report_id=source_report_id,
                source_path=source_path,
                module_name=module_name,
                finding_type=finding_type,
                priority=priority,
                text=cleaned,
                related_symbols=related_symbols,
                related_modules=related_modules,
                warnings=[]
            )
            findings.append(f)

            if len(findings) >= profile.max_findings:
                break

    return findings

def classify_finding_type(text: str) -> str:
    text_lower = text.lower()
    if "warning" in text_lower: return "warning_finding"
    if "risk" in text_lower: return "risk_finding"
    if "gap" in text_lower or "missing" in text_lower: return "gap_finding"
    if "quality" in text_lower: return "quality_finding"
    if "safety" in text_lower or "forbidden" in text_lower: return "safety_finding"
    if "performance" in text_lower: return "performance_finding"
    if "maintenance" in text_lower or "stale" in text_lower: return "maintenance_finding"
    if "scenario" in text_lower or "regression" in text_lower: return "scenario_finding"
    if "doc" in text_lower: return "documentation_finding"
    return "key_finding"

def infer_finding_priority(text: str) -> str:
    text_lower = text.lower()
    if "critical" in text_lower or "failed" in text_lower or "blocked" in text_lower:
        return "critical_priority"
    if "warning" in text_lower or "high" in text_lower or "risk" in text_lower:
        return "high_priority"
    if "missing" in text_lower or "gap" in text_lower:
        return "medium_priority"
    return "low_priority"

def extract_related_symbols(text: str) -> list[str]:
    known_symbols = [
        "GC=F", "SI=F", "HG=F", "PA=F", "PL=F", "CL=F", "BZ=F", "NG=F",
        "ZW=F", "ZC=F", "ZS=F", "KC=F", "CC=F", "SB=F", "CT=F",
        "USDTRY=X", "EURTRY=X", "GBPTRY=X", "JPYTRY=X", "CNHTRY=X"
    ]
    found = []
    for sym in known_symbols:
        if sym in text:
            found.append(sym)
    return found

def extract_related_modules(text: str) -> list[str]:
    modules = [
        "research_reports", "report_exports", "portfolio", "synthetic",
        "factor", "meta", "experiment", "governance", "planning",
        "knowledge", "command", "quality", "performance", "maintenance",
        "doc", "review", "scenario", "ux", "summary"
    ]
    found = []
    text_lower = text.lower()
    for m in modules:
        if m in text_lower:
            found.append(m)
    return found

def findings_to_dataframe(findings: list[ExtractedFinding]) -> pd.DataFrame:
    if not findings:
        return pd.DataFrame(columns=[
            "finding_id", "source_report_id", "source_path", "module_name",
            "finding_type", "priority", "text", "related_symbols", "related_modules", "warnings"
        ])
    return pd.DataFrame([f.__dict__ for f in findings])

def summarize_findings(findings_df: pd.DataFrame) -> dict:
    if findings_df.empty:
        return {"total_findings": 0}

    return {
        "total_findings": len(findings_df),
        "by_type": findings_df["finding_type"].value_counts().to_dict() if "finding_type" in findings_df else {},
        "by_priority": findings_df["priority"].value_counts().to_dict() if "priority" in findings_df else {},
        "critical_count": len(findings_df[findings_df["priority"] == "critical_priority"]) if "priority" in findings_df else 0
    }
