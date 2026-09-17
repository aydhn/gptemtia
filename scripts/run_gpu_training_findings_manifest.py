# -*- coding: utf-8 -*-
"""Phase 139: Run GPU Training Findings, Manifest, and Phase 140 Handoff Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.gpu_training_findings import (
    build_gpu_training_findings_registry,
)
from advanced_gpu_training_governance.gpu_training_manual_review import (
    build_gpu_training_manual_review_queue,
)
from advanced_gpu_training_governance.gpu_training_readiness_scoring import (
    build_gpu_training_readiness_score_report,
)
from advanced_gpu_training_governance.gpu_training_governance_manifest import (
    build_gpu_training_governance_manifest,
)
from advanced_gpu_training_governance.phase_140_handoff import (
    build_phase_140_ensemble_candidate_model_registry_handoff_report,
)
from reports.report_builder import ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_gpu_training_governance_profile()

    df_fnd, s_fnd = build_gpu_training_findings_registry(profile)
    data_lake.save_gpu_training_findings_registry(df_fnd, s_fnd)

    df_rev, s_rev = build_gpu_training_manual_review_queue(profile)
    data_lake.save_gpu_training_manual_review_queue(df_rev, s_rev)

    df_scr, s_scr = build_gpu_training_readiness_score_report(profile)
    data_lake.save_gpu_training_readiness_score_report(df_scr, s_scr)

    df_mf, s_mf = build_gpu_training_governance_manifest(profile)
    data_lake.save_gpu_training_governance_manifest(df_mf, s_mf)

    df_ho, s_ho = build_phase_140_ensemble_candidate_model_registry_handoff_report(profile)
    data_lake.save_phase_140_ensemble_candidate_model_registry_handoff_report(df_ho, s_ho)

    print("=" * 70)
    print("PHASE 139: GPU TRAINING FINDINGS, MANIFEST & PHASE 140 HANDOFF")
    print("=" * 70)
    print(ADVANCED_GPU_TRAINING_GOVERNANCE_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Findings      : {s_fnd['total_findings']}")
    print(f"Manual Reviews      : {s_rev['total_review_items']}")
    print(f"Readiness Score     : {s_scr['readiness_score']} ({s_scr['classification']})")
    print(f"Manifest Status     : Manifest valid (Training={s_mf['real_training_executed']})")
    print(f"Phase 140 Handoff   : {s_ho['handoff_status']} (Satisfied: {s_ho['all_satisfied']})")
    print("=" * 70)


if __name__ == "__main__":
    main()
