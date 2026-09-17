"""Phase 137: Run ML Dataset Findings, Manifest, and Handoff Script.

Builds and persists findings, manual review queue, readiness scoring,
the top-level manifest, and the Phase 138 handoff report.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_ml_dataset_registry.advanced_ml_dataset_config import (
    get_default_advanced_ml_dataset_profile,
)
from advanced_ml_dataset_registry.ml_dataset_findings import (
    build_ml_dataset_findings_registry,
)
from advanced_ml_dataset_registry.ml_dataset_manual_review import (
    build_ml_dataset_manual_review_queue,
)
from advanced_ml_dataset_registry.ml_dataset_readiness_scoring import (
    build_ml_dataset_readiness_score_report,
)
from advanced_ml_dataset_registry.advanced_ml_dataset_manifest import (
    build_advanced_ml_dataset_manifest,
)
from advanced_ml_dataset_registry.phase_138_handoff import (
    build_phase_138_baseline_ml_model_contracts_handoff_report,
)
from reports.report_builder import ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    profile = get_default_advanced_ml_dataset_profile()

    df_find, s_find = build_ml_dataset_findings_registry(profile)
    data_lake.save_ml_dataset_findings_registry(df_find, s_find)

    df_mr, s_mr = build_ml_dataset_manual_review_queue(profile)
    data_lake.save_ml_dataset_manual_review_queue(df_mr, s_mr)

    df_sc, s_sc = build_ml_dataset_readiness_score_report(profile)
    data_lake.save_ml_dataset_readiness_score_report(df_sc, s_sc)

    df_man, s_man = build_advanced_ml_dataset_manifest(profile)
    data_lake.save_advanced_ml_dataset_manifest(df_man, s_man)

    df_ho, s_ho = build_phase_138_baseline_ml_model_contracts_handoff_report(profile)
    data_lake.save_phase_138_baseline_ml_model_contracts_handoff_report(df_ho, s_ho)

    print("=" * 70)
    print("PHASE 137: ML DATASET FINDINGS, MANIFEST & HANDOFF")
    print("=" * 70)
    print(ADVANCED_ML_DATASET_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Findings        : {s_find['total_findings']}")
    print(f"Manual Review Items   : {s_mr['total_review_items']}")
    print(f"Readiness Score       : {s_sc['readiness_score']:.4f} ({s_sc['classification']})")
    print(f"Manifest Status       : {s_man['status']}")
    print(f"Handoff Status        : {s_ho['handoff_status']}")
    print(f"All Prerequisites     : {s_ho['all_satisfied']}")
    print(f"Non-Signal            : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
