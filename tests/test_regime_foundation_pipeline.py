from advanced_regime_foundation.regime_foundation_pipeline import (
    RegimeFoundationPipeline,
)


def test_regime_foundation_pipeline_dry_run():
    pipeline = RegimeFoundationPipeline()

    tables_p, summaries_p = pipeline.build_profiles_domains_taxonomy(save=False)
    assert "profiles" in tables_p
    assert "market_behavior" in tables_p
    assert "regime_states" in tables_p

    tables_f, summaries_f = pipeline.build_regime_families(save=False)
    assert "regime_families" in tables_f
    assert "volatility" in tables_f
    assert "trend" in tables_f
    assert "range" in tables_f

    tables_c, summaries_c = pipeline.build_context_registries(save=False)
    assert "macro" in tables_c
    assert "event" in tables_c
    assert "news_metadata" in tables_c
    assert "cross_asset" in tables_c

    tables_d, summaries_d = pipeline.build_contracts_dependencies_schema(save=False)
    assert "contracts" in tables_d
    assert "factor_dependencies" in tables_d
    assert "validation_dependencies" in tables_d
    assert "quality_dependencies" in tables_d
    assert "output_schema" in tables_d
    assert "namespace" in tables_d

    tables_m, summaries_m = pipeline.build_manifest_policies(save=False)
    assert "non_signal_policies" in tables_m
    assert "forbidden_claims" in tables_m
    assert "manifest" in tables_m

    tables_h, summaries_h = pipeline.build_health_validation_safety_handoff(save=False)
    assert "health" in tables_h
    assert "safety" in tables_h
    assert "validation_report" in tables_h
    assert "handoff" in tables_h

    df_stat, s_stat = pipeline.build_regime_foundation_status(save=False)
    assert not df_stat.empty
    assert s_stat["overall_status"] == "READY"
    assert s_stat["non_signal"] is True
