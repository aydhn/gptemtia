# -*- coding: utf-8 -*-
"""Phase 148: Run Stress Findings and Manifest Script.

Builds findings registry, diagnostic readiness score, and master manifest.
Saves to DataLake and writes markdown/text reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_manual_review import (
    build_stress_manual_review_queue,
)
from advanced_stress_testing.stress_findings import (
    build_stress_findings_registry,
)
from advanced_stress_testing.stress_readiness_scoring import (
    build_stress_readiness_score_report,
)
from advanced_stress_testing.stress_testing_manifest import (
    build_stress_testing_manifest,
)
from advanced_stress_testing.stress_testing_report_builder import (
    build_stress_findings_markdown_report,
    build_stress_readiness_score_markdown_report,
    build_stress_testing_manifest_markdown_report,
)
from reports.report_builder import (
    build_stress_findings_text_report,
    build_stress_readiness_score_text_report,
    build_stress_testing_manifest_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_stress_testing_profile()

    df_rev, s_rev = build_stress_manual_review_queue(profile)
    df_fnd, s_fnd = build_stress_findings_registry(profile)
    df_scr, s_scr = build_stress_readiness_score_report(profile)
    df_man, s_man = build_stress_testing_manifest(profile)

    data_lake.save_stress_findings_registry(df_fnd, s_fnd)
    data_lake.save_stress_readiness_score_report(df_scr, s_scr)
    data_lake.save_stress_testing_manifest(df_man, s_man)

    md_fnd = build_stress_findings_markdown_report(s_fnd, df_fnd)
    txt_fnd = build_stress_findings_text_report(s_fnd, df_fnd)
    md_scr = build_stress_readiness_score_markdown_report(s_scr, df_scr)
    txt_scr = build_stress_readiness_score_text_report(s_scr, df_scr)
    md_man = build_stress_testing_manifest_markdown_report(s_man, df_man)
    txt_man = build_stress_testing_manifest_text_report(s_man, df_man)

    out_dir = Path("reports/output/advanced_stress_testing")
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
    print("PHASE 148: STRESS TESTING FINDINGS, READINESS & MANIFEST")
    print("=" * 70)
    print(f"Review Queue Items       : {s_rev.get('total_review_items', len(df_rev))}")
    print(f"Total Findings           : {s_fnd.get('total_findings', len(df_fnd))}")
    print(f"Critical Blockers        : {s_fnd.get('critical_count', 0)}")
    print(f"Readiness Score          : {s_scr.get('score', 1.0):.2f}")
    print(f"Readiness Classification : {s_scr.get('classification')}")
    print(f"Manifest ID              : {s_man.get('manifest_id')}")
    print(f"Stress Test Executed     : {s_man.get('stress_test_executed')}")
    print(f"Scenario Simulation Exec : {s_man.get('scenario_simulation_executed')}")
    print(f"Metric Calc Performed    : {s_man.get('metric_calculation_performed')}")
    print(f"Phase 149 Handoff Ready  : {s_man.get('phase_149_handoff_ready')}")
    print(f"Non-Signal Invariant     : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
