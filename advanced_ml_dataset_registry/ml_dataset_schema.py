import pandas as pd
from typing import Dict, List, Tuple
from advanced_ml_dataset_registry.advanced_ml_dataset_config import AdvancedMlDatasetProfile, get_default_advanced_ml_dataset_profile

REQUIRED_SCHEMA_FIELDS = [
    "dataset_contract_key",
    "dataset_family",
    "entity_type",
    "entity_id",
    "timestamp_utc",
    "feature_namespace_ref",
    "source_catalog_ref",
    "validation_acceptance_ref",
    "no_lookahead_acceptance_ref",
    "metadata_only_news_acceptance_ref",
    "source_preservation_ref",
    "quality_dependency_ref",
    "validation_dependency_ref",
    "lineage_ref",
    "split_policy_ref",
    "manual_review_required",
    "non_signal",
]

FORBIDDEN_SCHEMA_FIELDS = [
    "signal", "buy", "sell", "long", "short", "position",
    "target", "label", "prediction", "recommendation",
    "future_return", "forward_return", "next_return",
    "full_text", "article_body", "raw_content", "scraped_html",
    "embedding", "vector", "sentiment", "sentiment_score",
]

_SCHEMAS = [
    {"schema_key": "regime_metadata_schema", "dataset_contract_key": "regime_metadata_ml_dataset_contract", "dataset_family": "regime_metadata"},
    {"schema_key": "featurestore_schema", "dataset_contract_key": "featurestore_ml_dataset_contract", "dataset_family": "featurestore"},
    {"schema_key": "technical_feature_schema", "dataset_contract_key": "technical_feature_ml_dataset_contract", "dataset_family": "technical_features"},
    {"schema_key": "factor_feature_schema", "dataset_contract_key": "factor_feature_ml_dataset_contract", "dataset_family": "factor_features"},
    {"schema_key": "cross_asset_feature_schema", "dataset_contract_key": "cross_asset_feature_ml_dataset_contract", "dataset_family": "cross_asset_features"},
    {"schema_key": "macro_event_news_metadata_schema", "dataset_contract_key": "macro_event_news_metadata_ml_dataset_contract", "dataset_family": "macro_event_news_metadata"},
    {"schema_key": "validation_accepted_schema", "dataset_contract_key": "validation_accepted_ml_dataset_contract", "dataset_family": "validation_accepted"},
    {"schema_key": "dry_run_baseline_schema", "dataset_contract_key": "dry_run_baseline_model_input_contract", "dataset_family": "dry_run_baseline"},
    {"schema_key": "phase_138_training_harness_schema", "dataset_contract_key": "phase_138_training_harness_input_contract", "dataset_family": "phase_138_training_harness"},
]


def build_ml_dataset_schema_registry(profile=None) -> Tuple[pd.DataFrame, Dict]:
    if profile is None:
        profile = get_default_advanced_ml_dataset_profile()
    rows = []
    for s in _SCHEMAS:
        rows.append({
            "schema_key": s["schema_key"],
            "dataset_contract_key": s["dataset_contract_key"],
            "dataset_family": s["dataset_family"],
            "required_fields": ", ".join(REQUIRED_SCHEMA_FIELDS),
            "forbidden_fields": ", ".join(FORBIDDEN_SCHEMA_FIELDS),
            "timestamp_field": "timestamp_utc",
            "non_signal": True,
            "manual_review_required": True,
            "current_phase": 137,
        })
    df = pd.DataFrame(rows)
    summary = {
        "total_schemas": len(rows),
        "current_phase": 137,
        "forbidden_columns_enforced": True,
        "timestamp_utc_required": True,
        "non_signal": True,
        "status": "READY",
    }
    return df, summary


def validate_ml_dataset_schema(df: pd.DataFrame, required_columns: List[str]) -> Dict:
    if df is None or not hasattr(df, "columns"):
        return {"valid": False, "issues": ["DataFrame is None or invalid"], "non_signal": True}
    issues = []
    missing = [c for c in required_columns if c not in df.columns]
    if missing:
        issues.append(f"Missing required columns: {missing}")
    forbidden = [c for c in FORBIDDEN_SCHEMA_FIELDS if c in (df.columns if hasattr(df, 'columns') else [])]
    if forbidden:
        issues.append(f"Forbidden columns found: {forbidden}")
    return {"valid": len(issues) == 0, "issues": issues, "non_signal": True}


def summarize_ml_dataset_schema(df: pd.DataFrame) -> Dict:
    return {
        "total_schemas": len(df),
        "current_phase": 137,
        "forbidden_columns_enforced": True,
        "timestamp_utc_required": True,
        "non_signal": True,
        "status": "READY",
    }
