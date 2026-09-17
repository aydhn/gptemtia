# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Acceptance Domain Registry."""

from typing import Any, Dict, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    ALL_DOMAINS,
    ADVANCED_ML_ACCEPTANCE_DOMAIN,
    ACCEPTANCE_READY,
)


def build_advanced_ml_acceptance_domain_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for advanced ML acceptance domains."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for d in ALL_DOMAINS:
        records.append({
            "domain_label": d,
            "current_phase": active.current_phase,
            "target_final_phase": active.target_final_phase,
            "next_phase": active.next_phase,
            "status": ACCEPTANCE_READY,
            "non_signal": True,
            "non_production": True,
            "offline_only": True,
        })

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": ADVANCED_ML_ACCEPTANCE_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_domains": len(df),
        "non_signal": True,
        "status": "READY",
    }
    return df, summary


def summarize_advanced_ml_acceptance_domains(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize domains DataFrame."""
    return {
        "domain_count": len(df),
        "non_signal": True,
    }
