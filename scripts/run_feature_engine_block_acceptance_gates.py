"""Phase 125: Run Feature Engine Block Acceptance Gates and Scoring Script.

Evaluates 16 core acceptance gates, computes weighted score, and queues manual reviews.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    get_default_feature_factor_acceptance_profile,
)
from advanced_feature_factor_acceptance.feature_engine_block_acceptance_gates import (
    build_feature_engine_block_acceptance_gate_registry,
)
from advanced_feature_factor_acceptance.feature_engine_block_acceptance_scoring import (
    build_feature_engine_block_acceptance_score_report,
)
from advanced_feature_factor_acceptance.feature_engine_block_manual_review import (
    build_feature_engine_block_manual_review_queue,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_report_builder import (
    build_acceptance_gate_markdown_report,
    build_acceptance_score_markdown_report,
    build_manual_review_markdown_report,
)
from reports.report_builder import (
    build_acceptance_gate_text_report,
    build_acceptance_score_text_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_feature_factor_acceptance_profile()

    df_gates, s_gates = build_feature_engine_block_acceptance_gate_registry(profile)
    df_score, s_score = build_feature_engine_block_acceptance_score_report(profile)
    df_rev, s_rev = build_feature_engine_block_manual_review_queue(profile)

    data_lake.save_feature_engine_block_acceptance_gate_registry(df_gates, s_gates)
    data_lake.save_feature_engine_block_acceptance_score_report(df_score, s_score)
    data_lake.save_feature_engine_block_manual_review_queue(df_rev, s_rev)

    md_gates = build_acceptance_gate_markdown_report(s_gates, df_gates)
    md_score = build_acceptance_score_markdown_report(s_score, df_score)
    md_rev = build_manual_review_markdown_report(s_rev, df_rev)

    txt_gates = build_acceptance_gate_text_report(s_gates, df_gates)
    txt_score = build_acceptance_score_text_report(s_score, df_score)

    out_dir = Path("reports/output/advanced_feature_factor_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "gates.md", "w", encoding="utf-8") as f:
        f.write(md_gates)
    with open(out_dir / "score.md", "w", encoding="utf-8") as f:
        f.write(md_score)
    with open(out_dir / "manual_review.md", "w", encoding="utf-8") as f:
        f.write(md_rev)
    with open(out_dir / "gates.txt", "w", encoding="utf-8") as f:
        f.write(txt_gates)
    with open(out_dir / "score.txt", "w", encoding="utf-8") as f:
        f.write(txt_score)

    print("=" * 70)
    print("PHASE 125: ACCEPTANCE GATES & SCORING")
    print("=" * 70)
    print(f"Total Gates    : {s_gates['total_gates']}")
    print(f"Passed Gates   : {s_gates['passed_gates']}")
    print(f"All Passed     : {s_gates['all_passed']}")
    print(f"Overall Score  : {s_score['overall_score']}")
    print(f"Score Tier     : {s_score['score_tier']}")
    print(f"Review Items   : {s_rev['total_items']}")
    print(f"Official Appr. : {s_score['official_approval']}")
    print(f"Production Rdy : {s_score['production_ready']}")
    print(f"Non-Signal     : {s_score['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
