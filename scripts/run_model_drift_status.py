# -*- coding: utf-8 -*-
"""Phase 142: Run Model Drift Monitoring Consolidated Status Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_model_drift_monitoring.model_drift_pipeline import run_model_drift_monitoring_pipeline
from advanced_model_drift_monitoring.model_drift_monitoring_manifest import build_model_drift_monitoring_manifest
from advanced_model_drift_monitoring.model_drift_report_builder import (
    build_model_drift_markdown_report,
    build_model_drift_text_summary,
)


def main():
    data_lake = DataLake()

    pipeline_result = run_model_drift_monitoring_pipeline(
        profile_name="balanced_local_model_drift_contracts",
        save=True,
    )

    manifest = build_model_drift_monitoring_manifest("balanced_local_model_drift_contracts")
    md_report = build_model_drift_markdown_report(manifest)
    txt_report = build_model_drift_text_summary(manifest)

    # Save to data lake
    data_lake.save_model_drift_monitoring_report(
        profile_name="balanced_local_model_drift_contracts",
        report=pipeline_result,
        markdown=md_report,
    )

    # Write report files directly to reports/output/advanced_model_drift_monitoring/
    rep_dir = Path(__file__).resolve().parent.parent / "reports" / "output" / "advanced_model_drift_monitoring"
    rep_dir.mkdir(parents=True, exist_ok=True)
    (rep_dir / "model_drift_monitoring_status_report.md").write_text(md_report, encoding="utf-8")
    (rep_dir / "model_drift_monitoring_status_report.txt").write_text(txt_report, encoding="utf-8")

    print(txt_report)


if __name__ == "__main__":
    main()
