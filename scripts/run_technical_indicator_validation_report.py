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
    tables, summary = pipeline.build_health_validation_safety_handoff(save=True)

    print("=" * 70)
    print("PHASE 117: TECHNICAL INDICATOR VALIDATION & SAFETY REPORT")
    print("=" * 70)
    print(f"Validation Status : {summary['validation']['validation_status']}")
    print(f"Total Rules       : {summary['validation']['total_rules_checked']}")
    print(f"Violations        : {summary['validation']['total_violations']}")
    print(f"Safety Status     : {summary['safety']['safety_status']}")
    print(f"No-Go Rules       : {summary['safety']['total_no_go']}")
    print(f"Safe-Go Rules     : {summary['safety']['total_safe_go']}")
    print(f"Handoff Status    : {summary['handoff']['handoff_status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
