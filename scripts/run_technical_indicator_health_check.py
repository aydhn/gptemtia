import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.technical_indicator_health import build_technical_indicator_health_check


def main():
    project_root = Path(__file__).resolve().parent.parent
    profile = get_default_technical_indicator_profile()
    df, summary = build_technical_indicator_health_check(project_root, profile)

    print("=" * 70)
    print("PHASE 117: TECHNICAL INDICATOR ENGINE HEALTH CHECK")
    print("=" * 70)
    print(f"Health Status : {summary['health_status']}")
    print(f"Total Checks  : {summary['total_checks']}")
    print(f"All Passed    : {summary['all_passed']}")
    print("-" * 70)
    for _, row in df.iterrows():
        print(f" - {row['check_item']:<35} : [{row['status']}] {row['detail']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
