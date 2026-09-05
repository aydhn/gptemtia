"""Phase 124: Run Feature Store Catalogs Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_store_integration.feature_store_integration_config import (
    get_default_feature_store_integration_profile,
)
from advanced_feature_store_integration.feature_store_entity_registry import (
    build_feature_store_entity_registry,
)
from advanced_feature_store_integration.feature_store_feature_registry import (
    build_feature_store_feature_registry,
)
from advanced_feature_store_integration.feature_store_factor_registry import (
    build_feature_store_factor_registry,
)
from advanced_feature_store_integration.feature_store_namespace_registry import (
    build_feature_store_namespace_registry,
)
from advanced_feature_store_integration.feature_store_schema_registry import (
    build_feature_store_schema_registry,
)


def main():
    data_lake = DataLake()
    profile = get_default_feature_store_integration_profile()

    df_ent, s_ent = build_feature_store_entity_registry(profile)
    df_feat, s_feat = build_feature_store_feature_registry(profile)
    df_fac, s_fac = build_feature_store_factor_registry(profile)
    df_ns, s_ns = build_feature_store_namespace_registry(profile)
    df_sch, s_sch = build_feature_store_schema_registry(profile)

    data_lake.save_feature_store_entity_registry(df_ent, s_ent)
    data_lake.save_feature_store_feature_registry(df_feat, s_feat)
    data_lake.save_feature_store_factor_registry(df_fac, s_fac)
    data_lake.save_feature_store_namespace_registry(df_ns, s_ns)
    data_lake.save_feature_store_schema_registry(df_sch, s_sch)

    print("=" * 70)
    print("PHASE 124: FEATURE STORE CATALOGS & REGISTRIES")
    print("=" * 70)
    print(f"Total Entities  : {s_ent['total_entities']}")
    print(f"Total Features  : {s_feat['total_features']}")
    print(f"Total Factors   : {s_fac['total_factors']}")
    print(f"Total Schemas   : {s_sch['total_schemas']}")
    print(f"Total Namespaces: {s_ns['total_namespaces']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
