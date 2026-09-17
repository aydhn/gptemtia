# -*- coding: utf-8 -*-
"""Phase 159: Run Release Candidate Findings and Manifest Script.

Builds and persists blockers, gaps, warnings, findings, readiness score, manifest,
and Phase 160 handoff artifacts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_hardening.final_hardening_config import (
    get_default_final_hardening_profile,
)
from advanced_final_hardening.release_candidate_blockers import (
    build_release_candidate_blocker_registry,
)
from advanced_final_hardening.release_candidate_gaps import (
    build_release_candidate_gap_registry,
)
from advanced_final_hardening.release_candidate_warnings import (
    build_release_candidate_warning_registry,
)
from advanced_final_hardening.release_candidate_findings import (
    build_release_candidate_findings_registry,
)
from advanced_final_hardening.release_candidate_readiness_scoring import (
    build_release_candidate_readiness_score_report,
)
from advanced_final_hardening.release_candidate_manifest import (
    build_release_candidate_manifest,
)
from advanced_final_hardening.phase_160_handoff import (
    build_phase_160_full_advanced_bot_final_delivery_handoff_report,
)
from advanced_final_hardening.final_hardening_report_builder import (
    build_release_candidate_manifest_markdown_report,
    build_phase_160_handoff_markdown_report,
)
from reports.report_builder import (
    build_release_candidate_manifest_text_report,
    build_phase_160_handoff_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_hardening_profile()

    df_blk, s_blk = build_release_candidate_blocker_registry(profile)
    df_gap, s_gap = build_release_candidate_gap_registry(profile)
    df_wrn, s_wrn = build_release_candidate_warning_registry(profile)
    df_fnd, s_fnd = build_release_candidate_findings_registry(profile)
    df_scr, s_scr = build_release_candidate_readiness_score_report(profile)
    df_mnf, s_mnf = build_release_candidate_manifest(profile)
    df_hnd, s_hnd = build_phase_160_full_advanced_bot_final_delivery_handoff_report(profile)

    data_lake.save_release_candidate_blocker_registry(df_blk, s_blk)
    data_lake.save_release_candidate_gap_registry(df_gap, s_gap)
    data_lake.save_release_candidate_warning_registry(df_wrn, s_wrn)
    data_lake.save_release_candidate_findings_registry(df_fnd, s_fnd)
    data_lake.save_release_candidate_readiness_score_report(df_scr, s_scr)
    data_lake.save_release_candidate_manifest(df_mnf, s_mnf)
    data_lake.save_phase_160_full_advanced_bot_final_delivery_handoff_report(df_hnd, s_hnd)

    out_dir = Path("reports/output/advanced_final_hardening")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_manifest = build_release_candidate_manifest_markdown_report(s_mnf, df_mnf)
    txt_manifest = build_release_candidate_manifest_text_report(s_mnf, df_mnf)
    md_handoff = build_phase_160_handoff_markdown_report(s_hnd, df_hnd)
    txt_handoff = build_phase_160_handoff_text_report(s_hnd, df_hnd)

    with open(out_dir / "manifest.md", "w", encoding="utf-8") as f:
        f.write(md_manifest)
    with open(out_dir / "manifest.txt", "w", encoding="utf-8") as f:
        f.write(txt_manifest)
    with open(out_dir / "phase_160_handoff.md", "w", encoding="utf-8") as f:
        f.write(md_handoff)
    with open(out_dir / "phase_160_handoff.txt", "w", encoding="utf-8") as f:
        f.write(txt_handoff)

    print("=" * 70)
    print("PHASE 159: RELEASE CANDIDATE FINDINGS, MANIFEST & HANDOFF INITIALIZED")
    print("=" * 70)
    print(f"Readiness Score: {s_scr['readiness_score']:.2f} ({s_scr['classification']})")
    print(f"Manifest ID: {s_mnf['manifest_id']} | Phase 160 Ready: {s_mnf['phase_160_handoff_ready']}")
    print(f"Status: {s_mnf['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
