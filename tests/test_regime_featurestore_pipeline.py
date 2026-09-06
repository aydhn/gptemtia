import pandas as pd
from advanced_regime_featurestore_integration.regime_featurestore_pipeline import RegimeFeatureStorePipeline


def test_regime_featurestore_pipeline_steps():
    pipeline = RegimeFeatureStorePipeline()

    # Step 1: Profiles, domains, contracts
    t1, s1 = pipeline.build_profiles_domains_contracts(save=False)
    assert len(t1["profiles"]) == 3
    assert len(t1["domains"]) == 33
    assert len(t1["contracts"]) == 10

    # Step 2: Entities, namespaces, schema, policies
    t2, s2 = pipeline.build_entities_namespace_schema(save=False)
    assert len(t2["entities"]) == 10
    assert len(t2["namespaces"]) == 8
    assert len(t2["schema"]) == 16
    assert len(t2["version_policies"]) == 3
    assert len(t2["partition_policies"]) >= 6

    # Step 3: Component catalogs
    t3, s3 = pipeline.build_component_store_catalogs(save=False)
    assert len(t3) == 8
    assert "taxonomy_catalog" in t3
    assert "matrix_catalog" in t3

    # Step 4: Accepted references, dependencies, lineage
    t4, s4 = pipeline.build_accepted_references_dependencies_lineage(save=False)
    assert "no_lookahead_accepted" in t4
    assert "quality_dependencies" in t4
    assert "lineage" in t4

    # Step 5: Read/write/query contracts, policies, manifest
    t5, s5 = pipeline.build_read_write_query_policies_manifest(save=False)
    assert len(t5["read_contracts"]) == 2
    assert len(t5["write_contracts"]) == 2
    assert len(t5["query_contracts"]) == 8
    assert len(t5["manifest"]) == 1

    # Step 6: Health, validation, safety, handoff
    t6, s6 = pipeline.build_health_validation_safety_handoff(save=False)
    assert s6["health"]["all_healthy"] is True
    assert s6["validation"]["all_passed"] is True
    assert s6["handoff"]["all_satisfied"] is True


def test_regime_featurestore_pipeline_end_to_end_status():
    pipeline = RegimeFeatureStorePipeline()
    status_df, summary = pipeline.build_regime_featurestore_status(save=False)

    assert isinstance(status_df, pd.DataFrame)
    assert len(status_df) == 12
    assert summary["current_phase"] == 134
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] == 135
    assert summary["all_healthy"] is True
    assert summary["all_validation_passed"] is True
    assert summary["all_handoff_ready"] is True
    assert summary["overall_status"] == "regime_store_ready"
    assert summary["non_signal"] is True
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
