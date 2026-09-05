"""Fusion Feature Dependency Registry.

Tracks upstream dependencies, required input columns, and predecessor phases
for each fusion feature.
Strictly non-signal, research use only.
"""

from typing import Any, Dict, List, Optional
from advanced_feature_fusion.fusion_feature_metadata_registry import get_fusion_feature_metadata_registry


def get_fusion_feature_dependency_registry() -> Dict[str, Dict[str, Any]]:
    """Return dictionary mapping feature_id to its upstream dependencies."""
    metadata_list = get_fusion_feature_metadata_registry()
    dep_dict = {}
    for meta in metadata_list:
        dep_dict[meta.feature_id] = {
            "feature_id": meta.feature_id,
            "domain": meta.domain,
            "family": meta.feature_family,
            "required_columns": list(meta.input_columns),
            "predecessor_phase": 119 if meta.domain == "market_base" else 120,
            "is_signal": False,
        }
    return dep_dict


def validate_dependencies_satisfied(feature_id: str, available_columns: List[str]) -> bool:
    """Check if all required input columns for a feature are in available_columns."""
    registry = get_fusion_feature_dependency_registry()
    if feature_id not in registry:
        return False
    required = registry[feature_id]["required_columns"]
    return all(col in available_columns for col in required)


def get_fusion_feature_dependency_summary() -> Dict[str, Any]:
    """Summary of feature dependency registry."""
    registry = get_fusion_feature_dependency_registry()
    return {
        "tracked_feature_count": len(registry),
        "feature_ids": list(registry.keys()),
        "predecessor_phase_requirement": "Phase 119 Cross-Asset Alignment",
        "zero_signal_guarantee": True,
    }
