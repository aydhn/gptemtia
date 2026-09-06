"""Phase 134 Script: Run Regime FeatureStore Policies, Manifest & Phase 135 Handoff.

Generates governance policies, manual review blocker store, metadata manifest, and Phase 135 handoff.
"""

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    get_default_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_manual_review_blocker_store import (
    build_regime_manual_review_blocker_store_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_forbidden_column_policies import (
    build_regime_featurestore_forbidden_column_policy_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_non_signal_policies import (
    build_regime_featurestore_non_signal_policy_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_source_preservation_policies import (
    build_regime_featurestore_source_preservation_policy_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_metadata_manifest import (
    build_regime_featurestore_metadata_manifest,
)
from advanced_regime_featurestore_integration.phase_135_handoff import (
    build_phase_135_regime_classification_acceptance_handoff_report,
)
from data.storage.data_lake import DataLake


def main() -> None:
    data_lake = DataLake()
    profile = get_default_regime_featurestore_profile()

    blk_df, blk_sum = build_regime_manual_review_blocker_store_registry(profile)
    fc_df, fc_sum = build_regime_featurestore_forbidden_column_policy_registry(profile)
    nsp_df, nsp_sum = build_regime_featurestore_non_signal_policy_registry(profile)
    spp_df, spp_sum = build_regime_featurestore_source_preservation_policy_registry(profile)
    man_df, man_sum = build_regime_featurestore_metadata_manifest(profile)
    ho_df, ho_sum = build_phase_135_regime_classification_acceptance_handoff_report(profile)

    data_lake.save_regime_manual_review_blocker_store_registry(blk_df, blk_sum)
    data_lake.save_regime_featurestore_forbidden_column_policy_registry(fc_df, fc_sum)
    data_lake.save_regime_featurestore_non_signal_policy_registry(nsp_df, nsp_sum)
    data_lake.save_regime_featurestore_source_preservation_policy_registry(spp_df, spp_sum)
    data_lake.save_regime_featurestore_metadata_manifest(man_df, man_sum)
    data_lake.save_phase_135_regime_classification_acceptance_handoff_report(ho_df, ho_sum)

    print(f"Phase 134: Blockers ({len(blk_df)}), Policies, Manifest, and Phase 135 Handoff ({len(ho_df)} items) registered.")


if __name__ == "__main__":
    main()
