"""Phase 137: Run ML Dataset Contracts and Source Catalog Registry Script.

Builds and persists ML dataset contracts and source catalog references.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    get_default_advanced_ml_dataset_profile,
)
from advanced_ml_dataset_registry.ml_dataset_contracts import (
    build_ml_dataset_contract_registry,
)
from advanced_ml_dataset_registry.ml_dataset_source_catalog import (
    build_ml_dataset_source_catalog_registry,
)
from reports.report_builder import ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_advanced_ml_dataset_profile()

    df_contracts, s_contracts = build_ml_dataset_contract_registry(profile)
    data_lake.save_ml_dataset_contract_registry(df_contracts, s_contracts)

    df_source, s_source = build_ml_dataset_source_catalog_registry(profile)
    data_lake.save_ml_dataset_source_catalog_registry(df_source, s_source)

    print("=" * 70)
    print("PHASE 137: ML DATASET CONTRACTS & SOURCE CATALOG")
    print("=" * 70)
    print(ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Contracts : {s_contracts['total_contracts']}")
    print(f"Total Sources   : {s_source['total_sources']}")
    print(f"Materialization : Blocked (contract-only)")
    print(f"Model Training  : Blocked")
    print(f"Non-Signal      : {s_contracts['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
