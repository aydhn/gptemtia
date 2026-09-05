"""Phase 123: Run Feature Quality and Drift Metric Registry Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_quality_drift.feature_quality_drift_config import get_default_feature_quality_drift_profile
from advanced_feature_quality_drift.feature_quality_metric_registry import build_feature_quality_metric_registry
from advanced_feature_quality_drift.feature_drift_metric_registry import build_feature_drift_metric_registry
from advanced_feature_quality_drift.feature_quality_thresholds import build_feature_quality_threshold_registry
from advanced_feature_quality_drift.feature_drift_thresholds import build_feature_drift_threshold_registry
from advanced_feature_quality_drift.feature_quality_input_contracts import build_feature_quality_input_contract_registry
from advanced_feature_quality_drift.feature_drift_input_contracts import build_feature_drift_input_contract_registry
from advanced_feature_quality_drift.feature_quality_drift_report_builder import (
    build_quality_metric_markdown_report,
    build_drift_metric_markdown_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_feature_quality_drift_profile()

    df_q_met, s_q_met = build_feature_quality_metric_registry(profile)
    df_d_met, s_d_met = build_feature_drift_metric_registry(profile)
    df_q_thr, s_q_thr = build_feature_quality_threshold_registry(profile)
    df_d_thr, s_d_thr = build_feature_drift_threshold_registry(profile)
    df_q_con, s_q_con = build_feature_quality_input_contract_registry(profile)
    df_d_con, s_d_con = build_feature_drift_input_contract_registry(profile)

    data_lake.save_feature_quality_metric_registry(df_q_met, s_q_met)
    data_lake.save_feature_drift_metric_registry(df_d_met, s_d_met)
    data_lake.save_feature_quality_threshold_registry(df_q_thr, s_q_thr)
    data_lake.save_feature_drift_threshold_registry(df_d_thr, s_d_thr)
    data_lake.save_feature_quality_input_contract_registry(df_q_con, s_q_con)
    data_lake.save_feature_drift_input_contract_registry(df_d_con, s_d_con)

    md_q = build_quality_metric_markdown_report(s_q_met, df_q_met)
    md_d = build_drift_metric_markdown_report(s_d_met, df_d_met)

    reports_dir = Path("reports/output/advanced_feature_quality_drift")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "quality_metrics.md", "w", encoding="utf-8") as f:
        f.write(md_q)
    with open(reports_dir / "drift_metrics.md", "w", encoding="utf-8") as f:
        f.write(md_d)

    print("=" * 70)
    print("PHASE 123: FEATURE QUALITY & DRIFT METRICS AND THRESHOLDS")
    print("=" * 70)
    print(f"Quality Metrics Registered : {s_q_met['total_quality_metrics']}")
    print(f"Drift Metrics Registered   : {s_d_met['total_drift_metrics']}")
    print(f"Quality Thresholds         : {s_q_thr['total_thresholds']}")
    print(f"Drift Thresholds           : {s_d_thr['total_thresholds']}")
    print(f"Quality Contracts          : {s_q_con['total_contracts']}")
    print(f"Drift Contracts            : {s_d_con['total_contracts']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
