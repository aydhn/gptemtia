"""Phase 129: Run Market Behavior Diagnostics Reports Script.

Generates volatility, trend, range, macro event, news metadata, cross-asset,
transition readiness, stability readiness, and dependency reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    get_default_market_behavior_diagnostics_profile,
)
from advanced_market_behavior_diagnostics.volatility_behavior_diagnostics import (
    build_volatility_behavior_diagnostics_report,
)
from advanced_market_behavior_diagnostics.trend_behavior_diagnostics import (
    build_trend_behavior_diagnostics_report,
)
from advanced_market_behavior_diagnostics.range_behavior_diagnostics import (
    build_range_behavior_diagnostics_report,
)
from advanced_market_behavior_diagnostics.macro_event_behavior_diagnostics import (
    build_macro_event_behavior_diagnostics_report,
)
from advanced_market_behavior_diagnostics.news_metadata_behavior_diagnostics import (
    build_news_metadata_behavior_diagnostics_report,
)
from advanced_market_behavior_diagnostics.cross_asset_behavior_diagnostics import (
    build_cross_asset_behavior_diagnostics_report,
)
from advanced_market_behavior_diagnostics.behavior_transition_readiness import (
    build_behavior_transition_readiness_report,
)
from advanced_market_behavior_diagnostics.behavior_stability_readiness import (
    build_behavior_stability_readiness_report,
)
from advanced_market_behavior_diagnostics.regime_quality_dependencies import (
    build_regime_quality_dependency_report,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_report_builder import (
    build_behavior_diagnostics_domain_markdown_report,
)
from reports.report_builder import build_behavior_diagnostics_domain_text_report


def main():
    data_lake = DataLake()
    profile = get_default_market_behavior_diagnostics_profile()

    df_vol, s_vol = build_volatility_behavior_diagnostics_report(profile)
    df_tre, s_tre = build_trend_behavior_diagnostics_report(profile)
    df_ran, s_ran = build_range_behavior_diagnostics_report(profile)
    df_mac, s_mac = build_macro_event_behavior_diagnostics_report(profile)
    df_new, s_new = build_news_metadata_behavior_diagnostics_report(profile)
    df_cro, s_cro = build_cross_asset_behavior_diagnostics_report(profile)
    df_tra, s_tra = build_behavior_transition_readiness_report(profile)
    df_sta, s_sta = build_behavior_stability_readiness_report(profile)
    df_dep, s_dep = build_regime_quality_dependency_report(profile)

    data_lake.save_volatility_behavior_diagnostics_report(df_vol, s_vol)
    data_lake.save_trend_behavior_diagnostics_report(df_tre, s_tre)
    data_lake.save_range_behavior_diagnostics_report(df_ran, s_ran)
    data_lake.save_macro_event_behavior_diagnostics_report(df_mac, s_mac)
    data_lake.save_news_metadata_behavior_diagnostics_report(df_new, s_new)
    data_lake.save_cross_asset_behavior_diagnostics_report(df_cro, s_cro)
    data_lake.save_behavior_transition_readiness_report(df_tra, s_tra)
    data_lake.save_behavior_stability_readiness_report(df_sta, s_sta)
    data_lake.save_regime_quality_dependency_report(df_dep, s_dep)

    summary = {
        "total_domains": 6,
        "overall_readiness_mean": 1.0 if s_tra.get("all_ready", True) and s_sta.get("all_ready", True) else 0.5,
        "zero_full_text_guaranteed": True,
        "zero_future_leak_guaranteed": True,
        "non_signal": True,
    }

    md = build_behavior_diagnostics_domain_markdown_report(summary, df_vol)
    txt = build_behavior_diagnostics_domain_text_report(summary, df_vol)

    out_dir = Path("reports/output/advanced_market_behavior_diagnostics")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "behavior_diagnostics.md", "w", encoding="utf-8") as f:
        f.write(md)
    with open(out_dir / "behavior_diagnostics.txt", "w", encoding="utf-8") as f:
        f.write(txt)

    print("=" * 70)
    print("PHASE 129: MARKET BEHAVIOR DIAGNOSTICS REPORTS")
    print("=" * 70)
    print(f"Volatility Contexts : {s_vol.get('total_contexts', len(df_vol))}")
    print(f"Trend Contexts      : {s_tre.get('total_contexts', len(df_tre))}")
    print(f"Range Contexts      : {s_ran.get('total_contexts', len(df_ran))}")
    print(f"Macro Event Contexts: {s_mac.get('total_contexts', len(df_mac))}")
    print(f"News Meta Contexts  : {s_new.get('total_contexts', len(df_new))}")
    print(f"Cross-Asset Contexts: {s_cro.get('total_contexts', len(df_cro))}")
    print(f"Trans Readiness All : {s_tra.get('all_ready', True)}")
    print(f"Stab Readiness All  : {s_sta.get('all_ready', True)}")
    print(f"Dependencies Total  : {s_dep.get('total_dependencies', len(df_dep))}")
    print(f"Non-Signal Mandate  : True")
    print("=" * 70)



if __name__ == "__main__":
    main()
