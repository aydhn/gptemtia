# -*- coding: utf-8 -*-
"""Phase 149: Run Monte Carlo Master Status Script.

Executes the full Phase 149 Monte Carlo robustness and parameter stability pipeline,
compiles master status, validates safety boundaries, checks Phase 150 handoff readiness,
and saves all reports to DataLake and output directories.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from advanced_monte_carlo_robustness.monte_carlo_config import (
    get_default_monte_carlo_profile,
)
from advanced_monte_carlo_robustness.monte_carlo_pipeline import (
    MonteCarloRobustnessPipeline,
)


def main():
    settings = get_settings()
    profile = get_default_monte_carlo_profile()
    pipeline = MonteCarloRobustnessPipeline(profile=profile)

    status_df, summary = pipeline.build_monte_carlo_status(save=True)

    print("=" * 70)
    print("PHASE 149: MONTE CARLO ROBUSTNESS & PARAMETER STABILITY MASTER STATUS")
    print("=" * 70)
    print(status_df.to_string(index=False))
    print("-" * 70)
    print(f"Phase                 : {summary.get('current_phase', 149)}")
    print(f"Target Final Phase    : {summary.get('target_final_phase', 160)}")
    print(f"Next Phase            : {summary.get('next_phase', 150)}")
    print(f"Profile               : {profile.profile_name}")
    print(f"All Components Ready  : {summary.get('all_components_ready')}")
    print(f"Phase Status          : {summary.get('phase_status')}")
    print(f"Non-Signal Invariant  : {summary.get('non_signal')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
