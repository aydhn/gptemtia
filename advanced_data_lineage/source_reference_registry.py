from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile
from advanced_data_lineage.data_lineage_models import (
    SourceReference,
    build_source_reference_id,
    build_provenance_source_id,
)


REFERENCE_SPECS = [
    ("fx_dry_run_fixture_source", "fx_fixture_provider", "local_fixture_uri", "file://fixtures/fx_contract_sample.parquet", "canonical://source/fx/sample_fixture", False, False, False, False),
    ("commodity_dry_run_fixture_source", "commodity_fixture_provider", "local_fixture_uri", "file://fixtures/commodity_contract_sample.parquet", "canonical://source/commodity/sample_fixture", False, False, False, False),
    ("macro_dry_run_fixture_source", "macro_fixture_provider", "local_fixture_uri", "file://fixtures/macro_contract_sample.parquet", "canonical://source/macro/sample_fixture", False, False, False, False),
    ("calendar_dry_run_fixture_source", "calendar_fixture_provider", "local_fixture_uri", "file://fixtures/calendar_contract_sample.parquet", "canonical://source/calendar/sample_fixture", False, False, False, False),
    ("news_metadata_dry_run_fixture_source", "news_fixture_provider", "metadata_only_uri", "file://fixtures/news_metadata_contract_sample.parquet", "canonical://source/news/metadata_only_fixture", True, False, False, False),
    ("manual_file_placeholder_source", "manual_file_provider", "file_path_reference", "data/manual_dropzone/manual_dataset.csv", "canonical://source/manual/dataset_placeholder", False, False, False, True),
    ("local_cache_placeholder_source", "local_cache_provider", "cache_manifest_key", "cache://local_snapshot/latest", "canonical://source/cache/snapshot_placeholder", False, False, False, False),
    ("official_api_placeholder_source", "official_api_placeholder", "endpoint_contract_id", "urn:api:official:endpoint_v1", "canonical://source/official/contract_placeholder", False, False, False, True),
    ("licensed_provider_placeholder_source", "licensed_provider_placeholder", "feed_contract_id", "urn:feed:licensed:market_data_v2", "canonical://source/licensed/feed_placeholder", False, False, False, True),
    ("public_dataset_placeholder_source", "public_dataset_placeholder", "doi_or_urn", "urn:public:macro_calendar_open", "canonical://source/public/dataset_placeholder", False, False, False, False),
]


def build_default_source_references(
    profile: DataLineageProfile,
) -> List[SourceReference]:
    refs: List[SourceReference] = []
    for s_name, provider, r_type, r_val, can_ref, meta_only, has_cred, has_full, rev_req in REFERENCE_SPECS:
        s_id = build_provenance_source_id(s_name, provider)
        ref_id = build_source_reference_id(s_id, r_type)
        refs.append(
            SourceReference(
                reference_id=ref_id,
                source_id=s_id,
                reference_type=r_type,
                reference_value=r_val,
                canonical_reference=can_ref,
                metadata_only=meta_only,
                contains_credentials=has_cred,
                contains_full_text=has_full,
                manual_review_required=rev_req,
            )
        )
    return refs


def build_source_reference_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    refs = build_default_source_references(profile)
    records = [r.to_dict() for r in refs]
    df = pd.DataFrame.from_records(records)
    summary = summarize_source_reference_registry(df)
    return df, summary


def summarize_source_reference_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_references": len(df),
        "reference_ids": df["reference_id"].tolist() if "reference_id" in df.columns else [],
        "zero_credentials": bool((~df["contains_credentials"]).all()) if "contains_credentials" in df.columns and len(df) > 0 else True,
        "zero_full_text": bool((~df["contains_full_text"]).all()) if "contains_full_text" in df.columns and len(df) > 0 else True,
        "manual_review_count": int(df["manual_review_required"].sum()) if "manual_review_required" in df.columns else 0,
        "current_phase": 114,
        "target_final_phase": 160,
    }
