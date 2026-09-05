"""Phase 127: Run Regime Matrix Health Check Script.

Runs subsystem health checks and saves health audit report for Phase 127.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_matrix.regime_matrix_health import (
    run_regime_matrix_health_check,
)


def main():
    data_lake = DataLake()

    df_hlth, s_hlth = run_regime_matrix_health_check()
    data_lake.save_regime_matrix_health(df_hlth, s_hlth)

    print("=" * 70)
    print("PHASE 127: REGIME MATRIX SUBSYSTEM HEALTH CHECK")
    print("=" * 70)
    print(f"Overall Health   : {s_hlth['overall_health']}")
    print(f"Total Subsystems : {s_hlth['total_subsystems']}")
    print(f"Healthy Count    : {s_hlth['healthy_subsystems']}")
    print(f"Degraded Count   : {s_hlth['degraded_subsystems']}")
    print(f"Non-Signal       : {s_hlth['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
