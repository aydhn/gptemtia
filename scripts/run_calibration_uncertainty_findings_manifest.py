# -*- coding: utf-8 -*-
"""Phase 141: Run Calibration & Uncertainty Findings, Review, Scoring & Manifest Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_calibration_uncertainty.calibration_uncertainty_findings import (
    build_calibration_uncertainty_findings_registry,
    summarize_calibration_uncertainty_findings,
)
from advanced_calibration_uncertainty.calibration_uncertainty_manual_review import (
    build_calibration_uncertainty_manual_review_queue,
    summarize_calibration_uncertainty_manual_review_queue,
)
from advanced_calibration_uncertainty.calibration_uncertainty_readiness_scoring import (
    build_calibration_uncertainty_readiness_score_report,
    summarize_calibration_uncertainty_readiness_scores,
)
from advanced_calibration_uncertainty.calibration_uncertainty_manifest import (
    build_calibration_uncertainty_manifest,
    summarize_calibration_uncertainty_manifest,
)
from reports.report_builder import ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    df_fnd, s_fnd = build_calibration_uncertainty_findings_registry()
    data_lake.save_calibration_uncertainty_findings_registry(df_fnd, s_fnd)

    df_rev, s_rev = build_calibration_uncertainty_manual_review_queue()
    data_lake.save_calibration_uncertainty_manual_review_queue(df_rev, s_rev)

    df_sco, s_sco = build_calibration_uncertainty_readiness_score_report()
    data_lake.save_calibration_uncertainty_readiness_score_report(df_sco, s_sco)

    df_man, s_man = build_calibration_uncertainty_manifest()
    data_lake.save_calibration_uncertainty_manifest(df_man, s_man)

    print("=" * 70)
    print("PHASE 141: FINDINGS, MANUAL REVIEW, SCORING & MANIFEST")
    print("=" * 70)
    print(ADVANCED_CALIBRATION_UNCERTAINTY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Findings             : {s_fnd.get('total_findings', 0)}")
    print(f"Manual Review Items        : {s_rev.get('total_items', len(df_rev))}")
    print(f"Readiness Score Mean       : {s_sco.get('readiness_score', 1.0)}")
    print(f"All Ready For Review       : {s_sco.get('meets_threshold', True)}")
    print(f"Manifest Total Artifacts   : {s_man.get('total_artifacts', len(df_man))}")
    print("=" * 70)


if __name__ == "__main__":
    main()
