# -*- coding: utf-8 -*-
"""Phase 158: Run System Integration Findings, Scoring, Manifest and Handoff Script.

Builds findings, calculates readiness score, generates master manifest, and prepares Phase 159 handoff.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_full_system_integration.full_system_integration_config import (
    get_default_full_system_integration_profile,
)
from advanced_full_system_integration.system_integration_blockers import (
    build_system_integration_blocker_registry,
)
from advanced_full_system_integration.system_integration_gaps import (
    build_system_integration_gap_registry,
)
from advanced_full_system_integration.system_integration_warnings import (
    build_system_integration_warning_registry,
)
from advanced_full_system_integration.system_integration_findings import (
    build_system_integration_findings_registry,
)
from advanced_full_system_integration.system_integration_readiness_scoring import (
    build_system_integration_readiness_score_report,
)
from advanced_full_system_integration.full_system_integration_manifest import (
    build_full_system_integration_manifest,
)
from advanced_full_system_integration.phase_159_handoff import (
    build_phase_159_final_hardening_operator_runbook_release_candidate_handoff_report,
)
from advanced_full_system_integration.full_system_integration_report_builder import (
    build_system_findings_markdown_report,
    build_system_readiness_score_markdown_report,
    build_full_system_integration_manifest_markdown_report,
    build_phase_159_handoff_markdown_report,
)
from reports.report_builder import (
    build_system_integration_findings_text_report,
    build_system_integration_readiness_score_text_report,
    build_full_system_integration_manifest_text_report,
    build_phase_159_handoff_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_full_system_integration_profile()

    df_blk, s_blk = build_system_integration_blocker_registry(profile)
    df_gap, s_gap = build_system_integration_gap_registry(profile)
    df_wrn, s_wrn = build_system_integration_warning_registry(profile)
    df_fnd, s_fnd = build_system_integration_findings_registry(profile)
    df_scr, s_scr = build_system_integration_readiness_score_report(profile)
    df_mnf, s_mnf = build_full_system_integration_manifest(profile)
    df_hnd, s_hnd = build_phase_159_final_hardening_operator_runbook_release_candidate_handoff_report(profile)

    data_lake.save_system_integration_findings_registry(df_fnd, s_fnd)
    data_lake.save_system_integration_readiness_score_report(df_scr, s_scr)
    data_lake.save_full_system_integration_manifest(df_mnf, s_mnf)
    data_lake.save_phase_159_final_hardening_operator_runbook_release_candidate_handoff_report(df_hnd, s_hnd)

    out_dir = Path("reports/output/advanced_full_system_integration")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_fnd = build_system_findings_markdown_report(s_fnd, df_fnd)
    txt_fnd = build_system_integration_findings_text_report(s_fnd, df_fnd)
    md_scr = build_system_readiness_score_markdown_report(s_scr, df_scr)
    txt_scr = build_system_integration_readiness_score_text_report(s_scr, df_scr)
    md_mnf = build_full_system_integration_manifest_markdown_report(s_mnf, df_mnf)
    txt_mnf = build_full_system_integration_manifest_text_report(s_mnf, df_mnf)
    md_hnd = build_phase_159_handoff_markdown_report(s_hnd, df_hnd)
    txt_hnd = build_phase_159_handoff_text_report(s_hnd, df_hnd)

    with open(out_dir / "findings.md", "w", encoding="utf-8") as f:
        f.write(md_fnd)
    with open(out_dir / "findings.txt", "w", encoding="utf-8") as f:
        f.write(txt_fnd)
    with open(out_dir / "readiness_score.md", "w", encoding="utf-8") as f:
        f.write(md_scr)
    with open(out_dir / "readiness_score.txt", "w", encoding="utf-8") as f:
        f.write(txt_scr)
    with open(out_dir / "manifest.md", "w", encoding="utf-8") as f:
        f.write(md_mnf)
    with open(out_dir / "manifest.txt", "w", encoding="utf-8") as f:
        f.write(txt_mnf)
    with open(out_dir / "phase_159_handoff.md", "w", encoding="utf-8") as f:
        f.write(md_hnd)
    with open(out_dir / "phase_159_handoff.txt", "w", encoding="utf-8") as f:
        f.write(txt_hnd)

    print("=" * 70)
    print("PHASE 158: FINDINGS, SCORING, MANIFEST & PHASE 159 HANDOFF")
    print("=" * 70)
    print(f"Readiness Score    : {s_scr['readiness_score']:.4f}")
    print(f"Classification     : {s_scr['classification']}")
    print(f"Meets Threshold    : {s_scr['meets_threshold']}")
    print(f"Manifest Completed : {s_mnf['full_system_integration_completed']}")
    print(f"Handoff Ready      : {s_hnd['handoff_ready']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
