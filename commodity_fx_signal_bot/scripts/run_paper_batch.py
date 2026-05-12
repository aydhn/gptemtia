import argparse
import sys
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from config.settings import settings
from paper.paper_config import get_paper_trading_profile
from paper.paper_pipeline import PaperTradingPipeline
import reports.report_builder as report_builder


def get_symbols(asset_class: str | None = None, specific_symbol: str | None = None) -> list[SymbolSpec]:
    from core.universe import COMMODITY_SYMBOLS, FX_SYMBOLS
    specs = []

    if specific_symbol:
        specs.append(SymbolSpec(specific_symbol, "unknown", "commodity", "metals", "USD"))
        return specs

    for s, n in COMMODITY_SYMBOLS.items():
        if asset_class is None or asset_class == "commodity":
            specs.append(SymbolSpec(s, n, "commodity", "metals", "USD"))

    for s, n in FX_SYMBOLS.items():
        if asset_class is None or asset_class == "fx":
            specs.append(SymbolSpec(s, n, "fx", "currency", "USD"))

    return specs

def main():


    parser = argparse.ArgumentParser(description="Run paper batch for a universe")
    parser.add_argument("--limit", type=int, help="Limit number of symbols to run")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class (e.g. commodity, fx)")
    parser.add_argument("--symbol", type=str, help="Run specific symbol only")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (e.g. 1d)")
    parser.add_argument("--profile", type=str, default="balanced_virtual_paper", help="Paper trading profile name")
    parser.add_argument("--save", action="store_true", default=True, help="Save the results to the data lake")

    args = parser.parse_args()

    lake = DataLake(settings)

    try:
        profile = get_paper_trading_profile(args.profile)
    except Exception as e:
        print(f"Error loading profile: {e}")
        return

    specs = get_symbols(args.asset_class, args.symbol)

    pipeline = PaperTradingPipeline(lake, settings, profile)
    print(f"Running Paper Batch Pipeline for {len(specs)} symbols ({args.timeframe}) using profile {args.profile}...")

    result = pipeline.build_for_universe(specs, args.timeframe, profile, args.limit, args.save)

    if not result or "summary_df" not in result:
        print("Batch processing returned no results.")
        return

    df = result["summary_df"]

    out_dir = Path("reports/output/paper_reports")
    out_dir.mkdir(parents=True, exist_ok=True)

    df.to_csv(out_dir / "paper_batch_summary.csv", index=False)

    overall_summary = {
        "processed_symbols": len(df),
        "total_virtual_orders": df['virtual_order_count'].sum() if 'virtual_order_count' in df else 0,
        "total_filled_orders": df['filled_order_count'].sum() if 'filled_order_count' in df else 0,
        "total_closed_positions": df['closed_position_count'].sum() if 'closed_position_count' in df else 0,
        "average_virtual_return_pct": df['total_virtual_return_pct'].mean() if 'total_virtual_return_pct' in df else 0.0,
    }

    report_text = report_builder.build_paper_batch_report(overall_summary, df)

    out_file = out_dir / "paper_batch_summary.txt"
    with open(out_file, "w") as f:
        f.write(report_text)

    print(f"Report saved to {out_file}")
    print("\n" + "="*40 + "\n")
    print(report_text)

if __name__ == "__main__":
    main()
