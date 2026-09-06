"""Phase 135: Run Phase 126-135 Acceptance Manifest Script.

Generates the final acceptance manifest for the entire regime block and creates
the Phase 136 advanced ML/GPU runtime handoff packet.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_regime_acceptance.regime_acceptance_config import (
    get_default_regime_acceptance_profile,
)
from advanced_regime_acceptance.phase_126_135_acceptance_manifest import (
    build_phase_126_135_acceptance_manifest,
)
from advanced_regime_acceptance.phase_136_handoff import (
    build_phase_136_advanced_ml_gpu_handoff_report,
)
from advanced_regime_acceptance.regime_acceptance_report_builder import (
    build_regime_acceptance_manifest_markdown_report,
    build_phase_136_handoff_markdown_report,
)
from reports.report_builder import (
    build_phase_126_135_acceptance_manifest_text_report,
    build_phase_136_handoff_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_regime_acceptance_profile()

    df_man, s_man = build_phase_126_135_acceptance_manifest(profile)
    df_hand, s_hand = build_phase_136_advanced_ml_gpu_handoff_report(profile)

    data_lake.save_phase_126_135_acceptance_manifest(df_man, s_man)
    data_lake.save_phase_136_advanced_ml_gpu_handoff_report(df_hand, s_hand)

    md_man = build_regime_acceptance_manifest_markdown_report(s_man, df_man)
    md_hand = build_phase_136_handoff_markdown_report(s_hand, df_hand)

    txt_man = build_phase_126_135_acceptance_manifest_text_report(s_man, df_man)
    txt_hand = build_phase_136_handoff_text_report(s_hand, df_hand)

    out_dir = Path("reports/output/advanced_regime_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "manifest.md", "w", encoding="utf-8") as f:
        f.write(md_man)
    with open(out_dir / "handoff_phase_136.md", "w", encoding="utf-8") as f:
        f.write(md_hand)
    with open(out_dir / "manifest.txt", "w", encoding="utf-8") as f:
        f.write(txt_man)
    with open(out_dir / "handoff_phase_136.txt", "w", encoding="utf-8") as f:
        f.write(txt_hand)

    print("=" * 70)
    print("PHASE 135: PHASE 126-135 REGIME BLOCK ACCEPTANCE MANIFEST & HANDOFF")
    print("=" * 70)
    print(f"Block Name        : {s_man['block_name']}")
    print(f"Phase Range       : {s_man['phase_start']}-{s_man['phase_end']}")
    print(f"Next Phase        : {s_man['next_phase']}")
    print(f"Target Final Phase: {s_man['target_final_phase']}")
    print(f"Acceptance Score  : {s_man['acceptance_score']}")
    print(f"Non-Signal        : {s_man['non_signal']}")
    print(f"Production Ready  : {s_man['production_ready']} (Research only)")
    print(f"Broker Ready      : {s_man['broker_ready']}")
    print(f"Handoff Satisfied : {s_hand['all_satisfied']} ({s_hand['satisfied_prerequisites']}/{s_hand['total_prerequisites']})")
    print("=" * 70)


if __name__ == "__main__":
    main()
