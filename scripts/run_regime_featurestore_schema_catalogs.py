"""Phase 134 Script: Run Regime FeatureStore Namespace, Schema & Access Contracts.

Generates namespaces, schemas, read contracts, write contracts, and query contracts.
"""

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    get_default_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_namespace import (
    build_regime_featurestore_namespace_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_schema import (
    build_regime_featurestore_schema_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_read_contracts import (
    build_regime_featurestore_read_contract_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_write_contracts import (
    build_regime_featurestore_write_contract_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_query_contracts import (
    build_regime_featurestore_query_contract_registry,
)
from data.storage.data_lake import DataLake


def main() -> None:
    data_lake = DataLake()
    profile = get_default_regime_featurestore_profile()

    n_df, n_sum = build_regime_featurestore_namespace_registry(profile)
    s_df, s_sum = build_regime_featurestore_schema_registry(profile)
    rc_df, rc_sum = build_regime_featurestore_read_contract_registry(profile)
    wc_df, wc_sum = build_regime_featurestore_write_contract_registry(profile)
    qc_df, qc_sum = build_regime_featurestore_query_contract_registry(profile)

    data_lake.save_regime_featurestore_namespace_registry(n_df, n_sum)
    data_lake.save_regime_featurestore_schema_registry(s_df, s_sum)
    data_lake.save_regime_featurestore_read_contract_registry(rc_df, rc_sum)
    data_lake.save_regime_featurestore_write_contract_registry(wc_df, wc_sum)
    data_lake.save_regime_featurestore_query_contract_registry(qc_df, qc_sum)

    print(f"Phase 134: Namespace ({len(n_df)}), Schema ({len(s_df)}), and Read/Write/Query contracts registered.")


if __name__ == "__main__":
    main()
