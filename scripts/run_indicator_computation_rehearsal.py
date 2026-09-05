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
    tables, summary = pipeline.run_indicator_computation_rehearsal(save=True)
    df = tables["rehearsal_report"]

    print("=" * 70)
    print("PHASE 117: INDICATOR COMPUTATION REHEARSAL SUITE")
    print("=" * 70)
    print(f"Total Computations Tested : {summary['total_rehearsals']}")
    print(f"All Rehearsals Passed     : {summary['all_passed']}")
    print(f"Zero Input Mutation       : {summary['no_mutation_guaranteed']}")
    print(f"Zero Forbidden Columns    : {summary['no_forbidden_columns_guaranteed']}")
    print(f"Overall Status            : {summary['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
