from pathlib import Path
import pytest
from advanced_factor_metadata.factor_metadata_config import get_default_factor_metadata_profile
from advanced_factor_metadata.factor_metadata_pipeline import FactorMetadataPipeline


def test_factor_metadata_pipeline_execution():
    project_root = Path(__file__).resolve().parent.parent
    profile = get_default_factor_metadata_profile()

    pipeline = FactorMetadataPipeline(
        data_lake=None,
        settings=None,
        project_root=project_root,
        profile=profile,
    )

    # Test build without saving to disk
    p_dfs, p_sums = pipeline.build_profiles_domains_families(save=False)
    assert len(p_dfs["profiles"]) >= 3
    assert len(p_dfs["domains"]) >= 32
    assert len(p_dfs["families"]) == 12

    c_dfs, c_sums = pipeline.build_contracts_namespace_schema(save=False)
    assert len(c_dfs["contracts"]) == 12
    assert len(c_dfs["namespaces"]) == 12

    d_dfs, d_sums = pipeline.build_dependencies(save=False)
    assert len(d_dfs["dependencies"]) >= 15

    t_dfs, t_sums = pipeline.build_technical_factor_families(save=False)
    assert len(t_dfs["trend"]) >= 4

    m_dfs, m_sums = pipeline.build_macro_event_news_cross_asset_families(save=False)
    assert len(m_dfs["macro_context"]) >= 4

    f_dfs, f_sums = pipeline.build_manifest_review_policies(save=False)
    assert len(f_dfs["manifest"]) == 12

    h_dfs, h_sums = pipeline.build_health_validation_safety_handoff(save=False)
    assert len(h_dfs["health"]) >= 8

    status_df, summary = pipeline.build_factor_metadata_status(save=False)
    assert not status_df.empty
    assert summary["status"] == "factor_ready"
    assert summary["current_phase"] == 122
    assert summary["target_final_phase"] == 160
