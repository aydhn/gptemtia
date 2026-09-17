# -*- coding: utf-8 -*-
"""Phase 142: Run Drift Findings & Manifest Script."""

import sys
from dataclasses import asdict
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_model_drift_monitoring.drift_findings import build_drift_findings, summarize_drift_findings
from advanced_model_drift_monitoring.drift_readiness_scoring import compute_domain_readiness_scores, evaluate_aggregate_drift_readiness
from advanced_model_drift_monitoring.model_drift_monitoring_manifest import (
    build_model_drift_monitoring_manifest,
    summarize_model_drift_monitoring_manifest,
)
from advanced_model_drift_monitoring.phase_143_handoff import build_phase_143_handoff_contract
from reports.report_builder import ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    findings = build_drift_findings()
    findings_summary = summarize_drift_findings(findings)
    data_lake.save_drift_findings_registry(pd.DataFrame([asdict(f) for f in findings]), findings_summary)

    scores = compute_domain_readiness_scores()
    score_eval = evaluate_aggregate_drift_readiness(scores)
    data_lake.save_drift_readiness_score_report(pd.DataFrame([asdict(s) for s in scores]), score_eval)

    manifest = build_model_drift_monitoring_manifest()
    manifest_summary = summarize_model_drift_monitoring_manifest(manifest)
    data_lake.save_model_drift_monitoring_manifest(pd.DataFrame([manifest_summary]))

    handoff = build_phase_143_handoff_contract()
    data_lake.save_phase_143_explainability_handoff_report(pd.DataFrame(handoff["preconditions"]), handoff)

    print("=" * 70)
    print("PHASE 142: DRIFT FINDINGS, READINESS & MANIFEST")
    print("=" * 70)
    print(ADVANCED_MODEL_DRIFT_MONITORING_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Drift Findings      : {findings_summary.get('total_findings', 0)}")
    print(f"Requires Human Review     : {findings_summary.get('requires_human_review_count', 0)}")
    print(f"Aggregate Readiness Score : {score_eval.get('overall_score', 0.0)}%")
    print(f"Readiness Status          : {score_eval.get('overall_status', 'unknown')}")
    print(f"Phase 143 Handoff Status  : {handoff.get('handoff_readiness', 'NOT_READY')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
