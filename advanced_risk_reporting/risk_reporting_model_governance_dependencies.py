# -*- coding: utf-8 -*-
"""Phase 155: Model Governance Dependencies Registry."""

from typing import Any, Dict, Tuple
import pandas as pd
from .risk_reporting_config import RiskReportingProfile, get_default_risk_reporting_profile


def build_risk_reporting_model_governance_dependency_registry(
    profile: RiskReportingProfile = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for Phase 144 model governance dependencies."""
    if profile is None:
        profile = get_default_risk_reporting_profile()

    rows = [
        {
            "dependency_name": "model_governance_dependency",
            "source_phase": 144,
            "target_phase": 155,
            "contract_type": "model_cards_and_audit",
            "status": "AVAILABLE_CONTRACT_ONLY",
        }
    ]
    df = pd.DataFrame(rows)
    df["current_phase"] = profile.current_phase
    df["target_final_phase"] = profile.target_final_phase
    df["next_phase"] = profile.next_phase
    return df, {"dependency_count": len(df), "is_satisfied": True}
