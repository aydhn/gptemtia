import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.technical_indicator_pipeline import TechnicalIndicatorPipeline


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_technical_indicator_profile()

    pipeline = TechnicalIndicatorPipeline(
        data_lake=data_lake,
        settings=settings,
        project_root=project_root,
        profile=profile,
    )
    status_df, summary = pipeline.build_technical_indicator_status(save=True)

    print("=" * 70)
    print("PHASE 117: TECHNICAL INDICATOR EXPANSION STATUS")
    print("=" * 70)
    print(f"Phase              : {summary['phase']} ({summary['phase_name']})")
    print(f"Target Final Phase : {summary['target_final_phase']}")
    print(f"Next Phase         : {summary['next_phase']}")
    print(f"Overall Status     : {summary['overall_status']}")
    print(f"Components Active  : {summary['components_count']}")
    print("-" * 70)
    for _, row in status_df.iterrows():
        print(f" - {row['component']:<30} : [{row['status']}] ({row['rows']} rows)")
    print("=" * 70)


if __name__ == "__main__":
    main()
