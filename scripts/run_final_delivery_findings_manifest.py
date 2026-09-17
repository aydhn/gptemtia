# -*- coding: utf-8 -*-
"""Phase 160: Run Final Delivery Findings and Manifest Script.

Builds and persists blockers, gaps, warnings, findings, readiness score, and final manifest.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_delivery.final_delivery_config import (
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_blockers import (
    build_final_delivery_blocker_registry,
)
from advanced_final_delivery.final_delivery_gaps import (
    build_final_delivery_gap_registry,
)
from advanced_final_delivery.final_delivery_warnings import (
    build_final_delivery_warning_registry,
)
from advanced_final_delivery.final_delivery_findings import (
    build_final_delivery_findings_registry,
)
from advanced_final_delivery.final_delivery_readiness_scoring import (
    build_final_delivery_readiness_score_report,
)
from advanced_final_delivery.final_delivery_manifest import (
    build_final_delivery_manifest,
)
from advanced_final_delivery.final_delivery_report_builder import (
    build_final_delivery_manifest_markdown_report,
    build_final_delivery_readiness_score_markdown_report,
)
from reports.report_builder import (
    build_final_delivery_manifest_text_report,
    build_final_delivery_readiness_score_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_delivery_profile()

    df_blk, s_blk = build_final_delivery_blocker_registry(profile)
    df_gap, s_gap = build_final_delivery_gap_registry(profile)
    df_wrn, s_wrn = build_final_delivery_warning_registry(profile)
    df_fnd, s_fnd = build_final_delivery_findings_registry(profile)
    df_scr, s_scr = build_final_delivery_readiness_score_report(profile)
    df_mnf, s_mnf = build_final_delivery_manifest(profile)

    if "--no-save" not in sys.argv and settings.final_delivery_save_reports:
        data_lake.save_final_delivery_findings_registry(df_fnd, s_fnd)
        data_lake.save_final_delivery_readiness_score_report(df_scr, s_scr)
        data_lake.save_final_delivery_manifest(df_mnf, s_mnf)

    out_dir = Path("reports/output/advanced_final_delivery")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_manifest = build_final_delivery_manifest_markdown_report(s_mnf, df_mnf)
    txt_manifest = build_final_delivery_manifest_text_report(s_mnf, df_mnf)
    md_score = build_final_delivery_readiness_score_markdown_report(s_scr, df_scr)
    txt_score = build_final_delivery_readiness_score_text_report(s_scr, df_scr)

    if "--no-save" not in sys.argv:
        with open(out_dir / "manifest.md", "w", encoding="utf-8") as f:
            f.write(md_manifest)
        with open(out_dir / "manifest.txt", "w", encoding="utf-8") as f:
            f.write(txt_manifest)
        with open(out_dir / "readiness_score.md", "w", encoding="utf-8") as f:
            f.write(md_score)
        with open(out_dir / "readiness_score.txt", "w", encoding="utf-8") as f:
            f.write(txt_score)

    print("=" * 70)
    print("PHASE 160: FINAL DELIVERY FINDINGS & MANIFEST INITIALIZED")
    print("=" * 70)
    print(f"Readiness Score: {s_scr['readiness_score']:.2f} ({s_scr['classification']})")
    print(f"Manifest ID: {s_mnf['manifest_id']} | Phase 160 Completed: {s_mnf['phase_160_completed']}")
    print(f"Status: {s_mnf['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
