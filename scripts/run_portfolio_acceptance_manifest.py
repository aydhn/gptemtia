# -*- coding: utf-8 -*-
"""Phase 157: Run Portfolio Acceptance Manifest Script.

Builds readiness score, master manifest, Phase 158 handoff report, and full markdown report.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_default_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_readiness_scoring import (
    build_portfolio_acceptance_readiness_score_report,
)
from advanced_portfolio_acceptance.portfolio_acceptance_manifest import (
    build_portfolio_acceptance_manifest,
)
from advanced_portfolio_acceptance.phase_158_handoff import (
    build_phase_158_full_system_integration_advanced_acceptance_rehearsal_handoff_report,
)
from advanced_portfolio_acceptance.portfolio_acceptance_component_registry import (
    build_portfolio_acceptance_component_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_report_builder import (
    build_portfolio_acceptance_readiness_score_markdown_report,
    build_portfolio_acceptance_manifest_markdown_report,
    build_phase_158_handoff_markdown_report,
    build_portfolio_acceptance_full_markdown_report,
)
from reports.report_builder import (
    build_portfolio_acceptance_readiness_score_text_report,
    build_portfolio_acceptance_manifest_text_report,
    build_phase_158_handoff_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_portfolio_acceptance_profile()

    df_scr, s_scr = build_portfolio_acceptance_readiness_score_report(profile)
    df_mnf, s_mnf = build_portfolio_acceptance_manifest(profile)
    df_hnd, s_hnd = build_phase_158_full_system_integration_advanced_acceptance_rehearsal_handoff_report(profile)
    df_cmp, s_cmp = build_portfolio_acceptance_component_registry(profile)

    data_lake.save_portfolio_acceptance_readiness_score_report(df_scr, s_scr)
    data_lake.save_portfolio_acceptance_manifest(df_mnf, s_mnf)
    data_lake.save_phase_158_full_system_integration_advanced_acceptance_rehearsal_handoff_report(df_hnd, s_hnd)

    out_dir = Path("reports/output/advanced_portfolio_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(out_dir / "readiness_score.md", "w", encoding="utf-8") as f:
        f.write(build_portfolio_acceptance_readiness_score_markdown_report(s_scr, df_scr))
    with open(out_dir / "readiness_score.txt", "w", encoding="utf-8") as f:
        f.write(build_portfolio_acceptance_readiness_score_text_report(s_scr, df_scr))

    with open(out_dir / "manifest.md", "w", encoding="utf-8") as f:
        f.write(build_portfolio_acceptance_manifest_markdown_report(s_mnf, df_mnf))
    with open(out_dir / "manifest.txt", "w", encoding="utf-8") as f:
        f.write(build_portfolio_acceptance_manifest_text_report(s_mnf, df_mnf))

    with open(out_dir / "phase_158_handoff.md", "w", encoding="utf-8") as f:
        f.write(build_phase_158_handoff_markdown_report(s_hnd, df_hnd))
    with open(out_dir / "phase_158_handoff.txt", "w", encoding="utf-8") as f:
        f.write(build_phase_158_handoff_text_report(s_hnd, df_hnd))

    full_md = build_portfolio_acceptance_full_markdown_report(
        {"components": df_cmp, "readiness_score": df_scr, "manifest": df_mnf, "handoff": df_hnd},
        {"active_profile": profile.profile_name, "readiness_score": s_scr["readiness_score"], "classification": s_scr["classification"]},
    )
    with open(out_dir / "portfolio_acceptance_report.md", "w", encoding="utf-8") as f:
        f.write(full_md)

    data_lake.save_portfolio_acceptance_report(
        profile.profile_name,
        {"manifest": s_mnf, "readiness": s_scr, "handoff": s_hnd},
        full_md,
    )

    print("=" * 70)
    print("PHASE 157: PORTFOLIO ACCEPTANCE MANIFEST & READINESS SCORE")
    print("=" * 70)
    print(f"Readiness Score        : {s_scr['readiness_score']:.4f}")
    print(f"Classification         : {s_scr['classification']}")
    print(f"Meets Threshold        : {s_scr['meets_threshold']}")
    print(f"Portfolio Block Done   : {s_mnf['portfolio_block_completed']}")
    print(f"Phase 158 Handoff Ready: {s_hnd['handoff_ready']}")
    print(f"Production Ready       : False")
    print(f"Broker Ready           : False")
    print(f"Live Trading Ready     : False")
    print(f"Strategy Approved      : False")
    print(f"Portfolio Approved     : False")
    print(f"Non-Signal             : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
