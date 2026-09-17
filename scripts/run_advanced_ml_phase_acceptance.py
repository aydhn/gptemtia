# -*- coding: utf-8 -*-
"""Phase 145: Run Advanced ML Phase Acceptance Script.

Builds phase acceptance registries for Phases 136 to 144 and saves them to DataLake.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    get_default_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.phase_136_gpu_runtime_acceptance import (
    build_phase_136_gpu_runtime_acceptance_registry,
)
from advanced_ml_acceptance.phase_137_dataset_contract_acceptance import (
    build_phase_137_dataset_contract_acceptance_registry,
)
from advanced_ml_acceptance.phase_138_baseline_model_acceptance import (
    build_phase_138_baseline_model_acceptance_registry,
)
from advanced_ml_acceptance.phase_139_gpu_training_governance_acceptance import (
    build_phase_139_gpu_training_governance_acceptance_registry,
)
from advanced_ml_acceptance.phase_140_ensemble_candidate_acceptance import (
    build_phase_140_ensemble_candidate_acceptance_registry,
)
from advanced_ml_acceptance.phase_141_calibration_uncertainty_acceptance import (
    build_phase_141_calibration_uncertainty_acceptance_registry,
)
from advanced_ml_acceptance.phase_142_drift_monitoring_acceptance import (
    build_phase_142_drift_monitoring_acceptance_registry,
)
from advanced_ml_acceptance.phase_143_explainability_acceptance import (
    build_phase_143_explainability_acceptance_registry,
)
from advanced_ml_acceptance.phase_144_model_governance_acceptance import (
    build_phase_144_model_governance_acceptance_registry,
)
from advanced_ml_acceptance.advanced_ml_acceptance_report_builder import (
    build_phase_acceptance_markdown_report,
)
from reports.report_builder import build_phase_acceptance_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_advanced_ml_acceptance_profile()

    phase_builders = [
        ("Phase 136", build_phase_136_gpu_runtime_acceptance_registry, data_lake.save_phase_136_gpu_runtime_acceptance_registry),
        ("Phase 137", build_phase_137_dataset_contract_acceptance_registry, data_lake.save_phase_137_dataset_contract_acceptance_registry),
        ("Phase 138", build_phase_138_baseline_model_acceptance_registry, data_lake.save_phase_138_baseline_model_acceptance_registry),
        ("Phase 139", build_phase_139_gpu_training_governance_acceptance_registry, data_lake.save_phase_139_gpu_training_governance_acceptance_registry),
        ("Phase 140", build_phase_140_ensemble_candidate_acceptance_registry, data_lake.save_phase_140_ensemble_candidate_acceptance_registry),
        ("Phase 141", build_phase_141_calibration_uncertainty_acceptance_registry, data_lake.save_phase_141_calibration_uncertainty_acceptance_registry),
        ("Phase 142", build_phase_142_drift_monitoring_acceptance_registry, data_lake.save_phase_142_drift_monitoring_acceptance_registry),
        ("Phase 143", build_phase_143_explainability_acceptance_registry, data_lake.save_phase_143_explainability_acceptance_registry),
        ("Phase 144", build_phase_144_model_governance_acceptance_registry, data_lake.save_phase_144_model_governance_acceptance_registry),
    ]

    out_dir = Path("reports/output/advanced_ml_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("PHASE 145: PHASE-LEVEL ACCEPTANCE AUDIT (PHASES 136-144)")
    print("=" * 70)

    for phase_name, builder, saver in phase_builders:
        df, summary = builder(profile)
        saver(df, summary)
        md = build_phase_acceptance_markdown_report(summary, df)
        txt = build_phase_acceptance_text_report(summary, df)

        safe_name = phase_name.lower().replace(" ", "_")
        with open(out_dir / f"{safe_name}_acceptance.md", "w", encoding="utf-8") as f:
            f.write(md)
        with open(out_dir / f"{safe_name}_acceptance.txt", "w", encoding="utf-8") as f:
            f.write(txt)

        print(f"[{summary['status']}] {phase_name}: {summary['passed_checks']}/{summary['total_checks']} checks passed.")

    print("=" * 70)
    print("All Phase 136-144 acceptance registries saved successfully.")
    print("=" * 70)


if __name__ == "__main__":
    main()
