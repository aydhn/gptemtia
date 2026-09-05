"""Phase 122: Run Factor Metadata Status Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_factor_metadata.factor_metadata_config import get_default_factor_metadata_profile
from advanced_factor_metadata.factor_metadata_pipeline import FactorMetadataPipeline


def main():
    settings = get_settings()
    data_lake = DataLake()
    project_root = Path(__file__).resolve().parent.parent
    profile = get_default_factor_metadata_profile()

    pipeline = FactorMetadataPipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=project_root,
        profile=profile,
    )

    status_df, summary = pipeline.build_factor_metadata_status(save=True)

    print("=" * 70)
    print("PHASE 122: FACTOR METADATA AND FACTOR FAMILIES STATUS")
    print("=" * 70)
    print(f"Active Profile   : {summary['active_profile']}")
    print(f"Current Phase    : {summary['current_phase']}")
    print(f"Next Phase       : {summary['next_phase']}")
    print(f"Target Final Phase: {summary['target_final_phase']}")
    print(f"Non-Signal       : {summary['non_signal']}")
    print(f"Status           : {summary['status']}")
    print("-" * 70)
    for _, row in status_df.iterrows():
        print(f"[{row['status']:<15}] {row['component']:<30} (Count: {row['count']})")
    print("=" * 70)


if __name__ == "__main__":
    main()
