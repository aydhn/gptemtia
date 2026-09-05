import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_fusion.fusion_feature_metadata_registry import (
    get_fusion_feature_metadata_registry,
    get_fusion_feature_metadata_summary,
)
from advanced_feature_fusion.fusion_feature_dependency_registry import (
    get_fusion_feature_dependency_registry,
    get_fusion_feature_dependency_summary,
)


def main():
    data_lake = DataLake()

    metadata_list = get_fusion_feature_metadata_registry()
    meta_summary = get_fusion_feature_metadata_summary()

    deps = get_fusion_feature_dependency_registry()
    dep_summary = get_fusion_feature_dependency_summary()

    data_lake.save_fusion_feature_metadata_registry([m.to_dict() for m in metadata_list])
    data_lake.save_fusion_feature_dependency_registry(deps)

    print("=" * 70)
    print("PHASE 120: FUSION FEATURE METADATA & DEPENDENCY REGISTRY")
    print("=" * 70)
    print(f"Total Features  : {meta_summary['total_features']}")
    print(f"Domains         : {meta_summary['domains']}")
    print(f"Families        : {meta_summary['families']}")
    print(f"Dependencies    : {dep_summary['tracked_feature_count']} features tracked")
    print(f"Non-Signal Mandate: {meta_summary['zero_signal_guarantee']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
