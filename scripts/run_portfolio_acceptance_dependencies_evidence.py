# -*- coding: utf-8 -*-
"""Phase 157: Run Portfolio Acceptance Dependencies and Evidence Script.

Builds and persists dependency registry, validation evidence, and safety boundary registry.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_default_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_dependencies import (
    build_portfolio_acceptance_dependency_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_validation_evidence import (
    build_portfolio_acceptance_validation_evidence_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_safety_boundary_registry import (
    build_portfolio_acceptance_safety_boundary_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_report_builder import (
    build_portfolio_acceptance_dependency_markdown_report,
    build_portfolio_validation_evidence_markdown_report,
    build_portfolio_acceptance_boundary_markdown_report,
)
from reports.report_builder import (
    build_portfolio_acceptance_dependency_text_report,
    build_portfolio_acceptance_validation_evidence_text_report,
    build_portfolio_acceptance_boundary_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_portfolio_acceptance_profile()

    df_dep, s_dep = build_portfolio_acceptance_dependency_registry(profile)
    df_evd, s_evd = build_portfolio_acceptance_validation_evidence_registry(profile)
    df_sba, s_sba = build_portfolio_acceptance_safety_boundary_registry(profile)

    data_lake.save_portfolio_acceptance_dependency_registry(df_dep, s_dep)
    data_lake.save_portfolio_acceptance_validation_evidence_registry(df_evd, s_evd)
    data_lake.save_portfolio_acceptance_safety_boundary_registry(df_sba, s_sba)

    out_dir = Path("reports/output/advanced_portfolio_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(out_dir / "dependencies.md", "w", encoding="utf-8") as f:
        f.write(build_portfolio_acceptance_dependency_markdown_report(s_dep, df_dep))
    with open(out_dir / "dependencies.txt", "w", encoding="utf-8") as f:
        f.write(build_portfolio_acceptance_dependency_text_report(s_dep, df_dep))

    with open(out_dir / "evidence.md", "w", encoding="utf-8") as f:
        f.write(build_portfolio_validation_evidence_markdown_report(s_evd, df_evd))
    with open(out_dir / "evidence.txt", "w", encoding="utf-8") as f:
        f.write(build_portfolio_acceptance_validation_evidence_text_report(s_evd, df_evd))

    with open(out_dir / "safety_boundaries.md", "w", encoding="utf-8") as f:
        f.write(build_portfolio_acceptance_boundary_markdown_report(s_sba, df_sba))
    with open(out_dir / "safety_boundaries.txt", "w", encoding="utf-8") as f:
        f.write(build_portfolio_acceptance_boundary_text_report(s_sba, df_sba))

    print("=" * 70)
    print("PHASE 157: PORTFOLIO DEPENDENCIES, EVIDENCE & BOUNDARIES")
    print("=" * 70)
    print(f"Total Dependencies : {s_dep['total_dependencies']}")
    print(f"Dependencies OK    : {s_dep['all_satisfied']}")
    print(f"Total Evidence     : {s_evd['total_evidence_items']}")
    print(f"Evidence Complete  : {s_evd['all_evidence_present']}")
    print(f"Total Safety Rules : {s_sba['total_rules']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
