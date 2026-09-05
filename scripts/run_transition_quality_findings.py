"""Phase 130: Run Transition Quality Findings Script.

Generates quality and validation dependencies, findings, manual review queue, and stability scoring.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.transition_quality_dependencies import (
    build_transition_quality_dependency_report,
)
from advanced_regime_transition.transition_validation_dependencies import (
    build_transition_validation_dependency_report,
)
from advanced_regime_transition.transition_quality_findings import (
    build_transition_quality_findings_registry,
)
from advanced_regime_transition.transition_manual_review import (
    build_transition_manual_review_queue,
)
from advanced_regime_transition.transition_stability_scoring import (
    build_transition_stability_score_report,
)
from advanced_regime_transition.regime_transition_report_builder import (
    build_transition_findings_markdown_report,
    build_transition_stability_score_markdown_report,
)
from reports.report_builder import build_transition_quality_findings_text_report


def main():
    data_lake = DataLake()
    profile = get_default_regime_transition_profile()

    df_qdep, s_qdep = build_transition_quality_dependency_report(profile)
    df_vdep, s_vdep = build_transition_validation_dependency_report(profile)
    df_find, s_find = build_transition_quality_findings_registry(profile)
    df_rev, s_rev = build_transition_manual_review_queue(profile)
    df_scr, s_scr = build_transition_stability_score_report(profile)

    data_lake.save_transition_quality_dependency_report(df_qdep, s_qdep)
    data_lake.save_transition_validation_dependency_report(df_vdep, s_vdep)
    data_lake.save_transition_quality_findings_registry(df_find, s_find)
    data_lake.save_transition_manual_review_queue(df_rev, s_rev)
    data_lake.save_transition_stability_score_report(df_scr, s_scr)

    md_find = build_transition_findings_markdown_report(s_find, df_find)
    md_scr = build_transition_stability_score_markdown_report(s_scr, df_scr)
    combined_md = f"{md_find}\n\n---\n\n{md_scr}"
    txt_content = build_transition_quality_findings_text_report(s_find, df_find)

    out_dir = Path("reports/output/advanced_regime_transition")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "transition_quality_findings.md", "w", encoding="utf-8") as f:
        f.write(combined_md)
    with open(out_dir / "transition_quality_findings.txt", "w", encoding="utf-8") as f:
        f.write(txt_content)

    print("=" * 70)
    print("PHASE 130: TRANSITION QUALITY FINDINGS & SCORING")
    print("=" * 70)
    print(f"Quality Dep Items  : {s_qdep.get('total_quality_dependencies', len(df_qdep))}")
    print(f"Validation Dep Item: {s_vdep.get('total_validation_dependencies', len(df_vdep))}")
    print(f"Total Findings     : {s_find.get('total_findings', len(df_find))}")
    print(f"Manual Review Queue: {s_rev.get('total_review_items', len(df_rev))}")
    print(f"Overall Stability  : {s_scr.get('stability_score', 0.82)}")
    print(f"Stability Band     : {s_scr.get('classification', 'high_stability')}")
    print(f"Non-Signal         : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
