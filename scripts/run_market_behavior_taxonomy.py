"""Phase 126: Run Market Behavior and Regime State Taxonomy Script.

Generates market behavior taxonomy and regime state taxonomy registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_foundation.regime_foundation_config import (
    get_default_regime_foundation_profile,
)
from advanced_regime_foundation.market_behavior_taxonomy import (
    build_market_behavior_taxonomy_registry,
)
from advanced_regime_foundation.regime_state_taxonomy import (
    build_regime_state_taxonomy_registry,
)
from advanced_regime_foundation.regime_foundation_report_builder import (
    build_market_behavior_taxonomy_markdown_report,
    build_regime_state_taxonomy_markdown_report,
)
from reports.report_builder import (
    build_market_behavior_taxonomy_text_report,
    build_regime_state_taxonomy_text_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_regime_foundation_profile()

    df_beh, s_beh = build_market_behavior_taxonomy_registry(profile)
    df_state, s_state = build_regime_state_taxonomy_registry(profile)

    data_lake.save_market_behavior_taxonomy_registry(df_beh, s_beh)
    data_lake.save_regime_state_taxonomy_registry(df_state, s_state)

    md_beh = build_market_behavior_taxonomy_markdown_report(s_beh, df_beh)
    md_state = build_regime_state_taxonomy_markdown_report(s_state, df_state)
    txt_beh = build_market_behavior_taxonomy_text_report(s_beh, df_beh)
    txt_state = build_regime_state_taxonomy_text_report(s_state, df_state)

    out_dir = Path("reports/output/advanced_regime_foundation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "market_behavior_taxonomy.md", "w", encoding="utf-8") as f:
        f.write(md_beh)
    with open(out_dir / "market_behavior_taxonomy.txt", "w", encoding="utf-8") as f:
        f.write(txt_beh)
    with open(out_dir / "regime_state_taxonomy.md", "w", encoding="utf-8") as f:
        f.write(md_state)
    with open(out_dir / "regime_state_taxonomy.txt", "w", encoding="utf-8") as f:
        f.write(txt_state)

    print("=" * 70)
    print("PHASE 126: MARKET BEHAVIOR & REGIME STATE TAXONOMY")
    print("=" * 70)
    print(f"Total Behaviors : {s_beh['total_behaviors']}")
    print(f"Ready Behaviors : {s_beh['ready_behaviors']}")
    print(f"Total States    : {s_state['total_states']}")
    print(f"Ready States    : {s_state['ready_states']}")
    print(f"Prefix Check    : {s_state['all_prefixed_correctly']}")
    print(f"Non-Signal      : {s_beh['all_non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
