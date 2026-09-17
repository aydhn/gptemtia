# -*- coding: utf-8 -*-
"""Phase 157: Run Portfolio Acceptance Boundaries and Findings Script.

Builds and persists non-production boundaries, manual review gates,
go/no-go boundaries, blockers, gaps, warnings, and findings.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_default_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_non_production_boundaries import (
    build_portfolio_acceptance_non_production_boundary_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_manual_review_gates import (
    build_portfolio_acceptance_manual_review_gate_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_go_no_go_boundaries import (
    build_portfolio_acceptance_go_no_go_boundary_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_blockers import (
    build_portfolio_acceptance_blocker_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_gaps import (
    build_portfolio_acceptance_gap_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_warnings import (
    build_portfolio_acceptance_warning_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_findings import (
    build_portfolio_acceptance_findings_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_report_builder import (
    build_portfolio_acceptance_findings_markdown_report,
    build_portfolio_blocker_gap_warning_markdown_report,
)
from reports.report_builder import (
    build_portfolio_acceptance_findings_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_portfolio_acceptance_profile()

    df_npb, s_npb = build_portfolio_acceptance_non_production_boundary_registry(profile)
    df_mrg, s_mrg = build_portfolio_acceptance_manual_review_gate_registry(profile)
    df_gng, s_gng = build_portfolio_acceptance_go_no_go_boundary_registry(profile)
    df_blk, s_blk = build_portfolio_acceptance_blocker_registry(profile)
    df_gap, s_gap = build_portfolio_acceptance_gap_registry(profile)
    df_wrn, s_wrn = build_portfolio_acceptance_warning_registry(profile)
    df_fnd, s_fnd = build_portfolio_acceptance_findings_registry(profile)

    data_lake.save_portfolio_acceptance_non_production_boundary_registry(df_npb, s_npb)
    data_lake.save_portfolio_acceptance_manual_review_gate_registry(df_mrg, s_mrg)
    data_lake.save_portfolio_acceptance_go_no_go_boundary_registry(df_gng, s_gng)
    data_lake.save_portfolio_acceptance_blocker_registry(df_blk, s_blk)
    data_lake.save_portfolio_acceptance_gap_registry(df_gap, s_gap)
    data_lake.save_portfolio_acceptance_warning_registry(df_wrn, s_wrn)
    data_lake.save_portfolio_acceptance_findings_registry(df_fnd, s_fnd)

    out_dir = Path("reports/output/advanced_portfolio_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(out_dir / "findings.md", "w", encoding="utf-8") as f:
        f.write(build_portfolio_acceptance_findings_markdown_report(s_fnd, df_fnd))
    with open(out_dir / "findings.txt", "w", encoding="utf-8") as f:
        f.write(build_portfolio_acceptance_findings_text_report(s_fnd, df_fnd))

    print("=" * 70)
    print("PHASE 157: PORTFOLIO BOUNDARIES, GATES & FINDINGS")
    print("=" * 70)
    print(f"Non-Prod Invariants: {s_npb['total_invariants']}")
    print(f"Manual Review Gates: {s_mrg['total_gates']}")
    print(f"Go Rules           : {s_gng['go_count']}")
    print(f"No-Go Rules        : {s_gng['no_go_count']}")
    print(f"Active Blockers    : {s_blk['active_blockers_count']}")
    print(f"Total Findings     : {s_fnd['total_findings']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
