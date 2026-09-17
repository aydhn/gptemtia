# -*- coding: utf-8 -*-
"""Phase 145: Run Advanced ML Dependency and Validation Evidence Script.

Builds dependency acceptance, validation evidence summary, and safety boundaries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    get_default_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_dependency_acceptance import (
    build_advanced_ml_dependency_acceptance_registry,
)
from advanced_ml_acceptance.advanced_ml_validation_evidence_summary import (
    build_advanced_ml_validation_evidence_summary_registry,
)
from advanced_ml_acceptance.advanced_ml_safety_boundary_acceptance import (
    build_advanced_ml_safety_boundary_acceptance_registry,
)
from advanced_ml_acceptance.advanced_ml_acceptance_report_builder import (
    build_dependency_acceptance_markdown_report,
    build_validation_evidence_markdown_report,
)
from reports.report_builder import (
    build_dependency_acceptance_text_report,
    build_validation_evidence_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_advanced_ml_acceptance_profile()

    df_dep, s_dep = build_advanced_ml_dependency_acceptance_registry(profile)
    df_evd, s_evd = build_advanced_ml_validation_evidence_summary_registry(profile)
    df_sba, s_sba = build_advanced_ml_safety_boundary_acceptance_registry(profile)

    data_lake.save_advanced_ml_dependency_acceptance_registry(df_dep, s_dep)
    data_lake.save_advanced_ml_validation_evidence_summary_registry(df_evd, s_evd)
    data_lake.save_advanced_ml_safety_boundary_acceptance_registry(df_sba, s_sba)

    out_dir = Path("reports/output/advanced_ml_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(out_dir / "dependencies.md", "w", encoding="utf-8") as f:
        f.write(build_dependency_acceptance_markdown_report(s_dep, df_dep))
    with open(out_dir / "dependencies.txt", "w", encoding="utf-8") as f:
        f.write(build_dependency_acceptance_text_report(s_dep, df_dep))

    with open(out_dir / "evidence.md", "w", encoding="utf-8") as f:
        f.write(build_validation_evidence_markdown_report(s_evd, df_evd))
    with open(out_dir / "evidence.txt", "w", encoding="utf-8") as f:
        f.write(build_validation_evidence_text_report(s_evd, df_evd))

    print("=" * 70)
    print("PHASE 145: DEPENDENCY & EVIDENCE ACCEPTANCE")
    print("=" * 70)
    print(f"Total Dependencies : {s_dep['total_dependencies']} ({s_dep['satisfied_dependencies']} satisfied)")
    print(f"Total Evidence     : {s_evd['total_evidence_items']} ({s_evd['verified_items']} verified)")
    print(f"Safety Boundaries  : {s_sba['total_boundaries']} enforced")
    print(f"Status             : {s_evd['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
