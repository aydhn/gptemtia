"""Run script: Multi-Domain Context Registries for Phase 131 Cross-Asset Regime Context."""

import sys
from advanced_cross_asset_regime_context.cross_asset_regime_pipeline import (
    CrossAssetRegimePipeline,
)
from advanced_cross_asset_regime_context.cross_asset_regime_report_builder import (
    build_fx_commodity_context_markdown_report,
    build_macro_calendar_news_context_markdown_report,
)
from reports.report_builder import (
    build_fx_commodity_regime_context_text_report,
)


def main():
    print("Executing Phase 131 Context Registries (FX, Commodity, Macro, Calendar, News)...")
    pipeline = CrossAssetRegimePipeline()
    dfs, summaries = pipeline.build_context_registries(save=True)

    print(f"FX/Commodity Records: {len(dfs['fx_commodity'])}")
    print(f"FX/Macro Records: {len(dfs['fx_macro'])}")
    print(f"Commodity/Macro Records: {len(dfs['commodity_macro'])}")
    print(f"Macro/Calendar Records: {len(dfs['macro_calendar'])}")
    print(f"Calendar/News Records: {len(dfs['calendar_news'])}")

    txt_fxc = build_fx_commodity_regime_context_text_report(summaries["fx_commodity"])
    print("\n--- FX/Commodity Context Summary ---")
    print(txt_fxc)
    print("\nSUCCESS: Phase 131 Cross-Asset Context Registries generated and saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
