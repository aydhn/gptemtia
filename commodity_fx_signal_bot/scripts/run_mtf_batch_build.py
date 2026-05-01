from config.paths import LAKE_DIR
import argparse
import sys
import pandas as pd
from pathlib import Path
from config.settings import settings
from config.paths import MTF_REPORTS_DIR
from data.storage.data_lake import DataLake
from config.symbols import get_symbol_spec, get_enabled_symbols
from mtf.mtf_config import get_mtf_profile
from mtf.mtf_pipeline import MTFPipeline


def parse_args():
    parser = argparse.ArgumentParser(description="Batch build MTF features")
    parser.add_argument("--limit", type=int, help="Limit number of symbols")
    parser.add_argument("--asset-class", type=str, help="Filter by asset class")
    parser.add_argument("--symbol", type=str, help="Specific symbol to process")
    parser.add_argument(
        "--profile", type=str, default="daily_swing", help="MTF profile name"
    )
    parser.add_argument(
        "--no-events", action="store_true", help="Skip event generation"
    )
    parser.add_argument(
        "--save", action="store_true", default=True, help="Save generated features"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    lake = DataLake(LAKE_DIR)
    universe = get_enabled_symbols()

    try:
        profile = get_mtf_profile(args.profile)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    pipeline = MTFPipeline(lake, settings, profile)

    specs = universe
    if args.symbol:
        specs = [s for s in specs if s.symbol == args.symbol]
    elif args.asset_class:
        specs = [s for s in specs if s.asset_class == args.asset_class]

    if not specs:
        print("No symbols found matching criteria.")
        sys.exit(1)

    print(
        f"Starting MTF batch build for {len(specs)} symbols using profile {args.profile}..."
    )

    results = pipeline.build_for_universe(
        specs,
        profile=profile,
        limit=args.limit,
        save=args.save,
        include_events=not args.no_events,
    )

    batch_results = results.get("batch_results", [])

    records = []
    for r in batch_results:
        rec = {
            "symbol": r.get("symbol"),
            "rows": r.get("rows", 0),
            "columns": r.get("columns", 0),
            "passed": r.get("quality_report", {}).get("passed", False),
            "warnings_count": len(r.get("warnings", [])),
        }
        records.append(rec)

    df = pd.DataFrame(records)

    MTF_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = MTF_REPORTS_DIR / "mtf_batch_summary.csv"
    txt_path = MTF_REPORTS_DIR / "mtf_batch_summary.txt"

    df.to_csv(csv_path, index=False)

    with open(txt_path, "w") as f:
        f.write(f"MTF Batch Build Summary | Profile: {args.profile}\n")
        f.write("=" * 60 + "\n")
        f.write(f"Total processed: {len(df)}\n")
        f.write(f"Successful: {df['passed'].sum()}\n")
        f.write("\nDetails:\n")
        f.write(df.to_string())

    print(f"Batch build complete. Summary saved to {csv_path}")


if __name__ == "__main__":
    main()
