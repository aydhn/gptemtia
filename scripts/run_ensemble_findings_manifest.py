# -*- coding: utf-8 -*-
"""Phase 140: Run Ensemble Findings, Manifest, and Phase 141 Handoff Script."""

import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ensemble_model_registry.ensemble_findings import (
    build_ensemble_findings,
    summarize_ensemble_findings,
)
from advanced_ensemble_model_registry.ensemble_manual_review import (
    build_ensemble_manual_review_queue,
    summarize_ensemble_manual_review_queue,
)
from advanced_ensemble_model_registry.ensemble_readiness_scoring import (
    calculate_ensemble_readiness_score,
    summarize_ensemble_readiness_score,
)
from advanced_ensemble_model_registry.ensemble_model_manifest import (
    build_ensemble_model_manifest,
    summarize_ensemble_model_manifest,
)
from advanced_ensemble_model_registry.phase_141_handoff import (
    build_phase_141_handoff_report,
    summarize_phase_141_handoff_report,
)
from reports.report_builder import ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()

    findings = build_ensemble_findings()
    s_fnd = summarize_ensemble_findings(findings)
    df_fnd = pd.DataFrame([f.__dict__ for f in findings])
    data_lake.save_ensemble_findings_registry(df_fnd, s_fnd)

    review_items = build_ensemble_manual_review_queue()
    s_rev = summarize_ensemble_manual_review_queue(review_items)
    df_rev = pd.DataFrame([r.__dict__ for r in review_items])
    data_lake.save_ensemble_manual_review_queue(df_rev, s_rev)

    readiness = calculate_ensemble_readiness_score()
    s_read = summarize_ensemble_readiness_score(readiness)
    df_read = pd.DataFrame([readiness.__dict__])
    data_lake.save_ensemble_readiness_score_report(df_read, s_read)

    manifest = build_ensemble_model_manifest(
        candidate_contract_count=10,
        ensemble_contract_count=7,
        disabled_execution_report_count=6,
        finding_count=len(findings),
        manual_review_count=len(review_items),
        readiness_score=readiness.readiness_score,
    )
    s_man = summarize_ensemble_model_manifest(manifest)
    df_man = pd.DataFrame([manifest.__dict__])
    data_lake.save_ensemble_model_manifest(df_man, s_man)

    handoff = build_phase_141_handoff_report()
    s_ho = summarize_phase_141_handoff_report(handoff)
    df_ho = pd.DataFrame([handoff])
    data_lake.save_phase_141_probability_calibration_handoff_report(df_ho, s_ho)

    print("=" * 70)
    print("PHASE 140: ENSEMBLE FINDINGS, MANIFEST & PHASE 141 HANDOFF")
    print("=" * 70)
    print(ADVANCED_ENSEMBLE_MODEL_REGISTRY_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Findings      : {s_fnd['total_findings']}")
    print(f"Manual Reviews      : {s_rev['total_items']}")
    print(f"Readiness Score     : {s_read['readiness_score']} ({s_read['classification']})")
    print(f"Manifest Status     : Valid={s_man['is_valid']} (Training={manifest.real_training_executed})")
    print(f"Phase 141 Handoff   : {s_ho['handoff_status']} (Valid: {s_ho['is_valid']})")
    print("=" * 70)


if __name__ == "__main__":
    main()
