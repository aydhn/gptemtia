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



    parser = argparse.ArgumentParser(description="Run paper trading preview for a symbol")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to run (e.g. GC=F)")
    parser.add_argument("--timeframe", type=str, default="1d", help="Timeframe (e.g. 1d)")
    parser.add_argument("--profile", type=str, default="balanced_virtual_paper", help="Paper trading profile name")
    parser.add_argument("--save", action="store_true", help="Save the results to the data lake")
    parser.add_argument("--last", type=int, default=20, help="Number of last ledger events to show")

    args = parser.parse_args()

    spec = SymbolSpec(args.symbol, "unknown", "commodity", "metals", "USD")
    lake = DataLake(settings)

    try:
        profile = get_paper_trading_profile(args.profile)
    except Exception as e:
        print(f"Error loading profile: {e}")
        return

    pipeline = PaperTradingPipeline(lake, settings, profile)

    print(f"Running Paper Trading Pipeline for {args.symbol} ({args.timeframe}) using profile {args.profile}...")
    artifacts, summary = pipeline.build_for_symbol_timeframe(spec, args.timeframe, profile, save=args.save)

    if "error" in summary or "warning" in summary:
        print("Completed with errors/warnings:")
        print(summary)
        return

    ledger_df = artifacts.get("ledger", pd.DataFrame())
    tail_df = ledger_df.tail(args.last) if not ledger_df.empty else None

    report_text = report_builder.build_paper_trading_preview_report(args.symbol, args.timeframe, args.profile, summary, tail_df)

    out_dir = Path("reports/output/paper_reports")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"paper_trading_preview_{args.symbol}_{args.timeframe}_{args.profile}.txt"

    with open(out_file, "w") as f:
        f.write(report_text)

    print(f"Report saved to {out_file}")
    print("\n" + "="*40 + "\n")
    print(report_text)

if __name__ == "__main__":
    main()
