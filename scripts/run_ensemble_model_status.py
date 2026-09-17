# -*- coding: utf-8 -*-
"""Phase 140: Run Ensemble Model Status Script."""

import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ensemble_model_registry.ensemble_model_pipeline import (
    run_ensemble_model_pipeline,
    summarize_ensemble_model_pipeline_result,
)
from advanced_ensemble_model_registry.ensemble_model_report_builder import (
    ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER,
    build_ensemble_model_text_report,
    build_ensemble_model_markdown_report,
)


def main():
    data_lake = DataLake()

    pipeline_result = run_ensemble_model_pipeline()
    s_pipe = summarize_ensemble_model_pipeline_result(pipeline_result)

    manifest = pipeline_result["manifest"]
    findings = pipeline_result["findings"]
    review_queue = pipeline_result["review_queue"]

    text_report = build_ensemble_model_text_report(manifest, findings, review_queue)
    md_report = build_ensemble_model_markdown_report(manifest, findings, review_queue)

    # Save to data lake
    data_lake.save_ensemble_model_report(
        profile_name="balanced_local_ensemble_model_contracts",
        report=s_pipe,
        markdown=md_report,
    )

    # Write markdown report to reports/output/advanced_ensemble_model_registry/
    rep_dir = Path(__file__).resolve().parent.parent / "reports" / "output" / "advanced_ensemble_model_registry"
    rep_dir.mkdir(parents=True, exist_ok=True)
    (rep_dir / "ensemble_model_status_report.md").write_text(md_report, encoding="utf-8")
    (rep_dir / "ensemble_model_status_report.txt").write_text(text_report, encoding="utf-8")

    print("=" * 70)
    print("PHASE 140: ENSEMBLE MODEL CONSOLIDATED STATUS")
    print("=" * 70)
    print(ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Current Phase           : {s_pipe['phase']}")
    print(f"Candidate Contracts     : {s_pipe['candidate_contracts']}")
    print(f"Ensemble Strategies     : {s_pipe['ensemble_strategies']}")
    print(f"Readiness Score         : {s_pipe['readiness_score']}")
    print(f"Health Status           : {s_pipe['health_status']}")
    print(f"Validation Status       : {s_pipe['validation_status']}")
    print(f"Real Training Executed  : {manifest.real_training_executed}")
    print(f"Model Fit Executed      : {manifest.model_fit_executed}")
    print(f"Model Predict Executed  : {manifest.model_predict_executed}")
    print(f"Ensemble Executed       : {manifest.ensemble_executed}")
    print(f"Artifact Persisted      : {manifest.artifact_persisted}")
    print(f"Registry Written        : {manifest.model_registry_written}")
    print(f"Non-Signal Certified    : {s_pipe['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
