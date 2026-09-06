"""Phase 134 Script: Run Regime Accepted Reference & Dependency Registries.

Generates accepted reference registries (no-lookahead, metadata-only news, source preservation,
non-signal), dependency stores, and lineage references.
"""

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    get_default_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_accepted_reference_registries import (
    build_regime_no_lookahead_accepted_reference_registry,
    build_regime_metadata_only_news_accepted_reference_registry,
    build_regime_source_preservation_accepted_reference_registry,
    build_regime_non_signal_accepted_reference_registry,
)
from advanced_regime_featurestore_integration.regime_quality_dependency_store import (
    build_regime_quality_dependency_store_registry,
)
from advanced_regime_featurestore_integration.regime_validation_dependency_store import (
    build_regime_validation_dependency_store_registry,
)
from advanced_regime_featurestore_integration.regime_lineage_references import (
    build_regime_lineage_reference_registry,
)
from data.storage.data_lake import DataLake


def main() -> None:
    data_lake = DataLake()
    profile = get_default_regime_featurestore_profile()

    nl_df, nl_sum = build_regime_no_lookahead_accepted_reference_registry(profile)
    mo_df, mo_sum = build_regime_metadata_only_news_accepted_reference_registry(profile)
    sp_df, sp_sum = build_regime_source_preservation_accepted_reference_registry(profile)
    ns_df, ns_sum = build_regime_non_signal_accepted_reference_registry(profile)
    qd_df, qd_sum = build_regime_quality_dependency_store_registry(profile)
    vd_df, vd_sum = build_regime_validation_dependency_store_registry(profile)
    lin_df, lin_sum = build_regime_lineage_reference_registry(profile)

    data_lake.save_regime_no_lookahead_accepted_reference_registry(nl_df, nl_sum)
    data_lake.save_regime_metadata_only_news_accepted_reference_registry(mo_df, mo_sum)
    data_lake.save_regime_source_preservation_accepted_reference_registry(sp_df, sp_sum)
    data_lake.save_regime_non_signal_accepted_reference_registry(ns_df, ns_sum)
    data_lake.save_regime_quality_dependency_store_registry(qd_df, qd_sum)
    data_lake.save_regime_validation_dependency_store_registry(vd_df, vd_sum)
    data_lake.save_regime_lineage_reference_registry(lin_df, lin_sum)

    total_refs = len(nl_df) + len(mo_df) + len(sp_df) + len(ns_df)
    print(f"Phase 134: Accepted references ({total_refs}), Dependencies ({len(qd_df) + len(vd_df)}), Lineage ({len(lin_df)}) registered.")


if __name__ == "__main__":
    main()
