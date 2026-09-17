# -*- coding: utf-8 -*-
"""Phase 141: Run Calibration & Uncertainty Consolidated Status Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_calibration_uncertainty.calibration_uncertainty_pipeline import (
    run_calibration_uncertainty_pipeline,
)
from advanced_calibration_uncertainty.calibration_uncertainty_report_builder import (
    ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER,
    build_calibration_uncertainty_consolidated_markdown_report,
    build_calibration_uncertainty_consolidated_text_report,
)


def main():
    data_lake = DataLake()

    pipeline_result = run_calibration_uncertainty_pipeline(
        profile_name="balanced_local_calibration_uncertainty_contracts"
    )

    md_report = build_calibration_uncertainty_consolidated_markdown_report(pipeline_result)
    txt_report = build_calibration_uncertainty_consolidated_text_report(pipeline_result)

    # Save to data lake
    data_lake.save_calibration_uncertainty_report(
        profile_name="balanced_local_calibration_uncertainty_contracts",
        report=pipeline_result,
        markdown=md_report,
    )

    # Write report files directly to reports/output/advanced_calibration_uncertainty/
    rep_dir = Path(__file__).resolve().parent.parent / "reports" / "output" / "advanced_calibration_uncertainty"
    rep_dir.mkdir(parents=True, exist_ok=True)
    (rep_dir / "calibration_uncertainty_status_report.md").write_text(md_report, encoding="utf-8")
    (rep_dir / "calibration_uncertainty_status_report.txt").write_text(txt_report, encoding="utf-8")

    print(txt_report)


if __name__ == "__main__":
    main()
