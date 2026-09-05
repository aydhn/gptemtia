"""Phase 124: Run Feature Store Validation Catalog Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_store_integration.feature_store_integration_config import (
    get_default_feature_store_integration_profile,
)
from advanced_feature_store_integration.feature_store_catalog_reports import (
    build_feature_store_feature_catalog_report,
    build_feature_store_factor_catalog_report,
    build_feature_store_validation_catalog_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_feature_store_integration_profile()

    df_fc, s_fc = build_feature_store_feature_catalog_report(profile)
    df_fac, s_fac = build_feature_store_factor_catalog_report(profile)
    df_vc, s_vc = build_feature_store_validation_catalog_report(profile)

    data_lake.save_feature_store_feature_catalog_report(df_fc, s_fc)
    data_lake.save_feature_store_factor_catalog_report(df_fac, s_fac)
    data_lake.save_feature_store_validation_catalog_report(df_vc, s_vc)

    print("=" * 70)
    print("PHASE 124: VALIDATION & FEATURE/FACTOR CATALOGS")
    print("=" * 70)
    print(f"Feature Catalog Count  : {s_fc['total_features']}")
    print(f"Factor Catalog Count   : {s_fac['total_factors']}")
    print(f"Validation Items Count : {s_vc['total_validations']}")
    print(f"Validation Passes      : {s_vc['pass_count']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
