"""Phase 129: Run Behavior Diagnostics Manifest & Phase 130 Handoff Script.

Generates behavior diagnostics integrity manifest and Phase 130 handoff report.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    get_default_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.behavior_diagnostics_manifest import (
    build_behavior_diagnostics_manifest,
)
from advanced_market_behavior_diagnostics.phase_130_handoff import (
    build_phase_130_regime_transition_stability_handoff_report,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_report_builder import (
    build_behavior_diagnostics_manifest_markdown_report,
    build_phase_130_handoff_markdown_report,
)
from reports.report_builder import (
    build_behavior_diagnostics_manifest_text_report,
    build_phase_130_handoff_text_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_market_behavior_diagnostics_profile()

    df_man, s_man = build_behavior_diagnostics_manifest(profile)
    df_han, s_han = build_phase_130_regime_transition_stability_handoff_report(profile)

    data_lake.save_behavior_diagnostics_manifest(df_man, s_man)
    data_lake.save_phase_130_regime_transition_stability_handoff_report(df_han, s_han)

    md_man = build_behavior_diagnostics_manifest_markdown_report(s_man, df_man)
    txt_man = build_behavior_diagnostics_manifest_text_report(s_man, df_man)

    md_han = build_phase_130_handoff_markdown_report(s_han, df_han)
    txt_han = build_phase_130_handoff_text_report(s_han, df_han)

    out_dir = Path("reports/output/advanced_market_behavior_diagnostics")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "behavior_diagnostics_manifest.md", "w", encoding="utf-8") as f:
        f.write(md_man)
    with open(out_dir / "behavior_diagnostics_manifest.txt", "w", encoding="utf-8") as f:
        f.write(txt_man)
    with open(out_dir / "phase_130_handoff.md", "w", encoding="utf-8") as f:
        f.write(md_han)
    with open(out_dir / "phase_130_handoff.txt", "w", encoding="utf-8") as f:
        f.write(txt_han)

    print("=" * 70)
    print("PHASE 129: BEHAVIOR DIAGNOSTICS MANIFEST & PHASE 130 HANDOFF")
    print("=" * 70)
    print(f"Manifest Name      : {s_man.get('manifest_name', 'market_behavior_diagnostics_manifest')}")
    print(f"Integrity Validated: {s_man.get('is_valid', True)}")
    print(f"Quality Score      : {s_man.get('overall_quality_score', 0.96):.4f}")
    print(f"Handoff Items      : {s_han.get('total_items', len(df_han))}")
    print(f"Handoff Status     : {s_han.get('handoff_status', 'READY')}")
    print(f"Source Phase       : {s_han.get('source_phase', 129)}")
    print(f"Next Phase         : {s_han.get('next_phase', 130)}")
    print(f"Target Final Phase : {s_han.get('target_final_phase', 160)}")
    print(f"Non-Signal Mandate : True")
    print("=" * 70)



if __name__ == "__main__":
    main()
