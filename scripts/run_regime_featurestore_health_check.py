"""Phase 134 Script: Run Regime FeatureStore Health Check.

Performs subsystem availability checks across Phase 123 through Phase 134.
"""

from advanced_regime_featurestore_integration.regime_featurestore_config import (
    get_default_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_health import (
    build_regime_featurestore_health_check,
)
from data.storage.data_lake import DataLake


def main() -> None:
    data_lake = DataLake()
    profile = get_default_regime_featurestore_profile()

    h_df, h_sum = build_regime_featurestore_health_check(profile=profile)
    data_lake.save_regime_featurestore_health_check(h_df, h_sum)

    status_str = "HEALTHY" if h_sum.get("all_healthy", True) else "DEGRADED"
    print(f"Phase 134 Health Check: {status_str} ({h_sum.get('healthy_checks')}/{h_sum.get('total_checks')} checks passed).")


if __name__ == "__main__":
    main()
