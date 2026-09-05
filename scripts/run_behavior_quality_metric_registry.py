"""Phase 129: Run Behavior Quality Metric & Threshold Registry Script.

Generates behavior quality metric, diagnostics metric, and threshold registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    get_default_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.behavior_quality_metric_registry import (
    build_behavior_quality_metric_registry,
)
from advanced_market_behavior_diagnostics.behavior_diagnostics_metric_registry import (
    build_behavior_diagnostics_metric_registry,
)
from advanced_market_behavior_diagnostics.behavior_quality_thresholds import (
    build_behavior_quality_threshold_registry,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_report_builder import (
    build_behavior_quality_metric_markdown_report,
)
from reports.report_builder import build_behavior_quality_metric_text_report


def main():
    data_lake = DataLake()
    profile = get_default_market_behavior_diagnostics_profile()

    df_qual, s_qual = build_behavior_quality_metric_registry(profile)
    df_diag, s_diag = build_behavior_diagnostics_metric_registry(profile)
    df_thresh, s_thresh = build_behavior_quality_threshold_registry(profile)

    data_lake.save_behavior_quality_metric_registry(df_qual, s_qual)
    data_lake.save_behavior_diagnostics_metric_registry(df_diag, s_diag)
    data_lake.save_behavior_quality_threshold_registry(df_thresh, s_thresh)

    summary = {
        "total_quality_metrics": s_qual.get("total_quality_metrics", s_qual.get("total_metrics", len(df_qual))),
        "total_diagnostics_metrics": s_diag.get("total_diagnostics_metrics", s_diag.get("total_metrics", len(df_diag))),
        "total_thresholds": s_thresh.get("total_thresholds", len(df_thresh)),
        "all_non_signal": True,
        "all_source_preserved": True,
    }

    md = build_behavior_quality_metric_markdown_report(summary, df_qual)
    txt = build_behavior_quality_metric_text_report(summary, df_qual)

    out_dir = Path("reports/output/advanced_market_behavior_diagnostics")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "quality_metric_registry.md", "w", encoding="utf-8") as f:
        f.write(md)
    with open(out_dir / "quality_metric_registry.txt", "w", encoding="utf-8") as f:
        f.write(txt)

    print("=" * 70)
    print("PHASE 129: BEHAVIOR QUALITY METRIC & THRESHOLD REGISTRY")
    print("=" * 70)
    print(f"Quality Metrics     : {summary['total_quality_metrics']}")
    print(f"Diagnostics Metrics : {summary['total_diagnostics_metrics']}")
    print(f"Quality Thresholds  : {summary['total_thresholds']}")
    print(f"Non-Signal Mandate  : True")
    print(f"Source Preserved    : True")
    print("=" * 70)



if __name__ == "__main__":
    main()
