"""Phase 135: Run Regime Acceptance Status Script.

Prints high-level operational status and artifacts status for Phase 135.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_regime_acceptance.regime_acceptance_config import (
    get_default_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_block_status import (
    build_regime_block_status_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_regime_acceptance_profile()

    df_stat, s_stat = build_regime_block_status_report(profile)
    data_lake.save_regime_block_status_report(df_stat, s_stat)

    print("=" * 70)
    print("PHASE 135: REGIME BLOCK OVERALL STATUS")
    print("=" * 70)
    print(f"Phase Range        : {s_stat['phase_start']}-{s_stat['phase_end']}")
    print(f"Next Phase         : {s_stat['next_phase']}")
    print(f"Target Final Phase : {s_stat['target_final_phase']}")
    print(f"Overall Status     : {s_stat['overall_status']}")
    print(f"Acceptance Score   : {s_stat['acceptance_score']}")
    print(f"Total Modules      : {s_stat['total_modules']}")
    print(f"Non-Signal         : {s_stat['non_signal']}")
    print(f"Official Approval  : {s_stat['official_approval']}")
    print(f"Production Ready   : {s_stat['production_ready']}")
    print(f"Broker Ready       : {s_stat['broker_ready']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
