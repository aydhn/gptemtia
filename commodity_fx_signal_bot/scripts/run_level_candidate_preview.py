import argparse
import sys
from pathlib import Path

# Add project root to sys.path
project_root = Path(__file__).parent.parent.resolve()
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from config.settings import Settings
from config.symbols import get_symbol_spec
from data.storage.data_lake import DataLake
from levels.level_pipeline import LevelPipeline
from levels.level_config import get_level_profile
import reports.report_builder as report_builder
from config.paths import REPORTS_LEVEL_REPORTS_DIR


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", type=str, required=True)
    parser.add_argument("--timeframe", type=str, default="1d")
    parser.add_argument("--profile", type=str, default="balanced_theoretical_levels")
    parser.add_argument("--last", type=int, default=10)
    parser.add_argument("--save", action="store_true", default=False)
    args = parser.parse_args()

    settings = Settings()
    from config.paths import LAKE_DIR

    data_lake = DataLake(LAKE_DIR)

    try:
        spec = get_symbol_spec(args.symbol)
    except Exception as e:
        print(f"Hata: {e}")
        return

    try:
        profile = get_level_profile(args.profile)
    except Exception as e:
        print(f"Hata: {e}")
        return

    pipeline = LevelPipeline(data_lake, settings, profile)
    df, summary = pipeline.build_for_symbol_timeframe(
        spec, args.timeframe, profile, save=args.save
    )

    if df.empty:
        tail_df = df
    else:
        tail_df = df.tail(args.last)

    report = report_builder.build_level_candidate_preview_report(
        spec.symbol, args.timeframe, profile.name, summary, tail_df
    )
    print(report)

    if args.save:
        REPORTS_LEVEL_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        out_path = (
            REPORTS_LEVEL_REPORTS_DIR
            / f"level_candidate_preview_{spec.symbol}_{args.timeframe}_{profile.name}.txt"
        )
        with open(out_path, "w") as f:
            f.write(report)
        print(f"Rapor kaydedildi: {out_path}")


if __name__ == "__main__":
    main()
