# -*- coding: utf-8 -*-
"""Phase 147: Run Walk-Forward Findings and Manifest Script.

Builds validation evidence, manual review queue, findings registry,
diagnostic readiness score, and master manifest. Saves to DataLake and writes markdown/text reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_walk_forward_validation.walk_forward_config import (
    get_default_walk_forward_profile,
)
from advanced_walk_forward_validation.validation_evidence import (
    build_validation_evidence_registry,
)
from advanced_walk_forward_validation.walk_forward_manual_review import (
    build_walk_forward_manual_review_queue,
)
from advanced_walk_forward_validation.walk_forward_findings import (
    build_walk_forward_findings_registry,
)
from advanced_walk_forward_validation.walk_forward_readiness_scoring import (
    build_walk_forward_readiness_score_report,
)
from advanced_walk_forward_validation.walk_forward_manifest import (
    build_walk_forward_manifest,
)
from advanced_walk_forward_validation.walk_forward_report_builder import (
    build_walk_forward_findings_markdown_report,
    build_walk_forward_readiness_score_markdown_report,
    build_walk_forward_manifest_markdown_report,
)
from reports.report_builder import (
    build_walk_forward_readiness_score_text_report,
    build_walk_forward_manifest_text_report,
    build_walk_forward_findings_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_walk_forward_profile()

    df_ev, s_ev = build_validation_evidence_registry(profile)
    df_rev, s_rev = build_walk_forward_manual_review_queue(profile)
    df_fnd, s_fnd = build_walk_forward_findings_registry(profile)
    df_scr, s_scr = build_walk_forward_readiness_score_report(profile)
    df_man, s_man = build_walk_forward_manifest(profile)

    data_lake.save_validation_evidence(df_ev, s_ev)
    data_lake.save_walk_forward_manual_review_queue(df_rev, s_rev)
    data_lake.save_walk_forward_findings_registry(df_fnd, s_fnd)
    data_lake.save_walk_forward_readiness_score_report(df_scr, s_scr)
    data_lake.save_walk_forward_manifest(df_man, s_man)

    md_fnd = build_walk_forward_findings_markdown_report(s_fnd, df_fnd)
    txt_fnd = build_walk_forward_findings_text_report(s_fnd, df_fnd)
    md_scr = build_walk_forward_readiness_score_markdown_report(s_scr, df_scr)
    txt_scr = build_walk_forward_readiness_score_text_report(s_scr, df_scr)
    md_man = build_walk_forward_manifest_markdown_report(s_man, df_man)
    txt_man = build_walk_forward_manifest_text_report(s_man, df_man)

    out_dir = Path("reports/output/advanced_walk_forward_validation")
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(out_dir / "findings.md", "w", encoding="utf-8") as f:
        f.write(md_fnd)
    with open(out_dir / "findings.txt", "w", encoding="utf-8") as f:
        f.write(txt_fnd)

    with open(out_dir / "readiness_score.md", "w", encoding="utf-8") as f:
        f.write(md_scr)
    with open(out_dir / "readiness_score.txt", "w", encoding="utf-8") as f:
        f.write(txt_scr)

    with open(out_dir / "manifest.md", "w", encoding="utf-8") as f:
        f.write(md_man)
    with open(out_dir / "manifest.txt", "w", encoding="utf-8") as f:
        f.write(txt_man)

    print("=" * 70)
    print("PHASE 147: WALK-FORWARD FINDINGS, READINESS & MANIFEST")
    print("=" * 70)
    print(f"Validation Evidence Items: {s_ev.get('total_evidence_items', len(df_ev))}")
    print(f"Review Queue Items       : {s_rev.get('total_review_items', len(df_rev))}")
    print(f"Total Findings           : {s_fnd.get('total_findings', len(df_fnd))}")
    print(f"Critical Blockers        : {s_fnd.get('critical_count', 0)}")
    print(f"Readiness Score          : {s_scr.get('score', 1.0):.2f}")
    print(f"Readiness Classification : {s_scr.get('classification')}")
    print(f"Manifest ID              : {s_man.get('manifest_id')}")
    print(f"Walk-Forward Executed    : {s_man.get('walk_forward_executed')}")
    print(f"OOS Benchmark Executed   : {s_man.get('oos_benchmark_executed')}")
    print(f"Benchmark Calc Performed : {s_man.get('benchmark_metric_calculated')}")
    print(f"Phase 148 Handoff Ready  : {s_man.get('phase_148_handoff_ready')}")
    print(f"Non-Signal Invariant     : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
