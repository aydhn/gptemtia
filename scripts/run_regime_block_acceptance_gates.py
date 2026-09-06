"""Phase 135: Run Regime Block Acceptance Gates Script.

Evaluates all 17 acceptance gates, calculates composite score, builds review queue,
and persists results to DataLake.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_regime_acceptance.regime_acceptance_config import (
    get_default_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_block_acceptance_gates import (
    build_regime_block_acceptance_gate_registry,
)
from advanced_regime_acceptance.regime_block_acceptance_scoring import (
    build_regime_block_acceptance_score_report,
)
from advanced_regime_acceptance.regime_block_manual_review import (
    build_regime_block_manual_review_queue,
)
from advanced_regime_acceptance.regime_acceptance_report_builder import (
    build_regime_acceptance_gate_markdown_report,
    build_regime_acceptance_score_markdown_report,
    build_regime_manual_review_markdown_report,
)
from reports.report_builder import (
    build_regime_acceptance_gate_text_report,
    build_regime_acceptance_score_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_regime_acceptance_profile()

    df_gate, s_gate = build_regime_block_acceptance_gate_registry(profile)
    df_score, s_score = build_regime_block_acceptance_score_report(profile)
    df_rev, s_rev = build_regime_block_manual_review_queue(profile)

    data_lake.save_regime_block_acceptance_gate_registry(df_gate, s_gate)
    data_lake.save_regime_block_acceptance_score_report(df_score, s_score)
    data_lake.save_regime_block_manual_review_queue(df_rev, s_rev)

    md_gate = build_regime_acceptance_gate_markdown_report(s_gate, df_gate)
    md_score = build_regime_acceptance_score_markdown_report(s_score, df_score)
    md_rev = build_regime_manual_review_markdown_report(s_rev, df_rev)

    txt_gate = build_regime_acceptance_gate_text_report(s_gate, df_gate)
    txt_score = build_regime_acceptance_score_text_report(s_score, df_score)

    out_dir = Path("reports/output/advanced_regime_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "gates.md", "w", encoding="utf-8") as f:
        f.write(md_gate)
    with open(out_dir / "score.md", "w", encoding="utf-8") as f:
        f.write(md_score)
    with open(out_dir / "manual_review.md", "w", encoding="utf-8") as f:
        f.write(md_rev)
    with open(out_dir / "gates.txt", "w", encoding="utf-8") as f:
        f.write(txt_gate)
    with open(out_dir / "score.txt", "w", encoding="utf-8") as f:
        f.write(txt_score)

    print("=" * 70)
    print("PHASE 135: REGIME BLOCK ACCEPTANCE GATES & SCORING")
    print("=" * 70)
    print(f"Total Gates        : {s_gate['total_gates']}")
    print(f"Passed Gates       : {s_gate['passed_gates']}")
    print(f"All Passed         : {s_gate['all_passed']}")
    print(f"Acceptance Score   : {s_score['acceptance_score']}")
    print(f"Classification     : {s_score['classification']}")
    print(f"Is Acceptable      : {s_score['is_acceptable']}")
    print(f"Manual Review Items: {s_rev['total_review_items']}")
    print(f"Non-Signal         : {s_score['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
