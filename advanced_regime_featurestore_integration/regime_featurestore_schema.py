"""Phase 134: Regime FeatureStore Schema Definition and Validation.

Defines the required non-signal schema fields, identifies forbidden schema fields,
and provides schema validation routines for FeatureStore datasets.
"""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    RegimeFeatureStoreProfile,
    get_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_labels import (
    REGIME_FEATURESTORE_SCHEMA_DOMAIN,
    REGIME_STORE_READY,
)

MINIMUM_SCHEMA_FIELDS: List[Dict[str, Any]] = [
    {"field_name": "store_key", "field_type": "string", "required": True, "description": "Unique canonical store key"},
    {"field_name": "store_entity_type", "field_type": "string", "required": True, "description": "Entity category type"},
    {"field_name": "entity_id", "field_type": "string", "required": True, "description": "Unique identifier of the entity"},
    {"field_name": "timestamp_utc", "field_type": "string", "required": True, "description": "UTC timestamp in ISO format"},
    {"field_name": "component_name", "field_type": "string", "required": True, "description": "Originating regime subsystem"},
    {"field_name": "source_phase", "field_type": "integer", "required": True, "description": "Phase index (126-134)"},
    {"field_name": "source_component_ref", "field_type": "string", "required": True, "description": "Component reference URI"},
    {"field_name": "validation_acceptance_ref", "field_type": "string", "required": True, "description": "Phase 133 acceptance verification ref"},
    {"field_name": "no_lookahead_acceptance_ref", "field_type": "string", "required": True, "description": "Proof of backward-only asof join"},
    {"field_name": "metadata_only_news_acceptance_ref", "field_type": "string", "required": True, "description": "Proof of news metadata-only purity"},
    {"field_name": "source_preservation_ref", "field_type": "string", "required": True, "description": "Proof of zero source overwrites"},
    {"field_name": "quality_dependency_ref", "field_type": "string", "required": True, "description": "Reference to quality checks"},
    {"field_name": "validation_dependency_ref", "field_type": "string", "required": True, "description": "Reference to validation dependencies"},
    {"field_name": "lineage_ref", "field_type": "string", "required": True, "description": "End-to-end lineage pointer"},
    {"field_name": "manual_review_required", "field_type": "boolean", "required": True, "description": "Flag indicating manual audit need"},
    {"field_name": "non_signal", "field_type": "boolean", "required": True, "description": "Mandatory non-signal invariant assertion"},
]

FORBIDDEN_SCHEMA_COLUMNS: List[str] = [
    "signal",
    "buy",
    "sell",
    "long",
    "short",
    "position",
    "target",
    "label",
    "prediction",
    "recommendation",
    "future_return",
    "forward_return",
    "next_return",
    "full_text",
    "article_body",
    "raw_content",
    "scraped_html",
    "embedding",
    "vector",
    "sentiment",
    "sentiment_score",
]


def build_regime_featurestore_schema_registry(
    profile: Optional[RegimeFeatureStoreProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Construct tabular schema registry."""
    active_profile = profile or get_regime_featurestore_profile()
    df = pd.DataFrame(MINIMUM_SCHEMA_FIELDS)
    summary = {
        "domain": REGIME_FEATURESTORE_SCHEMA_DOMAIN,
        "total_fields": len(df),
        "active_profile": active_profile.profile_name,
        "current_phase": 134,
        "target_final_phase": 160,
        "next_phase": 135,
        "forbidden_columns_count": len(FORBIDDEN_SCHEMA_COLUMNS),
        "status": REGIME_STORE_READY,
        "non_signal": True,
    }
    return df, summary


def validate_regime_featurestore_schema(
    df: pd.DataFrame,
    required_columns: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Validate DataFrame against required schema columns and check for forbidden columns."""
    req_cols = required_columns or [f["field_name"] for f in MINIMUM_SCHEMA_FIELDS]
    existing_cols = list(df.columns)

    missing_cols = [col for col in req_cols if col not in existing_cols]
    found_forbidden = [col for col in existing_cols if col.lower() in FORBIDDEN_SCHEMA_COLUMNS]

    is_valid = (len(missing_cols) == 0) and (len(found_forbidden) == 0)

    return {
        "is_valid": is_valid,
        "total_columns": len(existing_cols),
        "missing_columns": missing_cols,
        "found_forbidden_columns": found_forbidden,
        "non_signal": len(found_forbidden) == 0,
        "status": REGIME_STORE_READY if is_valid else "schema_validation_failed",
    }


def summarize_regime_featurestore_schema(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize schema registry DataFrame."""
    return {
        "total_fields": len(df),
        "required_fields_count": int((df["required"] == True).sum()) if not df.empty else 0,
        "field_names": df["field_name"].tolist() if not df.empty else [],
    }
