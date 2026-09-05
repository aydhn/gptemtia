"""Phase 130: Run Transition Context Reports Script.

Generates volatility, trend, range family diagnostics and macro, news, cross-asset transition contexts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_regime_transition.regime_transition_config import (
    get_default_regime_transition_profile,
)
from advanced_regime_transition.volatility_transition_diagnostics import (
    build_volatility_transition_diagnostics_report,
)
from advanced_regime_transition.trend_transition_diagnostics import (
    build_trend_transition_diagnostics_report,
)
from advanced_regime_transition.range_transition_diagnostics import (
    build_range_transition_diagnostics_report,
)
from advanced_regime_transition.macro_event_transition_context import (
    build_macro_event_transition_context_report,
)
from advanced_regime_transition.news_metadata_transition_context import (
    build_news_metadata_transition_context_report,
)
from advanced_regime_transition.cross_asset_transition_prep import (
    build_cross_asset_transition_prep_report,
)
from advanced_regime_transition.regime_transition_report_builder import (
    build_regime_family_transition_markdown_report,
    build_macro_news_cross_asset_transition_markdown_report,
)
from reports.report_builder import build_transition_context_text_report


def main():
    data_lake = DataLake()
    profile = get_default_regime_transition_profile()

    df_vol, s_vol = build_volatility_transition_diagnostics_report(profile)
    df_trd, s_trd = build_trend_transition_diagnostics_report(profile)
    df_rng, s_rng = build_range_transition_diagnostics_report(profile)
    df_mac, s_mac = build_macro_event_transition_context_report(profile)
    df_nws, s_nws = build_news_metadata_transition_context_report(profile)
    df_xast, s_xast = build_cross_asset_transition_prep_report(profile)

    data_lake.save_volatility_transition_diagnostics_report(df_vol, s_vol)
    data_lake.save_trend_transition_diagnostics_report(df_trd, s_trd)
    data_lake.save_range_transition_diagnostics_report(df_rng, s_rng)
    data_lake.save_macro_event_transition_context_report(df_mac, s_mac)
    data_lake.save_news_metadata_transition_context_report(df_nws, s_nws)
    data_lake.save_cross_asset_transition_prep_report(df_xast, s_xast)

    md_fam = build_regime_family_transition_markdown_report(s_vol, df_vol)
    md_ctx = build_macro_news_cross_asset_transition_markdown_report(s_mac, df_mac)
    combined_md = f"{md_fam}\n\n---\n\n{md_ctx}"
    txt_content = build_transition_context_text_report(s_vol, df_vol)

    out_dir = Path("reports/output/advanced_regime_transition")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "transition_context.md", "w", encoding="utf-8") as f:
        f.write(combined_md)
    with open(out_dir / "transition_context.txt", "w", encoding="utf-8") as f:
        f.write(txt_content)

    print("=" * 70)
    print("PHASE 130: TRANSITION CONTEXT & FAMILY DIAGNOSTICS")
    print("=" * 70)
    print(f"Volatility Pairs   : {s_vol.get('total_contexts', len(df_vol))}")
    print(f"Trend Pairs        : {s_trd.get('total_contexts', len(df_trd))}")
    print(f"Range Pairs        : {s_rng.get('total_contexts', len(df_rng))}")
    print(f"Macro Windows      : {s_mac.get('total_contexts', len(df_mac))}")
    print(f"News Metadata Wins : {s_nws.get('total_contexts', len(df_nws))}")
    print(f"Cross-Asset Pairs  : {s_xast.get('total_contexts', len(df_xast))}")
    print(f"Non-Signal         : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
