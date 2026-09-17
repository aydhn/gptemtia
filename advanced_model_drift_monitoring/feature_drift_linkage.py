# -*- coding: utf-8 -*-
"""Phase 142: Feature Drift Linkage Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_model_drift_monitoring.model_drift_config import (
    ModelDriftProfile,
    get_model_drift_profile,
)

FEATURE_DRIFT_LINKAGES: List[Dict[str, Any]] = [
    {
        "linkage_name": "link_phase_123_feature_drift_diagnostics",
        "linkage_type": "upstream_feature_drift",
        "source_phase_ref": "Phase 123",
        "upstream_contract_ref": "feature_quality_drift_contract",
        "target_drift_domain": "feature_drift_monitoring_contract_domain",
        "metadata_fields": ["psi_score", "distribution_drift", "rolling_stability"],
        "drift_calculation_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "linkage_name": "link_phase_123_distribution_summary",
        "linkage_type": "distribution_baseline",
        "source_phase_ref": "Phase 123",
        "upstream_contract_ref": "feature_distribution_summary_registry",
        "target_drift_domain": "reference_window_policy_domain",
        "metadata_fields": ["mean", "std", "quantiles", "min_max"],
        "drift_calculation_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "linkage_name": "link_phase_123_factor_drift_diagnostics",
        "linkage_type": "factor_drift_metadata",
        "source_phase_ref": "Phase 123",
        "upstream_contract_ref": "factor_drift_registry",
        "target_drift_domain": "feature_drift_monitoring_contract_domain",
        "metadata_fields": ["factor_drift_score", "staleness_score"],
        "drift_calculation_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
]


def build_feature_drift_linkage_registry(
    profile: Optional[ModelDriftProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for feature drift linkage contracts."""
    prof = profile or get_model_drift_profile()
    df = pd.DataFrame(FEATURE_DRIFT_LINKAGES)
    summary = summarize_feature_drift_linkage(df)
    return df, summary


def summarize_feature_drift_linkage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize feature drift linkage DataFrame."""
    return {
        "total_linkages": len(df),
        "linkages": df["linkage_name"].tolist() if not df.empty else [],
        "all_drift_calculation_disabled": bool((~df["drift_calculation_allowed"]).all()) if not df.empty else True,
        "all_model_action_disabled": bool((~df["model_action_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }


def validate_feature_drift_linkage(record: Any) -> Dict[str, Any]:
    """Validate feature drift linkage record."""
    def _get(key, default=None):
        if isinstance(record, dict):
            return record.get(key, default)
        return getattr(record, key, default)

    valid = (
        not _get("drift_calculation_allowed", False)
        and not _get("model_action_allowed", False)
        and not _get("execution_enabled", False)
        and _get("non_signal", True) is True
    )
    return {
        "valid": valid,
        "is_valid": valid,
        "linkage_name": _get("linkage_name", "unknown"),
        "non_signal": True,
    }


def build_feature_drift_linkages() -> List[Any]:
    """Return list of DriftLinkageItem objects for feature drift linkages."""
    from advanced_model_drift_monitoring.model_drift_models import DriftLinkageItem
    return [
        DriftLinkageItem(
            linkage_id=link.get("linkage_name"),
            linkage_name=link.get("linkage_name"),
            linkage_type=link.get("linkage_type", "feature_linkage"),
            source_phase_ref=link.get("source_phase_ref", "Phase 123"),
            upstream_contract_ref=link.get("upstream_contract_ref", ""),
            target_drift_domain=link.get("target_drift_domain", ""),
            metadata_fields=link.get("metadata_fields", []),
            drift_calculation_allowed=False,
            model_action_allowed=False,
            non_signal=True,
            status=link.get("status", "drift_contract_ready"),
            execution_enabled=False,
        )
        for link in FEATURE_DRIFT_LINKAGES
    ]


