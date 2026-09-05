"""Phase 124 Feature Store Schema Registry and Schema Validator."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

MINIMUM_SCHEMA_FIELDS: List[str] = [
    "store_key",
    "entity_type",
    "entity_id",
    "timestamp_field",
    "feature_name",
    "feature_family",
    "source_phase",
    "validation_status",
    "quality_score_ref",
    "drift_score_ref",
    "lineage_ref",
    "manual_review_required",
    "non_signal",
]


def validate_feature_store_schema(df: pd.DataFrame, required_columns: Optional[List[str]] = None) -> Dict[str, Any]:
    """Validate a DataFrame against required feature store schema columns."""
    req = required_columns or MINIMUM_SCHEMA_FIELDS
    present_cols = list(df.columns)
    missing_cols = [c for c in req if c not in present_cols]

    return {
        "is_valid": len(missing_cols) == 0,
        "required_columns_count": len(req),
        "present_columns_count": len(present_cols),
        "missing_columns": missing_cols,
        "missing_count": len(missing_cols),
        "non_signal": True,
    }


def build_feature_store_schema_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of feature store schemas."""
    prof = profile or get_default_feature_store_integration_profile()
    schemas = [
        {
            "schema_name": "canonical_feature_store_schema",
            "entity_type": "entity_fx_pair,entity_commodity_symbol",
            "required_fields": ",".join(MINIMUM_SCHEMA_FIELDS),
            "field_count": len(MINIMUM_SCHEMA_FIELDS),
            "timestamp_field": "timestamp",
            "version_tag": "v1.0.0",
            "source_phase": prof.current_phase,
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "schema_name": "factor_metadata_store_schema",
            "entity_type": "entity_factor_family",
            "required_fields": "factor_name,factor_family,entity_type,source_phase,input_feature_set_ref,validation_dependency_ref,quality_dependency_ref,non_signal",
            "field_count": 8,
            "timestamp_field": "timestamp",
            "version_tag": "v1.0.0",
            "source_phase": prof.current_phase,
            "non_signal": True,
            "source_preserved": True,
        },
        {
            "schema_name": "quality_drift_store_schema",
            "entity_type": "entity_fx_pair,entity_commodity_symbol",
            "required_fields": "score_id,feature_name,quality_score,drift_score,passed,non_signal",
            "field_count": 6,
            "timestamp_field": "timestamp",
            "version_tag": "v1.0.0",
            "source_phase": prof.current_phase,
            "non_signal": True,
            "source_preserved": True,
        },
    ]

    df = pd.DataFrame(schemas)
    summary = {
        "total_schemas": len(schemas),
        "minimum_fields_required": MINIMUM_SCHEMA_FIELDS,
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_feature_store_schema_registry(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize schema registry."""
    return {
        "total_schemas": len(df) if not df.empty else 0,
        "non_signal": True,
        "source_preserved": True,
    }
