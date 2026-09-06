"""Phase 136: Run GPU ML Runtime Findings & Manifest Script.

Generates and persists findings, manual review queue, readiness scoring, master manifest, and Phase 137 handoff.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_gpu_ml_runtime.gpu_ml_runtime_config import get_default_gpu_ml_runtime_profile
from advanced_gpu_ml_runtime.ml_runtime_findings import build_ml_runtime_findings_registry
from advanced_gpu_ml_runtime.ml_runtime_manual_review import build_ml_runtime_manual_review_queue
from advanced_gpu_ml_runtime.ml_runtime_readiness_scoring import build_ml_runtime_readiness_score_report
from advanced_gpu_ml_runtime.gpu_ml_runtime_manifest import build_gpu_ml_runtime_manifest
from advanced_gpu_ml_runtime.phase_137_handoff import build_phase_137_advanced_ml_dataset_experiment_handoff_report
from advanced_gpu_ml_runtime.gpu_ml_runtime_report_builder import build_gpu_ml_runtime_manifest_markdown_report
from reports.report_builder import GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_gpu_ml_runtime_profile()

    df_find, s_find = build_ml_runtime_findings_registry(profile)
    data_lake.save_ml_runtime_findings_registry(df_find, s_find)

    df_rev, s_rev = build_ml_runtime_manual_review_queue(profile)
    data_lake.save_ml_runtime_manual_review_queue(df_rev, s_rev)

    df_score, s_score = build_ml_runtime_readiness_score_report(profile)
    data_lake.save_ml_runtime_readiness_score_report(df_score, s_score)

    df_man, s_man = build_gpu_ml_runtime_manifest(profile)
    data_lake.save_gpu_ml_runtime_manifest(df_man, s_man)

    df_hand, s_hand = build_phase_137_advanced_ml_dataset_experiment_handoff_report(profile)
    data_lake.save_phase_137_advanced_ml_dataset_experiment_handoff_report(df_hand, s_hand)

    report_md = build_gpu_ml_runtime_manifest_markdown_report(s_man, df_man)
    report_dict = {
        "manifest": s_man,
        "readiness_score": s_score,
        "handoff": s_hand,
        "non_signal": True,
    }
    data_lake.save_gpu_ml_runtime_report(profile.profile_name, report_dict, report_md)

    print("=" * 70)
    print("PHASE 136: GPU & ML RUNTIME FINDINGS, MANIFEST AND HANDOFF")
    print("=" * 70)
    print(GPU_ML_RUNTIME_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Readiness Score    : {s_score.get('readiness_score', 0.0):.4f} ({s_score.get('classification', 'N/A')})")
    print(f"Total Findings     : {s_find.get('total_findings', 0)}")
    print(f"Manual Review Queue: {s_rev.get('total_items', 0)} items")
    print(f"Phase 137 Handoff  : {s_hand.get('status', 'READY')} (Next: Phase {s_hand.get('next_phase', 137)})")
    print(f"Non-Signal         : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
