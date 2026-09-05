from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_data_normalization.data_normalization_config import get_default_data_normalization_profile
from advanced_data_normalization.data_normalization_pipeline import DataNormalizationPipeline


def test_data_normalization_pipeline_save_false():
    root = Path(__file__).resolve().parent.parent
    settings = Settings()
    lake = DataLake()
    prof = get_default_data_normalization_profile()
    pipeline = DataNormalizationPipeline(data_lake=lake, settings=settings, project_root=root, profile=prof)

    p_tables, p_sum = pipeline.build_normalization_profiles_and_domains(save=False)
    assert "profile_registry" in p_tables
    assert p_sum["profile_summary"]["total_profiles"] >= 3

    r_tables, r_sum = pipeline.build_normalization_rules_and_canonical_schema(save=False)
    assert "rule_registry" in r_tables

    s_tables, s_sum = pipeline.run_symbol_indicator_event_tag_normalization(save=False)
    assert "fx_symbol_report" in s_tables

    v_tables, v_sum = pipeline.build_normalized_views_and_findings(save=False)
    assert "findings_registry" in v_tables
    assert "decision_registry" in v_tables

    st_df, st_sum = pipeline.build_data_normalization_status(save=False)
    assert not st_df.empty
    assert st_sum["all_ready"] is True
    assert st_sum["all_non_destructive"] is True
