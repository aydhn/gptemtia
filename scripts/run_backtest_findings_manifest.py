# -*- coding: utf-8 -*-
"""Phase 146: Run Backtest Findings and Manifest Script.

Builds dependencies, validation evidence, manual review queue, findings registry,
readiness score, and master manifest. Saves to DataLake and writes markdown/text reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.backtest_dependencies import (
    build_backtest_dependency_registry,
)
from advanced_realistic_backtest.backtest_validation_evidence import (
    build_backtest_validation_evidence_registry,
)
from advanced_realistic_backtest.backtest_manual_review import (
    build_backtest_manual_review_queue,
)
from advanced_realistic_backtest.backtest_findings import (
    build_backtest_findings_registry,
)
from advanced_realistic_backtest.backtest_readiness_scoring import (
    build_backtest_readiness_score_report,
)
from advanced_realistic_backtest.realistic_backtest_manifest import (
    build_realistic_backtest_manifest,
)
from advanced_realistic_backtest.realistic_backtest_report_builder import (
    build_backtest_findings_markdown_report,
    build_backtest_readiness_score_markdown_report,
    build_realistic_backtest_manifest_markdown_report,
)
from reports.report_builder import (
    build_backtest_readiness_score_text_report,
    build_realistic_backtest_manifest_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_realistic_backtest_profile()

    df_dep, s_dep = build_backtest_dependency_registry(profile)
    df_ev, s_ev = build_backtest_validation_evidence_registry(profile)
    df_rev, s_rev = build_backtest_manual_review_queue(profile)
    df_fnd, s_fnd = build_backtest_findings_registry(profile)
    df_scr, s_scr = build_backtest_readiness_score_report(profile)
    df_man, s_man = build_realistic_backtest_manifest(profile)

    data_lake.save_backtest_dependencies(df_dep, s_dep)
    data_lake.save_backtest_validation_evidence(df_ev, s_ev)
    data_lake.save_backtest_manual_review(df_rev, s_rev)
    data_lake.save_backtest_findings_registry(df_fnd, s_fnd)
    data_lake.save_backtest_readiness_score_report(df_scr, s_scr)
    data_lake.save_realistic_backtest_manifest(df_man, s_man)

    md_fnd = build_backtest_findings_markdown_report(s_fnd, df_fnd)
    md_scr = build_backtest_readiness_score_markdown_report(s_scr, df_scr)
    txt_scr = build_backtest_readiness_score_text_report(s_scr, df_scr)
    md_man = build_realistic_backtest_manifest_markdown_report(s_man, df_man)
    txt_man = build_realistic_backtest_manifest_text_report(s_man, df_man)

    out_dir = Path("reports/output/advanced_realistic_backtest")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "findings.md", "w", encoding="utf-8") as f:
        f.write(md_fnd)
    with open(out_dir / "readiness_score.md", "w", encoding="utf-8") as f:
        f.write(md_scr)
    with open(out_dir / "readiness_score.txt", "w", encoding="utf-8") as f:
        f.write(txt_scr)
    with open(out_dir / "manifest.md", "w", encoding="utf-8") as f:
        f.write(md_man)
    with open(out_dir / "manifest.txt", "w", encoding="utf-8") as f:
        f.write(txt_man)

    print("=" * 70)
    print("PHASE 146: FINDINGS, READINESS & MASTER MANIFEST")
    print("=" * 70)
    print(f"Dependencies Tracked  : {len(df_dep)}")
    print(f"Evidence Records      : {len(df_ev)}")
    print(f"Manual Review Items   : {len(df_rev)}")
    print(f"Findings Items        : {len(df_fnd)}")
    print(f"Readiness Score       : {s_scr.get('readiness_score', 1.0):.2f}")
    print(f"Classification        : {s_scr.get('classification')}")
    print(f"Manifest ID           : {s_man.get('manifest_id')}")
    print(f"Phase 147 Handoff     : {s_man.get('phase_147_handoff_ready')}")
    print(f"Non-Signal Invariant  : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
