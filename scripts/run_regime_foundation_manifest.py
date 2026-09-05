"""Phase 126: Run Regime Foundation Manifest and Phase 127 Handoff Script.

Generates non-signal policies, forbidden claim registries, foundation manifest, and Phase 127 handoff.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_foundation.regime_foundation_config import (
    get_default_regime_foundation_profile,
)
from advanced_regime_foundation.regime_non_signal_policies import (
    build_regime_non_signal_policy_registry,
)
from advanced_regime_foundation.regime_forbidden_claims import (
    build_regime_forbidden_claim_registry,
)
from advanced_regime_foundation.regime_foundation_manifest import (
    build_regime_foundation_manifest,
)
from advanced_regime_foundation.phase_127_handoff import (
    build_phase_127_regime_feature_matrix_handoff_report,
)
from advanced_regime_foundation.regime_foundation_report_builder import (
    build_regime_manifest_markdown_report,
    build_phase_127_handoff_markdown_report,
)
from reports.report_builder import (
    build_regime_manifest_text_report,
    build_phase_127_handoff_text_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_regime_foundation_profile()

    df_nsp, s_nsp = build_regime_non_signal_policy_registry(profile)
    df_fc, s_fc = build_regime_forbidden_claim_registry(profile)
    df_man, s_man = build_regime_foundation_manifest(profile)
    df_hand, s_hand = build_phase_127_regime_feature_matrix_handoff_report(profile)

    data_lake.save_regime_non_signal_policy_registry(df_nsp, s_nsp)
    data_lake.save_regime_forbidden_claim_registry(df_fc, s_fc)
    data_lake.save_regime_foundation_manifest(df_man, s_man)
    data_lake.save_phase_127_regime_feature_matrix_handoff_report(df_hand, s_hand)

    md_man = build_regime_manifest_markdown_report(s_man, df_man)
    md_hand = build_phase_127_handoff_markdown_report(s_hand, df_hand)
    txt_man = build_regime_manifest_text_report(s_man, df_man)
    txt_hand = build_phase_127_handoff_text_report(s_hand, df_hand)

    out_dir = Path("reports/output/advanced_regime_foundation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "regime_foundation_manifest.md", "w", encoding="utf-8") as f:
        f.write(md_man)
    with open(out_dir / "regime_foundation_manifest.txt", "w", encoding="utf-8") as f:
        f.write(txt_man)
    with open(out_dir / "phase_127_handoff.md", "w", encoding="utf-8") as f:
        f.write(md_hand)
    with open(out_dir / "phase_127_handoff.txt", "w", encoding="utf-8") as f:
        f.write(txt_hand)

    print("=" * 70)
    print("PHASE 126: REGIME FOUNDATION MANIFEST & PHASE 127 HANDOFF")
    print("=" * 70)
    print(f"Foundation     : {s_man['foundation_name']}")
    print(f"Current Phase  : {s_man['current_phase']}")
    print(f"Next Phase     : {s_man['next_phase']}")
    print(f"Regime Families: {s_man['regime_family_count']}")
    print(f"Regime States  : {s_man['regime_state_count']}")
    print(f"Handoff Status : {s_hand['handoff_status']}")
    print(f"Handoff Items  : {s_hand['ready_items']}/{s_hand['total_handoff_items']}")
    print(f"Non-Signal     : {s_man['non_signal']}")
    print(f"Source Preserv.: {s_man['source_preserved']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
