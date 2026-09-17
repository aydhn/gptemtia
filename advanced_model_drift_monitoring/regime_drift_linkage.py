# -*- coding: utf-8 -*-
"""Phase 142: Regime Drift Linkage Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_model_drift_monitoring.model_drift_config import (
    ModelDriftProfile,
    get_model_drift_profile,
)

REGIME_DRIFT_LINKAGES: List[Dict[str, Any]] = [
    {
        "linkage_name": "link_phase_126_regime_state_taxonomy",
        "linkage_type": "regime_taxonomy_linkage",
        "source_phase_ref": "Phase 126",
        "upstream_contract_ref": "regime_state_taxonomy_registry",
        "target_drift_domain": "drift_segment_policy_domain",
        "regime_family": "market_behavior_regimes",
        "drift_calculation_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "linkage_name": "link_phase_127_regime_feature_matrix",
        "linkage_type": "regime_feature_matrix_linkage",
        "source_phase_ref": "Phase 127",
        "upstream_contract_ref": "regime_feature_matrix_contract",
        "target_drift_domain": "data_drift_monitoring_contract_domain",
        "regime_family": "regime_matrix",
        "drift_calculation_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "linkage_name": "link_phase_130_regime_transition_diagnostics",
        "linkage_type": "regime_transition_linkage",
        "source_phase_ref": "Phase 130",
        "upstream_contract_ref": "regime_transition_matrix_report",
        "target_drift_domain": "regime_drift_linkage_domain",
        "regime_family": "regime_transitions",
        "drift_calculation_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "linkage_name": "link_phase_131_cross_asset_regime_context",
        "linkage_type": "cross_asset_regime_linkage",
        "source_phase_ref": "Phase 131",
        "upstream_contract_ref": "cross_asset_regime_context_contract",
        "target_drift_domain": "correlation_drift_metric_placeholder_domain",
        "regime_family": "cross_asset_context",
        "drift_calculation_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "linkage_name": "link_phase_135_regime_acceptance_manifest",
        "linkage_type": "regime_acceptance_manifest_linkage",
        "source_phase_ref": "Phase 135",
        "upstream_contract_ref": "phase_126_135_acceptance_manifest",
        "target_drift_domain": "validation_dependency_domain",
        "regime_family": "regime_block_acceptance",
        "drift_calculation_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
]


def build_regime_drift_linkage_registry(
    profile: Optional[ModelDriftProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for regime drift linkage."""
    prof = profile or get_model_drift_profile()
    df = pd.DataFrame(REGIME_DRIFT_LINKAGES)
    summary = summarize_regime_drift_linkage(df)
    return df, summary


def summarize_regime_drift_linkage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize regime drift linkage DataFrame."""
    return {
        "total_linkages": len(df),
        "linkages": df["linkage_name"].tolist() if not df.empty else [],
        "all_drift_calculation_disabled": bool((~df["drift_calculation_allowed"]).all()) if not df.empty else True,
        "all_model_action_disabled": bool((~df["model_action_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }


def validate_regime_drift_linkage(record: Any) -> Dict[str, Any]:
    """Validate regime drift linkage record."""
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


def build_regime_drift_linkages() -> List[Any]:
    """Return list of DriftLinkageItem objects for regime drift linkages."""
    from advanced_model_drift_monitoring.model_drift_models import DriftLinkageItem
    return [
        DriftLinkageItem(
            linkage_id=link.get("linkage_name"),
            linkage_name=link.get("linkage_name"),
            linkage_type=link.get("linkage_type", "regime_linkage"),
            source_phase_ref=link.get("source_phase_ref", "Phase 126-135"),
            upstream_contract_ref=link.get("upstream_contract_ref", ""),
            target_drift_domain=link.get("target_drift_domain", ""),
            metadata_fields=[link.get("regime_family", "regime_family")],
            drift_calculation_allowed=False,
            model_action_allowed=False,
            non_signal=True,
            status=link.get("status", "drift_contract_ready"),
            execution_enabled=False,
        )
        for link in REGIME_DRIFT_LINKAGES
    ]

