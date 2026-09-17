# -*- coding: utf-8 -*-
"""Phase 142: Run Drift Window & Threshold Policies Script."""

import sys
from dataclasses import asdict
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_model_drift_monitoring.reference_window_policies import build_reference_window_policies
from advanced_model_drift_monitoring.current_window_policies import build_current_window_policies
from advanced_model_drift_monitoring.rolling_window_placeholder_policies import build_rolling_window_placeholder_policies
from advanced_model_drift_monitoring.drift_segment_policies import build_drift_segment_policies
from advanced_model_drift_monitoring.drift_monitoring_schedule_placeholders import build_drift_monitoring_schedule_placeholders
from advanced_model_drift_monitoring.drift_threshold_placeholder_policies import build_drift_threshold_placeholders
from reports.report_builder import ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    ref_wins = build_reference_window_policies()
    df_rw = pd.DataFrame([asdict(w) for w in ref_wins])
    data_lake.save_reference_window_policy_registry(df_rw, {"total_reference_windows": len(ref_wins)})

    curr_wins = build_current_window_policies()
    df_cw = pd.DataFrame([asdict(w) for w in curr_wins])
    data_lake.save_current_window_policy_registry(df_cw, {"total_current_windows": len(curr_wins)})

    roll_wins = build_rolling_window_placeholder_policies()
    df_roll = pd.DataFrame([asdict(w) for w in roll_wins])
    data_lake.save_rolling_window_placeholder_policy_registry(df_roll, {"total_rolling_windows": len(roll_wins)})

    seg_policies = build_drift_segment_policies()
    df_seg = pd.DataFrame([asdict(w) for w in seg_policies])
    data_lake.save_drift_segment_policy_registry(df_seg, {"total_segments": len(seg_policies)})

    sched_policies = build_drift_monitoring_schedule_placeholders()
    df_sched = pd.DataFrame([asdict(w) for w in sched_policies])
    data_lake.save_drift_monitoring_schedule_placeholder_registry(df_sched, {"total_schedules": len(sched_policies)})

    thresholds = build_drift_threshold_placeholders()
    df_th = pd.DataFrame([asdict(t) for t in thresholds])
    data_lake.save_drift_threshold_placeholder_registry(df_th, {"total_thresholds": len(thresholds)})

    print("=" * 70)
    print("PHASE 142: DRIFT WINDOW & THRESHOLD POLICIES")
    print("=" * 70)
    print(ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Reference Window Policies     : {len(ref_wins)}")
    print(f"Current Window Policies       : {len(curr_wins)}")
    print(f"Rolling Window Policies       : {len(roll_wins)}")
    print(f"Segment Slicing Policies      : {len(seg_policies)}")
    print(f"Monitoring Schedules          : {len(sched_policies)}")
    print(f"Threshold Placeholders (PSI/KS): {len(thresholds)}")
    print("Execution Enabled             : False (All Non-Executing)")
    print("=" * 70)


if __name__ == "__main__":
    main()
