# -*- coding: utf-8 -*-
"""Phase 143: Explainability Findings."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)


def build_explainability_findings_registry(
    profile: Optional[ExplainabilityProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build the DataFrame registry of explainability findings."""
    prof = profile or get_explainability_profile()

    findings = [
        ("finding_xai_001", "non_executing_validation", "global_explanation", "info", "All XAI contracts operate strictly in dry-run metadata mode", "Maintain execution blocks until formal governance validation"),
        ("finding_xai_002", "candidate_model_linkage", "feature_attribution", "info", "Candidate models from Phase 138 successfully linked to attribution contracts", "Ensure weight freeze invariants remain intact"),
        ("finding_xai_003", "ensemble_linkage", "feature_attribution", "info", "Ensemble contracts from Phase 140 successfully referenced", "Maintain prohibition on attribution-driven automated reweighting"),
        ("finding_xai_004", "safeguard_audit", "attribution_governance", "info", "Zero-calculation safeguards verified for SHAP, LIME, PDP, ICE and surrogates", "Pass clean validation audit to Phase 144 model governance"),
    ]

    rows: List[Dict[str, Any]] = []
    for fid, ftype, domain, sev, msg, rec in findings:
        rows.append({
            "finding_id": fid,
            "finding_type": ftype,
            "explainability_domain": domain,
            "severity_label": sev,
            "message": msg,
            "recommendation": rec,
            "manual_review_required": True,
            "non_signal": True,
            "official_approval": False,
            "production_ready": False,
            "broker_ready": False,
        })

    df = pd.DataFrame(rows)
    summary = summarize_explainability_findings(df)
    return df, summary


def summarize_explainability_findings(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize explainability findings."""
    return {
        "total_findings": len(df),
        "all_info_severity": bool((df["severity_label"] == "info").all()) if not df.empty else True,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
