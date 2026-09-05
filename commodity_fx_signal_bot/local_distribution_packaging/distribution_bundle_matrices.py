import pandas as pd
from .packaging_config import LocalDistributionPackagingProfile
from .packaging_models import DistributionBundleItem, build_distribution_bundle_item_id

def build_default_distribution_bundle_items(profile: LocalDistributionPackagingProfile) -> list[DistributionBundleItem]:
    return [
        DistributionBundleItem(
            bundle_id=build_distribution_bundle_item_id("doc1", "ref1"),
            item_name="doc1",
            source_ref="ref1",
            bundle_area="docs",
            artifact_label="artifact_documentation_only",
            include_rehearsal=True,
            exclusion_reason="",
            manual_review_required=True,
            warnings=["Not a real release file"]
        )
    ]

def build_distribution_bundle_inclusion_matrix(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_distribution_bundle_items(profile)
    df = pd.DataFrame([i.__dict__ for i in items if i.include_rehearsal])
    return df, summarize_distribution_bundle_matrix(df)

def build_distribution_bundle_exclusion_matrix(profile: LocalDistributionPackagingProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_distribution_bundle_items(profile)
    df = pd.DataFrame([i.__dict__ for i in items if not i.include_rehearsal])
    return df, summarize_distribution_bundle_matrix(df)

def summarize_distribution_bundle_matrix(df: pd.DataFrame) -> dict:
    return {"status": "generated", "rows": len(df)}
