# -*- coding: utf-8 -*-
"""Phase 145: Run Advanced ML Acceptance Manifest Script.

Builds readiness scoring, acceptance manifest, Phase 146 handoff, and full report.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    get_default_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_readiness_scoring import (
    build_advanced_ml_readiness_score_report,
)
from advanced_ml_acceptance.advanced_ml_acceptance_manifest import (
    build_advanced_ml_acceptance_manifest,
)
from advanced_ml_acceptance.phase_146_handoff import (
    build_phase_146_realistic_backtest_transaction_cost_slippage_handoff_report,
)
from advanced_ml_acceptance.advanced_ml_component_registry import (
    build_advanced_ml_component_registry,
)
from advanced_ml_acceptance.advanced_ml_acceptance_report_builder import (
    build_advanced_ml_readiness_score_markdown_report,
    build_advanced_ml_acceptance_manifest_markdown_report,
    build_phase_146_handoff_markdown_report,
    build_advanced_ml_acceptance_full_markdown_report,
)
from reports.report_builder import (
    build_advanced_ml_readiness_score_text_report,
    build_advanced_ml_acceptance_manifest_text_report,
    build_phase_146_handoff_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_advanced_ml_acceptance_profile()

    df_cmp, s_cmp = build_advanced_ml_component_registry(profile)
    df_scr, s_scr = build_advanced_ml_readiness_score_report(profile)
    df_mnf, s_mnf = build_advanced_ml_acceptance_manifest(profile)
    df_hnd, s_hnd = build_phase_146_realistic_backtest_transaction_cost_slippage_handoff_report(profile)

    data_lake.save_advanced_ml_readiness_score_report(df_scr, s_scr)
    data_lake.save_advanced_ml_acceptance_manifest(df_mnf, s_mnf)
    data_lake.save_phase_146_realistic_backtest_transaction_cost_slippage_handoff_report(df_hnd, s_hnd)

    out_dir = Path("reports/output/advanced_ml_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(out_dir / "scoring.md", "w", encoding="utf-8") as f:
        f.write(build_advanced_ml_readiness_score_markdown_report(s_scr, df_scr))
    with open(out_dir / "scoring.txt", "w", encoding="utf-8") as f:
        f.write(build_advanced_ml_readiness_score_text_report(s_scr, df_scr))

    with open(out_dir / "manifest.md", "w", encoding="utf-8") as f:
        f.write(build_advanced_ml_acceptance_manifest_markdown_report(s_mnf, df_mnf))
    with open(out_dir / "manifest.txt", "w", encoding="utf-8") as f:
        f.write(build_advanced_ml_acceptance_manifest_text_report(s_mnf, df_mnf))

    with open(out_dir / "phase_146_handoff.md", "w", encoding="utf-8") as f:
        f.write(build_phase_146_handoff_markdown_report(s_hnd, df_hnd))
    with open(out_dir / "phase_146_handoff.txt", "w", encoding="utf-8") as f:
        f.write(build_phase_146_handoff_text_report(s_hnd, df_hnd))

    # Full Consolidated Markdown Report
    full_summary = {
        "active_profile": profile.profile_name,
        "readiness_score": s_scr["readiness_score"],
        "classification": s_scr["classification"],
        "status": "ACCEPTED",
    }
    full_md = build_advanced_ml_acceptance_full_markdown_report(
        {"components": df_cmp, "scoring": df_scr, "handoff": df_hnd},
        full_summary,
    )
    with open(out_dir / "advanced_ml_acceptance_consolidated_report.md", "w", encoding="utf-8") as f:
        f.write(full_md)

    data_lake.save_advanced_ml_acceptance_report(profile.profile_name, full_summary, full_md)

    print("=" * 70)
    print("PHASE 145: ACCEPTANCE MANIFEST & PHASE 146 HANDOFF")
    print("=" * 70)
    print(f"Readiness Score    : {s_scr['readiness_score']:.2f} ({s_scr['classification']})")
    print(f"Manifest ID        : {s_mnf['manifest_id']}")
    print(f"Block Completed    : {s_mnf['advanced_ml_block_completed']}")
    print(f"Phase 146 Handoff  : {s_hnd['status']} ({s_hnd['satisfied_prerequisites']}/{s_hnd['total_prerequisites']} satisfied)")
    print(f"Production Ready   : False (Enforced)")
    print(f"Broker Ready       : False (Enforced)")
    print("=" * 70)


if __name__ == "__main__":
    main()
