from config.paths import LAKE_DIR
import argparse
import sys
from pathlib import Path
from config.settings import settings
from config.paths import MTF_REPORTS_DIR
from data.storage.data_lake import DataLake
from config.symbols import get_symbol_spec, get_enabled_symbols
from mtf.mtf_config import get_mtf_profile
from mtf.mtf_pipeline import MTFPipeline
import pandas as pd


def parse_args():
    parser = argparse.ArgumentParser(description="Preview MTF alignment for a symbol")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to analyze")
    parser.add_argument(
        "--profile", type=str, default="daily_swing", help="MTF profile name"
    )
    parser.add_argument(
        "--last", type=int, default=10, help="Number of rows to display"
    )
    parser.add_argument(
        "--no-events", action="store_true", help="Skip event generation"
    )
    parser.add_argument(
        "--save", action="store_true", default=False, help="Save generated features"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    lake = DataLake(LAKE_DIR)
    spec = get_symbol_spec(args.symbol)

    if not spec:
        print(f"Error: Symbol {args.symbol} not found in universe.")
        sys.exit(1)

    try:
        profile = get_mtf_profile(args.profile)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    pipeline = MTFPipeline(lake, settings, profile)

    print(
        f"Running MTF alignment preview for {args.symbol} using profile {args.profile}..."
    )
    df, summary = pipeline.build_for_symbol(
        spec, profile=profile, save=args.save, include_events=not args.no_events
    )

    if df.empty:
        print(f"Error: Could not generate MTF dataframe for {args.symbol}.")
        print("Warnings:", summary.get("warnings", []))
        sys.exit(1)

    print("\n--- MTF Summary ---")
    print(f"Base Timeframe: {summary['base_timeframe']}")
    print(f"Context Timeframes: {summary['context_timeframes']}")
    print(f"Output Rows: {summary['rows']}")
    print(f"Output Columns: {summary['columns']}")
    print("Warnings:", summary.get("warnings", []))

    qr = summary.get("quality_report", {})
    print("\n--- Quality Report ---")
    print(f"Passed: {qr.get('report_builder = ReportBuilder()ed')}")
    print(f"NaN Ratio: {qr.get('total_nan_ratio', 0):.2%}")
    print(f"Stale Ratio: {qr.get('stale_context_ratio', 0):.2%}")

    print(f"\n--- Last {args.last} Rows ---")
    print(df.tail(args.last).to_string())

    report_path = (
        MTF_REPORTS_DIR / f"mtf_alignment_preview_{args.symbol}_{args.profile}.txt"
    )
    MTF_REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    with open(report_path, "w") as f:
        f.write(f"MTF Alignment Preview: {args.symbol} | Profile: {args.profile}\n")
        f.write("=" * 60 + "\n")
        f.write(f"Quality Passed: {qr.get('report_builder = ReportBuilder()ed')}\n")
        f.write(f"Warnings: {summary.get('warnings', [])}\n")
        f.write("\nTail:\n")
        f.write(df.tail(args.last).to_string())

    print(f"\nReport saved to {report_path}")


if __name__ == "__main__":
    main()
