from typing import Optional, Dict, List
import pandas as pd
from report_exports.export_models import ReportComparisonResult, build_comparison_id

def compare_research_scores(current: Dict, previous: Optional[Dict]) -> Dict:
    if not previous or previous.get("research_score") is None:
        return {"delta": None, "label": "insufficient_history"}
    curr_score = current.get("research_score")
    if curr_score is None:
        return {"delta": None, "label": "comparison_unknown"}
    prev_score = previous.get("research_score")
    delta = curr_score - prev_score
    if delta > 0.05:
        label = "improved"
    elif delta < -0.05:
        label = "deteriorated"
    else:
        label = "unchanged"
    return {"delta": delta, "label": label}

def compare_warning_counts(current: Dict, previous: Optional[Dict]) -> Dict:
    if not previous or previous.get("warning_count") is None:
        return {"delta": None}
    curr_count = current.get("warning_count", 0)
    prev_count = previous.get("warning_count", 0)
    return {"delta": curr_count - prev_count}

def compare_missing_sources(current: Dict, previous: Optional[Dict]) -> Dict:
    if not previous or previous.get("missing_sources_count") is None:
        return {"delta": None}
    curr_count = current.get("missing_sources_count", 0)
    prev_count = previous.get("missing_sources_count", 0)
    return {"delta": curr_count - prev_count}

def compare_report_sections(current_report: Dict, previous_report: Optional[Dict]) -> Dict:
    return {"changed_sections": []}

def compare_archive_records(current: Dict, previous: Optional[Dict]) -> ReportComparisonResult:
    comp_id = build_comparison_id(current.get("report_id", "unknown"), previous.get("report_id") if previous else None)
    score_comp = compare_research_scores(current, previous)
    warning_comp = compare_warning_counts(current, previous)
    missing_comp = compare_missing_sources(current, previous)
    section_comp = compare_report_sections(current, previous)
    warnings = []
    if previous is None:
        warnings.append("No previous report found for comparison.")
    elif warning_comp.get("delta") and warning_comp["delta"] > 0:
        warnings.append("Warning count increased since last report.")
    elif missing_comp.get("delta") and missing_comp["delta"] > 0:
        warnings.append("Missing data sources increased since last report.")
    return ReportComparisonResult(
        comparison_id=comp_id,
        current_report_id=current.get("report_id", "unknown"),
        previous_report_id=previous.get("report_id") if previous else None,
        symbol=current.get("symbol"),
        timeframe=current.get("timeframe", "unknown"),
        comparison_label=score_comp["label"],
        score_delta=score_comp["delta"],
        warning_delta=warning_comp["delta"],
        missing_sources_delta=missing_comp["delta"],
        changed_sections=section_comp["changed_sections"],
        summary={"disclaimer": "Comparison is not a trade signal."},
        warnings=warnings
    )

def build_report_comparison_table(comparisons: List[ReportComparisonResult]) -> pd.DataFrame:
    from report_exports.export_models import report_comparison_result_to_dict
    dicts = [report_comparison_result_to_dict(c) for c in comparisons]
    return pd.DataFrame(dicts)

def summarize_report_comparisons(comparison_df: pd.DataFrame) -> Dict:
    if comparison_df.empty:
        return {"total_comparisons": 0}
    return {
        "total_comparisons": len(comparison_df),
        "improved_count": int((comparison_df["comparison_label"] == "improved").sum()),
        "deteriorated_count": int((comparison_df["comparison_label"] == "deteriorated").sum()),
        "unchanged_count": int((comparison_df["comparison_label"] == "unchanged").sum())
    }
