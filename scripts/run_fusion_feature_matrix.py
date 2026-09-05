import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_fusion.fusion_feature_pipeline import run_fusion_feature_pipeline


def main():
    data_lake = DataLake()

    results = run_fusion_feature_pipeline(
        dry_run=True,
        data_lake=data_lake,
    )
    manifest = results["manifest"]
    handoff = results["handoff"]

    print("=" * 70)
    print("PHASE 120: FUSION FEATURE MATRIX EXECUTION")
    print("=" * 70)
    print(f"Matrix ID       : {manifest['matrix_id']}")
    print(f"Total Rows      : {manifest['total_rows']}")
    print(f"Total Columns   : {manifest['total_columns']}")
    print(f"Domains Included: {manifest['domains_included']}")
    print(f"Feature Columns : {len(manifest['feature_columns'])}")
    print(f"No Lookahead    : {manifest['no_lookahead_guaranteed']}")
    print(f"Metadata Only   : {manifest['is_strictly_metadata_only']}")
    print(f"Non-Signal      : {manifest['is_non_signal_guaranteed']}")
    print(f"Readiness Score : {handoff['readiness_score']}")
    print(f"Handoff Ready   : {handoff['handoff_ready']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
