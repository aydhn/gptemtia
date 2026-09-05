import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_engine_pipeline import FeatureEnginePipeline


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_feature_engine_profile()

    pipeline = FeatureEnginePipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=project_root,
        profile=profile,
    )

    tables, summary = pipeline.build_schemas_and_catalogs(save=True)
    ind_df = tables["indicator_catalogs"]
    ind_sum = summary["indicator_catalogs"]

    print("=" * 70)
    print("PHASE 116: INDICATOR CATALOG REGISTRY")
    print("=" * 70)
    print(f"Total Indicators: {ind_sum['total_indicators']}")
    print(f"Total Families  : {ind_sum['total_families']}")
    print(f"Families        : {', '.join(ind_sum['families'])}")
    print(f"Non-Signal      : {ind_sum['all_non_signal']}")
    print("-" * 70)
    for fam in ind_sum["families"]:
        fam_subset = ind_df[ind_df["indicator_family"] == fam]
        inds = ", ".join(fam_subset["indicator_name"].tolist())
        print(f" * {fam.upper():<16} : {inds}")
    print("=" * 70)


if __name__ == "__main__":
    main()
