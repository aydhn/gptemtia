# -*- coding: utf-8 -*-
"""Phase 145: Run Advanced ML Boundaries and Findings Script.

Builds non-production boundaries, review gates, go/no-go rules, and findings registry.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    get_default_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_non_production_boundaries import (
    build_advanced_ml_non_production_boundary_registry,
)
from advanced_ml_acceptance.advanced_ml_manual_review_gates import (
    build_advanced_ml_manual_review_gate_registry,
)
from advanced_ml_acceptance.advanced_ml_go_no_go_boundaries import (
    build_advanced_ml_go_no_go_boundary_registry,
)
from advanced_ml_acceptance.advanced_ml_blockers import (
    build_advanced_ml_blocker_registry,
)
from advanced_ml_acceptance.advanced_ml_gaps import (
    build_advanced_ml_gap_registry,
)
from advanced_ml_acceptance.advanced_ml_warnings import (
    build_advanced_ml_warning_registry,
)
from advanced_ml_acceptance.advanced_ml_findings import (
    build_advanced_ml_findings_registry,
)
from advanced_ml_acceptance.advanced_ml_acceptance_report_builder import (
    build_boundary_markdown_report,
    build_advanced_ml_findings_markdown_report,
)
from reports.report_builder import (
    build_advanced_ml_boundary_text_report,
    build_advanced_ml_findings_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_advanced_ml_acceptance_profile()

    df_npb, s_npb = build_advanced_ml_non_production_boundary_registry(profile)
    df_mrg, s_mrg = build_advanced_ml_manual_review_gate_registry(profile)
    df_gng, s_gng = build_advanced_ml_go_no_go_boundary_registry(profile)
    df_blk, s_blk = build_advanced_ml_blocker_registry(profile)
    df_gap, s_gap = build_advanced_ml_gap_registry(profile)
    df_wrn, s_wrn = build_advanced_ml_warning_registry(profile)
    df_fnd, s_fnd = build_advanced_ml_findings_registry(profile)

    data_lake.save_advanced_ml_non_production_boundary_registry(df_npb, s_npb)
    data_lake.save_advanced_ml_manual_review_gate_registry(df_mrg, s_mrg)
    data_lake.save_advanced_ml_go_no_go_boundary_registry(df_gng, s_gng)
    data_lake.save_advanced_ml_blocker_registry(df_blk, s_blk)
    data_lake.save_advanced_ml_gap_registry(df_gap, s_gap)
    data_lake.save_advanced_ml_warning_registry(df_wrn, s_wrn)
    data_lake.save_advanced_ml_findings_registry(df_fnd, s_fnd)

    out_dir = Path("reports/output/advanced_ml_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(out_dir / "boundaries.md", "w", encoding="utf-8") as f:
        f.write(build_boundary_markdown_report(s_npb, df_npb))
    with open(out_dir / "boundaries.txt", "w", encoding="utf-8") as f:
        f.write(build_advanced_ml_boundary_text_report(s_npb, df_npb))

    with open(out_dir / "findings.md", "w", encoding="utf-8") as f:
        f.write(build_advanced_ml_findings_markdown_report(s_fnd, df_fnd))
    with open(out_dir / "findings.txt", "w", encoding="utf-8") as f:
        f.write(build_advanced_ml_findings_text_report(s_fnd, df_fnd))

    print("=" * 70)
    print("PHASE 145: BOUNDARIES, GATES & FINDINGS REGISTRY")
    print("=" * 70)
    print(f"Non-Production Boundaries : {s_npb['total_boundaries']} enforced")
    print(f"Manual Review Gates       : {s_mrg['total_gates']} queued")
    print(f"Go / No-Go Boundaries     : {s_gng['total_boundaries']} ({s_gng['go_count']} Go, {s_gng['no_go_count']} No-Go)")
    print(f"Blockers Recorded         : {s_blk['total_blockers']}")
    print(f"Gaps Recorded             : {s_gap['total_gaps']}")
    print(f"Warnings Recorded         : {s_wrn['total_warnings']}")
    print(f"Findings Recorded         : {s_fnd['total_findings']}")
    print(f"Status                    : {s_npb['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
