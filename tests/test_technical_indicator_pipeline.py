from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.technical_indicator_pipeline import TechnicalIndicatorPipeline


def test_technical_indicator_pipeline():
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

    # Test pipeline dry-run (save=False)
    prof_tables, prof_sum = pipeline.build_profiles_domains_catalogs(save=False)
    assert not prof_tables["profile_registry"].empty

    fam_tables, fam_sum = pipeline.build_indicator_family_registries(save=False)
    assert fam_sum["families_count"] >= 12

    c_tables, c_sum = pipeline.build_contracts_schema_and_policies(save=False)
    assert not c_tables["parameters"].empty

    r_tables, r_sum = pipeline.run_indicator_computation_rehearsal(save=False)
    assert r_sum["all_passed"] is True

    status_df, status_sum = pipeline.build_technical_indicator_status(save=False)
    assert not status_df.empty
    assert status_sum["overall_status"] == "READY"
