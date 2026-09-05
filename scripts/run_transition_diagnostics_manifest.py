"""Phase 130: Run Transition Diagnostics Manifest Script.

Generates comprehensive manifest of Phase 130 datasets, metrics, reports, and contracts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.transition_diagnostics_manifest import (
    build_transition_diagnostics_manifest,
)
from advanced_regime_transition.regime_transition_report_builder import (
    build_transition_manifest_markdown_report,
)
from reports.report_builder import build_transition_diagnostics_manifest_text_report


def main():
    data_lake = DataLake()
    profile = get_default_regime_transition_profile()

    df_man, s_man = build_transition_diagnostics_manifest(profile)
    data_lake.save_transition_diagnostics_manifest(df_man, s_man)

    md_content = build_transition_manifest_markdown_report(s_man, df_man)
    txt_content = build_transition_diagnostics_manifest_text_report(s_man, df_man)

    out_dir = Path("reports/output/advanced_regime_transition")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "transition_diagnostics_manifest.md", "w", encoding="utf-8") as f:
        f.write(md_content)
    with open(out_dir / "transition_diagnostics_manifest.txt", "w", encoding="utf-8") as f:
        f.write(txt_content)

    print("=" * 70)
    print("PHASE 130: TRANSITION DIAGNOSTICS MANIFEST")
    print("=" * 70)
    print(f"Manifest Name      : {s_man.get('manifest_name')}")
    print(f"Total Artifacts    : {len(df_man.columns)}")
    print(f"Active Profile     : {s_man.get('active_profile')}")
    print(f"Current Phase      : {s_man.get('current_phase')}")
    print(f"Next Phase         : {s_man.get('next_phase')}")
    print(f"Target Final Phase : {s_man.get('target_final_phase')}")
    print(f"Non-Signal         : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
