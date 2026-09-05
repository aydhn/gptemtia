"""Phase 125: Run Phase 116-125 Acceptance Manifest and Handoff Script.

Generates the master block acceptance manifest and Phase 126 handoff specification.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    get_default_feature_factor_acceptance_profile,
)
from advanced_feature_factor_acceptance.feature_engine_block_status import (
    build_feature_engine_block_status_report,
)
from advanced_feature_factor_acceptance.phase_116_125_acceptance_manifest import (
    build_phase_116_125_acceptance_manifest,
)
from advanced_feature_factor_acceptance.phase_126_handoff import (
    build_phase_126_regime_classification_handoff_report,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_report_builder import (
    build_acceptance_manifest_markdown_report,
    build_phase_126_handoff_markdown_report,
)
from reports.report_builder import (
    build_acceptance_manifest_text_report,
    build_phase_126_handoff_text_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_feature_factor_acceptance_profile()

    df_stat, s_stat = build_feature_engine_block_status_report(profile)
    df_man, s_man = build_phase_116_125_acceptance_manifest(profile)
    df_hand, s_hand = build_phase_126_regime_classification_handoff_report(profile)

    data_lake.save_feature_engine_block_status_report(df_stat, s_stat)
    data_lake.save_phase_116_125_acceptance_manifest(df_man, s_man)
    data_lake.save_phase_126_regime_classification_handoff_report(df_hand, s_hand)

    md_man = build_acceptance_manifest_markdown_report(s_man, df_man)
    md_hand = build_phase_126_handoff_markdown_report(s_hand, df_hand)
    txt_man = build_acceptance_manifest_text_report(s_man, df_man)
    txt_hand = build_phase_126_handoff_text_report(s_hand, df_hand)

    out_dir = Path("reports/output/advanced_feature_factor_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "acceptance_manifest.md", "w", encoding="utf-8") as f:
        f.write(md_man)
    with open(out_dir / "phase_126_handoff.md", "w", encoding="utf-8") as f:
        f.write(md_hand)
    with open(out_dir / "acceptance_manifest.txt", "w", encoding="utf-8") as f:
        f.write(txt_man)
    with open(out_dir / "phase_126_handoff.txt", "w", encoding="utf-8") as f:
        f.write(txt_hand)

    print("=" * 70)
    print("PHASE 116-125 ACCEPTANCE MANIFEST & PHASE 126 HANDOFF")
    print("=" * 70)
    print(f"Block Name     : {s_man['block_name']}")
    print(f"Phase Range    : Phase {s_man['phase_start']} -> Phase {s_man['phase_end']}")
    print(f"Target Phase   : {s_man['target_final_phase']}")
    print(f"Next Phase     : {s_man['next_phase']}")
    print(f"Block Status   : {s_stat['overall_status']}")
    print(f"Acceptance Sc. : {s_man['acceptance_score']}")
    print(f"Handoff Status : {s_hand['handoff_status']}")
    print(f"Handoff Items  : {s_hand['ready_items']}/{s_hand['total_handoff_items']}")
    print(f"Non-Signal     : {s_man['non_signal']}")
    print(f"Official Appr. : {s_man['official_approval']}")
    print(f"Production Rdy : {s_man['production_ready']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
