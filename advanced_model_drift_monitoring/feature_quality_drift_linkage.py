# -*- coding: utf-8 -*-
"""Phase 142: Feature Quality Drift Linkage Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_model_drift_monitoring.model_drift_config import (
    ModelDriftProfile,
    get_model_drift_profile,
)

FEATURE_QUALITY_DRIFT_LINKAGES: List[Dict[str, Any]] = [
    {
        "linkage_name": "link_phase_123_missingness_rate_drift",
        "linkage_type": "quality_missingness_linkage",
        "source_phase_ref": "Phase 123",
        "upstream_contract_ref": "feature_missingness_registry",
        "target_drift_domain": "missingness_drift_metric_placeholder_domain",
        "quality_metric": "missing_rate",
        "drift_calculation_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "linkage_name": "link_phase_123_infinite_value_drift",
        "linkage_type": "quality_infinite_linkage",
        "source_phase_ref": "Phase 123",
        "upstream_contract_ref": "feature_infinite_value_registry",
        "target_drift_domain": "feature_quality_drift_linkage_domain",
        "quality_metric": "infinite_count",
        "drift_calculation_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "linkage_name": "link_phase_123_zero_variance_drift",
        "linkage_type": "quality_variance_linkage",
        "source_phase_ref": "Phase 123",
        "upstream_contract_ref": "feature_zero_variance_registry",
        "target_drift_domain": "feature_quality_drift_linkage_domain",
        "quality_metric": "zero_variance_flag",
        "drift_calculation_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "linkage_name": "link_phase_123_staleness_drift",
        "linkage_type": "quality_staleness_linkage",
        "source_phase_ref": "Phase 123",
        "upstream_contract_ref": "feature_staleness_registry",
        "target_drift_domain": "feature_quality_drift_linkage_domain",
        "quality_metric": "stale_bars_count",
        "drift_calculation_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
]


def build_feature_quality_drift_linkage_registry(
    profile: Optional[ModelDriftProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for feature quality drift linkage."""
    prof = profile or get_model_drift_profile()
    df = pd.DataFrame(FEATURE_QUALITY_DRIFT_LINKAGES)
    summary = summarize_feature_quality_drift_linkage(df)
    return df, summary


def summarize_feature_quality_drift_linkage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize feature quality drift linkage DataFrame."""
    return {
        "total_linkages": len(df),
        "linkages": df["linkage_name"].tolist() if not df.empty else [],
        "all_drift_calculation_disabled": bool((~df["drift_calculation_allowed"]).all()) if not df.empty else True,
        "all_model_action_disabled": bool((~df["model_action_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }


def validate_feature_quality_drift_linkage(record: Any) -> Dict[str, Any]:
    """Validate feature quality drift linkage record."""
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


def build_feature_quality_drift_linkages() -> List[Any]:
    """Return list of DriftLinkageItem objects for feature quality drift linkages."""
    from advanced_model_drift_monitoring.model_drift_models import DriftLinkageItem
    return [
        DriftLinkageItem(
            linkage_id=link.get("linkage_name"),
            linkage_name=link.get("linkage_name"),
            linkage_type=link.get("linkage_type", "quality_linkage"),
            source_phase_ref=link.get("source_phase_ref", "Phase 123"),
            upstream_contract_ref=link.get("upstream_contract_ref", ""),
            target_drift_domain=link.get("target_drift_domain", ""),
            metadata_fields=[link.get("quality_metric", "quality_metric")],
            drift_calculation_allowed=False,
            model_action_allowed=False,
            non_signal=True,
            status=link.get("status", "drift_contract_ready"),
            execution_enabled=False,
        )
        for link in FEATURE_QUALITY_DRIFT_LINKAGES
    ]


