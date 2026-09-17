# -*- coding: utf-8 -*-
"""Phase 144: Model Card Risk Disclosures Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
from advanced_model_governance.model_governance_config import (
    ModelGovernanceProfile,
    get_model_governance_profile,
)

RISK_DISCLOSURE_ITEMS: List[Dict[str, str]] = [
    {
        "risk_id": "RSK-01",
        "risk_name": "concept_drift_risk",
        "description": "Macroeconomic regime shifts or commodity shocks can invalidate prior statistical relationships.",
        "mitigation": "Monitored via Phase 142 drift monitoring contracts (PSI, KS, Wasserstein tests).",
    },
    {
        "risk_id": "RSK-02",
        "risk_name": "calibration_degradation_risk",
        "description": "Uncertainty intervals and class probabilities may lose calibration under high volatility.",
        "mitigation": "Controlled via Phase 141 reliability diagram contracts and Brier score tracking.",
    },
    {
        "risk_id": "RSK-03",
        "risk_name": "attribution_instability_risk",
        "description": "Feature attributions may vary across closely correlated features or changing market regimes.",
        "mitigation": "Supervised via Phase 143 XAI stability contracts and Spearman rank drift checks.",
    },
    {
        "risk_id": "RSK-04",
        "risk_name": "governance_bypass_risk",
        "description": "Premature transition from research contracts to live trading by bypassing approval boundaries.",
        "mitigation": "Strict boundary enforcement and mandatory manual review gates in Phase 144.",
    },
]


def build_model_card_risk_disclosure_registry(
    profile: Optional[ModelGovernanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for model card risk disclosures."""
    prof = profile or get_model_governance_profile()
    records = []
    for item in RISK_DISCLOSURE_ITEMS:
        row = dict(item)
        row["phase"] = prof.current_phase
        row["manual_review_required"] = True
        row["non_signal"] = True
        records.append(row)

    df = pd.DataFrame(records)
    summary = summarize_model_card_risk_disclosures(df)
    return df, summary


def summarize_model_card_risk_disclosures(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize model card risk disclosures."""
    return {
        "total_risk_disclosures": len(df),
        "all_manual_review_required": bool(df["manual_review_required"].all()),
        "non_signal_verified": bool(df["non_signal"].all()),
    }
