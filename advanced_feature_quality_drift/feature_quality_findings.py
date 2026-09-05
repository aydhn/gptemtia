"""Phase 123 Feature Quality Findings Registry.

Aggregates diagnostic quality findings across missingness, infinite values, all-NaN,
zero variance, duplicates, staleness, namespace, and factor levels.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_feature_quality_drift.feature_quality_drift_config import (
    FeatureQualityDriftProfile,
    get_default_feature_quality_drift_profile,
)


def build_feature_quality_findings_registry(
    profile: FeatureQualityDriftProfile | None = None,
    diagnostic_tables: Dict[str, pd.DataFrame] | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build standardized findings DataFrame across all quality diagnostic outputs."""
    active_profile = profile or get_default_feature_quality_drift_profile()
    records = []

    if diagnostic_tables:
        for tab_name, table in diagnostic_tables.items():
            if table is None or table.empty:
                continue
            if "manual_review_required" in table.columns:
                violations = table[table["manual_review_required"]]
                for _, row in violations.iterrows():
                    col = row.get("column", row.get("feature_column", "general"))
                    sev = row.get("severity", "quality_medium")
                    issue = row.get("notes", row.get("issue_description", f"Diagnostic flag in {tab_name}"))
                    records.append({
                        "finding_id": f"fqf_{tab_name}_{len(records)+1}",
                        "source_table": tab_name,
                        "feature_column": col,
                        "severity": sev,
                        "issue_description": issue,
                        "recommended_action": f"Inspect {tab_name} and verify feature computation pipeline",
                        "manual_review_required": True,
                        "destructive_action_allowed": False,
                        "non_signal": True,
                    })

    if not records:
        # Default nominal record when diagnostics pass cleanly
        records.append({
            "finding_id": "fqf_clean_baseline_1",
            "source_table": "feature_quality_baseline",
            "feature_column": "all_features",
            "severity": "quality_info",
            "issue_description": "Baseline feature quality checks completed with zero critical defects.",
            "recommended_action": "Maintain scheduled monitoring and metadata inspection",
            "manual_review_required": False,
            "destructive_action_allowed": False,
            "non_signal": True,
        })

    df = pd.DataFrame(records)
    summary = summarize_feature_quality_findings(df)
    summary["active_profile"] = active_profile.name
    summary["current_phase"] = active_profile.current_phase
    summary["target_final_phase"] = active_profile.target_final_phase
    summary["next_phase"] = active_profile.next_phase
    summary["non_signal"] = True
    summary["destructive_action_allowed"] = False
    return df, summary


def summarize_feature_quality_findings(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate overall summary statistics from feature quality findings DataFrame."""
    if df.empty:
        return {
            "total_findings": 0,
            "critical_findings": 0,
            "high_findings": 0,
            "medium_findings": 0,
            "info_findings": 0,
            "status": "diagnostic_pass",
            "manual_review_required": False,
        }

    total_f = len(df)
    crit_f = int((df["severity"] == "quality_critical").sum()) if "severity" in df.columns else 0
    high_f = int((df["severity"] == "quality_high").sum()) if "severity" in df.columns else 0
    med_f = int((df["severity"] == "quality_medium").sum()) if "severity" in df.columns else 0
    info_f = int((df["severity"] == "quality_info").sum()) if "severity" in df.columns else 0

    if crit_f > 0 or high_f > 0:
        status = "diagnostic_fail"
    elif med_f > 0:
        status = "diagnostic_pass_with_warnings"
    else:
        status = "diagnostic_pass"

    return {
        "total_findings": total_f,
        "critical_findings": crit_f,
        "high_findings": high_f,
        "medium_findings": med_f,
        "info_findings": info_f,
        "status": status,
        "manual_review_required": (crit_f + high_f + med_f) > 0,
    }
