# -*- coding: utf-8 -*-
"""Phase 148: Run Stress Testing Master Status Script.

Executes the full Phase 148 stress testing and scenario simulation contract layer pipeline,
compiles master status, validates safety boundaries, checks Phase 149 handoff readiness,
and saves all reports to DataLake and output directories.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_testing_pipeline import (
    StressTestingPipeline,
)


def main():
    settings = get_settings()
    profile = get_default_stress_testing_profile()
    pipeline = StressTestingPipeline(profile=profile)

    status_df, summary = pipeline.build_stress_testing_status(save=True)

    print("=" * 70)
    print("PHASE 148: STRESS TESTING & SCENARIO SIMULATION MASTER STATUS")
    print("=" * 70)
    print(status_df.to_string(index=False))
    print("-" * 70)
    print(f"Phase                 : {summary.get('current_phase', 148)}")
    print(f"Target Final Phase    : {summary.get('target_final_phase', 160)}")
    print(f"Next Phase            : {summary.get('next_phase', 149)}")
    print(f"Profile               : {profile.profile_name}")
    print(f"All Components Ready  : {summary.get('all_components_ready')}")
    print(f"Phase Status          : {summary.get('phase_status')}")
    print(f"Non-Signal Invariant  : {summary.get('non_signal')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
