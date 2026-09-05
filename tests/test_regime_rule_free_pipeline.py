from advanced_regime_rule_free.regime_rule_free_pipeline import RegimeRuleFreePipeline


def test_regime_rule_free_pipeline_builds():
    pipeline = RegimeRuleFreePipeline()

    tables, summaries = pipeline.build_profiles_domains_contracts(save=False)
    assert "profiles" in tables
    assert "domains" in tables
    assert "labeling_contracts" in tables
    assert "assignment_policies" in tables

    tables_s, summaries_s = pipeline.build_candidate_state_schemas(save=False)
    assert "candidate_state_schema" in tables_s
    assert "pseudo_state_schema" in tables_s
    assert "namespace" in tables_s

    tables_u, summaries_u = pipeline.build_unsupervised_prep_registries(save=False)
    assert "unsupervised_prep" in tables_u
    assert "clustering_inputs" in tables_u
    assert "clustering_algorithms" in tables_u
    assert "distance_metrics" in tables_u
    assert "normalization" in tables_u
    assert "scaling" in tables_u
    assert "dimensionality_reduction" in tables_u

    tables_f, summaries_f = pipeline.build_candidate_feature_metadata(save=False)
    assert "candidate_feature_sets" in tables_f
    assert "candidate_context" in tables_f
    assert "candidate_metadata" in tables_f

    tables_i, summaries_i = pipeline.build_integrity_guards_dependencies(save=False)
    assert "integrity_contracts" in tables_i
    assert "no_lookahead" in tables_i
    assert "timestamp_policy" in tables_i
    assert "quality_dependencies" in tables_i
    assert "validation_dependencies" in tables_i

    tables_p, summaries_p = pipeline.build_policies_review_manifest(save=False)
    assert "manual_review" in tables_p
    assert "non_signal_policies" in tables_p
    assert "forbidden_claims" in tables_p
    assert "source_preservation" in tables_p
    assert "integrity_manifest" in tables_p

    df_status, status_summary = pipeline.build_regime_rule_free_status(save=False)
    assert len(df_status) == 12
    assert status_summary["overall_status"] == "READY"
    assert status_summary["current_phase"] == 128
    assert status_summary["next_phase"] == 129
    assert status_summary["target_final_phase"] == 160
    assert status_summary["non_signal"] is True
    assert status_summary["zero_execution"] is True
