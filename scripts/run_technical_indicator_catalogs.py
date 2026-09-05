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
    c_tables, c_sum = pipeline.build_contracts_schema_and_policies(save=True)

    print("=" * 70)
    print("PHASE 117: TECHNICAL INDICATOR CATALOGS & CONTRACTS")
    print("=" * 70)
    print(f"Parameter Contracts : {c_sum['parameters']['total_parameter_contracts']}")
    print(f"Output Schemas      : {c_sum['schema']['total_schemas']}")
    print(f"Warmup Policies     : {c_sum['warmup']['total_warmup_policies']}")
    print(f"Lookahead Rules     : {c_sum['guard']['total_rules']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
