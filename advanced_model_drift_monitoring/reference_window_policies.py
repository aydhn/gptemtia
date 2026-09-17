# -*- coding: utf-8 -*-
"""Phase 142: Reference Window Policies Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_model_drift_monitoring.model_drift_config import (
    ModelDriftProfile,
    get_model_drift_profile,
)

REFERENCE_WINDOW_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_name": "fixed_in_sample_training_window_policy",
        "window_type": "reference",
        "window_size_description": "First 70% of historical series used for baseline training calibration",
        "min_observations_placeholder": 500,
        "alignment_method": "asof_backward",
        "data_materialization_allowed": False,
        "real_window_extraction_executed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "policy_name": "expanded_validation_baseline_window_policy",
        "window_type": "reference",
        "window_size_description": "Combined train + validation historical baseline window",
        "min_observations_placeholder": 750,
        "alignment_method": "asof_backward",
        "data_materialization_allowed": False,
        "real_window_extraction_executed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "policy_name": "rolling_lookback_reference_window_policy",
        "window_type": "reference",
        "window_size_description": "Preceding 252 trading bars sliding reference baseline",
        "min_observations_placeholder": 252,
        "alignment_method": "asof_backward",
        "data_materialization_allowed": False,
        "real_window_extraction_executed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "policy_name": "regime_conditioned_reference_window_policy",
        "window_type": "reference",
        "window_size_description": "Filtered baseline window conditioned on specific regime state",
        "min_observations_placeholder": 120,
        "alignment_method": "asof_backward",
        "data_materialization_allowed": False,
        "real_window_extraction_executed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
]


def build_reference_window_policy_registry(
    profile: Optional[ModelDriftProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for reference window policies."""
    prof = profile or get_model_drift_profile()
    df = pd.DataFrame(REFERENCE_WINDOW_POLICIES)
    summary = summarize_reference_window_policies(df)
    return df, summary


def summarize_reference_window_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize reference window policies DataFrame."""
    return {
        "total_policies": len(df),
        "policies": df["policy_name"].tolist() if not df.empty else [],
        "all_materialization_disabled": bool((~df["data_materialization_allowed"]).all()) if not df.empty else True,
        "all_extraction_unexecuted": bool((~df["real_window_extraction_executed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }


def validate_reference_window_policy(record: Any) -> Dict[str, Any]:
    """Validate reference window policy record."""
    def _get(key, default):
        if isinstance(record, dict):
            return record.get(key, default)
        return getattr(record, key, default)

    valid = (
        not _get("data_materialization_allowed", True)
        and not _get("real_window_extraction_executed", True)
        and not _get("execution_enabled", False)
        and _get("non_signal", True) is True
    )
    return {
        "valid": valid,
        "is_valid": valid,
        "policy_name": _get("policy_name", "unknown"),
        "non_signal": True,
    }


def build_reference_window_policies() -> List[Any]:
    """Return list of DriftWindowPolicy objects for reference windows."""
    from advanced_model_drift_monitoring.model_drift_models import DriftWindowPolicy
    return [
        DriftWindowPolicy(
            policy_id=p["policy_name"],
            policy_name=p["policy_name"],
            window_type=p["window_type"],
            window_size_description=p["window_size_description"],
            min_observations_placeholder=p["min_observations_placeholder"],
            alignment_method=p.get("alignment_method", "asof_backward"),
            data_materialization_allowed=p.get("data_materialization_allowed", False),
            real_window_extraction_executed=p.get("real_window_extraction_executed", False),
            non_signal=p.get("non_signal", True),
            status=p.get("status", "drift_contract_ready"),
            execution_enabled=False,
        )
        for p in REFERENCE_WINDOW_POLICIES
    ]


