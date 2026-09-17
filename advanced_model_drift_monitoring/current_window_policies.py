# -*- coding: utf-8 -*-
"""Phase 142: Current Window Policies Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_model_drift_monitoring.model_drift_config import (
    ModelDriftProfile,
    get_model_drift_profile,
)

CURRENT_WINDOW_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_name": "rolling_short_term_current_window_policy",
        "window_type": "current",
        "window_size_description": "Most recent 30 trading bars for prompt drift detection",
        "min_observations_placeholder": 30,
        "alignment_method": "asof_backward",
        "data_materialization_allowed": False,
        "real_window_extraction_executed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "policy_name": "rolling_medium_term_current_window_policy",
        "window_type": "current",
        "window_size_description": "Most recent 60 trading bars for stable drift metric evaluation",
        "min_observations_placeholder": 60,
        "alignment_method": "asof_backward",
        "data_materialization_allowed": False,
        "real_window_extraction_executed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "policy_name": "daily_session_current_window_policy",
        "window_type": "current",
        "window_size_description": "Single trading day intraday bars for daily batch monitoring",
        "min_observations_placeholder": 24,
        "alignment_method": "asof_backward",
        "data_materialization_allowed": False,
        "real_window_extraction_executed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "policy_name": "regime_transition_current_window_policy",
        "window_type": "current",
        "window_size_description": "Bars elapsed since the most recent regime transition event",
        "min_observations_placeholder": 15,
        "alignment_method": "asof_backward",
        "data_materialization_allowed": False,
        "real_window_extraction_executed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
]


def build_current_window_policy_registry(
    profile: Optional[ModelDriftProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for current window policies."""
    prof = profile or get_model_drift_profile()
    df = pd.DataFrame(CURRENT_WINDOW_POLICIES)
    summary = summarize_current_window_policies(df)
    return df, summary


def summarize_current_window_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize current window policies DataFrame."""
    return {
        "total_policies": len(df),
        "policies": df["policy_name"].tolist() if not df.empty else [],
        "all_materialization_disabled": bool((~df["data_materialization_allowed"]).all()) if not df.empty else True,
        "all_extraction_unexecuted": bool((~df["real_window_extraction_executed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }


def validate_current_window_policy(record: Any) -> Dict[str, Any]:
    """Validate a single current window policy."""
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


def build_current_window_policies() -> List[Any]:
    """Return list of DriftWindowPolicy objects for current windows."""
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
        for p in CURRENT_WINDOW_POLICIES
    ]


