from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    NormalizedViewManifest,
    build_normalized_view_manifest_id,
)


def create_normalized_view_manifest(
    dataset_name: str,
    dataset_type: str,
    provider_name: str,
    original_ref: str,
    normalized_ref: str,
    schema_version: str,
    row_count: int,
    normalized_field_count: int,
    manual_review_required: bool = False,
) -> NormalizedViewManifest:
    return NormalizedViewManifest(
        manifest_id=build_normalized_view_manifest_id(dataset_name, provider_name),
        dataset_name=dataset_name,
        dataset_type=dataset_type,
        provider_name=provider_name,
        original_ref=original_ref,
        normalized_ref=normalized_ref,
        schema_version=schema_version,
        row_count=row_count,
        normalized_field_count=normalized_field_count,
        source_preserved=True,
        destructive_action_allowed=False,
        manual_review_required=manual_review_required,
    )


def normalized_view_manifest_to_dict(manifest: NormalizedViewManifest) -> Dict[str, Any]:
    return manifest.to_dict()


def build_normalized_view_registry(
    manifests: List[NormalizedViewManifest],
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = [m.to_dict() for m in manifests]
    df = pd.DataFrame.from_records(records)
    summary = summarize_normalized_view_registry(df)
    return df, summary


def summarize_normalized_view_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_normalized_views": len(df),
        "all_source_preserved": bool(df["source_preserved"].all()) if "source_preserved" in df.columns and len(df) > 0 else True,
        "destructive_actions_prevented": bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns and len(df) > 0 else True,
        "total_rows_represented": int(df["row_count"].sum()) if "row_count" in df.columns else 0,
        "current_phase": 113,
        "target_final_phase": 160,
    }
