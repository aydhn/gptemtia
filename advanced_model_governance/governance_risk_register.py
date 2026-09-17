# -*- coding: utf-8 -*-
"""Phase 144: Governance Risk Register."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

RISK_REGISTER_ENTRIES: List[Dict[str, str]] = [
    {"risk_id": "REG-01", "risk_category": "data_quality_risk", "description": "Missing, noisy, or non-stationary input prices.", "impact_level": "HIGH", "mitigation_strategy": "Pre-check quality gates and validation dependencies.", "residual_risk": "LOW"},
    {"risk_id": "REG-02", "risk_category": "no_lookahead_risk", "description": "Inadvertent inclusion of future data or next return.", "impact_level": "CRITICAL", "mitigation_strategy": "Strict no-lookahead guards and chronological sort assertions.", "residual_risk": "VERY_LOW"},
    {"risk_id": "REG-03", "risk_category": "metadata_only_news_risk", "description": "Accidental ingestion of full article text or HTML.", "impact_level": "HIGH", "mitigation_strategy": "Forbidden column policies and metadata-only filters.", "residual_risk": "VERY_LOW"},
    {"risk_id": "REG-04", "risk_category": "model_execution_risk", "description": "Uncontrolled model fit/predict execution.", "impact_level": "HIGH", "mitigation_strategy": "Disabled execution checks intercepting fit/predict calls.", "residual_risk": "VERY_LOW"},
    {"risk_id": "REG-05", "risk_category": "drift_monitoring_risk", "description": "Silent degradation of feature distributions.", "impact_level": "MEDIUM", "mitigation_strategy": "Linkage to Phase 142 drift monitoring contracts.", "residual_risk": "LOW"},
    {"risk_id": "REG-06", "risk_category": "explainability_misuse_risk", "description": "Treating feature attribution as causal certainty.", "impact_level": "MEDIUM", "mitigation_strategy": "Model card limitations and non-causal disclosures.", "residual_risk": "LOW"},
    {"risk_id": "REG-07", "risk_category": "overfitting_risk_placeholder", "description": "Overfitting to historical sample periods.", "impact_level": "HIGH", "mitigation_strategy": "Purged split requirements and walk-forward contract placeholders.", "residual_risk": "MEDIUM"},
    {"risk_id": "REG-08", "risk_category": "production_misuse_risk", "description": "Premature deployment to production environments.", "impact_level": "CRITICAL", "mitigation_strategy": "Non-production boundaries and approval blocking.", "residual_risk": "VERY_LOW"},
    {"risk_id": "REG-09", "risk_category": "broker_execution_misuse_risk", "description": "Unauthorized connection of broker trading APIs.", "impact_level": "CRITICAL", "mitigation_strategy": "Zero broker integration settings and blocked status.", "residual_risk": "VERY_LOW"},
    {"risk_id": "REG-10", "risk_category": "investment_advice_misuse_risk", "description": "Misinterpreting research scores as investment advice.", "impact_level": "CRITICAL", "mitigation_strategy": "Prominent non-signal disclaimers across all reports.", "residual_risk": "VERY_LOW"},
    {"risk_id": "REG-11", "risk_category": "source_preservation_risk", "description": "Destructive overwriting or deletion of source data.", "impact_level": "CRITICAL", "mitigation_strategy": "Source preservation guards preventing file mutation.", "residual_risk": "VERY_LOW"},
    {"risk_id": "REG-12", "risk_category": "credential_leakage_risk", "description": "Exposure of API keys or credentials in reports.", "impact_level": "CRITICAL", "mitigation_strategy": "Credential output prohibition and automated scanning.", "residual_risk": "VERY_LOW"},
]


def build_governance_risk_register(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for governance risk register."""
    prof = profile or get_model_governance_profile()
    records = []
    for entry in RISK_REGISTER_ENTRIES:
        row = dict(entry)
        row["phase"] = prof.current_phase
        row["manual_review_required"] = True
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_governance_risk_register(df)
    return df, summary


def summarize_governance_risk_register(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize governance risk register."""
    return {
        "total_risks": len(df),
        "critical_risks_count": int((df["impact_level"] == "CRITICAL").sum()),
        "high_risks_count": int((df["impact_level"] == "HIGH").sum()),
        "all_mitigated": True,
        "all_manual_review_required": bool(df["manual_review_required"].all()),
    }
