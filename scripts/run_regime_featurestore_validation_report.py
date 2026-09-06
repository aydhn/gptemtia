"""Phase 134 Script: Run Regime FeatureStore Validation & Safety Report.

Runs comprehensive invariant validation, builds safety boundary reports, and saves them to DataLake.
"""

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    get_default_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_profile_registry import (
    build_regime_featurestore_profile_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_contracts import (
    build_regime_featurestore_contract_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_schema import (
    build_regime_featurestore_schema_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_metadata_manifest import (
    build_regime_featurestore_metadata_manifest,
)
from advanced_regime_featurestore_integration.regime_featurestore_validation import (
    build_regime_featurestore_validation_report,
)
from advanced_regime_featurestore_integration.regime_featurestore_safety_boundary import (
    build_regime_featurestore_safety_boundary,
)
from data.storage.data_lake import DataLake


def main() -> None:
    data_lake = DataLake()
    profile = get_default_regime_featurestore_profile()

    p_df, _ = build_regime_featurestore_profile_registry(profile)
    c_df, _ = build_regime_featurestore_contract_registry(profile)
    s_df, _ = build_regime_featurestore_schema_registry(profile)
    m_df, _ = build_regime_featurestore_metadata_manifest(profile)
    safe_df, safe_sum = build_regime_featurestore_safety_boundary(profile)

    tables = {
        "profiles": p_df,
        "contracts": c_df,
        "schema": s_df,
        "manifest": m_df,
    }
    v_df, v_sum = build_regime_featurestore_validation_report(tables, profile)

    data_lake.save_regime_featurestore_validation_report(v_df, v_sum)
    data_lake.save_regime_featurestore_safety_boundary(safe_df, safe_sum)

    val_status = "PASSED" if v_sum.get("all_passed", True) else "FAILED"
    print(f"Phase 134: Validation {val_status} ({v_sum.get('total_checks')} checks), Safety Status: {safe_sum.get('safety_status')}.")


if __name__ == "__main__":
    main()
