# -*- coding: utf-8 -*-
"""Phase 145: Advanced ML Warning Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    AdvancedMlAcceptanceProfile,
    get_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_labels import (
    WARNING_DOMAIN,
    ACCEPTANCE_READY_WITH_WARNINGS,
)

WARNING_ITEMS: List[Dict[str, Any]] = [
    {
        "warning_id": "WRN-01",
        "warning_type": "contract_only_acceptance",
        "phase_ref": "Phase 136-145",
        "message": "All components are accepted at contract and interface level only; no runtime execution occurred.",
        "action_required": "None. This is expected by design.",
    },
    {
        "warning_id": "WRN-02",
        "warning_type": "placeholder_only_evidence",
        "phase_ref": "Phase 138-143",
        "message": "Model weights, SHAP values, and drift metrics are placeholders without empirical calculation.",
        "action_required": "Do not treat placeholder schema definitions as empirical performance metrics.",
    },
    {
        "warning_id": "WRN-03",
        "warning_type": "no_real_training",
        "phase_ref": "Phase 138-139",
        "message": "Zero machine learning models were fitted or trained.",
        "action_required": "Maintain training loop prohibition unconditionally.",
    },
    {
        "warning_id": "WRN-04",
        "warning_type": "no_real_prediction",
        "phase_ref": "Phase 136-144",
        "message": "Zero prediction vectors or probabilities were generated.",
        "action_required": "Do not attempt to extract inferences from acceptance outputs.",
    },
    {
        "warning_id": "WRN-05",
        "warning_type": "no_backtest_execution",
        "phase_ref": "Phase 145",
        "message": "No backtesting, walk-forward, or slippage modeling executed in Phase 145.",
        "action_required": "Proceed to Phase 146 for realistic backtest architecture design.",
    },
    {
        "warning_id": "WRN-06",
        "warning_type": "manual_review_required",
        "phase_ref": "Phase 136-144",
        "message": "Manual review queue has pending checkpoints before future research execution.",
        "action_required": "Human operator must inspect review ledger before future execution phases.",
    },
    {
        "warning_id": "WRN-07",
        "warning_type": "phase_146_must_remain_non_live",
        "phase_ref": "Phase 146",
        "message": "Phase 146 realistic backtest framework must strictly remain offline and non-live.",
        "action_required": "Enforce zero broker connectivity and zero live capital in Phase 146.",
    },
]


def build_advanced_ml_warning_registry(
    profile: Optional[AdvancedMlAcceptanceProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for operational warnings."""
    active = profile or get_advanced_ml_acceptance_profile()

    records = []
    for w in WARNING_ITEMS:
        row = dict(w)
        row["current_phase"] = active.current_phase
        row["target_final_phase"] = active.target_final_phase
        row["next_phase"] = active.next_phase
        row["status"] = ACCEPTANCE_READY_WITH_WARNINGS
        row["non_signal"] = True
        row["production_ready"] = False
        row["broker_ready"] = False
        records.append(row)

    df = pd.DataFrame(records)
    summary: Dict[str, Any] = {
        "domain": WARNING_DOMAIN,
        "active_profile": active.profile_name,
        "current_phase": active.current_phase,
        "target_final_phase": active.target_final_phase,
        "next_phase": active.next_phase,
        "total_warnings": len(df),
        "non_signal": True,
        "status": "NOTICED",
    }
    return df, summary


def summarize_advanced_ml_warnings(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize warnings DataFrame."""
    return {
        "warning_count": len(df),
        "warnings": df["warning_type"].tolist() if not df.empty and "warning_type" in df.columns else [],
        "non_signal": True,
    }
