from config.paths import LAKE_DIR
import argparse
import sys
import pandas as pd
from config.settings import settings
from config.paths import MTF_REPORTS_DIR
from data.storage.data_lake import DataLake
from config.symbols import get_symbol_spec, get_enabled_symbols
from mtf.mtf_config import get_mtf_profile
from mtf.mtf_pipeline import MTFPipeline
from mtf.mtf_events import build_mtf_event_frame


def parse_args():
    parser = argparse.ArgumentParser(description="Preview MTF events for a symbol")
    parser.add_argument("--symbol", type=str, required=True, help="Symbol to analyze")
    parser.add_argument(
        "--profile", type=str, default="daily_swing", help="MTF profile name"
    )
    parser.add_argument(
        "--last", type=int, default=20, help="Number of rows to display"
    )
    parser.add_argument(
        "--use-saved-features",
        action="store_true",
        default=False,
        help="Use saved features if available",
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

    mtf_df = pd.DataFrame()
    if args.use_saved_features and lake.has_features(
        spec, profile.base_timeframe, "mtf"
    ):
        print("Using saved MTF features...")
        mtf_df = lake.load_features(spec, profile.base_timeframe, "mtf")
    else:
        print("Building MTF frame on the fly...")
        pipeline = MTFPipeline(lake, settings, profile)
        mtf_df, _ = pipeline.build_for_symbol(
            spec, profile=profile, save=False, include_events=False
        )

    if mtf_df.empty:
        print("Error: Could not obtain MTF dataframe.")
        sys.exit(1)

    event_df, summary = build_mtf_event_frame(mtf_df)

    print("\n--- Event Summary ---")
    print(f"Total Event Count: {summary['total_event_count']}")
    print(f"Active Last Row Events: {summary['active_last_row_events']}")
    print(f"Warning: {summary['notes']}")

    print(f"\n--- Last {args.last} Rows (Events Only) ---")
    print(event_df.tail(args.last).to_string())

    MTF_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = (
        MTF_REPORTS_DIR / f"mtf_event_preview_{args.symbol}_{args.profile}.txt"
    )

    with open(report_path, "w") as f:
        f.write(f"MTF Event Preview: {args.symbol} | Profile: {args.profile}\n")
        f.write("=" * 60 + "\n")
        f.write(f"Total Event Count: {summary['total_event_count']}\n")
        f.write(f"Active Last Row Events: {summary['active_last_row_events']}\n")
        f.write(f"Note: {summary['notes']}\n\n")
        f.write("Tail:\n")
        f.write(event_df.tail(args.last).to_string())

    print(f"\nReport saved to {report_path}")


if __name__ == "__main__":
    main()
