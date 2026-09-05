from pathlib import Path
from config.settings import Settings
from advanced_provider_benchmark.provider_benchmark_config import get_default_provider_benchmark_profile
from advanced_provider_benchmark.provider_benchmark_pipeline import ProviderBenchmarkPipeline


def test_provider_benchmark_pipeline():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    profile = get_default_provider_benchmark_profile()

    pipeline = ProviderBenchmarkPipeline(
        data_lake=None,
        settings=settings,
        project_root=project_root,
        profile=profile,
    )

    t_pdm, s_pdm = pipeline.build_profiles_domains_metrics(save=False)
    assert len(t_pdm["profiles"]) >= 3
    assert len(t_pdm["metrics"]) >= 10

    t_core, s_core = pipeline.build_core_benchmarks(save=False)
    assert len(t_core["coverage"]) > 0
    assert len(t_core["no_scraping"]) > 0

    t_dom, s_dom = pipeline.build_domain_benchmarks(save=False)
    assert len(t_dom["fx_benchmark"]) > 0
    assert len(t_dom["news_metadata_benchmark"]) > 0

    t_cd, s_cd = pipeline.build_cross_domain_benchmarks(save=False)
    assert len(t_cd["cross_domain"]) > 0

    t_srf, s_srf = pipeline.build_scores_rankings_findings(save=False)
    assert len(t_srf["scores"]) > 0
    assert len(t_srf["ranking"]) > 0

    t_hvs, s_hvs = pipeline.build_health_validation_safety_and_handoff(save=False)
    assert len(t_hvs["health"]) > 0
    assert len(t_hvs["safety"]) > 0
    assert len(t_hvs["phase_116_handoff"]) > 0

    status_df, overall_sum = pipeline.build_provider_benchmark_status(save=False)
    assert not status_df.empty
    assert overall_sum["current_phase"] == 115
    assert overall_sum["target_final_phase"] == 160
    assert overall_sum["next_phase"] == 116
    assert overall_sum["all_subsystems_ready"] is True
