import pandas as pd
from report_summarization.summary_config import ReportSummaryProfile
from report_summarization.summary_models import ExtractedFinding, build_finding_id
from report_summarization.text_summarizer import split_text_into_sentences, mask_sensitive_summary_text

def extract_warning_lines(source_report_id: str, source_path: str, module_name: str, text: str, profile: ReportSummaryProfile) -> list[ExtractedFinding]:
    sentences = split_text_into_sentences(text)
    warnings = []

    warning_patterns = [
        "warning", "caution", "blocked", "failed", "missing", "unsafe",
        "forbidden", "critical", "high risk", "canli emir", "broker",
        "deploy", "daemon", "scraping", "yatirim tavsiyesi"
    ]

    for s in sentences:
        s_lower = s.lower()
        if any(pat in s_lower for pat in warning_patterns):
            if "canli emir yoktur" in s_lower or "yatirim tavsiyesi degildir" in s_lower or "broker entegrasyonu yoktur" in s_lower:
                priority = "low_priority"
            else:
                priority = classify_warning_priority(s_lower)

            cleaned = mask_sensitive_summary_text(s)

            w = ExtractedFinding(
                finding_id=build_finding_id(source_report_id, cleaned),
                source_report_id=source_report_id,
                source_path=source_path,
                module_name=module_name,
                finding_type="warning_finding",
                priority=priority,
                text=cleaned,
                related_symbols=[],
                related_modules=[],
                warnings=[]
            )
            warnings.append(w)

            if len(warnings) >= profile.max_warnings:
                break

    return warnings

def classify_warning_priority(text: str) -> str:
    if "critical" in text or "blocked" in text or "failed" in text or "forbidden" in text:
        return "critical_priority"
    return "high_priority"

def group_warnings_by_module(warnings_df: pd.DataFrame) -> pd.DataFrame:
    if warnings_df.empty:
        return pd.DataFrame()
    return warnings_df.groupby("module_name").size().reset_index(name="warning_count")

def build_warning_summary_table(warnings_df: pd.DataFrame) -> pd.DataFrame:
    if warnings_df.empty:
        return pd.DataFrame()
    return warnings_df[["module_name", "priority", "text", "source_path"]].copy()

def summarize_warnings(warnings_df: pd.DataFrame) -> dict:
    if warnings_df.empty:
        return {"total_warnings": 0}
    return {
        "total_warnings": len(warnings_df),
        "critical_warnings": len(warnings_df[warnings_df["priority"] == "critical_priority"]),
        "modules_with_warnings": warnings_df["module_name"].nunique()
    }
