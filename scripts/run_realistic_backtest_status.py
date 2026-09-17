# -*- coding: utf-8 -*-
"""Phase 146: Run Realistic Backtest Master Status Script.

Executes the full Phase 146 realistic backtest contract layer pipeline,
compiles master status, validates safety boundaries, checks Phase 147 handoff readiness,
and saves all reports to DataLake and output directories.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.realistic_backtest_pipeline import (
    RealisticBacktestPipeline,
)


def main():
    settings = get_settings()
    profile = get_default_realistic_backtest_profile()
    pipeline = RealisticBacktestPipeline(profile=profile)

    status_df, summary = pipeline.build_realistic_backtest_status(save=True)

    print("=" * 70)
    print("PHASE 146: REALISTIC BACKTEST MASTER PIPELINE & STATUS")
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
    print(f"Phase 147 Handoff     : {summary.get('phase_147_handoff_ready')}")
    print(f"Live Trading          : {summary.get('live_trading')}")
    print(f"Broker Execution      : {summary.get('broker_execution')}")
    print(f"Non-Signal Invariant  : {summary.get('non_signal')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
