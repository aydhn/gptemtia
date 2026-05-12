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
def main():



    parser = argparse.ArgumentParser(description="Run paper order book preview for a symbol")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to run (e.g. GC=F)")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (e.g. 1d)")
    parser.add_argument("--profile", type=str, default="balanced_virtual_paper", help="Paper trading profile name")
    parser.add_argument("--last", type=int, default=50, help="Number of last orders to show")
    parser.add_argument("--rebuild", action="store_true", help="Rebuild the pipeline instead of loading from data lake")

    args = parser.parse_args()

    spec = SymbolSpec(args.symbol, "unknown", "commodity", "metals", "USD")
    lake = DataLake(settings)

    try:
        profile = get_paper_trading_profile(args.profile)
    except Exception as e:
        print(f"Error loading profile: {e}")
        return

    orders_df = pd.DataFrame()
    summary = {}

    if args.rebuild:
        print(f"Rebuilding Paper Trading Pipeline for {args.symbol} ({args.timeframe}) using profile {args.profile}...")
        pipeline = PaperTradingPipeline(lake, settings, profile)
        artifacts, summary = pipeline.build_for_symbol_timeframe(spec, args.timeframe, profile, save=True)
        orders_df = artifacts.get("orders", pd.DataFrame())
    else:
        print(f"Loading paper orders for {args.symbol} ({args.timeframe}) using profile {args.profile}...")
        try:
            orders_df = lake.load_paper_orders(args.symbol, args.timeframe, args.profile)
            summary = lake.load_paper_summary(args.symbol, args.timeframe, args.profile)
        except Exception as e:
            print(f"Failed to load: {e}. Try running with --rebuild")
            return

    tail_df = orders_df.tail(args.last) if not orders_df.empty else None

    report_text = report_builder.build_paper_order_book_preview_report(args.symbol, args.timeframe, args.profile, summary, tail_df)

    out_dir = Path("reports/output/paper_reports")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"paper_order_book_preview_{args.symbol}_{args.timeframe}_{args.profile}.txt"

    with open(out_file, "w") as f:
        f.write(report_text)

    print(f"Report saved to {out_file}")
    print("\n" + "="*40 + "\n")
    print(report_text)

if __name__ == "__main__":
    main()
