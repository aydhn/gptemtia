# -*- coding: utf-8 -*-
"""Phase 147: Run Walk-Forward Master Status Script.

Executes the full Phase 147 walk-forward validation and OOS benchmarking contract layer pipeline,
compiles master status, validates safety boundaries, checks Phase 148 handoff readiness,
and saves all reports to DataLake and output directories.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from advanced_walk_forward_validation.walk_forward_config import (
    get_default_walk_forward_profile,
)
from advanced_walk_forward_validation.walk_forward_pipeline import (
    WalkForwardValidationPipeline,
)


def main():
    settings = get_settings()
    profile = get_default_walk_forward_profile()
    pipeline = WalkForwardValidationPipeline(profile=profile)

    status_df, summary = pipeline.build_walk_forward_status(save=True)

    print("=" * 70)
    print("PHASE 147: WALK-FORWARD VALIDATION & OOS BENCHMARKING MASTER STATUS")
    print("=" * 70)
    print(status_df.to_string(index=False))
    print("-" * 70)
    print(f"Phase                 : {summary.get('phase')}")
    print(f"Target Final Phase    : {summary.get('target_final_phase')}")
    print(f"Next Phase            : {summary.get('next_phase')}")
    print(f"Profile               : {summary.get('profile')}")
    print(f"Readiness Score       : {summary.get('readiness_score', 1.0):.2f}")
    print(f"Validation Status     : {summary.get('validation_status')}")
    print(f"Health Status         : {summary.get('health_status')}")
    print(f"Safety Status         : {summary.get('safety_status')}")
    print(f"Phase 148 Handoff     : {summary.get('phase_148_handoff_ready')}")
    print(f"Live Trading          : {summary.get('live_trading')}")
    print(f"Broker Execution      : {summary.get('broker_execution')}")
    print(f"Walk-Forward Executed : {summary.get('walk_forward_executed')}")
    print(f"Benchmark Executed    : {summary.get('benchmark_executed')}")
    print(f"Metric Calculated     : {summary.get('metric_calculated')}")
    print(f"Non-Signal Invariant  : {summary.get('non_signal')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
