"""Phase 124: Run Feature Store Quality & Drift Catalog Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_store_integration.feature_store_integration_config import (
    get_default_feature_store_integration_profile,
)
from advanced_feature_store_integration.feature_store_quality_scores import (
    build_feature_store_quality_score_registry,
)
from advanced_feature_store_integration.feature_store_drift_scores import (
    build_feature_store_drift_score_registry,
)
from advanced_feature_store_integration.feature_store_catalog_reports import (
    build_feature_store_quality_drift_catalog_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_feature_store_integration_profile()

    df_qual, s_qual = build_feature_store_quality_score_registry(profile)
    df_drift, s_drift = build_feature_store_drift_score_registry(profile)
    df_qd, s_qd = build_feature_store_quality_drift_catalog_report(profile)

    data_lake.save_feature_store_quality_score_registry(df_qual, s_qual)
    data_lake.save_feature_store_drift_score_registry(df_drift, s_drift)
    data_lake.save_feature_store_quality_drift_catalog_report(df_qd, s_qd)

    print("=" * 70)
    print("PHASE 124: QUALITY & DRIFT CATALOG")
    print("=" * 70)
    print(f"Mean Quality Score: {s_qual['mean_quality_score']}")
    print(f"Mean Drift Score  : {s_drift['mean_drift_score']}")
    print(f"Catalog Items     : {s_qd['total_items']}")
    print(f"Non-Signal        : {s_qd['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
