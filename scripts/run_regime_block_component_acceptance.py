"""Phase 135: Run Regime Block Component Acceptance Script.

Evaluates granular component-level acceptance across Phases 126 to 135
and persists findings to DataLake.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_regime_acceptance.regime_acceptance_config import (
    get_default_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_block_component_acceptance import (
    build_regime_block_component_acceptance_report,
)
from advanced_regime_acceptance.regime_acceptance_report_builder import (
    build_regime_component_acceptance_markdown_report,
)
from reports.report_builder import (
    build_regime_component_acceptance_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_regime_acceptance_profile()

    df_comp, s_comp = build_regime_block_component_acceptance_report(profile)
    data_lake.save_regime_block_component_acceptance_report(df_comp, s_comp)

    md_comp = build_regime_component_acceptance_markdown_report(s_comp, df_comp)
    txt_comp = build_regime_component_acceptance_text_report(s_comp, df_comp)

    out_dir = Path("reports/output/advanced_regime_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "component_acceptance.md", "w", encoding="utf-8") as f:
        f.write(md_comp)
    with open(out_dir / "component_acceptance.txt", "w", encoding="utf-8") as f:
        f.write(txt_comp)

    print("=" * 70)
    print("PHASE 135: REGIME BLOCK COMPONENT ACCEPTANCE")
    print("=" * 70)
    print(f"Total Components : {s_comp['total_components']}")
    print(f"All Accepted     : {s_comp['all_accepted']}")
    print(f"Phase Range      : {s_comp['phase_start']}-{s_comp['phase_end']}")
    print(f"Non-Signal       : {s_comp['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
