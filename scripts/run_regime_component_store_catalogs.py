"""Phase 134 Script: Run Regime Component Store Catalogs.

Generates all 8 component store catalogs for Phase 126-133 outputs, registering them in DataLake.
"""

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    get_default_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_taxonomy_store_catalog import (
    build_regime_taxonomy_store_catalog,
)
from advanced_regime_featurestore_integration.regime_matrix_store_catalog import (
    build_regime_matrix_store_catalog,
)
from advanced_regime_featurestore_integration.candidate_state_store_catalog import (
    build_candidate_state_store_catalog,
)
from advanced_regime_featurestore_integration.pseudo_state_store_catalog import (
    build_pseudo_state_store_catalog,
)
from advanced_regime_featurestore_integration.transition_store_catalog import (
    build_transition_store_catalog,
)
from advanced_regime_featurestore_integration.cross_asset_regime_store_catalog import (
    build_cross_asset_regime_store_catalog,
)
from advanced_regime_featurestore_integration.macro_event_news_regime_store_catalog import (
    build_macro_event_news_regime_store_catalog,
)
from advanced_regime_featurestore_integration.regime_validation_acceptance_store_catalog import (
    build_regime_validation_acceptance_store_catalog,
)
from data.storage.data_lake import DataLake


def main() -> None:
    data_lake = DataLake()
    profile = get_default_regime_featurestore_profile()

    tax_df, tax_sum = build_regime_taxonomy_store_catalog(profile)
    mat_df, mat_sum = build_regime_matrix_store_catalog(profile)
    cand_df, cand_sum = build_candidate_state_store_catalog(profile)
    ps_df, ps_sum = build_pseudo_state_store_catalog(profile)
    tr_df, tr_sum = build_transition_store_catalog(profile)
    ca_df, ca_sum = build_cross_asset_regime_store_catalog(profile)
    mne_df, mne_sum = build_macro_event_news_regime_store_catalog(profile)
    va_df, va_sum = build_regime_validation_acceptance_store_catalog(profile)

    data_lake.save_regime_taxonomy_store_catalog(tax_df, tax_sum)
    data_lake.save_regime_matrix_store_catalog(mat_df, mat_sum)
    data_lake.save_candidate_state_store_catalog(cand_df, cand_sum)
    data_lake.save_pseudo_state_store_catalog(ps_df, ps_sum)
    data_lake.save_transition_store_catalog(tr_df, tr_sum)
    data_lake.save_cross_asset_regime_store_catalog(ca_df, ca_sum)
    data_lake.save_macro_event_news_regime_store_catalog(mne_df, mne_sum)
    data_lake.save_regime_validation_acceptance_store_catalog(va_df, va_sum)

    total_catalog_items = (
        len(tax_df) + len(mat_df) + len(cand_df) + len(ps_df) + len(tr_df) + len(ca_df) + len(mne_df) + len(va_df)
    )
    print(f"Phase 134: All 8 component store catalogs generated successfully ({total_catalog_items} total catalog entries).")


if __name__ == "__main__":
    main()
