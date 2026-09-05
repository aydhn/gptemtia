from pathlib import Path
from config.settings import Settings
from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.data_lineage_pipeline import DataLineagePipeline


def test_data_lineage_pipeline_no_save():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    profile = get_default_data_lineage_profile()

    pipeline = DataLineagePipeline(
        data_lake=None,
        settings=settings,
        project_root=project_root,
        profile=profile,
    )

    t_prof, s_prof = pipeline.build_lineage_profiles_and_domains(save=False)
    assert len(t_prof["profiles"]) >= 3

    t_prov, s_prov = pipeline.build_source_and_provider_provenance(save=False)
    assert len(t_prov["sources"]) >= 8

    t_ds, s_ds = pipeline.build_dataset_schema_transformation_provenance(save=False)
    assert len(t_ds["datasets"]) >= 8

    t_norm, s_norm = pipeline.build_normalization_quality_manual_lineage(save=False)
    assert len(t_norm["normalization_lineage"]) >= 8

    t_dom, s_dom = pipeline.build_domain_lineage(save=False)
    assert len(t_dom["fx_lineage"]) >= 3

    t_bnd, s_bnd = pipeline.build_license_copyright_usage_boundaries(save=False)
    assert len(t_bnd["licenses"]) >= 5

    t_aud, s_aud = pipeline.build_audit_findings_and_scores(save=False)
    assert len(t_aud["audit_trail"]) >= 8

    t_cd, s_cd = pipeline.build_cross_domain_and_handoff(save=False)
    assert len(t_cd["cross_domain"]) >= 5

    t_hlth, s_hlth = pipeline.build_health_validation_safety(save=False)
    assert s_hlth["health_summary"]["overall_status"] == "PASS"

    status_df, overall_sum = pipeline.build_data_lineage_status(save=False)
    assert len(status_df) == 9
    assert overall_sum["all_subsystems_ready"] is True
