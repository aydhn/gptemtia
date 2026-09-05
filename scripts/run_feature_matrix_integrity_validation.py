import sys
import pandas as pd
import numpy as np
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_validation.feature_matrix_integrity_contracts import (
    get_feature_matrix_integrity_contracts,
    validate_feature_matrix_integrity,
)
from advanced_feature_validation.feature_matrix_integrity_manifest import create_feature_matrix_integrity_manifest
from advanced_feature_validation.warmup_nan_validation import validate_warmup_nans
from advanced_feature_validation.duplicate_feature_validation import validate_duplicate_feature_columns
from advanced_feature_validation.namespace_collision_validation import validate_namespace_collisions
from advanced_feature_validation.feature_numeric_sanity_validation import validate_feature_numeric_sanity
from advanced_feature_validation.feature_missingness_validation import validate_feature_missingness
from advanced_feature_validation.feature_infinite_value_validation import validate_feature_infinite_values


def main():
    settings = get_settings()
    data_lake = DataLake()

    # Create dummy matrix
    sample_df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=10, freq="D"),
        "asset_symbol": ["BRENT"] * 10,
        "feat_sma_5": [np.nan, np.nan, np.nan, np.nan, 75.2, 75.5, 75.8, 76.0, 76.2, 76.5],
        "feat_ret_1d": [0.01, -0.02, 0.005, 0.012, -0.004, 0.008, -0.001, 0.015, -0.003, 0.002],
    })

    contracts = get_feature_matrix_integrity_contracts()
    integrity_res = validate_feature_matrix_integrity(sample_df, matrix_name="sample_matrix")
    manifest = create_feature_matrix_integrity_manifest(sample_df, matrix_name="sample_matrix")
    warmup_res = validate_warmup_nans(sample_df, warmup_window=4)
    dup_res = validate_duplicate_feature_columns(sample_df)
    ns_res = validate_namespace_collisions(sample_df)
    sanity_res = validate_feature_numeric_sanity(sample_df)
    miss_res = validate_feature_missingness(sample_df)
    inf_res = validate_feature_infinite_values(sample_df)

    data_lake.save_feature_matrix_integrity_contracts(integrity_res)
    data_lake.save_feature_matrix_integrity_manifest(manifest)
    data_lake.save_warmup_nan_validation_registry(warmup_res)
    data_lake.save_duplicate_feature_validation_registry(dup_res)
    data_lake.save_namespace_collision_validation_registry(ns_res)
    data_lake.save_feature_numeric_sanity_validation_registry(sanity_res)
    data_lake.save_feature_missingness_validation_registry(miss_res)
    data_lake.save_feature_infinite_value_validation_registry(inf_res)

    print("=" * 70)
    print("PHASE 121: FEATURE MATRIX INTEGRITY VALIDATION")
    print("=" * 70)
    print(f"Matrix Integrity Valid : {integrity_res['is_valid']}")
    print(f"Total Columns          : {manifest['total_columns']}")
    print(f"Warmup NaNs Preserved  : {warmup_res['is_valid']}")
    print(f"Duplicate Columns      : {dup_res['duplicate_columns_count']}")
    print(f"Namespace Collisions   : {ns_res['collision_count']}")
    print(f"Numeric Sanity Valid   : {sanity_res['is_valid']}")
    print(f"Infinite Values Count  : {inf_res['infinite_count']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
