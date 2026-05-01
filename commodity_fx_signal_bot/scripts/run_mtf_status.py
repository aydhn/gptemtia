from config.paths import LAKE_DIR
import argparse
import pandas as pd
from pathlib import Path
from config.paths import MTF_REPORTS_DIR
from data.storage.data_lake import DataLake
from config.symbols import get_symbol_spec, get_enabled_symbols
from mtf.mtf_config import list_mtf_profiles


def main():
    parser = argparse.ArgumentParser(description="Check MTF feature generation status")
    parser.parse_args()

    lake = DataLake(LAKE_DIR)
    universe = get_enabled_symbols()

    specs = universe
    profiles = list_mtf_profiles(enabled_only=True)

    records = []

    for spec in specs:
        if spec.asset_class in ("macro", "synthetic"):
            continue

        for profile in profiles:
            has_mtf = lake.has_features(spec, profile.base_timeframe, "mtf")
            has_events = lake.has_features(spec, profile.base_timeframe, "mtf_events")

            rows = 0
            cols = 0
            nan_ratio = 0.0

            if has_mtf:
                df = lake.load_features(spec, profile.base_timeframe, "mtf")
                rows = len(df)
                cols = len(df.columns)
                if rows > 0 and cols > 0:
                    nan_ratio = df.isna().sum().sum() / df.size

            records.append(
                {
                    "symbol": spec.symbol,
                    "profile": profile.name,
                    "base_timeframe": profile.base_timeframe,
                    "has_mtf": has_mtf,
                    "has_events": has_events,
                    "rows": rows,
                    "columns": cols,
                    "nan_ratio": nan_ratio,
                }
            )

    df = pd.DataFrame(records)

    MTF_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = MTF_REPORTS_DIR / "mtf_status.csv"
    txt_path = MTF_REPORTS_DIR / "mtf_status_report.txt"

    df.to_csv(csv_path, index=False)

    with open(txt_path, "w") as f:
        f.write("MTF Status Report\n")
        f.write("=" * 60 + "\n")
        f.write(f"Total symbols checked: {len(specs)}\n")
        f.write(f"Profiles checked: {[p.name for p in profiles]}\n")
        f.write(f"Total MTF features generated: {df['has_mtf'].sum()}\n")
        f.write(f"Total MTF events generated: {df['has_events'].sum()}\n")

    print(f"Status check complete. Report saved to {txt_path}")


if __name__ == "__main__":
    main()
