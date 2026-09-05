import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_input_contracts import (
    build_feature_input_contract_registry,
)


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_feature_engine_profile()

    df, summary = build_feature_input_contract_registry(profile)
    data_lake.save_feature_input_contract_registry(df, summary)

    print("=" * 70)
    print("PHASE 116: CANONICAL FEATURE INPUT CONTRACTS REGISTRY")
    print("=" * 70)
    print(f"Total Contracts: {summary['total_contracts']}")
    print(f"Non-Signal     : {summary['non_signal']}")
    print("-" * 70)
    for _, row in df.iterrows():
        req_fields = ", ".join(row["required_fields"])
        print(f" - {row['dataset_type']:<30} | Fields: {req_fields}")
        print(f"   Quality Dep     : {row['quality_dependency']}")
        print(f"   Normalization   : {row['normalization_dependency']}")
        print(f"   Lineage Dep     : {row['lineage_dependency']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
