"""Phase 130: Run Regime Transition Metrics Script.

Generates transition and stability metric registries, thresholds, and guards.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_metric_registry import (
    build_regime_transition_metric_registry,
)
from advanced_regime_transition.regime_stability_metric_registry import (
    build_regime_stability_metric_registry,
)
from advanced_regime_transition.regime_transition_thresholds import (
    build_regime_transition_threshold_registry,
)
from advanced_regime_transition.regime_transition_timestamp_policies import (
    build_regime_transition_timestamp_policy_registry,
)
from advanced_regime_transition.regime_transition_no_lookahead_guard import (
    build_regime_transition_no_lookahead_guard_registry,
)
from advanced_regime_transition.regime_transition_source_phases import (
    build_regime_transition_source_phase_registry,
)
from advanced_regime_transition.regime_transition_report_builder import (
    build_transition_metric_markdown_report,
)
from reports.report_builder import build_regime_transition_metrics_text_report


def main():
    data_lake = DataLake()
    profile = get_default_regime_transition_profile()

    df_tmet, s_tmet = build_regime_transition_metric_registry(profile)
    df_smet, s_smet = build_regime_stability_metric_registry(profile)
    df_th, s_th = build_regime_transition_threshold_registry(profile)
    df_tp, s_tp = build_regime_transition_timestamp_policy_registry(profile)
    df_gd, s_gd = build_regime_transition_no_lookahead_guard_registry(profile)
    df_sp, s_sp = build_regime_transition_source_phase_registry(profile)

    data_lake.save_regime_transition_metric_registry(df_tmet, s_tmet)
    data_lake.save_regime_stability_metric_registry(df_smet, s_smet)
    data_lake.save_regime_transition_threshold_registry(df_th, s_th)
    data_lake.save_regime_transition_timestamp_policy_registry(df_tp, s_tp)
    data_lake.save_regime_transition_no_lookahead_guard_registry(df_gd, s_gd)
    data_lake.save_regime_transition_source_phase_registry(df_sp, s_sp)

    md_content = build_transition_metric_markdown_report(s_tmet, df_tmet)
    txt_content = build_regime_transition_metrics_text_report(s_tmet, df_tmet)

    out_dir = Path("reports/output/advanced_regime_transition")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "transition_metrics.md", "w", encoding="utf-8") as f:
        f.write(md_content)
    with open(out_dir / "transition_metrics.txt", "w", encoding="utf-8") as f:
        f.write(txt_content)

    print("=" * 70)
    print("PHASE 130: REGIME TRANSITION & STABILITY METRICS")
    print("=" * 70)
    print(f"Transition Metrics : {s_tmet.get('total_metrics')}")
    print(f"Stability Metrics  : {s_smet.get('total_metrics')}")
    print(f"Thresholds Count   : {s_th.get('total_thresholds')}")
    print(f"Timestamp Policies : {s_tp.get('total_policies')}")
    print(f"Lookahead Guards   : {s_gd.get('total_guards')}")
    print(f"Source Phases      : {s_sp.get('total_source_phases')}")
    print(f"Non-Signal         : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
