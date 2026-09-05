"""Phase 129: Run Market Behavior Diagnostics Profile and Domain Registry Script.

Generates profile registry and functional domain mapping for Phase 129.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    get_default_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_profile_registry import (
    build_market_behavior_diagnostics_profile_registry,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_domain_registry import (
    build_market_behavior_diagnostics_domain_registry,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_report_builder import (
    build_market_behavior_diagnostics_profile_markdown_report,
)
from reports.report_builder import build_market_behavior_diagnostics_text_report


def main():
    data_lake = DataLake()
    profile = get_default_market_behavior_diagnostics_profile()

    df_prof, s_prof = build_market_behavior_diagnostics_profile_registry(profile)
    df_dom, s_dom = build_market_behavior_diagnostics_domain_registry(profile)

    data_lake.save_market_behavior_diagnostics_profile_registry(df_prof, s_prof)
    data_lake.save_market_behavior_diagnostics_domain_registry(df_dom, s_dom)

    md_prof = build_market_behavior_diagnostics_profile_markdown_report(s_prof, df_prof)
    txt_prof = build_market_behavior_diagnostics_text_report(s_prof, df_prof)

    out_dir = Path("reports/output/advanced_market_behavior_diagnostics")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "profile_registry.md", "w", encoding="utf-8") as f:
        f.write(md_prof)
    with open(out_dir / "profile_registry.txt", "w", encoding="utf-8") as f:
        f.write(txt_prof)

    print("=" * 70)
    print("PHASE 129: MARKET BEHAVIOR DIAGNOSTICS PROFILE & DOMAIN REGISTRY")
    print("=" * 70)
    print(f"Active Profile : {s_prof['active_profile']}")
    print(f"Total Profiles : {s_prof['total_profiles']}")
    print(f"Total Domains  : {s_dom['total_domains']}")
    print(f"Current Phase  : {s_prof['current_phase']}")
    print(f"Next Phase     : {s_prof['next_phase']}")
    print(f"Non-Signal     : {s_prof.get('all_non_signal', s_prof.get('non_signal', True))}")
    print(f"Clustering Exec: False")
    print("=" * 70)



if __name__ == "__main__":
    main()
