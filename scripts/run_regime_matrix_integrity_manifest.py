"""Phase 127: Run Regime Matrix Integrity Manifest Script.

Generates and saves integrity contracts, manifest, source phases, dependencies, and manual review queue.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_matrix.regime_matrix_config import (
    get_default_regime_matrix_profile,
)
from advanced_regime_matrix.regime_matrix_integrity_contracts import (
    build_regime_matrix_integrity_contracts,
)
from advanced_regime_matrix.regime_matrix_integrity_manifest import (
    build_regime_matrix_integrity_manifest,
)
from advanced_regime_matrix.regime_matrix_source_phases import (
    build_regime_matrix_source_phases_registry,
)
from advanced_regime_matrix.regime_matrix_validation_dependencies import (
    build_regime_matrix_validation_dependencies,
)
from advanced_regime_matrix.regime_matrix_quality_dependencies import (
    build_regime_matrix_quality_dependencies,
)
from advanced_regime_matrix.regime_matrix_manual_review import (
    build_regime_matrix_manual_review_queue,
)
from advanced_regime_matrix.regime_matrix_report_builder import (
    build_regime_matrix_integrity_markdown_report,
)
from reports.report_builder import build_regime_matrix_integrity_text_report


def main():
    data_lake = DataLake()
    profile = get_default_regime_matrix_profile()

    df_ic, s_ic = build_regime_matrix_integrity_contracts(profile)
    df_man, s_man = build_regime_matrix_integrity_manifest(profile)
    df_sp, s_sp = build_regime_matrix_source_phases_registry()
    df_vd, s_vd = build_regime_matrix_validation_dependencies()
    df_qd, s_qd = build_regime_matrix_quality_dependencies()
    df_mr, s_mr = build_regime_matrix_manual_review_queue()

    data_lake.save_regime_matrix_integrity_contracts(df_ic, s_ic)
    data_lake.save_regime_matrix_integrity_manifest(df_man, s_man)
    data_lake.save_regime_matrix_source_phases(df_sp, s_sp)
    data_lake.save_regime_matrix_validation_dependencies(df_vd, s_vd)
    data_lake.save_regime_matrix_quality_dependencies(df_qd, s_qd)
    data_lake.save_regime_matrix_manual_review_queue(df_mr, s_mr)

    md_ic = build_regime_matrix_integrity_markdown_report(s_man, df_man)
    txt_ic = build_regime_matrix_integrity_text_report(s_man, df_man)

    out_dir = Path("reports/output/advanced_regime_matrix")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "integrity_manifest.md", "w", encoding="utf-8") as f:
        f.write(md_ic)
    with open(out_dir / "integrity_manifest.txt", "w", encoding="utf-8") as f:
        f.write(txt_ic)

    print("=" * 70)
    print("PHASE 127: REGIME MATRIX INTEGRITY MANIFEST & DEPENDENCIES")
    print("=" * 70)
    print(f"Manifest Status  : {s_man['manifest_status']}")
    print(f"Integrity Rules  : {s_ic['total_rules']}")
    print(f"Source Phases    : {s_sp['total_source_phases']}")
    print(f"Validation Deps  : {s_vd['total_dependencies']}")
    print(f"Quality Deps     : {s_qd['total_dependencies']}")
    print(f"Review Items     : {s_mr['total_items']}")
    print(f"Source Preserved : {s_man['source_preserved']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
