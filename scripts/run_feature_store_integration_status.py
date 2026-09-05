"""Phase 124: Run Status Report Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_feature_store_integration.feature_store_integration_pipeline import (
    FeatureStoreIntegrationPipeline,
)


def main():
    pipeline = FeatureStoreIntegrationPipeline()
    df_stat, s_stat = pipeline.build_feature_store_integration_status(save=False)

    print("=" * 70)
    print("PHASE 124: FEATURE STORE INTEGRATION STATUS")
    print("=" * 70)
    print(f"Overall Status   : {s_stat['overall_status']}")
    print(f"Total Components : {s_stat['total_components']}")
    print(f"Ready Components : {s_stat['ready_components']}")
    print(f"Current Phase    : {s_stat['current_phase']}")
    print(f"Next Phase       : {s_stat['next_phase']}")
    print(f"Target Phase     : {s_stat['target_final_phase']}")
    print(f"Non-Signal       : {s_stat['non_signal']}")
    print(f"Source Preserved : {s_stat['source_preserved']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
