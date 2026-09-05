"""Phase 128: Run Regime Rule-Free Profile and Domain Registry Script.

Generates profile registry and functional domain mapping for Phase 128.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_rule_free.regime_rule_free_config import (
    get_default_regime_rule_free_profile,
)
from advanced_regime_rule_free.regime_rule_free_profile_registry import (
    build_regime_rule_free_profile_registry,
)
from advanced_regime_rule_free.regime_rule_free_domain_registry import (
    build_regime_rule_free_domain_registry,
)
from advanced_regime_rule_free.regime_rule_free_report_builder import (
    build_regime_rule_free_profile_markdown_report,
)
from reports.report_builder import build_regime_rule_free_text_report


def main():
    data_lake = DataLake()
    profile = get_default_regime_rule_free_profile()

    df_prof, s_prof = build_regime_rule_free_profile_registry(profile)
    df_dom, s_dom = build_regime_rule_free_domain_registry(profile)

    data_lake.save_regime_rule_free_profile_registry(df_prof, s_prof)
    data_lake.save_regime_rule_free_domain_registry(df_dom, s_dom)

    md_prof = build_regime_rule_free_profile_markdown_report(s_prof, df_prof)
    txt_prof = build_regime_rule_free_text_report(s_prof, df_prof)

    out_dir = Path("reports/output/advanced_regime_rule_free")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "profile_registry.md", "w", encoding="utf-8") as f:
        f.write(md_prof)
    with open(out_dir / "profile_registry.txt", "w", encoding="utf-8") as f:
        f.write(txt_prof)

    print("=" * 70)
    print("PHASE 128: REGIME RULE-FREE PROFILE & DOMAIN REGISTRY")
    print("=" * 70)
    print(f"Active Profile : {s_prof['active_profile']}")
    print(f"Total Profiles : {s_prof['total_profiles']}")
    print(f"Total Domains  : {s_dom['total_domains']}")
    print(f"Current Phase  : {s_prof['current_phase']}")
    print(f"Next Phase     : {s_prof['next_phase']}")
    print(f"Non-Signal     : {s_prof['all_non_signal']}")
    print(f"Clustering Exec: False")
    print("=" * 70)


if __name__ == "__main__":
    main()
