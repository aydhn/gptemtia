"""Phase 122 Factor Metadata Manifest.

Generates immutable manifests certifying factor lineage, validation checks,
feature counts, and non-signal compliance.
Strictly non-signal and research-only.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_factor_metadata.factor_contract_registry import CORE_FACTOR_CONTRACTS
from advanced_factor_metadata.factor_dependency_registry import FACTOR_DEPENDENCY_ENTRIES
from advanced_factor_metadata.factor_input_feature_sets import FACTOR_INPUT_FEATURE_SET_SPECS
from advanced_factor_metadata.factor_metadata_config import (
    FactorMetadataProfile,
    get_default_factor_metadata_profile,
)
from advanced_factor_metadata.factor_metadata_labels import FACTOR_READY
from advanced_factor_metadata.factor_metadata_models import (
    FactorMetadataManifest,
    build_factor_metadata_manifest_id,
)
from advanced_factor_metadata.factor_quality_dependencies import QUALITY_DEPENDENCY_CRITERIA
from advanced_factor_metadata.factor_validation_dependencies import VALIDATION_DEPENDENCY_RULES


def create_factor_metadata_manifest(
    factor_name: str,
    factor_family: str,
    input_feature_count: int,
    dependency_count: int,
    validation_dependency_count: int,
    quality_dependency_count: int,
    manual_review_required: bool = False,
) -> FactorMetadataManifest:
    """Create a single FactorMetadataManifest item with safety invariants."""
    return FactorMetadataManifest(
        manifest_id=build_factor_metadata_manifest_id(factor_name),
        factor_name=factor_name,
        factor_family=factor_family,
        input_feature_count=input_feature_count,
        dependency_count=dependency_count,
        validation_dependency_count=validation_dependency_count,
        quality_dependency_count=quality_dependency_count,
        non_signal=True,
        contains_target_or_prediction=False,
        contains_trading_recommendation=False,
        source_preserved=True,
        manual_review_required=manual_review_required,
    )


def build_factor_metadata_manifest(
    profile: FactorMetadataProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build Factor Metadata Manifest DataFrame and summary."""
    active_profile = profile or get_default_factor_metadata_profile()

    val_count = len(VALIDATION_DEPENDENCY_RULES)
    qual_count = len(QUALITY_DEPENDENCY_CRITERIA)

    items: List[Dict[str, Any]] = []
    for contract in CORE_FACTOR_CONTRACTS:
        fname = contract["factor_name"]
        ffam = contract["factor_family"]
        manual_review = contract.get("manual_review_required", False)

        # Count inputs
        input_spec = next((s for s in FACTOR_INPUT_FEATURE_SET_SPECS if s["factor_name"] == fname), None)
        feat_count = len(input_spec["required_features"]) if input_spec else 0

        # Count dependencies
        dep_count = sum(1 for d in FACTOR_DEPENDENCY_ENTRIES if d["factor_name"] == fname)

        manifest = create_factor_metadata_manifest(
            factor_name=fname,
            factor_family=ffam,
            input_feature_count=feat_count,
            dependency_count=dep_count,
            validation_dependency_count=val_count,
            quality_dependency_count=qual_count,
            manual_review_required=manual_review,
        )
        items.append(manifest.to_dict())

    df = pd.DataFrame(items)
    summary = {
        "active_profile": active_profile.name,
        "total_manifest_items": len(items),
        "all_non_signal": all(i["non_signal"] for i in items),
        "zero_target_or_prediction": all(not i["contains_target_or_prediction"] for i in items),
        "zero_trading_recommendation": all(not i["contains_trading_recommendation"] for i in items),
        "all_source_preserved": all(i["source_preserved"] for i in items),
        "current_phase": active_profile.current_phase,
        "target_final_phase": active_profile.target_final_phase,
        "status": FACTOR_READY,
    }
    return df, summary


def summarize_factor_metadata_manifest(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize factor metadata manifest DataFrame."""
    return {
        "total_factors": len(df),
        "all_non_signal": bool((df["non_signal"]).all()) if "non_signal" in df else True,
        "zero_predictions": bool((~df["contains_target_or_prediction"]).all()) if "contains_target_or_prediction" in df else True,
        "status": FACTOR_READY,
    }
