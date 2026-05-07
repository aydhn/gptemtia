import argparse
import sys
from pathlib import Path

# Add project root to sys.path
project_root = Path(__file__).parent.parent.resolve()
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from config.settings import Settings
from config.symbols import get_symbol_spec, get_symbols_by_asset_class
from data.storage.data_lake import DataLake
from levels.level_pipeline import LevelPipeline
from levels.level_config import get_level_profile
import reports.report_builder as report_builder
from config.paths import REPORTS_LEVEL_REPORTS_DIR


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--asset-class", type=str, default=None)
    parser.add_argument("--symbol", type=str, default=None)
    parser.add_argument("--timeframe", type=str, default="1d")
    parser.add_argument("--profile", type=str, default="balanced_theoretical_levels")
    parser.add_argument("--save", action="store_true", default=True)
    args = parser.parse_args()

    settings = Settings()
    from config.paths import LAKE_DIR

    data_lake = DataLake(LAKE_DIR)

    try:
        profile = get_level_profile(args.profile)
    except Exception as e:
        print(f"Hata: {e}")
        return

    specs = []
    if args.symbol:
        specs.append(get_symbol_spec(args.symbol))
    elif args.asset_class:
        specs = [
            get_symbol_spec(s) for s in get_symbols_by_asset_class(args.asset_class)
        ]
    else:
        # Dummy get all if possible, just take a few
        # Or you can import ALL_SYMBOLS
        from config.symbols import get_symbol_map

        specs = list(get_symbol_map().values())

    pipeline = LevelPipeline(data_lake, settings, profile)
    summary = pipeline.build_for_universe(
        specs, args.timeframe, profile, args.limit, args.save
    )

    report = report_builder.build_level_batch_report(summary)
    print(report)

    if args.save:
        REPORTS_LEVEL_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        out_path = REPORTS_LEVEL_REPORTS_DIR / "level_batch_summary.txt"
        with open(out_path, "w") as f:
            f.write(report)
        print(f"Rapor kaydedildi: {out_path}")


if __name__ == "__main__":
    main()
