# -*- coding: utf-8 -*-
"""Phase 152: Run Backtest Acceptance Boundaries & Findings Script.

Builds non-production boundaries, review gates, go/no-go boundaries, blockers, gaps,
warnings, and findings registries, saving them to DataLake.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_backtest_acceptance.backtest_acceptance_config import (
    get_default_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_non_production_boundaries import (
    build_backtest_acceptance_non_production_boundary_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_manual_review_gates import (
    build_backtest_acceptance_manual_review_gate_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_go_no_go_boundaries import (
    build_backtest_acceptance_go_no_go_boundary_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_blockers import (
    build_backtest_acceptance_blocker_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_gaps import (
    build_backtest_acceptance_gap_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_warnings import (
    build_backtest_acceptance_warning_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_findings import (
    build_backtest_acceptance_findings_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_report_builder import (
    build_boundary_markdown_report,
    build_blocker_gap_warning_markdown_report,
    build_backtest_acceptance_findings_markdown_report,
)
from reports.report_builder import (
    build_backtest_acceptance_boundary_text_report,
    build_backtest_acceptance_findings_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_backtest_acceptance_profile()

    df_npb, s_npb = build_backtest_acceptance_non_production_boundary_registry(profile)
    df_mrg, s_mrg = build_backtest_acceptance_manual_review_gate_registry(profile)
    df_gng, s_gng = build_backtest_acceptance_go_no_go_boundary_registry(profile)

    df_blk, s_blk = build_backtest_acceptance_blocker_registry(profile)
    df_gap, s_gap = build_backtest_acceptance_gap_registry(profile)
    df_wrn, s_wrn = build_backtest_acceptance_warning_registry(profile)
    df_fnd, s_fnd = build_backtest_acceptance_findings_registry(profile)

    data_lake.save_backtest_acceptance_non_production_boundary_registry(df_npb, s_npb)
    data_lake.save_backtest_acceptance_manual_review_gate_registry(df_mrg, s_mrg)
    data_lake.save_backtest_acceptance_go_no_go_boundary_registry(df_gng, s_gng)
    data_lake.save_backtest_acceptance_blocker_registry(df_blk, s_blk)
    data_lake.save_backtest_acceptance_gap_registry(df_gap, s_gap)
    data_lake.save_backtest_acceptance_warning_registry(df_wrn, s_wrn)
    data_lake.save_backtest_acceptance_findings_registry(df_fnd, s_fnd)

    out_dir = Path("reports/output/advanced_backtest_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(out_dir / "non_production_boundaries.md", "w", encoding="utf-8") as f:
        f.write(build_boundary_markdown_report(s_npb, df_npb))
    with open(out_dir / "manual_review_gates.md", "w", encoding="utf-8") as f:
        f.write(build_boundary_markdown_report(s_mrg, df_mrg))
    with open(out_dir / "go_no_go_boundaries.md", "w", encoding="utf-8") as f:
        f.write(build_boundary_markdown_report(s_gng, df_gng))

    with open(out_dir / "blockers.md", "w", encoding="utf-8") as f:
        f.write(build_blocker_gap_warning_markdown_report(s_blk, df_blk))
    with open(out_dir / "gaps.md", "w", encoding="utf-8") as f:
        f.write(build_blocker_gap_warning_markdown_report(s_gap, df_gap))
    with open(out_dir / "warnings.md", "w", encoding="utf-8") as f:
        f.write(build_blocker_gap_warning_markdown_report(s_wrn, df_wrn))
    with open(out_dir / "findings.md", "w", encoding="utf-8") as f:
        f.write(build_backtest_acceptance_findings_markdown_report(s_fnd, df_fnd))
    with open(out_dir / "findings.txt", "w", encoding="utf-8") as f:
        f.write(build_backtest_acceptance_findings_text_report(s_fnd, df_fnd))

    print("=" * 70)
    print("PHASE 152: BOUNDARIES, GATES & FINDINGS")
    print("=" * 70)
    print(f"Non-Production Boundaries : {s_npb['total_boundaries']}")
    print(f"Manual Review Gates      : {s_mrg['total_gates']}")
    print(f"Go / No-Go Rules         : {s_gng['total_rules']} (Go: {s_gng['go_count']}, No-Go: {s_gng['no_go_count']})")
    print(f"Blockers                 : {s_blk['total_blockers']}")
    print(f"Gaps                     : {s_gap['total_gaps']}")
    print(f"Warnings                 : {s_wrn['total_warnings']}")
    print(f"Findings                 : {s_fnd['total_findings']}")
    print(f"Non-Signal               : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
