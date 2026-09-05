"""Phase 126: Run Regime Family Registry Script.

Generates master regime family registry and specialized family sub-registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_foundation.regime_foundation_config import (
    get_default_regime_foundation_profile,
)
from advanced_regime_foundation.regime_family_registry import (
    build_regime_family_registry,
)
from advanced_regime_foundation.volatility_regime_families import (
    build_volatility_regime_family_registry,
)
from advanced_regime_foundation.trend_regime_families import (
    build_trend_regime_family_registry,
)
from advanced_regime_foundation.range_regime_families import (
    build_range_regime_family_registry,
)
from advanced_regime_foundation.liquidity_regime_placeholders import (
    build_liquidity_regime_placeholder_registry,
)
from advanced_regime_foundation.regime_foundation_report_builder import (
    build_regime_family_markdown_report,
)
from reports.report_builder import build_regime_family_text_report


def main():
    data_lake = DataLake()
    profile = get_default_regime_foundation_profile()

    df_fam, s_fam = build_regime_family_registry(profile)
    df_vol, s_vol = build_volatility_regime_family_registry(profile)
    df_trend, s_trend = build_trend_regime_family_registry(profile)
    df_range, s_range = build_range_regime_family_registry(profile)
    df_liq, s_liq = build_liquidity_regime_placeholder_registry(profile)

    data_lake.save_regime_family_registry(df_fam, s_fam)
    data_lake.save_volatility_regime_family_registry(df_vol, s_vol)
    data_lake.save_trend_regime_family_registry(df_trend, s_trend)
    data_lake.save_range_regime_family_registry(df_range, s_range)
    data_lake.save_liquidity_regime_placeholder_registry(df_liq, s_liq)

    md_fam = build_regime_family_markdown_report(s_fam, df_fam)
    txt_fam = build_regime_family_text_report(s_fam, df_fam)

    out_dir = Path("reports/output/advanced_regime_foundation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "regime_families.md", "w", encoding="utf-8") as f:
        f.write(md_fam)
    with open(out_dir / "regime_families.txt", "w", encoding="utf-8") as f:
        f.write(txt_fam)

    print("=" * 70)
    print("PHASE 126: REGIME FAMILY REGISTRIES")
    print("=" * 70)
    print(f"Total Families : {s_fam['total_families']}")
    print(f"Ready Families : {s_fam['ready_families']}")
    print(f"Vol Sub-Fam    : {s_vol['total_sub_families']}")
    print(f"Trend Sub-Fam  : {s_trend['total_sub_families']}")
    print(f"Range Sub-Fam  : {s_range['total_sub_families']}")
    print(f"Liq Placehldr  : {s_liq['total_placeholders']}")
    print(f"Non-Signal     : {s_fam['all_non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
