from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)
from advanced_cross_asset_alignment.cross_asset_alignment_models import (
    AlignedFeatureMatrixManifest,
    build_aligned_feature_matrix_manifest_id,
)


DEFAULT_MANIFESTS: List[Dict[str, Any]] = [
    {
        "matrix_name": "fx_cross_asset_aligned_matrix_v1",
        "base_domain": "fx",
        "aligned_domains": ["commodity", "macro", "calendar", "news"],
        "row_count": 1000,
        "feature_count": 28,
        "join_policy": "join_policy_asof_backward",
        "source_preserved": True,
        "non_signal": True,
        "contains_target_or_prediction": False,
        "manual_review_required": False,
    },
    {
        "matrix_name": "commodity_cross_asset_aligned_matrix_v1",
        "base_domain": "commodity",
        "aligned_domains": ["fx", "macro", "calendar", "news"],
        "row_count": 1000,
        "feature_count": 32,
        "join_policy": "join_policy_asof_backward",
        "source_preserved": True,
        "non_signal": True,
        "contains_target_or_prediction": False,
        "manual_review_required": False,
    },
]


def create_aligned_feature_matrix_manifest(
    matrix_name: str,
    base_domain: str,
    aligned_domains: List[str],
    row_count: int,
    feature_count: int,
    join_policy: str = "join_policy_asof_backward",
    manual_review_required: bool = False,
) -> AlignedFeatureMatrixManifest:
    return AlignedFeatureMatrixManifest(
        manifest_id=build_aligned_feature_matrix_manifest_id(matrix_name),
        matrix_name=matrix_name,
        base_domain=base_domain,
        aligned_domains=aligned_domains,
        row_count=row_count,
        feature_count=feature_count,
        join_policy=join_policy,
        source_preserved=True,
        non_signal=True,
        contains_target_or_prediction=False,
        manual_review_required=manual_review_required,
    )


def build_aligned_feature_matrix_manifest(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()

    rows = []
    for item in DEFAULT_MANIFESTS:
        manifest = create_aligned_feature_matrix_manifest(
            matrix_name=item["matrix_name"],
            base_domain=item["base_domain"],
            aligned_domains=item["aligned_domains"],
            row_count=item["row_count"],
            feature_count=item["feature_count"],
            join_policy=item["join_policy"],
            manual_review_required=item["manual_review_required"],
        )
        rows.append(manifest.to_dict())

    df = pd.DataFrame(rows)
    summary = summarize_aligned_feature_matrix_manifest(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_aligned_feature_matrix_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_manifests": 0, "status": "EMPTY"}

    all_non_signal = bool(df["non_signal"].all()) if "non_signal" in df.columns else False
    all_no_targets = bool((~df["contains_target_or_prediction"]).all()) if "contains_target_or_prediction" in df.columns else False
    all_source_preserved = bool(df["source_preserved"].all()) if "source_preserved" in df.columns else False

    is_ready = all_non_signal and all_no_targets and all_source_preserved

    return {
        "total_manifests": len(df),
        "matrix_names": list(df["matrix_name"]) if "matrix_name" in df.columns else [],
        "all_source_preserved": all_source_preserved,
        "all_non_signal": all_non_signal,
        "all_no_target_or_prediction": all_no_targets,
        "status": "READY" if is_ready else "SAFETY_VIOLATION",
    }


build_aligned_feature_matrix_manifest_registry = build_aligned_feature_matrix_manifest

