"""Phase 134 Script: Run Regime FeatureStore Contracts, Entities & Policies.

Generates contracts, entities, and version/partition policies, registering them in DataLake.
"""

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    get_default_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_contracts import (
    build_regime_featurestore_contract_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_entities import (
    build_regime_featurestore_entity_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_version_policies import (
    build_regime_featurestore_version_policy_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_partition_policies import (
    build_regime_featurestore_partition_policy_registry,
)
from data.storage.data_lake import DataLake


def main() -> None:
    data_lake = DataLake()
    profile = get_default_regime_featurestore_profile()

    c_df, c_sum = build_regime_featurestore_contract_registry(profile)
    e_df, e_sum = build_regime_featurestore_entity_registry(profile)
    v_df, v_sum = build_regime_featurestore_version_policy_registry(profile)
    pt_df, pt_sum = build_regime_featurestore_partition_policy_registry(profile)

    data_lake.save_regime_featurestore_contract_registry(c_df, c_sum)
    data_lake.save_regime_featurestore_entity_registry(e_df, e_sum)
    data_lake.save_regime_featurestore_version_policy_registry(v_df, v_sum)
    data_lake.save_regime_featurestore_partition_policy_registry(pt_df, pt_sum)

    print(f"Phase 134: Contracts ({len(c_df)}), Entities ({len(e_df)}), Policies generated successfully.")


if __name__ == "__main__":
    main()
