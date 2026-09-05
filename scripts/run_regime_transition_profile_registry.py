"""Phase 130: Run Regime Transition Profile & Domain Registry Script.

Generates operational profiles and master domain registry for Phase 130.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.regime_transition_profile_registry import (
    build_regime_transition_profile_registry,
)
from advanced_regime_transition.regime_transition_domain_registry import (
    build_regime_transition_domain_registry,
)
from advanced_regime_transition.regime_transition_report_builder import (
    build_regime_transition_profile_markdown_report,
)
from reports.report_builder import build_regime_transition_text_report


def main():
    data_lake = DataLake()
    profile = get_default_regime_transition_profile()

    df_prof, s_prof = build_regime_transition_profile_registry(profile)
    df_dom, s_dom = build_regime_transition_domain_registry(profile)

    data_lake.save_regime_transition_profile_registry(df_prof, s_prof)
    data_lake.save_regime_transition_domain_registry(df_dom, s_dom)

    md_content = build_regime_transition_profile_markdown_report(s_prof, df_prof)
    txt_content = build_regime_transition_text_report(s_prof, df_prof)

    out_dir = Path("reports/output/advanced_regime_transition")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "profile_registry.md", "w", encoding="utf-8") as f:
        f.write(md_content)
    with open(out_dir / "profile_registry.txt", "w", encoding="utf-8") as f:
        f.write(txt_content)

    print("=" * 70)
    print("PHASE 130: REGIME TRANSITION PROFILE & DOMAIN REGISTRY")
    print("=" * 70)
    print(f"Active Profile : {s_prof.get('active_profile')}")
    print(f"Total Profiles : {s_prof.get('total_profiles')}")
    print(f"Total Domains  : {s_dom.get('total_domains')}")
    print(f"Current Phase  : {s_prof.get('current_phase')}")
    print(f"Target Final   : {s_prof.get('target_final_phase')}")
    print(f"Next Phase     : {s_prof.get('next_phase')}")
    print(f"Non-Signal     : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
