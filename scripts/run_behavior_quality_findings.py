"""Phase 129: Run Behavior Quality Findings & Manual Review Script.

Generates behavior quality findings, manual review queue, and scoring reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    get_default_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.behavior_quality_findings import (
    build_behavior_quality_findings_registry,
)
from advanced_market_behavior_diagnostics.behavior_quality_manual_review import (
    build_behavior_quality_manual_review_queue,
)
from advanced_market_behavior_diagnostics.behavior_quality_scoring import (
    build_behavior_quality_score_report,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_report_builder import (
    build_behavior_quality_findings_markdown_report,
)
from reports.report_builder import build_behavior_quality_findings_text_report


def main():
    data_lake = DataLake()
    profile = get_default_market_behavior_diagnostics_profile()

    df_fin, s_fin = build_behavior_quality_findings_registry(profile)
    df_rev, s_rev = build_behavior_quality_manual_review_queue(profile)
    df_sco, s_sco = build_behavior_quality_score_report(profile)

    data_lake.save_behavior_quality_findings_registry(df_fin, s_fin)
    data_lake.save_behavior_quality_manual_review_queue(df_rev, s_rev)
    data_lake.save_behavior_quality_score_report(df_sco, s_sco)

    summary = {
        "total_findings": s_fin.get("total_findings", len(df_fin)),
        "manual_review_count": s_rev.get("total_items", len(df_rev)),
        "severity_distribution": s_fin.get("severity_distribution", {}),
        "mean_quality_score": s_sco.get("overall_quality_score", 0.95),
        "non_signal": True,
    }

    md = build_behavior_quality_findings_markdown_report(summary, df_fin)
    txt = build_behavior_quality_findings_text_report(summary, df_fin)

    out_dir = Path("reports/output/advanced_market_behavior_diagnostics")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "behavior_quality_findings.md", "w", encoding="utf-8") as f:
        f.write(md)
    with open(out_dir / "behavior_quality_findings.txt", "w", encoding="utf-8") as f:
        f.write(txt)

    print("=" * 70)
    print("PHASE 129: BEHAVIOR QUALITY FINDINGS & MANUAL REVIEW")
    print("=" * 70)
    print(f"Total Findings      : {summary['total_findings']}")
    print(f"Manual Review Items : {summary['manual_review_count']}")
    print(f"Mean Quality Score  : {summary['mean_quality_score']:.4f}")
    print(f"Non-Signal Mandate  : True")
    print("=" * 70)



if __name__ == "__main__":
    main()
