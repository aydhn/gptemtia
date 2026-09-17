# -*- coding: utf-8 -*-
"""Phase 142: Rolling Window Placeholder Policies Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_model_drift_monitoring.model_drift_config import (
    ModelDriftProfile,
    get_model_drift_profile,
)

ROLLING_WINDOW_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_name": "rolling_step_fixed_size_placeholder_policy",
        "rolling_type": "fixed_stride_rolling",
        "window_size": 90,
        "stride_step": 5,
        "real_extraction_executed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_placeholder_only",
    },
    {
        "policy_name": "expanding_window_placeholder_policy",
        "rolling_type": "expanding_anchored",
        "window_size": 180,
        "stride_step": 10,
        "real_extraction_executed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_placeholder_only",
    },
    {
        "policy_name": "exponential_decay_window_placeholder_policy",
        "rolling_type": "decay_weighted",
        "window_size": 120,
        "stride_step": 1,
        "real_extraction_executed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_placeholder_only",
    },
    {
        "policy_name": "volatility_adaptive_window_placeholder_policy",
        "rolling_type": "regime_adaptive_length",
        "window_size": 45,
        "stride_step": 1,
        "real_extraction_executed": False,
        "drift_calculation_allowed": False,
        "non_signal": True,
        "status": "drift_contract_placeholder_only",
    },
]


def build_rolling_window_placeholder_policy_registry(
    profile: Optional[ModelDriftProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for rolling window placeholder policies."""
    prof = profile or get_model_drift_profile()
    df = pd.DataFrame(ROLLING_WINDOW_POLICIES)
    summary = summarize_rolling_window_placeholder_policies(df)
    return df, summary


def summarize_rolling_window_placeholder_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize rolling window placeholder policies DataFrame."""
    return {
        "total_policies": len(df),
        "policies": df["policy_name"].tolist() if not df.empty else [],
        "all_extractions_unexecuted": bool((~df["real_extraction_executed"]).all()) if not df.empty else True,
        "all_drift_calculation_disabled": bool((~df["drift_calculation_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }


def validate_rolling_window_placeholder_policy(record: Any) -> Dict[str, Any]:
    """Validate rolling window placeholder policy record."""
    def _get(key, default=None):
        if isinstance(record, dict):
            return record.get(key, default)
        return getattr(record, key, default)

    valid = (
        not _get("real_extraction_executed", False)
        and not _get("real_window_extraction_executed", False)
        and not _get("drift_calculation_allowed", False)
        and not _get("execution_enabled", False)
        and _get("non_signal", True) is True
    )
    return {
        "valid": valid,
        "is_valid": valid,
        "policy_name": _get("policy_name", "unknown"),
        "non_signal": True,
    }



def build_rolling_window_placeholder_policies() -> List[Any]:
    """Return list of DriftWindowPolicy objects for rolling window placeholders."""
    from advanced_model_drift_monitoring.model_drift_models import DriftWindowPolicy
    return [
        DriftWindowPolicy(
            policy_id=p["policy_name"],
            policy_name=p["policy_name"],
            window_type=p.get("window_type", p.get("rolling_type", "rolling")),
            window_size_description=str(p.get("window_size", "rolling_window")),
            min_observations_placeholder=int(p.get("window_size", 30)),
            alignment_method="asof_backward",
            data_materialization_allowed=False,
            real_window_extraction_executed=False,
            non_signal=p.get("non_signal", True),
            status=p.get("status", "drift_contract_placeholder_only"),
            execution_enabled=False,
        )
        for p in ROLLING_WINDOW_POLICIES
    ]



