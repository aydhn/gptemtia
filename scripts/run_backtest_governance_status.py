# -*- coding: utf-8 -*-
"""Phase 150: Run Backtest Governance Master Status Script.

Executes the full Phase 150 Backtest Governance & Bias Control pipeline,
compiles master status, validates safety boundaries, checks Phase 151 handoff readiness,
and saves all reports to DataLake and output directories.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_governance_pipeline import (
    BacktestGovernancePipeline,
)


def main():
    settings = get_settings()
    profile = get_default_backtest_governance_profile()
    pipeline = BacktestGovernancePipeline(profile=profile)

    status_df, summary = pipeline.build_governance_status(save=True)

    print("=" * 70)
    print("PHASE 150: BACKTEST GOVERNANCE & BIAS CONTROL MASTER STATUS")
    print("=" * 70)
    print(status_df.to_string(index=False))
    print("-" * 70)
    print(f"Phase                 : {summary.get('current_phase', 150)}")
    print(f"Target Final Phase    : {summary.get('target_final_phase', 160)}")
    print(f"Next Phase            : {summary.get('next_phase', 151)}")
    print(f"Profile               : {profile.profile_name}")
    print(f"All Components Ready  : {summary.get('all_components_ready')}")
    print(f"Phase Status          : {summary.get('phase_status')}")
    print(f"Non-Signal Invariant  : {summary.get('non_signal')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
