import pytest
from pathlib import Path
from config.settings import Settings
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.data_quality_pipeline import DataQualityPipeline


def test_data_quality_pipeline_dry_run_save_false(tmp_path):
    settings = Settings()
    profile = get_default_data_quality_profile()
    pipeline = DataQualityPipeline(data_lake=None, settings=settings, project_root=tmp_path, profile=profile)

    # All pipeline steps must execute cleanly with save=False without crashing
    p_tables, p_sum = pipeline.build_quality_profiles_and_domains(save=False)
    assert "profile_registry" in p_tables

    r_tables, r_sum = pipeline.build_quality_rules(save=False)
    assert "rule_registry" in r_tables

    d_tables, d_sum = pipeline.run_domain_quality_contracts(save=False)
    assert "fx_rules" in d_tables

    f_tables, f_sum = pipeline.build_findings_and_manual_review(save=False)
    assert "quality_findings" in f_tables

    s_tables, s_sum = pipeline.build_quality_scores(save=False)
    assert "provider_quality_scores" in s_tables

    h_tables, h_sum = pipeline.build_health_and_validation(save=False)
    assert "health_check" in h_tables

    status_df, status_sum = pipeline.build_data_quality_status(save=False)
    assert len(status_df) >= 5
    assert status_sum["pipeline_status"] == "PASS"
