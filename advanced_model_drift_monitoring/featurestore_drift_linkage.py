# -*- coding: utf-8 -*-
"""Phase 142: FeatureStore Drift Linkage Registry."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_model_drift_monitoring.model_drift_config import (
    ModelDriftProfile,
    get_model_drift_profile,
)

FEATURESTORE_DRIFT_LINKAGES: List[Dict[str, Any]] = [
    {
        "linkage_name": "link_phase_124_featurestore_catalog",
        "linkage_type": "store_catalog_linkage",
        "source_phase_ref": "Phase 124",
        "upstream_contract_ref": "featurestore_integration_catalog",
        "target_drift_domain": "featurestore_drift_linkage_domain",
        "store_namespace": "ml_feature_store",
        "drift_calculation_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "linkage_name": "link_phase_124_featurestore_schema",
        "linkage_type": "store_schema_drift",
        "source_phase_ref": "Phase 124",
        "upstream_contract_ref": "featurestore_schema_registry",
        "target_drift_domain": "data_drift_monitoring_contract_domain",
        "store_namespace": "ml_feature_store_schema",
        "drift_calculation_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "linkage_name": "link_phase_124_featurestore_version_policy",
        "linkage_type": "store_version_consistency",
        "source_phase_ref": "Phase 124",
        "upstream_contract_ref": "featurestore_version_policy",
        "target_drift_domain": "lineage_domain",
        "store_namespace": "ml_feature_store_version",
        "drift_calculation_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
    {
        "linkage_name": "link_phase_124_featurestore_read_write_contracts",
        "linkage_type": "store_access_contract",
        "source_phase_ref": "Phase 124",
        "upstream_contract_ref": "featurestore_read_contracts",
        "target_drift_domain": "drift_input_contract_domain",
        "store_namespace": "ml_feature_store_read",
        "drift_calculation_allowed": False,
        "model_action_allowed": False,
        "non_signal": True,
        "status": "drift_contract_ready",
    },
]


def build_featurestore_drift_linkage_registry(
    profile: Optional[ModelDriftProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for FeatureStore drift linkage."""
    prof = profile or get_model_drift_profile()
    df = pd.DataFrame(FEATURESTORE_DRIFT_LINKAGES)
    summary = summarize_featurestore_drift_linkage(df)
    return df, summary


def summarize_featurestore_drift_linkage(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize FeatureStore drift linkage DataFrame."""
    return {
        "total_linkages": len(df),
        "linkages": df["linkage_name"].tolist() if not df.empty else [],
        "all_drift_calculation_disabled": bool((~df["drift_calculation_allowed"]).all()) if not df.empty else True,
        "all_model_action_disabled": bool((~df["model_action_allowed"]).all()) if not df.empty else True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty else True,
    }


def validate_featurestore_drift_linkage(record: Any) -> Dict[str, Any]:
    """Validate FeatureStore drift linkage record."""
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


def build_featurestore_drift_linkages() -> List[Any]:
    """Return list of DriftLinkageItem objects for FeatureStore drift linkages."""
    from advanced_model_drift_monitoring.model_drift_models import DriftLinkageItem
    return [
        DriftLinkageItem(
            linkage_id=link.get("linkage_name"),
            linkage_name=link.get("linkage_name"),
            linkage_type=link.get("linkage_type", "store_linkage"),
            source_phase_ref=link.get("source_phase_ref", "Phase 124"),
            upstream_contract_ref=link.get("upstream_contract_ref", ""),
            target_drift_domain=link.get("target_drift_domain", ""),
            metadata_fields=[link.get("store_namespace", "store_namespace")],
            drift_calculation_allowed=False,
            model_action_allowed=False,
            non_signal=True,
            status=link.get("status", "drift_contract_ready"),
            execution_enabled=False,
        )
        for link in FEATURESTORE_DRIFT_LINKAGES
    ]

