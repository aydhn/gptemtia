"""Phase 126: Run Regime Foundation Status Script.

Generates and displays comprehensive overall status for Phase 126.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_foundation.regime_foundation_config import (
    get_default_regime_foundation_profile,
)
from advanced_regime_foundation.regime_foundation_pipeline import (
    RegimeFoundationPipeline,
)


def main():
    data_lake = DataLake()
    profile = get_default_regime_foundation_profile()
    pipeline = RegimeFoundationPipeline(data_lake=data_lake, profile=profile)

    df_stat, s_stat = pipeline.build_regime_foundation_status(save=True)

    print("=" * 70)
    print("PHASE 126: REGIME FOUNDATION OVERALL STATUS")
    print("=" * 70)
    print(f"Subsystem      : {df_stat.iloc[0]['subsystem']}")
    print(f"Phase          : {df_stat.iloc[0]['phase']}")
    print(f"Target Phase   : {df_stat.iloc[0]['target_final_phase']}")
    print(f"Next Phase     : {df_stat.iloc[0]['next_phase']}")
    print(f"Active Profile : {df_stat.iloc[0]['profile']}")
    print(f"Health Status  : {df_stat.iloc[0]['health_status']}")
    print(f"Validation     : {df_stat.iloc[0]['validation_status']}")
    print(f"Handoff Status : {df_stat.iloc[0]['handoff_status']}")
    print(f"Overall Status : {df_stat.iloc[0]['status']}")
    print(f"Non-Signal     : {df_stat.iloc[0]['non_signal']}")
    print(f"Model Training : {df_stat.iloc[0]['model_training_executed']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
